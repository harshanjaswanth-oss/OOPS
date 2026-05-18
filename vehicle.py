class vehicle:
    def __init__(self,name,maximumspeed,mileage):
        self.name=name
        self.maximumspeed=maximumspeed
        self.mileage=mileage

class bus(vehicle):
    pass 
obj=bus("volvo",120,600)
print(obj.name,obj.maximumspeed,obj.mileage)
