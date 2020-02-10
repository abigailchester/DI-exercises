class Family:
	def __init__(self, members):
		self.members = []

	def add_member(self, name, age, sex, is_child):
		member = {}
		member["name"] = name
		member["age"] = age
		member["sex"] = sex
		member["is_child"] = is_child
		self.members.append(member)

	def born(self, **kwargs):
		children_list = []
		member = {**kwargs}
		children_list.append(member)
		self.members.append(member)
		values = list(member.values())
		print(f"mazal tov!! {values[0]} has been born!!")
		print(children_list)

	def is_18(self, name):
		family = self.members
		for member in family:
			if member["name"] != name:
				continue
			elif member["name"] == name:
				if member["age"] >= 18:
					return True
				else:
					return False
				break

	def nice_list(self):
		family = self.members
		temp = 0
		for member in family:
			temp += 1
			values = list(member.values())
			print(f"Family member {temp}: {values[0]}, {values[1]} years old")


chesterFamily = Family("Chesters")
chesterFamily.add_member("Jim", 58, "male", False)
chesterFamily.add_member("Karen", 55, "female", False)
chesterFamily.add_member("Kara", 27, "female", False)
chesterFamily.add_member("Julia", 23, "female", False)
chesterFamily.add_member("Jay", 20, "male", False)
chesterFamily.add_member("Eddie", 4, "male", True)
chesterFamily.add_member("Eden", 1, "female", True)


print(chesterFamily.members)

print(chesterFamily.is_18("Kara"))
print(chesterFamily.is_18("Julia"))
print(chesterFamily.is_18("Eddie"))

chesterFamily.nice_list()

chesterFamily.born(name="Kennedy", age=0, sex="female", is_child=True)
print(chesterFamily.members)

# Exercise 2

class TheIncredibles(Family):

	def add_keys(self, name, power, incredible_name):
		members = incrediblesFamilynormal.members
		for member in members:
			if member["name"] != name:
				continue
			elif member["name"] == name:
				member["power"] = power
				member["incredible_name"] = incredible_name
				self.members.append(member)
				break

	def use_power(self):
		members = self.members
		for member in members:
			if member["age"] > 18:
				print(member["power"])
#			elif member["age"] < 18:
#				raise Exception("You have no power here!")

	def incredible_presentation(self):
		members = self.members
		for member in members:
			values = list(member.values())
			print(f"superhero name: {values[5]}, superhero power: {values[4]}")


incrediblesFamilynormal = Family("The Incredibles Family Normal")

print(incrediblesFamilynormal.members)

#normal presentation
incrediblesFamilynormal.add_member("Bob", 40, "male", False)
incrediblesFamilynormal.add_member("Helen", 39, "female", False)
incrediblesFamilynormal.add_member("Violet", 16, "female", True)
incrediblesFamilynormal.add_member("Dash", 12, "male", True)
# incrediblesFamilynormal.add_member("Jack Jack", 2, "male", True)

print(incrediblesFamilynormal.members)


incrediblesFamilynormal.nice_list()

incrediblesFamilySuper = TheIncredibles(Family)

incrediblesFamilySuper.add_keys("Bob", "super strength", "Mr. Incredible")
incrediblesFamilySuper.add_keys("Helen", "super flexibility", "Elastigirl")
incrediblesFamilySuper.add_keys("Violet", "invisibility and force field", "Invisigirl")
# incrediblesFamilySuper.add_keys("Jack Jack", "super transform", "transformer")
incrediblesFamilySuper.add_keys("Dash", "super speed", "Dash")

print(incrediblesFamilySuper.members)

incrediblesFamilySuper.use_power()

incrediblesFamilySuper.nice_list()
incrediblesFamilySuper.incredible_presentation()

incrediblesFamilySuper.born(name="Jack Jack", age=0, sex="male", is_child=True, power="unknown", incredible_name="TBD")
incrediblesFamilySuper.nice_list()
incrediblesFamilySuper.incredible_presentation()
# print(incrediblesFamilySuper.members)


# Exercise 3

class BankAccount:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def deposit(self, deposit):
		self.deposit = deposit
		if deposit > 0:
			self.balance += deposit
		elif deposit < 0:
			print("deposit not accepted")

	def withdraw(self, withdraw):
		self.withdraw = withdraw
		if withdraw < self.balance:
			self.balance -= withdraw
		elif withdraw > self.balance:
			print("withdraw not accepted")

abbys_bank_account = BankAccount("Abby", 15000)
print(abbys_bank_account.balance)

abbys_bank_account.deposit(3000)
print(abbys_bank_account.balance)

abbys_bank_account.withdraw(1000)
print(abbys_bank_account.balance)


class Owner(BankAccount):
	def __init__(self, cred_num, password):
		self.cred_num = cred_num
		self.password = password
	# def add_details(self, cred_num, password):
	# 	self.cred_num = cred_num
	# 	self.password = password

	def check_owner_info(self):
		cc_attempt1 = int(input("type your credit card number"))
		pw_attempt1 = input("type your password")
		if cc_attempt1 != self.cred_num or pw_attempt1 != self.password:
			print("either your card number or password wasn't correct. you have one more attempt")
			cc_attempt2 = int(input("type your credit card number again"))
			pw_attempt2 = input("type your password again")
			if cc_attempt2 != self.cred_num or pw_attempt2 != self.password:
				print("your card has been eaten by the machine")
				del self.cred_num
				logged_in = False
			else:
				logged_in = True
		else:
			logged_in = True
		if logged_in == True:
			intention = input("would you like to deposit or withdraw?")
			if intention == "deposit":
				deposit_amount = input("How many $20 bills would you like to deposit?")
				if deposit_amount == "none":
					pass
				else:
					total_deposit = int(deposit_amount)*20
					print(f"you deposited {total_deposit} dollars")
					return total_deposit

			elif intention == "withdraw":
				withdraw_amount = input("how many $20 bills would you like to withdraw?")
				if withdraw_amount == "none":
					pass
				else:
					print(f"you withdrew {int(withdraw_amount)*20} dollars")
			else:
				print("I didn't understand your intention")


owner_abby = Owner(12345678, "qwerty")
print(owner_abby.cred_num)
print(owner_abby.password)

owner_abby.check_owner_info()

