document.addEventListener('DOMContentLoaded', function () {
    // Get all switches with a class (assuming you add a common class to all switches)
    var switches = document.querySelectorAll('.toggle-switch');

    // Iterate over each switch
    switches.forEach(function (switchInput) {
        var inactiveLabel = document.getElementById('inactiveLabel' + switchInput.dataset.bookId);
        var activeLabel = document.getElementById('activeLabel' + switchInput.dataset.bookId);

        // Initial label state
        updateLabel();

        // Update label and value when the switch state changes
        switchInput.addEventListener('change', function () {
            updateLabel();
            updateValue();
        });

        function updateLabel() {
            if (switchInput.checked) {
                inactiveLabel.style.display = 'none';
                activeLabel.style.display = 'inline-block';
            } else {
                activeLabel.style.display = 'none';
                inactiveLabel.style.display = 'inline-block';
            }
        }

        function updateValue() {
            switchInput.value = switchInput.checked;
        }
    });
});
