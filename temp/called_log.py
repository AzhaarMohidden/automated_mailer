import write_sheet_v2 as ws2



if __name__ == '__main__':
    NUMBER = str(input("Please enter Phone NUMBER: "))
    NAME = str(input("Please enter Phone NAME: "))
    COMPANY = str(input("Please enter Phone COMPANY: "))
    POSITION = str(input("Please enter Phone POSITION: "))
    OFFER = str(input("Please enter Phone OFFER: "))
    DEMAND = str(input("Please enter Phone DEMAND: "))
    ws2.write_mail(NUMBER, NAME, COMPANY, POSITION, OFFER, DEMAND)
