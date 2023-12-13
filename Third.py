#Operators
#and (multiply)
#or (add)
#not (true/false)

num1=int(input("Enter a number 1: "))
num2=int(input("Enter a number 2: "))

if(num1 >= 50 and num2 >= 50):
    print("Both numbers are above 50!!1")
elif(num1 <= 50 or num2 <= 50):
    print("One of the number is less than 50 !!!")
else:
    print("Both numbers are less than 50")


num3=False

if (not num3):
    print("\n OK")

#Bitwise Operator

# & (Conjunction) - Multipy - AND
# | (Disjunction) - Add - OR
# ~ (Negation)
# ^ (Exclusive) - opp to Conjuction - XOR

num4=int(input("\nEnter a number 1: "))
num5=int(input("\nEnter a number 2: "))

print("\nBinary of number 1 is:", bin(num4))
print("\nBinary of number 2 is:", bin(num5))

Conj = num4 & num5
print("\nConjuction operation(AND) of #1 and #2 is:", Conj ,"And its binary is:" , bin(Conj))

Disj=num4 | num5
print("\nDisjunction operation(OR) of #1 and #2 is:", Disj ,"And its binary is:" , bin(Disj))

Nega= num4 ^ num5
print("\nExclusive operation(XOR) of #1 and #2 is:", Nega ,"And its binary is:" , bin(Nega))

#Bit Swifting

print("\nBefore Bit right shift number 1:", bin(num4))
print("\nBefore Bit right shift number 1:", bin(num4>>1))

print("\nBefore Bit left shift number 1:", bin(num4))
print("\nBefore Bit left shift number 1:", bin(num4<<1))

#   (22>>2)==(22//4)
#   (22<<2)==(22*4)


