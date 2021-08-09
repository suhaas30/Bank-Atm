class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def Balance(self):
        print("Your balance is 10000")

    def withdrawl(self,amount):
        new_amount = 10000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))