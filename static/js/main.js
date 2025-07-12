document.addEventListener("DOMContentLoaded", function () {
    const dropdownBtn = document.getElementById("userDropdownBtn");
    const dropdownMenu = document.getElementById("userDropdownMenu");
    const wrapper = document.getElementById("userDropdownWrapper");

    let isClickedOpen = false;

    // Toggle dropdown on click
    dropdownBtn.addEventListener("click", function (event) {
        event.stopPropagation();
        isClickedOpen = !isClickedOpen;

        if (isClickedOpen) {
            dropdownMenu.classList.remove("hidden");
        } else {
            dropdownMenu.classList.add("hidden");
        }
    });

    // Hover in: show dropdown (only if not clicked open)
    wrapper.addEventListener("mouseenter", function () {
        if (!isClickedOpen) {
            dropdownMenu.classList.remove("hidden");
        }
    });

    // Hover out: hide dropdown (only if not clicked open)
    wrapper.addEventListener("mouseleave", function () {
        if (!isClickedOpen) {
            dropdownMenu.classList.add("hidden");
        }
    });

    // Click outside: close dropdown and reset hover
    document.addEventListener("click", function (event) {
        if (!wrapper.contains(event.target)) {
            dropdownMenu.classList.add("hidden");
            isClickedOpen = false;
        }
    });
});
