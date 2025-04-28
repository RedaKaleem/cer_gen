import os
from flask import request

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    # Save the uploaded file
    csv_file = request.files['csv_file']
    file_path = os.path.join('input', csv_file.filename)
    csv_file.save(file_path)

    # Process the CSV
    participants = read_csv(file_path)

    # Generate certificates and send emails (same logic as before)
    for participant in participants:
        name = participant['Name']
        email = participant['Email']
        event = participant['Event']

        template_path = 'templates/certificate_template.png'
        output_path = f'static/certificates/{name}_certificate.png'
        generate_certificate(name, event, template_path, output_path)

        subject = f"Your Certificate for {event}"
        body = f"Dear {name},\n\nAttached is your certificate for participating in {event}.\n\nBest regards,\nCertificate Generator"
        send_email(app, email, subject, body, output_path)

    return "Certificates generated and emailed successfully!"