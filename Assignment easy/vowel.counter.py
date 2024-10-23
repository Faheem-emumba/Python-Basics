#Vowel Counter

test_string= input("Please enter a String ")

counter=0

for char in test_string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        counter+=1
    else:
        continue

print("So the number of vowels are : ", counter)