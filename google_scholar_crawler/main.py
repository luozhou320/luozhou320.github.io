"""Fetch and normalize Google Scholar statistics for the homepage."""

from __future__ import annotations

import json
import multiprocessing
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RESULTS_DIR = Path(__file__).resolve().parent / "results"


def _fetch_author_once(scholar_id: str, connection: Any) -> None:
    """Fetch inside a child process so captcha handling can be terminated."""
    try:
        from scholarly import scholarly

        scholarly.set_timeout(10)
        scholarly.set_retries(2)
        author = scholarly.search_author_id(scholar_id)
        if not author:
            raise RuntimeError(f"Scholar profile {scholar_id!r} was not found")

        filled = scholarly.fill(
            author,
            sections=["basics", "indices", "counts", "publications"],
        )
        if not isinstance(filled, dict):
            raise RuntimeError("Scholar returned an unexpected author payload")
        connection.send(("ok", filled))
    except BaseException as error:  # Send child-process failures to the parent.
        connection.send(("error", f"{type(error).__name__}: {error}"))
    finally:
        connection.close()


def fetch_author_once(scholar_id: str, timeout: int) -> dict[str, Any]:
    """Run one Scholar request with a hard process-level deadline."""
    context = multiprocessing.get_context("spawn")
    parent_connection, child_connection = context.Pipe(duplex=False)
    process = context.Process(
        target=_fetch_author_once,
        args=(scholar_id, child_connection),
    )
    process.start()
    child_connection.close()

    try:
        if not parent_connection.poll(timeout):
            process.terminate()
            process.join(5)
            if process.is_alive() and hasattr(process, "kill"):
                process.kill()
                process.join()
            raise TimeoutError(f"Google Scholar request exceeded {timeout} seconds")

        status, payload = parent_connection.recv()
        process.join(5)
        if status == "error":
            raise RuntimeError(payload)
        return payload
    finally:
        parent_connection.close()
        if process.is_alive():
            process.terminate()
            process.join()


def fetch_author(
    scholar_id: str,
    attempts: int = 3,
    attempt_timeout: int = 90,
) -> dict[str, Any]:
    """Fetch an author profile, retrying transient Scholar failures."""
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            print(
                f"Fetching Google Scholar profile (attempt {attempt}/{attempts})...",
                flush=True,
            )
            return fetch_author_once(scholar_id, attempt_timeout)
        except Exception as error:  # scholarly exposes several network exceptions
            last_error = error
            if attempt == attempts:
                break
            delay = 5 * (2 ** (attempt - 1))
            print(
                f"Scholar request failed: {error}. Retrying in {delay} seconds...",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(delay)

    raise RuntimeError(
        f"Unable to fetch Google Scholar profile after {attempts} attempts"
    ) from last_error


def normalize_author(author: dict[str, Any], scholar_id: str) -> dict[str, Any]:
    """Create a stable, JSON-serializable schema for the frontend."""
    cited_by = author.get("citedby", 0)
    if not isinstance(cited_by, int) or cited_by < 0:
        raise ValueError("Scholar payload has an invalid citedby value")

    publications: dict[str, dict[str, Any]] = {}
    for publication in author.get("publications", []):
        if not isinstance(publication, dict):
            continue
        publication_id = publication.get("author_pub_id")
        if not publication_id:
            continue
        publications[str(publication_id)] = publication

    normalized = dict(author)
    normalized.update(
        {
            "scholar_id": scholar_id,
            "citedby": cited_by,
            "updated": datetime.now(timezone.utc).isoformat(),
            "publications": publications,
        }
    )
    return normalized


def write_outputs(author: dict[str, Any]) -> None:
    """Atomically write the site payload and Shields.io payload."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    payloads = {
        "gs_data.json": author,
        "gs_data_shieldsio.json": {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(author["citedby"]),
        },
    }

    for filename, payload in payloads.items():
        destination = RESULTS_DIR / filename
        temporary = destination.with_suffix(destination.suffix + ".tmp")
        temporary.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        temporary.replace(destination)


def main() -> None:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise SystemExit("GOOGLE_SCHOLAR_ID is required")

    attempts = int(os.environ.get("GOOGLE_SCHOLAR_ATTEMPTS", "3"))
    attempt_timeout = int(os.environ.get("GOOGLE_SCHOLAR_ATTEMPT_TIMEOUT", "90"))
    if attempts < 1 or attempt_timeout < 1:
        raise SystemExit("Scholar attempts and attempt timeout must be positive integers")

    author = normalize_author(
        fetch_author(scholar_id, attempts, attempt_timeout),
        scholar_id,
    )
    write_outputs(author)
    print(
        f"Saved {author['citedby']} citations and "
        f"{len(author['publications'])} publications for {author.get('name', scholar_id)}."
    )


if __name__ == "__main__":
    main()
