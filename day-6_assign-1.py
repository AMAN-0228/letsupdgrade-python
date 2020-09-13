class bankaccount:
    def __init__(self,ownername,balance):  
        self.ownername = ownername
        self.balance = balance

    def deposits(self,depositing_money):
        self.balance +=  depositing_money
        print('NAME =',self.ownername,'\nBALANCE =',self.balance,"\n")

    def withdraw(self,money):
        if money <=self.balance :
            self.balance -= money
            print("NAME:",self.ownername,"\nBALANCE:{}".format(self.balance),'\n')

aman_account = bankaccount('aman',24000)
aman_account.deposits(500)
aman_account.withdraw(1000)
aman_account.deposits(500)
aman_account.deposits(1500)
aman_account.deposits(5000)
aman_account.withdraw(500)
aman_account.withdraw(4500)

abc_account = bankaccount("abc",152000)
abc_account.withdraw(25000)
abc_account.deposits(40000)
aman_account.deposits(7000)