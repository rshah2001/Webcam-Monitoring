import smtplib
import imghdr
from email.message import EmailMessage

password = "mkncsskaimjbpquz"
email ="rishil13123@gmail.com"
receiver = email

def send_email(image_path):
    print("Email is being sent")
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up"
    email_message.set_content("hew, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email, password)
    gmail.sendmail(email, receiver, email_message.as_string())
    gmail.quit()
    print("Email was sent")
if __name__ == "__main__":
    send_email(image_path="images/60.png")
