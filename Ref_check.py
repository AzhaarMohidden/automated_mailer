import os
# from email.message import EmailMessage
import Filename as fn
import sys
import write_sheet as ws
import list_read as ls
list_sel = sys.argv[1]
ref_email = sys.argv[2]

# Sample call python Ref_check.py sample azhaar

email_adr, cover_list, resume_list, msg_list, pos_list, url_list = ls.list_get(list_sel)

def parser(rref):
        l = [email_adr.index(i) for i in email_adr if rref in i]
        for m in range(len(l)):
            print(str(email_adr.index(email_adr[l[m]])+2), end = ' ')
            print(email_adr[l[m]])
        print("Total found " + str(len(l)))
def temp_print(ref):
    available = False
    for num in email_adr:
        if (num == ref):
            print(str(email_adr.index(num) + 1)+"/"+str(len(email_adr))+" >> "+str(email_adr.index(num) + 1)+ ". " + email_adr[email_adr.index(num)] + ", "  +cover_list[email_adr.index(num)] +", "+resume_list[email_adr.index(num)]+", "+ msg_list[email_adr.index(num)]+ ", "+pos_list[email_adr.index(num)] )
            available = True
    if (available == False):
        print("Entry Not available, please apply...")
def send(sender, reciever, pas, position, messg, res, cover):
    print(messg)


# temp_print(ref_email)
parser(ref_email)
