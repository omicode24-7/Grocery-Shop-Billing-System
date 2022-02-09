import random
shop_list=[]
class Bazar:
    def __init__(self,login_id='',password='',account_no='',total=0,grocery_bill=0,bakery_bill=0,electronics_bill=0,dairy_bill=0):
        self.login_id=login_id
        self.password=password
        self.account_no=account_no
        self.total=total
        self.grocery_bill=grocery_bill
        self.bakery_bill=bakery_bill
        self.electronics_bill=electronics_bill
        self.dairy_bill=dairy_bill
    def __str__(self):
        return f"product[{self.account_no,self.login_id,self.password,self.total,self.grocery_bill,self.bakery_bill,self.electronics_bill,self.dairy_bill}]"
    def create_account(self):
        self.login_id=input("Create login id: ")
        self.password=input("Create password: ")
        self.account_no=''.join(random.choices('1234567890',k=11))
        print("Account created successfully with below credentials")
        print("Login id:",self.login_id)
        print("Password:",self.password)
        print("Account No:",self.account_no)
        c=Bazar(self.login_id,self.password,self.account_no,self.total,self.grocery_bill,self.bakery_bill,self.electronics_bill,self.dairy_bill)
        shop_list.append(c)
        print("")
    def login(self):
        print("Enter your login credentials to proceed")
        log=input("Enter login id: ")
        pas=input("Enter password: ")
        acc=input("Enter account No: ")
        for i in shop_list:
            if log==i.login_id:
                if pas==i.password:
                    if acc==i.account_no:
                        print("Login Successful\nWelcome to Sasta Bazar")
                        choice=0
                        while choice!=6:
                            try:
                                print("(1) Go to Grocery Section")
                                print("(2) Go to Bakery Section")
                                print("(3) Go to Electronics section")
                                print("(4) Go to Dairy section")
                                print("(5) Total bill")
                                print("(6) Exit")
                                choice=int(input("Enter your choice: "))
                            except:
                                print("Invalid Choice")
                                break
                            if choice==1:
                                self.grocery()
                            elif choice==2:
                                self.bakery()
                            elif choice==3:
                                self.electronics()
                            elif choice==4:
                                self.dairy()
                            elif choice==5:
                                self.total_bill()
                            elif choice==6:
                                break
                    else:
                        print("Incorrect Account no.")
                        break
                else:
                    print("Incorrect password")
                    break
            else:
                print("Incorrect login id")
                break
        print("")
    def grocery(self):
        print("Fruits")
        print("(1) Banana (1 dozon).......Rs 20")
        print("(2) Mango (1 dozon)........Rs 100")
        print("(3) Papaya (1 kg)..........Rs 40")
        print("Vegetable")
        print("(4) Spinach (1 sheaf)......Rs 20")
        print("(5) Eggplant (1 kg)........Rs 20")
        print("(6) Cabbage (1 kg).........Rs 15")
        order=int(input("Enter product serial no: "))
        qty=int(input("Enter quantity: "))
        if order == 1:
            self.grocery_bill=20*qty
        elif order==2:
            self.grocery_bill=100*qty
        elif order==3:
            self.grocery_bill=40*qty
        elif order==4:
            self.grocery_bill=20*qty
        elif order==5:
            self.grocery_bill=20*qty
        elif order==6:
            self.grocery_bill=15*qty
        else:
            print("Choose from above products")
        for i in shop_list:
            i.grocery_bill=+self.grocery_bill
        print("")
    def bakery(self):
        print("(1) While wheat bread.....Rs 35")
        print("(2) Pita bread............Rs 25")
        print("(3) Bagel.................Rs 45")
        print("(4) Coberg................Rs 60")
        print("(5) Pretzel...............Rs 80")
        print("(6) Croissant.............Rs 25")
        order=int(input("Enter product serial no: "))
        qty=int(input("Enter quantity: "))
        if order == 1:
            self.bakery_bill=35*qty
        elif order==2:
            self.bakery_bill=25*qty
        elif order==3:
            self.bakery_bill=45*qty
        elif order==4:
            self.bakery_bill=60*qty
        elif order==5:
            self.bakery_bill=80*qty
        elif order==6:
            self.bakery_bill=25*qty
        else:
            print("Select from above list")
        for i in shop_list:
            i.bakery_bill=+self.bakery_bill
        print("")
    def electronics(self):
        print("(1) Bulb 40w.....................Rs 80")
        print("(2) Tube light 80w...............Rs 120")
        print("(3) Trimmer......................Rs 240")
        print("(4) Mixer Grinder 750 watts......Rs 750")
        print("(5) Water Heater.................Rs 275")
        print("(6) Extension board..............Rs 60")
        order=int(input("Enter product serial no: "))
        qty=int(input("Enter quantity: "))
        if order == 1:
            self.electronics_bill=80*qty
        elif order==2:
            self.electronics_bill=120*qty
        elif order==3:
            self.electronics_bill=240*qty
        elif order==4:
            self.electronics_bill=750*qty
        elif order==5:
            self.electronics_bill=275*qty
        elif order==6:
            self.electronics_bill=60*qty
        else:
            print("Select from above list")
        for i in shop_list:
            i.electronics_bill=+self.electronics_bill
        print("")
    def dairy(self):
        print("(1) Cow milk (1 Ltr)..............Rs 48")
        print("(2) Buffalo milk (1 Ltr)..........Rs 56")
        print("(3) Cheese (100 gram).............Rs 20")
        print("(4) Yogurt (100 gram).............Rs 15")
        print("(5) Butter (100 gram).............Rs 25")
        print("(6) Sour creame (100 gram)........Rs 25")
        order=int(input("Enter product serial no: "))
        qty=int(input("Enter quantity: "))
        if order == 1:
            self.dairy_bill=48*qty
        elif order==2:
            self.dairy_bill=56*qty
        elif order==3:
            self.dairy_bill=20*qty
        elif order==4:
            self.dairy_bill=15*qty
        elif order==5:
            self.dairy_bill=25*qty
        elif order==6:
            self.dairy_bill=25*qty
        else:
            print("Select from above list")
        for i in shop_list:
            i.dairy_bill=+self.dairy_bill
        print("")
    def delete_account(self):
        acc=input("Enter account No: ")
        exist=list(filter(lambda account:account.account_no,shop_list))
        if len(exist)<0:
            print("Account does not exist")
            return
        for i in shop_list:
            if acc==i.account_no:
                shop_list.remove(i)
                print("Account deleted successfully")
        print("")
    def total_bill(self):
        print("Account no",self.account_no)
        print("Total Grocery bill:     ",self.grocery_bill)
        print("Total Bakery bill:      ",self.bakery_bill)
        print("Total Electronics bill: ",self.electronics_bill)
        print("Total Dairy bill:       ",self.dairy_bill)
        self.total=self.grocery_bill+self.bakery_bill+self.electronics_bill+self.dairy_bill
        print("-"*30)
        print("Total bill:             ",self.total)
        print("")
def SastaBazar():
    s=Bazar()
    choice=0
    while choice!=4:
        try:
            print("(1) Create New Account")
            print("(2) Log in")
            print("(3) Delete Account")
            print("(4) Exit")
            choice=int(input("Enter your choice: "))
        except:
            print("Invalid Choice")
        if choice==1:
            s.create_account()
        elif choice==2:
            s.login()
        elif choice==3:
            s.delete_account()
        else:
            print("Thank you for visiting... Please visit again")
            break
SastaBazar()
