import os
import sys
import list_read as ls
import list_read_d as ls_d


list_sel_d = "sample"
email_adr_d, cover_list_d, resume_list_d, msg_list_d, pos_list_d= ls_d.list_get(list_sel_d)

def parser_d(rref_d):
    print("Cads search: " + rref_d)
    l_d = [email_adr_d.index(i_d) for i_d in email_adr_d if rref_d in i_d]
    if (len(l_d) == 0):
        print("Entry Does not exist in: Sample.xlsx \n")
        return 0
    else:
        for m_d in range(len(l_d)):
            print(str(email_adr_d.index(email_adr_d[l_d[m_d]])+2), end = ' ')
            print(email_adr_d[l_d[m_d]] + " << " + list_sel_d)
            num = email_adr_d.index(email_adr_d[l_d[m_d]])+2
            return num
