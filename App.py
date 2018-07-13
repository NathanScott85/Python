
#This is how we do comments
#Assigning String Values
character_name = "John"
character_age = "35"
#True or false Booleans
is_Male = True

#Passing Values to print
print("There once was a man named "+ character_name + ",")
print("he was " + character_age + " years old")
#Modifying Values
character_name = "Mike"
print("He really liked the name " +character_name +",")
character_age = "105"
print("but does not like been age " + character_age)

# \n is a new line
#Converting to lower case and checking if a string is lower case
phrase = "Python\n Academy"
print(phrase.lower().islower())
#Length of a string

#Grab a letter from a word in a string
#Can also assign .upper after getting the letter from a string to change its casing
print(phrase[3].upper())
print(phrase, len(phrase))
#String concatenation
phrase_two = "Python "
phrase_three = "Learning"
print(phrase_two.lower() + phrase_three.upper()) 
#return the index location of a string
print(phrase_two.index("t"))

# . dot notation using replace
print(phrase.replace("Academy", "School"))