# 7-Python-PCEP-prep
Getting to know the basics of Python !!!
Python was created by Guido van Rossum, born in 1956 in Haarlem, the Netherlands. 

Python is an interpreted language. This means that it inherits all the described advantages and disadvantages. Of course, it adds some of its unique features to both sets.
If you want to program in Python, you'll need the Python interpreter. You won't be able to run your code without it. Fortunately, Python is free. This is one of its most important advantages.

Compilation – the source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows) containing the machine code. Now you can distribute the file worldwide; the program that performs this translation is called a compiler or translator.

Interpretation – you (or any user of the code) can translate the source program each time it has to be run. The program performing this kind of transformation is called an interpreter, as it interprets the code every time it is intended to be executed. It also means that you cannot just distribute the source code as-is, because the end-user also needs the interpreter to execute it.

	**Compilation**
Advantages
✓the execution of the translated code is usually faster;
✓only the user has to have the compiler – the end-user may use the code without it;
✓the translated code is stored using machine language – as it is very hard to understand it, your own inventions and programming tricks are likely to remain your secret.

Disadvantages
❌the compilation itself may be a very time-consuming process – you may not be able to run your code immediately after making an amendment;
❌you have to have as many compilers as hardware platforms you want your code to be run on.

**Interpretation**
**Advantages**
✓you can run the code as soon as you complete it – there are no additional phases of translation;
✓the code is stored using programming language, not machine language - this means that it can be run on computers using different machine languages; you don't compile your code separately for each different architecture.
Disadvantages
❌don't expect interpretation to ramp up your code to high speed - your code will share the computer's power with the interpreter, so it can't be really fast;
❌both you and the end user have to have the interpreter to run your code.

print("2") == print(2)

print(9 % 6 % 2) == 1(This operator has left-sided binding)
print(2 ** 2 ** 3) ==256(The exponentiation operator uses right-sided binding)


Priority	Operator	
1	+, -	unary
2	**	
3	*, /, //, %	
4	+, -	binary
5	<, <=, >, >=	
6	==, !=	


print(2 * 3 % 5) ==1

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) ==10.0

Some operators act before others - the hierarchy of priorities:

->the ** operator (exponentiation) has the highest priority;
->then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more strongly, for example 4 ** -1 equals 0.25)
->then: *, /, and %,
->and finally, the lowest priority: binary + and -.

Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.

The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.

Keywords
Take a look at the list of words that play a very special role in every Python program.

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

They are called keywords or (more precisely) reserved keywords. They are reserved because you mustn't use them as names: neither for your variables, nor functions, nor any other named entities you want to create.

String operators
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

Replication
For example:

"James" * 3 gives "JamesJamesJames"
3 * "an" gives "ananan"
5 * "2" (or "2" * 5) gives "22222" (not 10!)

x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")
Output:55

#Finding largest in 200 numbers
largest_number = -999999999
while True:
  number = int(input())
  if number == -1:
    print(largest_number)
    exit()
  if number > largest_number:
    largest_number = number

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


Bitwise operators
Here are all of them:
& (ampersand) ‒ bitwise conjunction;
| (bar) ‒ bitwise disjunction;
~ (tilde) ‒ bitwise negation;
^ (caret) ‒ bitwise exclusive or (xor).

Bitwise operations (&, |, and ^)
A	B     A & B   A | B   A ^ B
0	0	0	0	0
0	1	0	1	1
1	0	0	1	1
1	1	1	1	0

And here is the updated priority table, containing all the operators introduced so far:

Priority	Operator	
1	~, +, -	unary
2	**	
3	*, /, //, %	
4	+, -	binary
5	<<, >>	
6	<, <=, >, >=	
7	==, !=	
8	&	
9	|	
10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=	


#Lists

beatles=[]
beatles.append("John Lennon")
beatles.append('Paul McCartney')
beatles.append("George Harrison")
print("Step 1:", beatles)

for i in range(2):
    add=input("Enter")
    beatles.append(add)
print("Step 2:", beatles)

del beatles[3:]
print("Step 3:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 4:", beatles)


#Swap lists
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
 
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 print(my_list)
####
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)

#####
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)


####
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Element found at index", i)
else:
    print("absent")

 ####
 drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)

####
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp_list=[]
for i in my_list:
    print(i)
    if i not in temp_list:
        temp_list.append(i)
print("The list with unique elements only:")
print(temp_list)



