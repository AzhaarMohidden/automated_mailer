import smtplib
import os
from email.message import EmailMessage
import imghdr
import pandas as pd

print("Python Email client.....")

sender_email = "azhaarm94@gmail.com"
password = "lsupvvcwfzuwciou"

df = pd.read_excel(r'E:\Qatar job\automated\sheet.xlsx')
email_list = df['list'].tolist()

def msg(x):
    # print(str(email_list.index(x) + 1) +". "  + email_list[email_list.index(x)])
    rec_email = email_list[email_list.index(x)]
    position = "test position"+str(email_list.index(x))
    message = EmailMessage()
    message['Subject'] = "{} Engineer Resume".format(position)
    message['From'] = sender_email
    message['To'] = rec_email
    message.set_content("""
    This is an automated EmailMessage
    line 2
    """)
    with open('Azhaar_resume_G.docx', 'rb') as f:
        file_data = f.read()
        file_name = f.name
    message.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename=file_name)
    server.send_message(message)
    print("sent email " + str(email_list.index(x))  + " to " + rec_email)
    return message



print("Initializing server...")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender_email, password)
print("login success..")

print("sending email....")
for c in email_list:
    msg(c)
print("email sent...")
