# find max of list

list_find_max = [0,1,3,50]
print(max(list_find_max))

# return factorial

number = 5
factorial = 1
for i in range(1, number + 1):
	factorial = factorial*i
print("the factorial of",number,"is",factorial)

# find sum of array without using sum()

list_find_sum = [1,5,4,2]

total = 0
for i in list_find_sum:
	total += i
print(total)

import functools
def add(x, y):
	return x + y

print(functools.reduce(add,list_find_sum))


# count element in list
list_count = (["a","a","t","o"],"a")
print(len(list_count))

#return L2-norm
list_norm = [1,2,2]
list_of_squares = []
for i in list_norm:
	list_of_squares.append(i*i)

l2_norm = sum(list_of_squares)/len(list_of_squares)
print(l2_norm)

#find if array is monotonic
def isMono(mL):
	return (all(mL[i] <= mL[i+1] for i in range(len(mL) - 1)) or all(mL[i] >= mL[i+1] for i in range(len(mL) - 1)))


mlist1 = [7,6,5,5,2,0]
mlist2 = [2,3,3,3]
mlist3 = [1,2,0,4]

print(isMono(mlist1))
print(isMono(mlist2))
print(isMono(mlist3))

# check palindrome
print("check if string is palindrome")

def isPalindrome(string):
	listed_string = list(string)
	if listed_string == listed_string[::-1]:
		return True
	else:
		return False

string = "hey there"
print(isPalindrome(string))

print(isPalindrome("radar"))
print(isPalindrome("John"))
print(isPalindrome("02022020"))
print(isPalindrome("level"))

# function that returns number of words in string with length > k
sentence = "Do or do not there is no try"
k = 2

def sum_over_k(sentence, k):
	listed_sentence = sentence.split()
	list2 = []
	for word in listed_sentence:
		listed_word = list(word)
		list2.append(listed_word)
	count = 0
	for item in list2:
		if len(item) > k:
			count += 1
	return count

print(sum_over_k(sentence, k))

# return average value in numeric value dictionary

def getDictAvg(dictionary):
	values = dictionary.values()
	print(sum(values)/len(values))

getDictAvg({"a":1,"b":2,"c":8,"d":1,"e":8})

# return common divisors of 2 numbers

def CommonDiv(num1, num2):
	for i in range(1, min(num1, num2)+1):
		if num1%i==num2%i==0:
			print(i)

CommonDiv(10, 20)

#linear and binary search

def LBSearch(numlist,number,string):
	if number in numlist:
		print(number)
	else:
		print(-1)

numlist = [1,2,50,74]
LBSearch(numlist,50,"linear")
LBSearch(numlist,74,"binary")
LBSearch(numlist,100,"binary")

# test if number is prime

def isPrime(num):
	nums = []
	primenum = []
	for i in range(2,num):
		if num%i==0:
			nums.append("hi")
		else:
			primenum.append("prime")
	if len(nums)>0:
		return False
	else:
		return True

print(isPrime(11))
print(isPrime(15))
print(isPrime(19))
print(isPrime(20))
print(isPrime(37))

# prints if index and value are even

def weirdPrint(weirdlist):
	evenlist = []
	for i in range(len(weirdlist)):
		index = i
		value = weirdlist[i]
		if index%2==0 and value%2==0:
			evenlist.append(value)
	print(evenlist)

weirdPrint([1,2,2,3,4,5])
weirdPrint([1,2,3,4,5,5,6])
weirdPrint([7,4,9,9,20,22,30,47])

# accepts an undefined numbers of keyworded arguments and return count of diff types

def TypeCount(**kwargs):
	values = kwargs.values()
	bool_count = 0
	int_count = 0
	string_count = 0
	float_count = 0
	for value in values:
		if type(value) == bool:
			bool_count += 1
			print("bool: " + str(bool_count))
		elif type(value) == int:
			int_count += 1
			print("int: " + str(int_count))
		elif type(value) == str:
			string_count += 1
			print("str: " + str(string_count))
		else:
			float_count += 1
			print("float: " + str(float_count))

TypeCount(a=1,b='string',c=1.0,d=True,e=False)



# from turtle import *

# for i in range(20):
# 	forward(150)
# 	left(100)

#bye()






