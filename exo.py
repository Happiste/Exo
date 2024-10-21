#exo 1 

first = "Hello World"
print (first)

#exo 2

#This is a comment.

#exo 3 
print ("I AM A COPUTER!")

#exo 4

if 1 < 2 and 4 > 2:
    print ("Math is fun.")
    
#exo 5

nope = None

#exo 6

result = True and False
print(result)

#exo 7

string = "What's my length?"
print(len(string))

#exo 8
string = "i am shouting"
print(string.upper())

#exo 9

thousand = "1000"
print(type(int(thousand)))

#exo 10
string = "real"
four = 4 
sentence = str(four) + string
print(sentence)

#exo 11
record = 3 * "cool"
print(record)

#exo 12
try:
    notpossible = 1 / 0
except ZeroDivisionError:
    print("Division by zero is not possible!")
    

#exo 13
    
mylist = []
print(type(mylist))

#exo 14
print("What is your name ?")
name = input()
print("Your name is " + name)

#exo 15
print("Please, chose a number ?")
strnumber = input()
intnumber = int(strnumber)
if intnumber < 0:
    print("That number is less than 0!")
elif intnumber > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

#exo 16

fruit = "apple"
index_of_l = fruit.index('l')
print(index_of_l)

#exo 17
xylo = "xylophone"
thereY = "y" in xylo
print(thereY)

#exo 18
print("write a sentence in lowercase or uppercase")
my_string = input()
print("Your string is all in lowercase: " + str(my_string.islower()))
    



