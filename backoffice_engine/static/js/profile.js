document.addEventListener("DOMContentLoaded", function() {
    const updateBtn = document.getElementById("updateProfileBtn");
    const updateForm = document.getElementById("updateProfileForm");
    const closeBtn = document.getElementById("closeForm");

    updateBtn.addEventListener("click", function(e) {
        e.preventDefault();
        updateForm.classList.add("active");
    });

    closeBtn.addEventListener("click", function() {
        updateForm.classList.remove("active");
    });
});
