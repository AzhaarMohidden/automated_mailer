# import smtplib
# import os
# import imghdr
#
# def calc(operator = str(input("Operator: ")), num1 = int(input("num1: ")), num2 = int(input("num2: "))):
#     if operator == "add":
#         return num1 + num2
#     elif operator == "sub":
#         return num1 - num2
#     elif operator == "mul":
#         return num1 * num2
#     elif operator == "div":
#         return num1 / num2
#
#
#
# with open('random_image.jpeg', 'rb') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#
# CV_available = ['ELV', 'Electrical', 'R&D', 'test']
#
# def CV_type():
#     print("PLease select the type Of job applying for...")
#     i = 1
#     for cv in CV_available:
#         print(str(CV_available.index(cv)+1) + ". " + cv)
#         i = i+1
# # operator = str(input("Operator: "))
# # num1 = int(input("num1: "))
# # num2 = int(input("num2: "))
# try:
#     result = calc()
#     print(result)
# except ZeroDivisionError:
#     print('you cannot divide by zero...')

#
# import Filename as fn
#
# data = fn.list_dir(r"E:\Qatar job\automated\resume")
# print(data)
# from email.message import EmailMessage
#
# with open("Pure_R&D_mail.txt") as f:
#     data = f.read()
#     print(data)

#
# import smtplib, ssl
#
# def read_creds():
#     user = passw = ""
#     with open("credentials.txt", "r") as f:
#         file = f.readlines()
#         user = file[0].strip()
#         passw = file[1].strip()
#
#     return user, passw
#
#
# port = 465
#
# sender, password = read_creds()
#
# recieve = sender
#
# message = """\
# Subject: Python Email Tutorial
#
# This is from python!
#
# Tech With Tim
# """
#
# context = ssl.create_default_context()
#
# print("Starting to send")
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login(sender, password)
#     server.sendmail(sender, recieve, message)
#
# print("sent email!")
x = 1
while(1):
    x = x +1
    print(x)
