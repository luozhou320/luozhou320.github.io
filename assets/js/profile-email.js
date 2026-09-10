(function () {
  "use strict";

  const toastId = "profile-email-toast";
  let toastTimer;

  function showToast(message) {
    let toast = document.getElementById(toastId);

    if (!toast) {
      toast = document.createElement("div");
      toast.id = toastId;
      toast.className = "profile-email-toast";
      toast.setAttribute("role", "status");
      toast.setAttribute("aria-live", "polite");
      document.body.appendChild(toast);
    }

    toast.textContent = message;
    toast.classList.add("is-visible");
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(() => toast.classList.remove("is-visible"), 1800);
  }

  function fallbackCopy(value) {
    const field = document.createElement("textarea");
    field.value = value;
    field.setAttribute("readonly", "");
    field.style.cssText = "position:fixed;inset:0 auto auto 0;opacity:0;pointer-events:none";
    document.body.appendChild(field);
    field.select();

    let copied = false;
    try {
      copied = document.execCommand("copy");
    } catch (_error) {
      copied = false;
    }

    field.remove();
    return copied;
  }

  async function copyEmail(link) {
    const email = decodeURIComponent(link.href.replace(/^mailto:/i, "").split("?")[0]);

    try {
      if (!navigator.clipboard || !window.isSecureContext) {
        throw new Error("Clipboard API unavailable");
      }
      await navigator.clipboard.writeText(email);
      showToast("Email copied to clipboard");
    } catch (_error) {
      showToast(fallbackCopy(email) ? "Email copied to clipboard" : email);
    }
  }

  function initializeEmailLink() {
    const link = document.querySelector('.profile-social a[href^="mailto:"]');
    if (!link) return;

    link.setAttribute("aria-label", "Copy email address to clipboard");
    link.setAttribute("title", "Copy email address");
    link.setAttribute("role", "button");

    link.addEventListener("click", (event) => {
      event.preventDefault();
      copyEmail(link);
    });

    link.addEventListener("keydown", (event) => {
      if (event.key !== " ") return;
      event.preventDefault();
      copyEmail(link);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeEmailLink);
  } else {
    initializeEmailLink();
  }
})();
