# Start your Python journey here

#Fundamentals

#Print
#Builtin function. Used to print values or another standard output.
print("Hello!, Mohankumar Palaniappan \nWelcome! to the world of Python!!!\n" )

print("Hello!, Mohankumar Palaniappan ", end="")
print("Welcome! to the world of Python!!!\n")

print("Hello!, Mohankumar Palaniappan ")
print("Welcome! to the world of Python!!!\n")

print ("Hello","Mohankumar Palaniappan", sep="!, " ,end="\n")
print ("Welcome","to the world of Python", sep="! " ,end="!!!\n")

#Literals
#1.Integers -> Octal 
#Ex:0o123 -> 8^2*1=64 8^1*2=16 8^0*3=3 -> 83
print("\n",0o421)
#Hexadecimal -> Ex:0x123 -> 16^2*1=256 16^1*2=32 16^0*3=3 -> 291
print("\n",0x421)
#2.Floating point
#3.Strings
#4.Booleans -> True/False

#Operators
#Exponential -> ** -> 2 ** 3 -> 8
print("\n",2 ** 4)
#Multiplciation -> *
print("\n", 2 * 4)
#Division -> / (Always returns as float)
print("\n", 10 / 2)
#Floor Divsion -> // (Always returns as lesser integer) -> 6 // 4 -> 1.0
print("\n", 10 // 2)
#Modulo -> % (Returns remainder) -> 5 % 2 -> 1
print("\n", 13 % 2)


#Variables
a=10
b=7
print ("\n",a+b)
a=a+1  #a+=1(shortcut operators)
print ("\n",a)

#Inputs
#This function is used to receive inputs from User, values always accepted as string.
number=input("Enter your favourite number: ")
print("\nYour favourite number is "+ number)

age=input("\nEnter your Birth Year: ")
print("\nYour age: ", 2023 - int(age))


#String Methods
print("Go! " * 10)

minutes=60
hours=input("\nHow many hours you sleep: ")

minutes1= minutes*int(hours)  

print("\nYour sleep minutes: ", minutes1)

#Operators
# == != > >= <= <
print(5 != 10)
