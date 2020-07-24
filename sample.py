# import smtplib
# import os
# from email.message import EmailMessage
# import Filename as fn
# import write_sheet as ws
# import list_read as ls
# sender_email = "azhaarm94@gmail.com"
# password = "lsupvvcwfzuwciou"
# attachment = ['Azhaar_ resume_ELV.docx', 'cover', 'Biomed_International_Service_letter.pdf', 'Call_Lanka_Telecom_Serviceletter.pdf', 'Terabyte_Tech_service_Letter.pdf']
#
# email_adr, cover_list, resume_list, msg_list, pos_list = ls.list_get()
#
# def msg_send(msg):
#     f = open(msg)
#     msg1_read = f.read()
#     msg_read = msg1_read.format(position)
#     message = EmailMessage()
#     message['Subject'] = "{} Engineer Resume".format(position)
#     message['From'] = sender_email
#     message['To'] = rec_email
#     message.set_content(msg_read)
#     for x in attachment:
#         a = open(attachment[attachment.index(x)], 'rb')
#         file_data = a.read()
#         file_name = a.name
#         message.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename=file_name)
#         print("attached file: " + file_name)
#     print("Initializing server...")
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login(sender_email, password)
#     print("login success..")
#     server.send_message(message)
#     print("email sent...")
#     return message
#
# def temp_print():
#     for num in email_adr:
#         print(email_adr[email_adr.index(num)] + ", "  +cover_list[email_adr.index(num)] +", "+resume_list[email_adr.index(num)]+", "+ msg_list[email_adr.index(num)]+ ", "+pos_list[email_adr.index(num)] )
#
# def send(sender, reciever, pas, position, messg, res, cover):
#     print(messg)


# import os
# # os.system("exit()")
#
#  string = "start, echo hello world"
# #
# # os.system(string2)
# # # os.system('pause')
# # os.system('exit')

import os
# from email.message import EmailMessage
import Filename as fn
import sys
import write_sheet as ws
import list_read as ls

ref_email = sys.argv[1]
email_adr, cover_list, resume_list, msg_list, pos_list = ls.list_get()
def temp_print(ref):
    for num in email_adr:
        if (num == ref):
            print(str(email_adr.index(num) + 1)+"/"+str(len(email_adr))+" >> "+str(email_adr.index(num) + 1)+ ". " + email_adr[email_adr.index(num)] + ", "  +cover_list[email_adr.index(num)] +", "+resume_list[email_adr.index(num)]+", "+ msg_list[email_adr.index(num)]+ ", "+pos_list[email_adr.index(num)] )

def send(sender, reciever, pas, position, messg, res, cover):
    print(messg)


temp_print(ref_email)
