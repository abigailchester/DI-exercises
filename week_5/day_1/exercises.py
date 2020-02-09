
#Exercise 2

class Zoo:
	def __init__(self, zooName):
		self.zooName = zooName
		self.animals = []
		# self.name = name
		# self.pen = {}

	def addAnimal(self, newAnimal):
		if newAnimal not in self.animals:
			self.animals.append(newAnimal)

	def getAnimals(self, animals):
		print(self.animals)

	def sellAnimal(self, newAnimal):
		print(f"goodbye {self.newAnimal}")
		animals.remove(newAnimal)


	def sortAnimal(self,animals):
		sorted_animals = self.animals.sort()
		print(sorted_animals)
		temp = 0
		pen = {}
		for x,y in zip(animals[::],animals[1::]):
			if x[0] == y[0]:
				pen[temp] = [x, y]
			else:
				temp += 1
				pen[temp] = (x)
				pen[temp] = (y)
		print(pen)



columbus_zoo = Zoo("Columbus Zoo")

print(columbus_zoo.zooName)

columbus_zoo.addAnimal("zebra")
columbus_zoo.addAnimal("pig")
columbus_zoo.addAnimal("parrot")
columbus_zoo.addAnimal("dog")
columbus_zoo.addAnimal("cat")
columbus_zoo.addAnimal("giraffe")
columbus_zoo.addAnimal("elephante")
columbus_zoo.addAnimal("tiger")
columbus_zoo.addAnimal("bear")
columbus_zoo.addAnimal("leopard")
columbus_zoo.addAnimal("lion")
print(columbus_zoo.animals)

columbus_zoo.sortAnimal(columbus_zoo.animals)


# columbus_zoo.getPen()

print(columbus_zoo.animals[0][0])
print(columbus_zoo.animals[0])
