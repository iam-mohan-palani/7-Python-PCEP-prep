#Lists
#Example #1
countries=["India","USA","UK","Canada"]
length=len(countries)

print(countries[0])


for i in range (length):
    print(countries[i])

del(countries[2])

list1 = [10, 11, 12, 13, 14]
print(list1[::3])

#List Method
#list.append -> To add as last item
#list.insert -> To insert an item 

countries.append("Australia")
countries.insert(1, "Russia")

print(countries)


#Example #2
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


#Swap
#Example #1
temp =countries[2]
countries[2]=countries[4]
countries[4]=temp
print(countries)

#Another Swap method

countries[2],countries[4]=countries[4],countries[2]
print(countries)

#Example #2
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
 
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

#Sort
number=[22,85,20,17,89]
number.sort() # ascending
print(number)

number.reverse()
print(number) #reverse

#Iterating List
marks=[70,77,85,80,95,84]
total=0
for mark in marks:
    total+=mark
average=total/len(marks)
print(average)

#Slicing List
#list[start:end]

print(marks[0:2])
print(marks[1:])
print(marks[:3])
print(marks[1:-1])

my_list = [0, 1, 2, 3, 4]
print(my_list[::2])
print(my_list[::-1])
print(my_list[-1])

#Finding in list
print(2 in my_list)
print(8 in my_list)
print(8 not in my_list)
print(2 not in my_list)

# 2D - List
countries = [['Egypt', 'USA', 'India'],
       ['Dubai', 'America', 'Spain'], 
       ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in 
                       sublist if len(country) < 6]
print(countries2)

a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)
print(a)

matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix)

# 3D - List

matrix1 = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
matrix2 = []
for submatrix in matrix1:
  for val in submatrix:
    matrix2.append(val)
print(matrix2)

matrix3 = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix3[1][2])

Colors= [ [['Blue','Green','White','Black']], [['Green','Blue','White','Yellow']] , [['White','Blue','Red','Green']] ]
print(Colors[2][0][2])

