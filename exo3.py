#exo1
lst = [("name", "Elie"), ("job", "Instructor")]
dico = {x : val for x,  val in lst}
print(dico)

#exo2
lst1 = ["CA", "NJ", "RI"]
lst2 = ["California", "New Jersey", "Rhode Island"]
zipped = zip(lst1, lst2)
print(type(zipped))
zipped2 = list(zipped)
print(zipped2)
dico = {x : val for x, val in zipped2}
print(dico)

#exo3
vowels = 'aeiou'
dico = {x : 0 for x in vowels}
print (dico)

#exo4
val = chr(65)
dico = {x + 1 : chr(x + 65) for x in range(0,26)}
print(dico)

#exo5 
salsa = "awesome sauce"
vowels = "aeiou"
dico  = {key : salsa.count(key) for key, in vowels}
print(dico)
