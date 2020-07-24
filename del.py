import write_sheet_del as wd
import sys
sel_x = "sample"
# del_x = sys.argv[2]

# def write_mail(eid, cov, res, ms, pos, url, sel_excel, del):


# def write_mail(sel_excel, del):
def dell(d_x):
    d_x = int(del_x)-1
    wd.write_mail(sel_x, d_x)
