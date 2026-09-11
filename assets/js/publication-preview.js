(() => {
  const initializePublicationPreviews = () => {
    if (typeof HTMLDialogElement === "undefined") return;

    const previews = document.querySelectorAll(".publications img[data-zoomable]");
    if (!previews.length) return;

    const dialog = document.createElement("dialog");
    dialog.className = "publication-preview-dialog";
    dialog.setAttribute("aria-labelledby", "publication-preview-title");

    const closeButton = document.createElement("button");
    closeButton.type = "button";
    closeButton.className = "publication-preview-dialog__close";
    closeButton.textContent = "Close";
    closeButton.setAttribute("aria-label", "Close enlarged publication preview");

    const image = document.createElement("img");
    image.className = "publication-preview-dialog__image";
    image.alt = "";

    const caption = document.createElement("p");
    caption.id = "publication-preview-title";
    caption.className = "publication-preview-dialog__caption";

    dialog.append(closeButton, image, caption);
    document.body.append(dialog);

    let opener = null;

    const getPublicationTitle = (preview) =>
      preview.closest(".row")?.querySelector(".title")?.textContent?.trim() || preview.alt || "Publication preview";

    const setNativeDisplayWidth = (sourceWidth) => {
      const pixelRatio = Math.max(1, window.devicePixelRatio || 1);
      const nativeCssWidth = Math.max(1, Math.floor(sourceWidth / pixelRatio));
      dialog.style.setProperty("--preview-native-width", `${nativeCssWidth}px`);
    };

    const closeDialog = () => {
      dialog.close();
      opener?.focus();
    };

    const openDialog = (preview) => {
      opener = preview;
      const title = getPublicationTitle(preview);

      setNativeDisplayWidth(preview.naturalWidth || preview.width * Math.max(1, window.devicePixelRatio || 1));
      image.onload = () => setNativeDisplayWidth(image.naturalWidth);
      image.src = preview.src;
      image.alt = title;
      caption.textContent = title;
      dialog.showModal();
      closeButton.focus();
    };

    closeButton.addEventListener("click", closeDialog);
    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) closeDialog();
    });
    dialog.addEventListener("close", () => opener?.focus());

    previews.forEach((preview) => {
      preview.removeAttribute("data-zoomable");
      preview.dataset.publicationPreview = "";
      preview.tabIndex = 0;
      preview.setAttribute("role", "button");
      preview.setAttribute("aria-label", `Enlarge publication preview: ${getPublicationTitle(preview)}`);
      preview.addEventListener("click", () => openDialog(preview));
      preview.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" && event.key !== " ") return;
        event.preventDefault();
        openDialog(preview);
      });
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializePublicationPreviews, { once: true });
  } else {
    initializePublicationPreviews();
  }
})();
