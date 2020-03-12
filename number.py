for number in range(1,5):
	print(number)
numbers=list(range(1,10))
print(numbers)

squares=[]
for value in range(1,10):
	squares.append(value**2)
	
print(squares)

squares_1=[value**2 for value in range(1,10,2)]
print(squares_1)

players=['a','b','c','d','e']
print(players[0:2])
print(players[-2:])
print(players[1:])
for player in players[-3:]:
	print(player.title())

other_players=players[:]
print(other_players)
