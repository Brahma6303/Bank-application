class bank :
    IFSC="SBIN000123"
    b_name="SBI"
    br_name="Marhatahalli"
    R_O_I=0.06
    def __init__(self,name,account,mno,Bal,pin):
        self.name=name
        self.account=account
        self.mno=mno
        self.Bal=Bal
        self.pin=pin
    @staticmethod
    def validate():
        return int(input("Enter the 4 digit pin::"))
    def deposite(self):
        if self.pin == self.valdate():
            amount=int(input("Enter the amount:"))
            self.Bal +=amount
            print("Your amount deposited successfully")
        else:
            print("incorrect pin")
    def withdraw(self):
        if self.pin==self.validate():
            amount=int(input("Enter the amount::"))
            if self.Bal >= amount:
                self.Bal -=amount
                print("your amount debited succussfully")
            else:
                print("your amount not sufficient")
        else:
            print("incorrect pin")
    def checkbal(self):
        if self.pin==self.validate():
            print(f'{self.name} available balance is{self.Bal}')
        else:
            print("incorrect pin")
    @classmethod
    def changeROI(cls):
        bank.R_O_I=float(input("Enter the Rate Of Interest::"))
        print(bank.R_O_I)
    def changepin(self):
        if self.pin==self.validate():
            pin1=int(input("Enter the 4 digit pin::"))
            pin2=int(input("Re-Enter the 4 digit pin::"))
            if pin1==pin2:
                self.pin=pin1
                print("pin change successfully")
            else:
                print("pin1 and pin2 doesn't match")
        else:
            print("Incorrect pin")
b1= bank("kanna",2345223654,3454354566,10000,1111)
b2= bank("jyothi",32752858254,23462344,15000,2222)
'''
b1.deposite()
print(b1.Bal)
'''
'''
b1.withdraw()
print(b1.Bal)
'''
'''
b1.checkbal()
'''
'''
bank.changeROI()
'''

b1.changepin()
print(b1.pin)
