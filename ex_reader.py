# import smtplib
import os
# from email.message import EmailMessage
import list_read as ls
import sys

arg = sys.argv[1]
email_adr, cover_list, resume_list, msg_list, pos_list, url_list = ls.list_get(arg)

def temp_print():
    for num in email_adr:
        print(str(email_adr.index(num) + 1)+"/"+str(len(email_adr))+" >> "+str(email_adr.index(num) + 1)+ ". " + email_adr[email_adr.index(num)] + ", "  +cover_list[email_adr.index(num)] +", "+resume_list[email_adr.index(num)]+", "+ msg_list[email_adr.index(num)]+ ", "+pos_list[email_adr.index(num)] +" , "+ url_list[email_adr.index(num)] )

def send(sender, reciever, pas, position, messg, res, cover):
    print(messg)

def remove_spaces(str):
    new_str = ""
    for i in range(len(str)):
        if (str[i] != " "):
            new_str += str[i]
    return new_str

def temp_w():
    j= len(email_adr)
    n = 1
    while(n <= j):
        print(n, end ='')
        print(" / ", end ='')
        print(j, end = '')
        try:
            print(" >> "+str(email_adr.index(email_adr[n-1])+1)+ ". " + email_adr[n-1] + ", "  +cover_list[n-1] +", "+ resume_list[n-1]+", "+ msg_list[n-1]+ ", "+pos_list[n-1] + ", " + url_list[n-1])
        except UnicodeEncodeError:
            print(" Unicode encode error at: " + str(n))
        n = n+1



# a = 0
# while(a<100):
#     # temp_print()
#     temp_w()
#     a=a+1
# count_w()
temp_w()
