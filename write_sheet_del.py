import pandas as pd
import xlsxwriter as xl
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






def write_mail(sel_excel, delt):
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
        ids_c = 0
        for ids in mail_array:
            if (mail_array.index(ids) == delt):
                print("Deleted: " + str(mail_array.index(ids)) +", "+ ids )
                pass
            else:
                sheet.write(ids_c, 0, ids)
                sheet.write(ids_c, 1, cov_array[mail_array.index(ids)])
                sheet.write(ids_c, 2, res_array[mail_array.index(ids)])
                sheet.write(ids_c, 3, ms_array[mail_array.index(ids)])
                sheet.write(ids_c, 4, ps_array[mail_array.index(ids)])
                sheet.write(ids_c, 5, url_array[mail_array.index(ids)])
                ids_c = ids_c + 1
        print("Excell Updated>>>>")
        workbook.close()
    elif (sel_excel == "sample"):
        workbook = xl.Workbook("sample_email.xlsx")
        sheet = workbook.add_worksheet()
        email_list, cover_list, resume_list, msg_list, pos_list, url_list = ls2.list_get("sample")
        mail_array = mail_list + email_list
        cov_array = cov_list + cover_list
        res_array = res_list + resume_list
        ms_array = ms_list + msg_list
        ps_array = ps_list + pos_list
        url_array = URL_list + url_list
        ids_c = 0
        for ids in mail_array:
            if (mail_array.index(ids) == delt):
                print("Deleted: " + str(mail_array.index(ids)) +", "+ ids )
                pass
            else:
                sheet.write(ids_c, 0, ids)
                sheet.write(ids_c, 1, cov_array[mail_array.index(ids)])
                sheet.write(ids_c, 2, res_array[mail_array.index(ids)])
                sheet.write(ids_c, 3, ms_array[mail_array.index(ids)])
                sheet.write(ids_c, 4, ps_array[mail_array.index(ids)])
                sheet.write(ids_c, 5, url_array[mail_array.index(ids)])
                ids_c = ids_c +1
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
        ids_c = 0
        for ids in Num_array:
            if (Num_array.index(ids) == delt):
                print("Deleted: " + str(Num_array.index(ids)) +", "+ ids )
                pass
            else:
                sheet.write(ids_c, 0, ids)
                sheet.write(ids_c, 1, name_array[mail_array.index(ids)])
                sheet.write(ids_c, 2, com_array[mail_array.index(ids)])
                sheet.write(ids_c, 3, poss_array[mail_array.index(ids)])
                sheet.write(ids_c, 4, off_array[mail_array.index(ids)])
                sheet.write(ids_c, 5, dem_array[mail_array.index(ids)])
                ids_c = ids_c + 1
        print("Excell Updated>>>>")
        workbook.close()
