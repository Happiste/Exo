def difference(a , b):
    return(a - b)

print(difference(0,2))

def print_day(a):
    day_of_week = {
      1 : 'Lundi',
      2 : 'mardi',
      3 : 'mercredi',
      4 : 'jeudi',
      5 : 'vendredi',
      6 : 'samedi',
      7 : 'dimanche'
    }
    return day_of_week.get(a, None)

print(print_day(1))

def last_element(lst):
  return lst[-1] if lst else None
print(last_element([1,2,3,4]))

def compare(a, b):
    if a > b:
      return 'first is greater'
    elif a < b:
      return 'second is greater'
    else:
      return 'they are equal'

print(compare(55,55))

def single_letter_count(word, letter):
    return(word.lower().count(letter.lower()))
  
print(single_letter_count('Jonathan Bitane, agee de trente quatre ans', 'a'))

def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}

print(multiple_letter_count("hello"))


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

print(list_manip([1, 2, 3], "add", 'beginning', 15))

def is_palindrome(word):
    return word == word[::-1]

def frequency(my_list, search):
    return print((my_list.count(search)))

frequency([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10], 5)

def capitalize(string):
    return print(string.title())
capitalize('hello world')

def compact(lst):
    compacted = [x for x in lst if x]
    return print(compacted)

compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]

#lst = ["a", "aa", 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']
#stringsup3 = [x for x in lst if x.len() > 3]
#print(stringsup3)


def is_even(num):
    return num % 2 == 0

def partition(lst, fn):
    truth = [x for x in lst if fn(x)]
    false = [x for x in lst if not fn(x)]
    return [truth, false]

print(partition([1, 2, 3, 4, 5, 6], is_even))


def is_even(num):
    return num % 2 == 0
    
def partition(lst, func):
    true = [x for x in lst if func(x)]
    false = [x for x in lst if not func(x)]
    return [true, false]
    
print(partition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], is_even))

def intersection(lst1, lst2 ):
    return [num for num in lst1 if num in lst2]
    
print(intersection([1, 2, 3, 4, 5, 6, 55], [2, 5, 1, 6, 7, 9,55]))

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



    



    
