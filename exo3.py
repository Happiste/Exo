list_two = [("name", "Tim"), ("job", "doctor"), ("age", "30")]
result = dict(list_two)
print(result)

lsit_one = [("name", "Tim"), ("job", "doctor"), ("age", "30")]
result = {x: value for x, value in lsit_one}
print(result)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
result = {key: value for key, value in zip(list1, list2)}
#result = list(zip(list1, list2))
print(result)

vowels = 'aeiou'
dico = {}
for v in vowels:
    dico[v] = 0
print(dico)

alpha = {i + 1: chr(i + 65) for i in range(26)}
print(alpha)

str = "jonathan bitane"
vowels = 'aeiou'
dico = {key: str.count(key) for key in vowels}
print(dico)
