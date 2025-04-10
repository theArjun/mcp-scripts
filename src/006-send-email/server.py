import os
import smtplib

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables from .env file
load_dotenv()

# Initialize FastMCP with a name
mcp = FastMCP("Arjuns Personal Mail Sender")

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")


@mcp.tool("send_email", description="Send an email using SMTP server. ")
def send_email(
    recipient_email: str,
    subject: str,
    body: str,
):
    """
    Send an email using SMTP server.
    """
    try:
        # Create a secure SSL context
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(SENDER_EMAIL, recipient_email, message)
        return "Email sent successfully"
    except Exception as e:
        return f"Failed to send email: {e}"
