import smtplib, ssl
import os
from email.message import EmailMessage
import imghdr
import sys
from tqdm.auto import tqdm
import pandas as pd
import mail_send_module as ms
import list_read as ls
# module import

number = int(sys.argv[1])
acc_sel = int(sys.argv[2])
list_sel = sys.argv[3]
# input sample [ python main.py 0 1 Excel ] => [python main.py number__to_start_from sender_email_select List_selection]

if (acc_sel == 1):
    sender_email = "azhaarm94@gmail.com"
    password = "scscsgcvcpfastog"
elif (acc_sel == 2):
    sender_email = "azhaarm9494@gmail.com"
    password = "wnblipdnscxfsnvn"
# select account

context = ssl.create_default_context()
print("Initializing server...")
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
server.login(sender_email, password)
email_adr, cover_list, resume_list, msg_list, pos_list, url_list = ls.list_get(list_sel)
print("Initiating message send....")

l = number
def remove_spaces(str):
    new_str = ""
    for i in range(len(str)):
        if (str[i] != " "):
            new_str += str[i]
    return new_str

while(l < len(email_adr)):
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Starting to send>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    e_str = remove_spaces(email_adr[l])
    # ms.send("azhaarm94@gmail.com", e_str, "lsupvvcwfzuwciou", pos_list[email_adr.index(l)], msg_list[email_adr.index(l)], resume_list[email_adr.index(l)], cover_list[email_adr.index(l)])
    ms.send(sender_email, e_str, password, pos_list[l], msg_list[l], resume_list[l], cover_list[l], server)
    print(str(l + 1) + "/" + str(len(email_adr)) + " - "+" Sent from: "+ sender_email +" >>>> mail sent to: " + email_adr[l])
    if (url_list[l] == "No_URL"):
        pass
    else:
        print("Job ad Posted On: " + url_list[l])
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Message sent>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(str(int(((l + 1) / len(email_adr)) * 100))+"% Completed..."  )
    print("\n ")
    l = l+1
