#exo 1
lst = [1, 2, 3, 4]
print(lst)

#exo 2
new_lst = [x * 20 for x in lst]
print(new_lst)

#exo 3
name_list = ["Elie", "Tim", "Matt"]
first_letter_list = [x[0] for x in name_list]
print(first_letter_list)

#exo4
lst = [1, 2, 3, 4, 5, 6]
even_lst = [x for x in lst if x % 2 == 0]
print(even_lst)

#exo5
lst1 = [1,2,3,4]
lst2 = [3,4,5,6]
lst3 = [x for x in lst1 if x in lst2]
print(lst3)

#exo 6
reverse_list = [x[::-1].lower() for x in name_list]
print(reverse_list)

#exo 7
first = "first"
third = "third"
lst = [x for x in first if x in third]
print(lst)

#exo 8 
num = range(1,101)
list_num = list(num)
divideby12 = [x for x in list_num if x % 12 == 0]
print(divideby12)

#exo 9
vowels = "aeiou"
str1 = "amazing"
lst = [x for x in str1 if x not in vowels]
print(lst)

#exo 10
lst = [[0,1,2] for x in range(1,4)]
print(lst)

#exo 11
lst = list(range(1,10))
matrix = [lst for x in range(1, 10)]
print(matrix)

