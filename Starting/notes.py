input_string = "presumptious"

print(input_string[0:3]) # so the slicing start at the alphabet p and ends at the letter e as the index 3 is not included in the slicing.    
print(input_string[4:10]) # same principle, the slicing starts at the alphabet u and ends at the letter t as the index 10 is not included in the slicing.

# if the beginning index is left out, it defaults to 0
print(input_string[:3])
# if the end index is left out, it defaults to the length of the string
print(input_string[4:])

string = input("Please type in a string: ")
vowels = "aeo"
index = 0
 
while index < len(vowels):
    vowel = vowels[index] #This start the chek on the first vowel in the string and then moves to the next vowel in the string until all vowels have been checked.
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1
 