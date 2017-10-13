class Car:
	def __init__(self, make, model, year, color)
		self.make = make
		self.model = model
		self.year = year
		self.color = color
	def __repr__(self)
		return '%s %s, %s, %s' % (self.make, self.model, self.year, self.color)
car1 = Car('Isuzu', 'Rodeo', 1997, 'Green')
car2 = Car('Hyundai', 'Sonata', 2006, 'Silver')
Print(car1)
Print(car2)