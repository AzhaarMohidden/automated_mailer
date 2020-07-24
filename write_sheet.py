import pandas as pd
import xlsxwriter as xl
import list_read as ls
mail_list = ["list"]
cov_list = ["cover_list"]
res_list = ["resume_list"]
ms_list = ["msg_list"]
ps_list = ["pos_list"]
URL_list = ["url_list"]




def write_mail(eid, cov, res, ms, pos, url):
    workbook = xl.Workbook("Excel_list.xlsx")
    sheet = workbook.add_worksheet()
    email_list, cover_list, resume_list, msg_list, pos_list, url_list = ls.list_get("Excel")
    mail_array = mail_list + email_list
    cov_array = cov_list + cover_list
    res_array = res_list + resume_list
    ms_array = ms_list + msg_list
    ps_array = ps_list + pos_list
    url_array = URL_list + url_list
    mail_array.append(eid)
    cov_array.append(cov)
    res_array.append(res)
    ms_array.append(ms)
    ps_array.append(pos)
    url_array.append(url)
    temp = 0
    for ids in mail_array:
        sheet.write(mail_array.index(ids), 0, ids)
        sheet.write(mail_array.index(ids), 1, cov_array[mail_array.index(ids)])
        sheet.write(mail_array.index(ids), 2, res_array[mail_array.index(ids)])
        sheet.write(mail_array.index(ids), 3, ms_array[mail_array.index(ids)])
        sheet.write(mail_array.index(ids), 4, ps_array[mail_array.index(ids)])
        sheet.write(mail_array.index(ids), 5, url_array[mail_array.index(ids)])
        temp = ids

    print("Excell Updated >>>> Location " + str(mail_array.index(temp)))
    workbook.close()
