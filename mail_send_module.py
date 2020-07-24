import smtplib, ssl
# import os
from email.message import EmailMessage
from tqdm.auto import tqdm
from time import sleep
# import imghdr
# import pandas as pd

CV_available = ['Azhaar_ resume_ELV.docx','Azhaar_resume_ER.docx', 'Azhaar_resume_G.docx', 'Azhaar_resume_R.docx']
cover_available = ['Cover_letter_BMS.docx', 'Cover_letter_E.docx','Cover_letter_Electrical&Electronics.docx', 'Cover_letter_Electrical.docx', 'Cover_letter_Electronics.docx','Cover_letter_RD.docx']
message_available = ['Pure ELectrical - posted', 'Pure R&D - posted', 'ELV - posted', 'Electrical & Electronics - posted', 'Pure ELectrical - not posted', 'Pure R&D - not posted', 'ELV - not posted', 'Electrical & Electronics - not posted']
attachment = ['Azhaar_ resume_ELV.docx', 'cover', 'Biomed_International_Service_letter.pdf', 'Call_Lanka_Telecom_Serviceletter.pdf', 'Terabyte_Tech_service_Letter.pdf']
# context = ssl.create_default_context()
#
# # sender_email = "azhaarm94@gmail.com"
# # password = "lsupvvcwfzuwciou"
#
# # sender_email = "azhaarm94@gmail.com"
# # password = "scscsgcvcpfastog"
# # sender_email = "azhaarm9494@gmail.com"
# # password = "wnblipdnscxfsnvn"
# print("Initializing server...")
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
# # server.ehlo()
# # server.starttls()
# # server.ehlo()
# server.login(sender_email, password)
print("login success..")
def send(sender, reciever, pas, position, messg, res, cover, server):
    print("Attachment initiation..", end = '\r')
    attachment[0] = res
    attachment[1] = cover
    print("Sender mail initiation..", end = '\r')
    sender_email = sender
    password = pas
    rec_email = reciever
    position = position
    print("Message openning....", end = '\r')
    f = open(messg)
    msg_cont = f.read().format(position)
    message = EmailMessage()
    message['Subject'] = "{} Engineer Resume".format(position)
    message['From'] = sender_email
    message['To'] = rec_email
    message.set_content(msg_cont)
    print("EMail Setup...", end = '\r')
    for x in attachment:
        a = open(attachment[attachment.index(x)], 'rb')
        file_data = a.read()
        file_name = a.name
        strn = "Reading..." + file_name
        print(strn, end = '\r')
        message.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename=file_name)
        print("attached file: " + file_name)
    print("Please Wait sending mail to..........." + rec_email)
    print("Sending Email", end = '\r')
    server.send_message(message)
    print("Sending Email", end = '\r')
    return message


# print("Attachment initiation..", end = '\r')
# attachment[0] = res
# attachment[1] = cover
# print("Sender mail initiation..", end = '\r')
# sender_email = sender
# password = pas
# rec_email = reciever
# position = position
# print("Message openning....", end = '\r')
# f = open(messg)
# msg_cont = f.read().format(position)
# message = EmailMessage()
# message['Subject'] = "{} Engineer Resume".format(position)
# message['From'] = sender_email
# message['To'] = rec_email
# message.set_content(msg_cont)
# print("EMail Setup...", end = '\r')
# for x in attachment:
#     a = open(attachment[attachment.index(x)], 'rb')
#     file_data = a.read()
#     file_name = a.name
#     strn = "Reading..." + file_name
#     print(strn, end = '\r')
#     message.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename=file_name)
#     print("attached file: " + file_name)
# print("Please Wait sending mail to..........." + rec_email)
# print("Sending Email", end = '\r')
# server.send_message(message)
# print("Sending Email", end = '\r')
