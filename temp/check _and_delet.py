import os
# from email.message import EmailMessage
import Filename as fn
import sys
import write_sheet as ws
import list_read as ls
import list_read_d as ls_d
import concurrent.futures
# list_sel = sys.argv[1]
# ref_email = sys.argv[1]

# Sample call python Ref_check.py sample azhaar
list_sel = "sample"
list_sel_d = "Excel"


email_adr, cover_list, resume_list, msg_list, pos_list, url_list = ls.list_get(list_sel)
email_adr_d, cover_list_d, resume_list_d, msg_list_d, pos_list_d= ls_d.list_get(list_sel_d)

def parser_d(rref_d):
    l_d = [email_adr_d.index(i_d) for i_d in email_adr_d if rref_d in i_d]
    for m_d in range(len(l_d)):
        print(str(email_adr_d.index(email_adr_d[l_d[m_d]])+2), end = ' ')
        print(email_adr_d[l_d[m_d]] + " << " + list_sel_d)
        number = email_adr.index(email_adr[l[m]])+2
    # print("Total found " + str(len(l_d)))
    return number

def parser(rref):
    l = [email_adr.index(i) for i in email_adr if rref in i]
    for m in range(len(l)):
        print(str(email_adr.index(email_adr[l[m]])+2), end = ' ')
        print(email_adr[l[m]] + " << " + list_sel)
        number = email_adr.index(email_adr[l[m]])+2
    # print("Total found " + str(len(l)))
    return len(l)

def temp_print(ans):

    # for num in email_adr:
        # if (num == ref):
        #     print(str(email_adr.index(num) + 1)+"/"+str(len(email_adr))+" >> "+str(email_adr.index(num) + 1)+ ". " + email_adr[email_adr.index(num)] + ", "  +cover_list[email_adr.index(num)] +", "+resume_list[email_adr.index(num)]+", "+ msg_list[email_adr.index(num)]+ ", "+pos_list[email_adr.index(num)] )
        #     available = True
    if (ans == 0):
        print("Entry Not available, please apply...")

def send(sender, reciever, pas, position, messg, res, cover):
    print(messg)

# def mail_checker():
#     a= parser(ref_email)
#     b= parser_d(ref_email)
#     c = a+b
#     print("total found: " + str(a + b))
#     temp_print(c)
# if __name__ == '__main__':
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         f1 = executor.submit(parser, ref_email)
#         f2 = executor.submit(parser_d, ref_email)
#
#         print(f1.result() + f2.result())
