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



