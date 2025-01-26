from flask import Flask, render_template, request
from gen_qr import generate_qr_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    qr_type = request.form.get('type')
    data = ""  # Initialize data

    # Handle different QR types (your existing logic here)
    if qr_type == 'url':
        url = request.form.get('url')
        if not url:
            return "No URL provided."
        data = url
        filename = "url_qrcode.png"
    elif qr_type == 'vcard':
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        phone = request.form.get('phone', '').strip()
        email = request.form.get('email', '').strip()
        company = request.form.get('company', '').strip()
        job_title = request.form.get('job_title', '').strip()
        street = request.form.get('street', '').strip()
        city = request.form.get('city', '').strip()
        country = request.form.get('country', '').strip()

        # Construct the vCard data with all placeholders in the ADR field
        data = f"""BEGIN:VCARD
        VERSION:3.0
        N:{last_name};{first_name};;;
        FN:{first_name} {last_name}
        TEL:{phone}
        EMAIL:{email}
        ORG:{company}
        TITLE:{job_title}
        ADR:;;{street};{city};;;{country}
        END:VCARD"""
        filename = "vcard_qrcode.png"
    elif qr_type == 'text':
        text = request.form.get('text', '').strip()
        if not text:
            return "No text provided."
        data = text
        filename = "text_qrcode.png"
    elif qr_type == 'email':
        email = request.form.get('email_address', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        if not email or not subject or not message:
            return "Email, subject, and message are required."

        data = f"mailto:{email}?subject={subject}&body={message}"
        filename = "email_qrcode.png"
    elif qr_type == 'sms':
        phone = request.form.get('sms_phone', '').strip()
        sms_message = request.form.get('sms-message', '').strip()

        if not phone or not sms_message:
            return "Phone number and message are required."

        data = f"sms:{phone}?body={sms_message}"
        filename = "sms_qrcode.png"
    elif qr_type == 'wifi':
        network_name = request.form.get('network-name', '').strip()
        password = request.form.get('wifi-password', '').strip()
        encryption = request.form.get('encryption', 'WPA/WPA2')

        if not network_name or not password:
            return "Network name and password are required."

        data = f"WIFI:T:{encryption};S:{network_name};P:{password};;"
        filename = "wifi_qrcode.png"
    elif qr_type == 'whatsapp':
        whatsapp_number = request.form.get('whatsapp-number', '').strip()
        whatsapp_message = request.form.get('whatsapp-message', '').strip()

        if not whatsapp_number or not whatsapp_message:
            return "Phone number and message are required."

        data = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
        filename = "whatsapp_qrcode.png"
    else:
        return "Invalid type selected."

    # Generate the QR code
    qr_code = generate_qr_code(data)
    return render_template('index.html', qr_code=qr_code, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)