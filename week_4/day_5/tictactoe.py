
tictactoe = [0,1,2,3,4,5,6,7,8]

# for i in range(len(tictactoe)):
# 	print(i,i+1,i+2)

	# print(i+3,i+4,i+5)
	# print(i+6,i+7,i+8)
def display_board5():
	for i in range(len(tictactoe))[::3]:
		print(i,i+1,i+2)

display_board5()


print(tictactoe)

def playerX():
	turnX = int(input("X: which number box do you want to fill?"))
	for i in tictactoe:
		if turnX == i:
			tictactoe[i] = "X"
			print(tictactoe)

#playerX()

def playerO():
	turnO = int(input("O: what box do you want to fill?"))
	for i in tictactoe:
		if turnO == i:
			tictactoe[i] = "O"
			print(tictactoe)

#playerO()

def playGame():
	count = 0
	for i in tictactoe:
		count += 1
		if count%2==0:
			playerX()
		else:
			playerO()

playGame()







