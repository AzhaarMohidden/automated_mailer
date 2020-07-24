import smtplib
import os
from email.message import EmailMessage
import imghdr
import sys
import pandas as pd
import mail_send_module as ms
import Sample_list_read as ls

sender_email = "azhaarm94@gmail.com"
password = "scscsgcvcpfastog"
# f = open("Pure_R&D_mail.txt")
# msg_read = f.read()
# ms.send("azhaarm94@gmail.com", "azhaarm94@protonmail.com", "lsupvvcwfzuwciou", "R&D", "R&D Engineer", msg_read)
email_adr, cover_list, resume_list, msg_list, pos_list = ls.list_get()
print("Initiating message send....")
for l in email_adr:
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Starting to send>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    ms.send("azhaarm94@gmail.com", l, "lsupvvcwfzuwciou", pos_list[email_adr.index(l)], msg_list[email_adr.index(l)], resume_list[email_adr.index(l)], cover_list[email_adr.index(l)])
    print(str(email_adr.index(l) + 1) + "/" + str(len(email_adr)) + ">> mail sent to " + l)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Message send>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n ")
