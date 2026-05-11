class vehicle:
    def __init__ (self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
BMW=vehicle(200,500)
print(BMW.max_speed,BMW.mileage)