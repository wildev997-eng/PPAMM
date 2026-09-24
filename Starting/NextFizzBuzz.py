x = int(input("Starting number:"))
y = x + 1

while True:
    if y % 5 == 0:
        if y % 3 == 0:
            fizzbuzz = True
        else:
            fizzbuzz = False
    else:
        fizzbuzz = False

    if fizzbuzz:
        break
    y = y + 1

print(f"The Fizzbuzz after {x} is {y}")