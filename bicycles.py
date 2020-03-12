bicycles=['trek','can','red','sped']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])

message="My first bicycle is a "+bicycles[-1].title()
print(message)

bicycles.append('docat')
print(bicycles)
bicycles.insert(1,'yamaha')
print(bicycles)

del bicycles[1]
print(bicycles)

popped_bicycles=bicycles.pop()
print(bicycles)
print(popped_bicycles)

bicycles.remove('can')
print(bicycles)

cars=['bmw','audi','toyota','subaru']
print(cars)
cars.sort()
print(cars)
cars.reverse()
print(cars)
print(sorted(cars))
print(cars)
print(len(cars))
