from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
TO_ADDRESS = "recipient_email@example.com"

# Function to send email
def send_email():
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Subject'] = "Daily Report - {}".format(datetime.now().strftime("%Y-%m-%d"))

    # HTML body of the email
    html = f"""
    <html>
    <head></head>
    <body>
        <h1 style="color: #333333;">Daily Report</h1>
        <p><b>Date:</b> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p style="color: #ff5733;">This is the <b>daily report</b> email sent on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.</p>
        <p>Here is an image for your reference:</p>
        <img src="https://via.placeholder.com/150" alt="Sample Image">
    </body>
    </html>
    """

    # Attach the HTML body to the email
    msg.attach(MIMEText(html, 'html'))

    try:
        # Connect to the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send the email
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, TO_ADDRESS, text)
        print("Email sent successfully")

    except Exception as e:
        print("Failed to send email:", str(e))
    finally:
        server.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email_route():
    send_email()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
