from flask import Flask, render_template, request, redirect, url_for
from app.certificate import generate_certificate

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Form for entering participant details

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    event = request.form['event']

    # Generate a certificate
    template_path = 'templates/certificate_template.png'
    output_path = f'static/certificates/{name}_certificate.png'
    generate_certificate(name, event, template_path, output_path)

    return f"Certificate generated for {name}. Download <a href='/{output_path}'>here</a>."

if __name__ == '__main__':
    app.run(debug=True)
    
    
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail.init_app(app)