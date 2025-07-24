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



// for image replace

 function toggleEditMode() {
            const viewMode = document.getElementById('profileViewMode');
            const editForm = document.getElementById('profileEditForm');
            const editBtn = document.getElementById('editProfileBtn');

            if (viewMode.classList.contains('hidden')) {
                // Currently in edit mode, switch to view mode
                viewMode.classList.remove('hidden');
                editForm.classList.add('hidden');
                editBtn.textContent = 'Edit';
                editBtn.classList.remove('bg-red-100', 'text-red-700', 'hover:bg-red-200');
                editBtn.classList.add('bg-indigo-100', 'text-indigo-700', 'hover:bg-indigo-200');
            } else {
                // Currently in view mode, switch to edit mode
                viewMode.classList.add('hidden');
                editForm.classList.remove('hidden');
                editBtn.textContent = 'Cancel'; // Change button text to indicate active edit mode
                editBtn.classList.remove('bg-indigo-100', 'text-indigo-700', 'hover:bg-indigo-200');
                editBtn.classList.add('bg-red-100', 'text-red-700', 'hover:bg-red-200'); // Change button style
            }
        }

        // Apply Tailwind classes to Django form fields rendered by {{ form.field }}
        // This makes sure dynamically rendered fields look good
        document.addEventListener('DOMContentLoaded', function() {
            const formElements = document.querySelectorAll('#profileEditForm input');
            formElements.forEach(function(input) {
                // Only apply if it's not a hidden input or submit button
                if (input.type !== 'hidden' && input.type !== 'submit' && input.type !== 'button') {
                    input.classList.add('w-full', 'p-3', 'border', 'border-gray-300', 'rounded-lg', 'focus:ring-2', 'focus:ring-indigo-500', 'focus:border-indigo-500');
                }
            });
        });