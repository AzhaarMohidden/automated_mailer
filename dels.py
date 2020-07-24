import write_sheet_del as wd
import sys
sec = sys.argv[1]
sel_x = "sample"

def dell(d_x):
    del_x = int(d_x)-1
    print("Deleted: " + str(del_x) + "\n")
    wd.write_mail(sel_x, del_x)

if __name__ == '__main__':
    dell(sec)
