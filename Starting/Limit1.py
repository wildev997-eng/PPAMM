x = int(input("Limit:"))
z = 1
y = 0

while z <= x:
    y += 1
    z += y
    print(z)

print(z)