from abc import ABC , abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class creditcard(payment):
    def pay(self,amount):
        print(f"Payment done using credit card {amount}")

class UPI(payment):
    def pay(self,amount):
        print(f"payment done using UPI {amount}")

class Debitcard(payment):
    def pay(self,amount):
        print(f"payment done using Debitcard {amount}")
obj=creditcard()
obj1=UPI()
obj2=Debitcard()

obj.pay(500)
obj1.pay(2674)
obj2.pay(2300)



