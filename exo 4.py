#exo1
def dif(a, b):
    return a + b
print (dif(5,5))

#exo2
def print_day(a):
    day = {
        1:"Dimanche",
        2:"Lundi",
        3:"Mardi",
        4:"Mercredi",
        5:"Jeudi",
        6:"Vendredi",
        7:"Samedi, Yom Shabbat"
    }
    return day.get(a, None)
    
print(print_day(7))

#exo3
def last_element(lst):
    return lst[-1]
    
print(last_element([1,2,3,4,5]))

#exo4
def compare(a,b):
    try:
        a = int(a)
        b = int(b)
        if a < b:
            return "the second number is greater"
        elif a > b:
         return "the first number is greater"
        else:
            return "Number are equal"
    except ValueError:
            return "this is not a number"
        
        
print (compare(1,'2'))

#exo5
def single_letter_count(string, x):
    return(string.lower().count(x.lower()))
    
print(single_letter_count("alloA", "a"))

#exo6
def multiple_letter_count(string):
    dico = {x: string.count(x) for x in string}
    return dico
print(multiple_letter_count("salut"))

    
#exo7
def list_manip(my_list, command, position, value = None):
    if command == "remove" and position == "end":
        return my_list.pop()
    elif command == "remove" and position == "beginning":
        return my_list.pop(0)
    elif command == "add" and position == "end":
        my_list.append(value)
        return my_list
    elif command == "add" and position == "beginning":
        my_list.insert(0, value)
        return(my_list)
    
print(list_manip([5, 5, 5, 5], "add", 'beginning', 5))

#exo8
def is_palindrome(string):
    return string == string[::-1]
    
print(is_palindrome("holloh"))

#exo9
def frequency(lst, x):
    num = lst.count(x)
    return num
print(frequency([1,23,1,4,1,5,5,3,23,6, 5, 7, 5, 10,13,5], 5))

#exo10
def multiply_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    product = 1
    for num in even_numbers:
        product *= num
    return product
    
#exo11
def is_even(num):
    return num % 2 == 0

def partition(lst, fn):
    truth = [x for x in lst if fn(x)]
    false = [x for x in lst if not fn(x)]
    return [truth, false]

print(partition([1, 2, 3, 4, 5, 6], is_even))

#exo 12
def intersection(lst1, lst2 ):
    return [num for num in lst1 if num in lst2]
    
print(intersection([1, 2, 3, 4, 5, 6, 55], [2, 5, 1, 6, 7, 9,55]))

#exo 13 
def once(func):
    def inner(*args, **kwargs):
        if not inner.has_run:
            inner.has_run = True  
            return func(*args, **kwargs)  
        return None 
    inner.has_run = False  
    return inner

def add(a,b):
    return a + b

one_addition = once(add)
print(one_addition(2,4))
