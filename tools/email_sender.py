import smtplib

from email.message import EmailMessage

from dotenv import dotenv_values


config=dotenv_values(".env")



def send_email(
    filename
):


    msg=EmailMessage()


    msg["Subject"] = (
        "Weekly AI Stock Analysis Report"
    )


    msg["From"] = config["EMAIL"]

    msg["To"] = config["TARGET_EMAIL"]



    msg.set_content(
        """
        Your weekly AI stock analysis report
        is attached.
        """
    )



    with open(
        filename,
        "rb"
    ) as f:


        file_data=f.read()



    msg.add_attachment(

        file_data,

        maintype="application",

        subtype="json",

        filename=filename

    )



    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:


        smtp.login(

            config["EMAIL"],

            config["APP_PASSWORD"]

        )


        smtp.send_message(msg)