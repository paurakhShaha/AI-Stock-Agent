from tools.email_sender import send_email


# Use any existing file for testing
test_file = "test_report.json"


# Create dummy report file
with open(test_file, "w", encoding="utf-8") as f:
    f.write(
        """
        {
            "message": "This is a test email from AI Stock Agent"
        }
        """
    )


# Send email
send_email(test_file)


print("Email sent successfully")