my_fav_numbers = set()

my_fav_numbers.add(20)
my_fav_numbers.add(88)

my_fav_numbers.remove(20)

print(my_fav_numbers)

friend_fav_numbers = set()

friend_fav_numbers.add(25)
print(friend_fav_numbers)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

my_fav_numbers_tup = (20, 88)

tuppleList = list(my_fav_numbers_tup)
tuppleList.append(60)
tuppleList.append(25)

tuppleList.remove(25)

my_fav_numbers_tup = tuple(tuppleList)

print(my_fav_numbers_tup)
print(tuppleList)

friend_fav_numbers_tup = (22, 6)

our_fav_numbers_tup = friend_fav_numbers_tup + my_fav_numbers_tup

print(our_fav_numbers_tup)

a = [i for i in range(10)]
print(a)
# [0,1,2,3,4,5,6,7,8,9]
b = [i for i in range(1,11)]
print(b)
#[1,2,3,4,5,6,7,8,9,10]
c = [i for i in range(-9,5)]
print(c)
#[-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4]
d = [i for i in range(5,11)[::-1]]
print(d)
#[10,9,8,7,6,5]
e = [i for i in range(1,14)[::2]]
print(e)
#[1,3,5,7,9,11,13]
#f = [i for i in range(2,129)[::2**]]

f = []
for i in range(8):
	f.append(2**i)
print(f)

#[2,4,8,16,32,64,128]

g = []
for i in range(2,6):
	g.append(i-0.5)
	g.append(i)
print(g)
#[1.5,2,2.5,3,3.5,4,4.5,5]
