print("hello world")
# creating variables in python
# JS let or const, boolean or all other ones
name = "Adrian"
last_name = "Aguinaga"
age = 100
found = True

print("my age is"+ str(age))

# if /else statement
# if(age < 100){console.log("no worries youre not that old")}
if age <99:    
    print("dont worry youre not that old")
    
        
elif age >101:
    print("congratz youre a century")
else:
    "i dont know how you get here!"

print("im outside of the if statement")

# fuctions
#fuction name_of_the_function() -->this is the JS
def say_hello():
    print("Hello there!")

def say_good_bye(name):
    print("Good bye "+ name)

def test(name,age,country):
    print("hello my name is "+ name +" i have " + str(age) + " years old and im from "+ country)
    
#call the function
say_hello()
# name = "adrian"
say_good_bye(name)
test(name,age,"Mexico")

#create a function that prints "hello my name is" age "and im from" country

