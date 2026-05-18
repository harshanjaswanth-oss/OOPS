class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)
class employee(person):
    def __init__(self,name,id,salary,post):
        self.name=name
        self.id=id
        super().__init__(name,id)
obj=employee("Harshan",806408,1000000,"CEO")
obj.display()

