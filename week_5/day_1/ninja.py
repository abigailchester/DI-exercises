# exercise 1 ----> menu manager


class menuManager:
	def __init__(self, restaurantName):
		self.menu = restaurantName
		self.menuItems = []

	def add_item(self, name, price, spice, gluten):
		item = {}
		item["name"] = name
		item["price"] = price
		if spice == "A":
			item["spice"] = "not spicy"
		elif spice == "B":
			item["spice"] = "a little spicy"
		elif spice == "C":
			item["spice"] = "very spicy"
		item["gluten"] = gluten
		self.menuItems.append(item)

	def update_item(self, name, price, spice, gluten):
		menu_items = self.menuItems
		for item in menu_items:
			key = item.keys()
			value = item.values()
			value_list = list(value)
			if value_list[0] != name:
				continue
			elif value_list[0] == name:
				item.update({"price": price, "spice": spice, "gluten": gluten})
				if spice == "A":
					item["spice"] = "not spicy"
				elif spice == "B":
					item["spice"] = "a little spicy"
				elif spice == "C":
					item["spice"] = "very spicy"
				print(f"We updated {name}. Here is the updated menu:")
				print(menu_items)
				print(item)
				return False
		if False:
		 	print("already printed updated menu")
		else:
			print(f"{name} is not on the menu")

	def remove_item(self, name):
		menu_items = self.menuItems
		for i in range(len(menu_items)):
			if menu_items[i]["name"] == name:
				del menu_items[i]
				print(f"We removed {name}. Here is the updated menu:")
				print(menu_items)
				# break
				return False
		if False:
			print("find something more efficient here")
		else:
			print(f"{name} can't be removed because it is already on the menu")



mamasMenu = menuManager("Mama Mia's Pizza Menu")
soup = mamasMenu.add_item("Soup", 10, "B", False)
hamburger = mamasMenu.add_item("Hamburger", 15, "A", True)
fries = mamasMenu.add_item("French Fries", 5, "C", False)
beef = mamasMenu.add_item("Boeuf Bourgignon", 25, "B", True)

print(mamasMenu.menu)
print(mamasMenu.menuItems)

mamasMenu.update_item("Hamburger", 20, "A", True)
mamasMenu.update_item("Pasta", 15, "A", False)
mamasMenu.update_item("Salad", 10, "A", True)
mamasMenu.add_item("Salad", 10, "A", True)

print(mamasMenu.menuItems)

mamasMenu.remove_item("French Fries")
mamasMenu.remove_item("Sandwich")



