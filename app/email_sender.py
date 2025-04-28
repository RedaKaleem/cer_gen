from flask_mail import Mail, Message

mail = Mail()

def send_email(app, recipient, subject, body, attachment_path):
    with app.app_context():
        msg = Message(subject, recipients=[recipient])
        msg.body = body

        with app.open_resource(attachment_path) as fp:
            msg.attach("certificate.png", "image/png", fp.read())

        mail.send(msg)
        