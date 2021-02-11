class Vehicle:
	def __init__(self,max_speed,mileage):
		self.max_speed=max_speed
		self.mileage=mileage
modelx=Vehicle(240,18)
print(modelx.max_speed,modelx.mileage)

class Vehicle:
    pass
class Vehicle():
	def __init__(self,name,max_speed,mileage):
		self.name=name
		self.max_speed=max_speed
		self.mileage=mileage
class Bus(Vehicle):
	pass
