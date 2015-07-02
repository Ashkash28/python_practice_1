greetings = "Hello Sir!"

print greetings

print "What is your name?"

name = raw_input()
#raw_input() takes in a user's input and changes it to a string

print "How old are you?"

age = input()
#input() takes in a user's input as is

print "Your name is ", name
print "Your age is ", age, " years old"

my_string = "hello world"
print my_string.capitalize()
#capitalizes the first word in a string only

my_string = "Hello WORLD"
print my_string.lower()
#lowercases the entire string
print my_string.swapcase()
#swap cases each letter in string
print my_string.upper()
#uppercases entire string
print my_string.find("ll")
#returns the index of where the given substring begins from the entire string
print my_string.replace("WORLD", "puppy")
#replaces word in string with given word

ninjas = ["Rozen", "KB", "Oliver"]

print "ninja 1: ", ninjas[0]
print "ninja 2: ", ninjas[1]
print "ninja 3: ", ninjas[2]

my_list = [1, "Zen", "Hi"]

print len(my_list)
#returns length of list

my_list = [1, 7, 5]
print max(my_list)
#returns max value in list
print min(my_list)
#returns min value in list

my_list = [0, "hi", ""]
print any(my_list)
#the output of this is true because "hi" equates to true
my_list = [0, ""]
print any(my_list) 
#this output of this is false because both items equate to false

