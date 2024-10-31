import os
import io
import base64
from flask import Flask, render_template_string, request, url_for, redirect
import segno

app = Flask(__name__)

# HTML Template for landing page and displaying QR Code
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code Generator</title>
</head>
<body>
    <h1>QR Code Generator</h1>
    <form action="{{ url_for('generate_qr') }}" method="post">
        <label for="data">Input your message:</label>
        <input type="text" name="data" id="data" required>
        <button type="submit">Generate QR Code</button>
    </form>

    {% if message and qr_image %}
    <h2>Generated QR Code for: "{{ message }}"</h2>
    <img src="data:image/svg+xml;base64,{{ qr_image }}" alt="QR Code">
    {% endif %}
</body>
</html>
'''

def home():
    return render_template_string(HTML_TEMPLATE)

# QR Code generation and display controller
@app.route('/gen_qr_code_view', methods=['POST'])
def gen_qr_code_view():
    # Get the data from the form
    message = request.form['data']

    # Generate the QR code using segno
    qr = segno.make(message)
    buffer = io.BytesIO()
    qr.save(buffer, kind='svg', scale=3, dark='darkblue')
    base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # Render the template with the generated QR code and message
    return render_template_string(HTML_TEMPLATE, message=message, qr_image=base64_img)

if __name__ == '__main__':
    # Run the application in development mode
    app.run(host='0.0.0.0', port=5000)
