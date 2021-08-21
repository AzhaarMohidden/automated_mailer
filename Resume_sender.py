import smtplib, ssl
import os
import sys
from email.message import EmailMessage
import Filename as fn
import write_sheet as ws
sender_email = "azhaarm94@gmail.com"
password = "scscsgcvcpfastog"

# CV_available = ['Azhaar_ resume_ELV.docx','Azhaar_resume_ER.docx', 'Azhaar_resume_G.docx', 'Azhaar_resume_R.docx']
# cover_available = ['Cover_letter_BMS.docx', 'Cover_letter_E.docx','Cover_letter_Electrical&Electronics.docx', 'Cover_letter_Electrical.docx', 'Cover_letter_Electronics.docx','Cover_letter_RD.docx']
# message_available = ['Pure ELectrical - posted', 'Pure R&D - posted', 'ELV - posted', 'Electrical & Electronics - posted', 'Pure ELectrical - not posted', 'Pure R&D - not posted', 'ELV - not posted', 'Electrical & Electronics - not posted']
CV_available = fn.list_dir(r'C:\Azhaar_Data\Git\automated_mailer\resume')
cover_available = fn.list_dir(r'C:\Azhaar_Data\Git\automated_mailer\cover')
message_available = fn.list_dir(r'C:\Azhaar_Data\Git\automated_mailer\message')
attachment = ['Azhaar_ resume_ELV.docx', 'cover', 'Biomed_International_Service_letter.pdf', 'Call_Lanka_Telecom_Serviceletter.pdf', 'Terabyte_Tech_service_Letter.pdf']
context = ssl.create_default_context()

def CV_type():
    print("Please select the type Of job applying for...")
    for cv in CV_available:
        print(str(CV_available.index(cv)+1) + ". " + cv)
    cv_type_selection = int(input("\n selection in Numbers: "))
    return CV_available[cv_type_selection - 1]
    print("CV TYPE Selected...")

def cover_type():
    """ make covers for 3 types with posted and non posted
    """
    for c in cover_available:
        print(str(cover_available.index(c) + 1) + ". " + c)
    cover_type_selection = int(input("\n Please select cover type in Number: "))
    print("Cover type selected....")
    return cover_available[cover_type_selection - 1]

def msg_type(position):
    ans = "N"
    while (ans == "N" or "n" ):
        for m in message_available:
            print(str(message_available.index(m) + 1) + ". " + m)
        message_type_selection = int(input("\n Please select message type in Number: "))
        print(message_available[message_type_selection - 1])
        l = open(message_available[message_type_selection - 1])
        print(l.read().format(position))
        ans = str(input("Confirm Y/N: "))
        if ans == "y":
            break
    print("Message type Selected ....")
    return message_available[message_type_selection - 1]


def details():
    applying_position = input(str("\nPlease Enter the position that you are applying for..."))
    resume_type = CV_type() #select the type of cv from 3 cvs
    cover_letter_type = cover_type()
    message_type = msg_type(applying_position)

    return applying_position, resume_type, cover_letter_type, message_type

def msg_send(msg):
    f = open(msg)
    msg1_read = f.read()
    msg_read = msg1_read.format(position)
    message = EmailMessage()
    message['Subject'] = "{} Engineer Resume".format(position)
    message['From'] = sender_email
    message['To'] = rec_email
    message.set_content(msg_read)
    for x in attachment:
        a = open(attachment[attachment.index(x)], 'rb')
        file_data = a.read()
        file_name = a.name
        message.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename=file_name)
        print("attached file: " + file_name)
    print("Initializing server...")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    # server.ehlo()
    # server.starttls()
    # server.ehlo()
    server.login(sender_email, password)
    print("login success..")
    server.send_message(message)
    print("email sent...")
    return message

try:
    mode_sel = sys.argv[1] # not send mail "save"
except:
    mode_sel = ""

while(1):
    rec_email = str(input("please enter reciever email: "))
    ad_url = str(input("Please paste url: "))
    if (ad_url == ""):
        ad_url = "No_URL"
    position, attachment[0], attachment[1], message_t = details()
    print("Please verify the below selection....")
    print("Position: " + position)
    print("Resume: " + attachment[0])
    print("cover: " + attachment[1])
    print("message: " + message_t)
    print("Email Sent to: " + rec_email)
    # ws.write_mail(rec_email, attachment[0], attachment[1],  message_t, position, ad_url)
    os.system("pause")
    if (mode_sel== "save"):
        print("details saved to excel. please schedule send.. Later")
    else:
        msg_send(message_t)
