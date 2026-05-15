class employee:
    def __init__(self, id,name):
        self.id=id
        self.name=name
        print("constructor is called")
    def __del__(sell):
        print("object is destroyed")

employee1=employee(1967,"harshan")
del employee1

employee2=employee(1133,"Harshan")
employee2.name