#Conditional Loops

#If-else

age= int(input("Enter your age: "))
if (age < 18):
         print ("You are younger than 18")
elif (age == 18):
         print ("You are exactly 18 years old")
else:
         print("You are older than 18 years old")

#while
number=3
guess=int(input("\nGuess a number:"))
while guess != number:
        guess=int(input("Guess a number: "))
else:
        print("\nYou guessed correctly!!!")


#for
num=int(input("\nEnter a number: \n"))
for i in range (num):
        print(i)

for i in range (17,25):
        print(i)

#CISCO

#Finding largest in n numbers
largest_number = -999999999
while True:
  number = int(input("Enter Number: "))
  if number == -1:
    print(largest_number)
    break
  if number > largest_number:
    largest_number = number
print(largest_number)

#Vowel eater
user_word=input("Enter:")
user_word = user_word.upper()
for letter in user_word:
    if (letter == 'A' or letter == 'E'or letter == 'I' or letter == 'O'or letter == 'U'):
     continue
    else:
        print(letter)

#Finding Pyramid Block
blocks = int(input("Enter the number of blocks: "))
height = 0
inlayer = 1
while inlayer <= blocks:
    height += 1
    blocks -= inlayer
    inlayer += 1
print("The height of the pyramid: ", height)

#Collatz's hypothesis
num=int(input('Enter:'))
counter=0
while (num != 1):
    if (num%2 == 0):
        num/=2
        print(num)
        counter+=1
    else:
        num= 3 * num + 1
        counter+=1
print('steps=', + int(counter))




