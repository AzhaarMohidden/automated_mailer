# import smtplib
# import os
# from email.message import EmailMessage
# import imghdr
import pandas as pd

try:
    def list_get(sel):
        print("Reading << " + sel )
        if (sel == "Excel"):
            df = pd.read_excel(r'E:\Qatar job\automated\Excel_list.xlsx')
        elif (sel == "sample"):
            df = pd.read_excel(r'E:\Qatar job\automated\sample_email.xlsx')
        email_list = df['list'].tolist()
        cover_list = df['cover_list'].tolist()
        resume_list = df['resume_list'].tolist()
        msg_list = df['msg_list'].tolist()
        pos_list = df['pos_list'].tolist()
        url_list = df['url_list'].tolist()
        return email_list, cover_list, resume_list, msg_list, pos_list, url_list
except IndexError:
    print("Please pass list argument")

    # for x in email_list:
    #     print(str(email_list.index(x) + 1) +". "  + email_list[email_list.index(x)])
