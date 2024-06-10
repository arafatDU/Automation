import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
TO_ADDRESS = "arafat.du.iit@gmail.com"

# Function to send email
def send_email():
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Subject'] = "Daily Report - {}".format(datetime.now().strftime("%Y-%m-%d"))

    # Body of the email
    body = "This is the daily report email sent on {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    msg.attach(MIMEText(body, 'plain'))

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

# Send the email
send_email()
