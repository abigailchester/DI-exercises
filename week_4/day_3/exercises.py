ninjalist = ["abby", 26, "miranda", 25, "jon", 3]

intlist = []
stringlist = []

for item in ninjalist:
	if type(item) == str:
		stringlist.append(item)
	elif type(item) == int:
		intlist.append(item)

print(stringlist)
print(intlist)

# he made a list of random strings and integers using random function ----> in slack

long_index = map(len, stringlist)

max_length = 1
for index,s in enumerate(stringlist):
	temp = len(s)
	if temp > max_length:
		max_length = temp
		long_index = index

print(stringlist[long_index])
print(max_length)


# stringlist.sortby(len())

# print(stringlist)

print(sorted(stringlist, key=len)[-1])
#exercise 3

exercise2string = "hey my name is abby and i love the beach"

ex2list = []

ex2list.append(exercise2string)


#exercise 4 ninja

password = "mypassword"

length = len(password)

print("*" * length)

#exercise 5 ninja

sandwich_orders = ["ham and cheese", "pastrami", "meatball", "tuna", "pastrami", "omelet", "spicy chicken", "pastrami", "shakshuka"]

finished_sandwiches = []

for sandwich in sandwich_orders:
	message = "I made your " + sandwich + " sandwich"
	print(message)
	finished_sandwiches.append(message)


print(finished_sandwiches)

print("I made your " + ", ".join(sandwich_orders) + " sandwiches.")

# exercise ninja 6

print("the deli has run out of pastrami")
for sandwich in sandwich_orders:
	if sandwich == "pastrami":
		sandwich_orders.remove(sandwich)

print(sandwich_orders)

#come back to make this while loop


def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 

text = input("type string to encrypt")
s = int(input("type a secret key"))
print( "Text  : " + text )
print( "Shift : " + str(s) )
print( "Cipher: " + encrypt(text,s))


#ninja exercise 8

# for i in range(1, 6):
# 	print("*" * i)

# for i in range(1, 6)[::-1]:
# 	numofstars = "*" * i
# 	print(numofstars)
# 	if len(numofstars) < 5 and len(numofstars) > 1:
# 		print(" " + numofstars)






