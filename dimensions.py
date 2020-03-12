dimensions=(100,2000,200,234,45,234)
print(dimensions[0])
print(dimensions)

for dimension in dimensions:
	print(dimension)

print("*"*100)
print(*dimensions)
print("*"*100)

dim = [1,2,3,4,5]
print("dim: ",dim)
print("*dim: ",*dim)

