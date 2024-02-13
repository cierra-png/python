class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance=account_balance
        self.phone_number=phone_number
    def send_money(self,amount,recipient):
        if  self.account_balance >=amount:
            self.account_balance -=amount
            print(f"{amount} KES sent to {recipient} successful")
        else:
            print("insufficient balance")
class Personal_Mpesa(Mpesa):
    def __init__(self,account_balance, phone_number, id_number):
        super().__init__(account_balance,phone_number)
        self.id_number = id_number
    def buyairtime(self,amount):
        if self.account_balance >=amount:
           self.account_balance -=amount
           print(f"{amount} KES  airtime bought  successful")
        else:
           print("insufficient funds")
class Business_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name= business_name
    def recieve_money(self,amount):
         self.account_balance += amount
         print(f"{amount} KES received successfully")
personal=Personal_Mpesa(account_balance=500,phone_number=24355676,id_number=2344553)
personal.send_money(400,344556276)
personal.buyairtime(30)

business=Business_Mpesa(account_balance=1000,phone_number=8765253,business_name=3422)
business.recieve_money(500)

