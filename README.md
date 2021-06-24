# Python OOP
## Four pillars of OOP
### Functions and good practices of functions
### DRY - Dont repeat yourself

# Let's create a function
# Syntax def is used to declare follwed by name of function()
#  First iterations
`def greeting():
     print("Welcome on Board! enjoy your trip")
    #pass # pass is the keyword that allows the interpretor to this without any errors
greeting()` # if we didn't call rge function it would execute the code with no error but no outcome
#  Dry Dont Repeat Ypurself by declaring functions and reusing code
# Second iteration
`def greeting():
    print("Good morning")
    return "WElcome on board! Enjoy your trip!"
print(greeting())`

#  Third iteration with user name as a string as an argument/args

`def greeting(name):
    print(name)
    return "Welcome on Board! " + name`

# print(greeting("Dini Hassan"))

#  Create a function to prompt the user to enter their name and display the name baack to the user with a greeting message
n`ame = input("What is your name? ")
def greeting(name):
    return "Welcome on board! " + name
print(greeting(name))`

`def nultiply(num1, num2):
    print("This func will multiply 2 numbers")
    return num1 * num2
    print(" this is the required outcome of 2 numbers") #This will not execure as the return statement is the last line of code that functions execute
print(nultiply(2,3)`)