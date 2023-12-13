#Tuples
#Similiar to list, whereas list is mutable and tuple is immutable i.e., you cant edit the content of tuples.A tuple is a collection of items that are ordered, unchangeable, and allow duplicate values.

#Dictionaries
#Dictionaries consist of key-value pairs are surrounded by {}. Get values by writting key which value we want.

#dictionary.keys()
#dictionary.values()
#dictionary.items()

class12_B = {
    "1":"Anand",
    "2":"Akshaya",
    "3":"David",
    "4":"Elango",
    "5":"Satish"
}
class12_B["4"] ="Elan"
class12_B.update({"6":"Vinish"})
print(class12_B)

del class12_B["2"]

print(class12_B)

class12_B.popitem()

print(class12_B)

#Exception
#During Exception suspended program can resume using keyword except: and its excution will continue. Order of exception branch matters.

try:
    x=int(input("Enter a number: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter an Integer")
except:
    print("Something went wrong")
print("All done!!!")

#Exception can be handled inside functions
def calculate():
   try:
    x=int(input("Enter a number: "))
    y=1/x
    print(y)
   except ZeroDivisionError:
        print("You can't divide by zero")
   except ValueError:
    print("Enter an Integer")
   except:
    print("Something went wrong")
    print("All done!!!")
   return None
calculate()

#Another method 

def calculate():
   x=int(input("Enter a number: "))
   y=1/x
   print(y)
   return None
try:
   calculate()
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter an Integer")
except:
    print("Something went wrong")
print("All done!!!")


#assert refer python docs
#revisit hierarchy of exceptions

   
   


