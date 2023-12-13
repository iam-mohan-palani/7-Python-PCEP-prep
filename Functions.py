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