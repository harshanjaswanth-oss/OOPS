class India:
    def capital(self):
        print("The capital of india is delhi")
    def language(self):
        print("The National language of india is Hindi")
    def currency(self):
        print("The currency of india is rupess")

class Japan:
    def capital(self):
        print("the capital of Japan is tokyo")
    def language(self):
        print("The national language of japan is Japenese")
    def currency(self):
        print("The currency of japan is yen")
obj=India()
obj1=Japan()

for country in (obj,obj1):
    country.capital()
    country.currency()
    country.language()

    
