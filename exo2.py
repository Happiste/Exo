#Excercice 1 
my_list = [1, 2, 3, 4]
for num in my_list:
    print(num)
    
#Excercice 2
my_list = [1, 2, 3, 4]
for num in my_list:
    num = num*20
    print(num)    
    
#Excercice 3
name_list = ["Elie", "Tim", "Matt"]
capitalize = [new_list[0] for new_list  in name_list]
print(capitalize)

#Excercice 4
my_list = [1,2,3,4,5,6]
new_list = [num for num in my_list if num % 2 == 0]

print(new_list)

#Excercice 5
first_list = [1,2,3,4]
second_list = [3,4,5,6]
final_list = [num for num in first_list if num in second_list]
print(final_list)

#Excercice 6
name_list = ["Elie", "Tim", "Matt"]
reverse_list = [name[::-1].lower() for name in name_list]
print(reverse_list)

#Excercice 7 
word_first = "first"
word_third = "third"
final = [num for num in word_first if num in word_third]
print(final)

#Excercice 8
number_list = list(range(1, 101))
new_list = [num for num in number_list if num % 12 == 0]
print(new_list)

#Excercice 9 
consonant = []
for letters in 'amazing':
    if letters in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
        consonant.append(letters)

print(consonant)
    
#Excercice 10 
list_matr = [[0, 1, 2] for num in range (3)]

print(list_matr)

#Excercice 11
list_matr = [[i for i in range(10)] for num in range(10)]
print(list_matr)


