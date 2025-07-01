function openModal(imageUrl, category, instruction, creativity) {
  // Set image and details
  document.getElementById("modalImage").src = imageUrl;
  document.getElementById("modalCategory").innerText = category;
  document.getElementById("modalInstruction").innerText = instruction;
  document.getElementById("modalCreativity").innerText = creativity;

  // Set download link
  document.getElementById("downloadBtn").href = imageUrl;

  // Show modal
  const modal = document.getElementById("myModal");
  modal.style.display = "flex";
  modal.classList.add("modal-active"); // Optional: for animation if you use one
}

function closeModal() {
  const modal = document.getElementById("myModal");
  modal.classList.remove("modal-active");
  setTimeout(() => {
    modal.style.display = "none";
  }, 200); // Match this to any fade-out animation timing
}
