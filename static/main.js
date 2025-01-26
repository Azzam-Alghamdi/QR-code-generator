function toggleInputs() {
    const type = document.querySelector('input[name="type"]:checked').value;
    const sections = {
        url: document.getElementById('url-inputs'),
        vcard: document.getElementById('vcard-inputs'),
        text: document.getElementById('text-inputs'),
        email: document.getElementById('email-inputs'),
        sms: document.getElementById('sms-inputs'),
        wifi: document.getElementById('wifi-inputs'),
        whatsapp: document.getElementById('whatsapp-inputs')
    };

    // Hide all and disable/remove required
    Object.values(sections).forEach(section => {
        if (section) {
            section.style.display = 'none';
            const inputs = section.querySelectorAll('input, textarea');
            inputs.forEach(input => {
                input.removeAttribute('required');
                input.disabled = true;
            });
        }
    });

    // Show active section and enable/set required
    const activeSection = sections[type];
    if (activeSection) {
        activeSection.style.display = 'block';
        const inputs = activeSection.querySelectorAll('input, textarea');
        inputs.forEach(input => {
            input.setAttribute('required', 'required');
            input.disabled = false;
        });
    }
}

// Initialize with URL selected
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('input[value="url"]').checked = true;
    toggleInputs();
});

// Function to open the modal and display the QR code
function openModal() {
    const modal = document.getElementById('qr-modal');
    modal.style.display = 'block';

    // Set the download link for the QR code
    const qrImage = document.getElementById('qr-image');
    const downloadBtn = document.getElementById('download-btn');
    if (qrImage && downloadBtn) {
        downloadBtn.href = qrImage.src; // Set the href to the QR code image source
    }
}

// Function to close the modal
function closeModal() {
    const modal = document.getElementById('qr-modal');
    modal.style.display = 'none';
}

// Automatically open the modal if a QR code is generated
document.addEventListener('DOMContentLoaded', function () {
    const qrCode = document.querySelector('#qr-modal img');
    if (qrCode && qrCode.src) {
        openModal();
    }
});