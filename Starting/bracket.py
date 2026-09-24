x = input("Word:")
## code analysis
left = int((28 - len(x)) / 2) # example the word Makan = 5, 28 - 5 = 23, 23 / 2 = 11.5, int(11.5) = 11
right = int((28 - len(x)) - left) # example the word Makan = 5, 28 - 5 = 23, 23 - 11 = 12
z = left * " " # so the left side of the word will have 11 spaces
zz = right * " " # and the right side of the word will have 12 spaces

print(30 * "*")

print(f"*{z}{x}{zz}*")

print(30 * "*")