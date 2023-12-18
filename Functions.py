#Functions

def input_number():
    return int(input("Enter a number:"))

input1= input_number()
input2= input_number()

print(input1)

#
def print_info(name, age=18):
    print(name, age)

print_info('john', 19)

#Arguments
def my_function(*students):
  print("The tallest student is " + students[2])

my_function("James", "Ella", "Jackson")

#
def input_number(num):
    return int(input("Enter a number:")) *num

input3= input_number(11)

print(input3)

#
def input_number(num1, num2):
    return int(input("Enter a number:")) *num1 - num2

input4= input_number(11,10)

print(input4)

#Return
def print_number(a ,b):
    sum=a+b
    if(sum==0):
        return
    print("The sum is: ", sum)

#
def even_num(num):
    if(num%2==0):
        return True
print(even_num(6))
print(even_num(9))

#List as Arguments
def list_arg(list):
    new_list=[]
    for item in list:
        new_list.append(item*2)
        return new_list
print(list_arg([1,2,3]))

#
def get_even_func(numbers):
    even_numbers = [num for num in numbers if not num % 2]
    return even_numbers

print(get_even_func([1, 2, 3, 4, 5, 6]))

#
def get_odd_func(numbers):
    odd_numbers = [num for num in numbers if num % 2]
    return odd_numbers

print(get_odd_func([7, 4, 5, 6, 9, 8, 12]))

#Scopes
# Function variables have no scope outside function.We can use same name for both Global & Function variable, function will always use function variable(only if there is one).
# Inorder to use Function variable outside function use Global keyword. 

#CISCO
#BMI
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
def lb_to_kg(lb):
    return lb * 0.4535923
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

#Factorial
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
for n in range(1, 6): # testing
    print(n, factorial_function(n))

#Fib
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
for n in range(1, 10): # testing
    print(n, "->", fib(n))

#Factorial (recursive)
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
