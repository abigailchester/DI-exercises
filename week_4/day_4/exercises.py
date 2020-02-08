import random

def get_random_temp(season):
	if season.lower() == "winter":
		return round(random.uniform(-10.00,16.00), 2)
	elif season.lower() == "summer":
		return round(random.uniform(20.00,41.00), 2)
	if season.lower() == "fall":
		return round(random.uniform(14.00,30.00), 2)
	else:
		return round(random.uniform(8.00,23.00), 2)

def main():
	month = int(input("What month is it? Enter a number between 1 and 12; 1 is January, 12 is December"))
	if month <=2 or month == 12:
		season = "winter"
	elif month >= 3 and month <=5:
		season = "spring"
	elif month >= 6 and month <= 8:
		season = "summer"
	else:
		season = "fall"
	random_temp = get_random_temp(season)
	print("The temperature right now is " + str(random_temp) + " degrees Celcius.")
	if random_temp < 0:
		print("Brrr, that's freezing! Wear some extra layers today")
	elif random_temp <= 16:
		print("Quite chilly! Don't forget your coat.")
	elif random_temp <= 23:
		print("It's a beautiful day! Have fun outside")
	elif random_temp <= 32:
		print("It's a hot one! Enjoy the beach and don't forget sunscreen.")
	else:
		print("It's very hot. Have fun sweating!")

main()


# Exercise 2

def throw_dice():
	return random.randint(1,6)


def throw_until_doubles():
	roll_results = (throw_dice(), throw_dice())
	print(roll_results)
	# for i in 
	if roll_results[0] == roll_results[1]:
		print("you got doubles!")
	else:
		results2 = (throw_dice(), throw_dice())
		print(results2)
		if results2[0] == results2[1]:
			print("you got doubles!")
		else:
			print("try again")

throw_until_doubles()

def throw_2():
	results_list = {}
	roll_results = (throw_dice(), throw_dice())
	if roll_results[0] == roll_results[1]:
		#print(roll_results[0], roll_results[1])
		print(roll_results)
		return True
	else:
		# print(roll_results[0], roll_results[1])
		# print(roll_results)
		return False
	# while True:

# throw_2()

def throw_3():
	results_list2 = {}
	count = 0
	# roll1 = throw_dice()
	# roll2 = throw_dice()
	while True:
		roll1 = throw_dice()
		roll2 = throw_dice()
		# if roll1 == roll2:
		# results_list{roll_1: roll_2}
		results_list2[count] = [roll1, roll2]
		# count = results_list2{roll1: roll2}
		count += 1
		if roll1 == roll2:
			print("you got it")
		return count

throw_3()


# for i in range(50):
# 	if throw_2():
# 		print(i)


# while throw_2():
# 	print(i)
# 	break

list2 = []

for i in range(100):
	if throw_2():
		print(i)
		list2.append(i)

print(list2)

print(len(list2))

while len(list2) < 2:
	print(roll_results)
	print(len(i))


def throw_until_doubles3():
	results3 = []
	count = 0
	while True:
		val1 = throw_dice()
		val2 = throw_dice()
		roll = (val1, val2)
		results3.append(roll)
		#print(results3)
		count += 1
		if val1 == val2:
			return count

print(throw_until_doubles3())

def main_function(num_of_doubles):
	results4 = []
	number_of_rolls = throw_until_doubles3()
	results4.append(number_of_rolls)
	if len(results4) == num_of_doubles:
		print(results4) #comes up as None
		#return sum(results4)/len(results4)

print(main_function(100)) # comes up as None

def main2():
	results4 = []
	while True:
		number_of_rolls = throw_until_doubles3()
		results4.append(number_of_rolls)
		if len(results4) == 100:
			#print(sum(results4))
			print(results4)
			total_throws = sum(results4)
			average_to_doubles = (total_throws/len(results4))
			print("it took a total of " + str(total_throws) + " to reach 100 doubles and " + str(average_to_doubles) + " is the average of throws to reach doubles." )
			#return sum(results4)/len(results4)

main2()

#something is still wrong ----> should go to more than 2 decimal places, need more results from first function
