# 7-Python-PCEP-prep

Getting to know the basics of Python !!!

Python was created by Guido van Rossum, born in 1956 in Haarlem, the Netherlands. 
Python is an interpreted language. This means that it inherits all the described advantages and disadvantages. Of course, it adds some of its unique features to both sets.
If you want to program in Python, you'll need the Python interpreter. You won't be able to run your code without it. Fortunately, Python is free. This is one of its most important advantages.

Compilation – the source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows) containing the machine code. Now you can distribute the file worldwide; the program that performs this translation is called a compiler or translator.

Interpretation – you (or any user of the code) can translate the source program each time it has to be run. The program performing this kind of transformation is called an interpreter, as it interprets the code every time it is intended to be executed. It also means that you cannot just distribute the source code as-is, because the end-user also needs the interpreter to execute it.

# **Compilation**
**Advantages**
✓the execution of the translated code is usually faster;
✓only the user has to have the compiler – the end-user may use the code without it;
✓the translated code is stored using machine language – as it is very hard to understand it, your own inventions and programming tricks are likely to remain your secret.

**Disadvantages**
❌the compilation itself may be a very time-consuming process – you may not be able to run your code immediately after making an amendment;
❌you have to have as many compilers as hardware platforms you want your code to be run on.

# **Interpretation**
**Advantages**
✓you can run the code as soon as you complete it – there are no additional phases of translation;
✓the code is stored using programming language, not machine language - this means that it can be run on computers using different machine languages; you don't compile your code separately for each different architecture.
**Disadvantages**
❌don't expect interpretation to ramp up your code to high speed - your code will share the computer's power with the interpreter, so it can't be really fast;
❌both you and the end user have to have the interpreter to run your code.

# Operators
Priority	Operator	
1	+, -	unary
2	**	
3	*, /, //, %	
4	+, -	binary
5	<, <=, >, >=	
6	==, !=	

Some operators act before others - the hierarchy of priorities:

->the ** operator (exponentiation) has the highest priority;
->then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more strongly, for example 4 ** -1 equals 0.25)
->then: *, /, and %,
->and finally, the lowest priority: binary + and -.

Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.

The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.

# Keywords
Take a look at the list of words that play a very special role in every Python program.

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

They are called keywords or (more precisely) reserved keywords. They are reserved because you mustn't use them as names: neither for your variables, nor functions, nor any other named entities you want to create.

# String operators
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

Replication:
"James" * 3 gives "JamesJamesJames"
3 * "an" gives "ananan"
5 * "2" (or "2" * 5) gives "22222" (not 10!)

x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")
Output:55

# Bitwise operators
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


# Lists
squares = [x ** 2 for x in range(10)] -> (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
twos = [2 ** i for i in range(8)] -> (1, 2, 4, 8, 16, 32, 64, 128)

# Tuples
What else can tuples do for you?

the len() function accepts tuples, and returns the number of elements contained inside;
the + operator can join tuples together (we've shown you this already)
the * operator can multiply tuples, just like lists;
the in and not in operators work in the same way as in lists.

#to find dupilicates
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4
 



