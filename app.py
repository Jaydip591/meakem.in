from flask import Flask,render_template,request,redirect,flash
from flask_mail import Mail, Message

app =Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'info@meakem.in'
app.config['MAIL_PASSWORD'] = 'hwzc geli jxpk llet'
app.config['MAIL_DEFAULT_SENDER'] = 'info@meakem.in'
DRIVE_FILE_LINK = 'https://drive.google.com/file/d/1HlYOWPlNlRRLqnaMDm1MJsbR_ln_TPk5/view?usp=sharing'

mail = Mail(app)
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Handles catalog requests and sends a Canva file link via email."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            flash('Both name and email are required!', 'danger')
            return redirect('/home')

        try:
            file_link = DRIVE_FILE_LINK

            subject = "Your Requested Product Catalog"
            message_body = f"""
            Dear {name},

            Thank you for requesting our product catalog! 
            You can access the catalog using the following link:

            {file_link}

            Best regards,
            meakem
            """
            msg = Message(subject, recipients=[email], body=message_body)
            mail.send(msg)

            flash('The product catalog has been sent to your email successfully!', 'success')

        except Exception as e:
            flash(f'An error occurred while sending the email: {e}', 'danger')

        return redirect('/home')

    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True, port=5555)
