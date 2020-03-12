cars=['bmw','audi','toyuta']
cars_1='bmm'

print(cars_1 in cars)

alien={'color':'green','points':5}

print(alien['color'])
print(alien['points'])
print(alien)

alien['x']=1
alien['y']=2
print(alien)

alien['color']='red'
print(alien)

for key,value in alien.items():
	print('\nkey:'+key)
	print('value:'+str(value))
