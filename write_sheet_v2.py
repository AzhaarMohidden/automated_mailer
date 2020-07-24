import pandas as pd
import xlsxwriter as xl
# import list_read as ls
import list_read_v2 as ls2
mail_list = ["list"]
cov_list = ["cover_list"]
res_list = ["resume_list"]
ms_list = ["msg_list"]
ps_list = ["pos_list"]
URL_list = ["url_list"]
Num_list = ['Number_list']
name_list = ['Name_list']
com_list = ['Comp_list']
poss_list = ['Pos_list']
off_list = ['offer_list']
dem_list = ['dem_list']






def write_mail(eid, cov, res, ms, pos, url, sel_excel):
    if (sel_excel == "Excel"):
        workbook = xl.Workbook("Excel_list.xlsx")
        sheet = workbook.add_worksheet()
        email_list, cover_list, resume_list, msg_list, pos_list, url_list = ls2.list_get("Excel")
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
        for ids in mail_array:
            sheet.write(mail_array.index(ids), 0, ids)
            sheet.write(mail_array.index(ids), 1, cov_array[mail_array.index(ids)])
            sheet.write(mail_array.index(ids), 2, res_array[mail_array.index(ids)])
            sheet.write(mail_array.index(ids), 3, ms_array[mail_array.index(ids)])
            sheet.write(mail_array.index(ids), 4, ps_array[mail_array.index(ids)])
            sheet.write(mail_array.index(ids), 5, url_array[mail_array.index(ids)])
        print("Excell Updated>>>>")
        workbook.close()
    elif (sel_excel == "called"):
        workbook = xl.Workbook("called.xlsx")
        sheet = workbook.add_worksheet()
        Num_list_r, name_list_r, com_list_r, poss_list_r, off_list_r, dem_list_r = ls2.list_get("called")
        Num_array = Num_list + Num_list_r
        name_array = name_list + name_list_r
        com_array = com_list + com_list_r
        poss_array = poss_list + poss_list_r
        off_array = off_list + off_list_r
        dem_array = dem_list + dem_list_r
        Num_array.append(eid)
        name_array.append(cov)
        com_array.append(res)
        poss_array.append(ms)
        off_array.append(pos)
        dem_array.append(url)
        for ids in Num_array:
            sheet.write(Num_array.index(ids), 0, ids)
            sheet.write(Num_array.index(ids), 1, name_array[Num_array.index(ids)])
            sheet.write(Num_array.index(ids), 2, com_array[Num_array.index(ids)])
            sheet.write(Num_array.index(ids), 3, poss_array[Num_array.index(ids)])
            sheet.write(Num_array.index(ids), 4, off_array[Num_array.index(ids)])
            sheet.write(Num_array.index(ids), 5, dem_array[Num_array.index(ids)])
        print("Excell Updated>>>>")
        workbook.close()
