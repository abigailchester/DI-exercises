class House:
	def __init__(self, city, num_rooms, landlord):
		self.city = city
		self.num_rooms = num_rooms
		self.landlord = landlord

		self.rent = 1000 * self.num_rooms
		if city == "tel aviv":
			rent *= 2

	def sign_contract(self, name, date):
		if self.landlord == "Moti":
			self.rent *= 2
		print(f"rental agreement between {name} and {self.landlord} for NIS{self.rent}")

	def complain_about_broken_window(self):
		print(f"{self.landlord} says 'sorry I can't help'")


class Dog:
	def __init__(self, name, height):
		self.name = name
		self.height = height
		self.winner = False

	def talk(self):
		print("woof")

	def jump(self, height):
		print(self.height * 2)

	def fight(self, another_dog):
		if self.height > another_dog.height:
			return self
		else:
			return another_dog



davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

davids_dog.talk()
davids_dog.jump(50)
sarahs_dog.talk()
sarahs_dog.jump(20)

if sarahs_dog.height > davids_dog.height:
	sarahs_dog.winner = True
else:
	davids_dog.winner = True


print(sarahs_dog.winner)
print(davids_dog.winner)



fight_winner = davids_dog.fight(sarahs_dog)

print(f"the winner is {fight_winner.name}")

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


