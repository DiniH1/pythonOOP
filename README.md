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

# Python's extensive documentation on python.org
#  We have used funcs that we created as well as built in

`import math`
- to calcuate values
`from random import random`
- to generate random numbers


`num1 = 23.44`

# in real life situations you have to round the figure depending on the value
#  if the value is less than .50 round down to 23 if 23.51 then round it up

`print(math.ceil(num1))
print(math.floor(num1))`

# Random class/methods
`print(random())`
# generates a random number everytime the prorams executes between 0.0 to .99
`print(math.pi)`
import math, datetime, sys #sys is used to get system specific information
work_dir = os.getcwd() # getcwd provides location/path
# print(work_dir)
#
# print(os.getuid())
# print(os.uname())
# print(os.cpu_count())
#
# print(datetime.date.today()) # Today's date
# print(sys.path)
# type() len()

import requests  # requests is a package to interact with a live API -
# we can make API call to any web adress using python requests packages
# pip is a package manager in python to install any packages not available by default

# pip instal requests using pip
- 'pip install requests'

import requests

requests_api = requests.get("https://www.bbc.co.uk/")
if requests_api.status_code == 200:
    print("Success")
print(type(requests_api.status_code)) # 200 for success 404 and above for failure
print(type(requests_api.headers))
print(type(requests_api.content))

# Object oriented Programming
## Four pillars of OOP

-  Abstraction
 - Abstraction is an extension of encapsulation. It is the process of selecting data from a larger pool to show only the relevant details to the object. 
- 
- Inheritance
 -  Inheritance is the ability of one object to acquire some/all properties of another object
 - With inheritance, reusability is a major advantage. You can reuse the fields and methods of the existing class
- Encapsulation
  - Enacapsulation is when an object is in private state where it can not be altered or accessed unless explicity allowed 
- Polymorphism
 - Polymorphism gives us a way to use a class exactly like its parent so there is no confusion with mixing types. This being said, each child sub-class keeps its own functions/methods as they are.
- step one create an animal.py file to create parent class
- step two to create file called reptile.py to abstract data and inherit from animal.py
- step three create a file called snake.py
- step fourcreate a file called python.py and at this point we should be able to utilise inheritance from multiple classes -> everything available from animal class to python


# Let's create an Animal class

`class Animal: # follow the correct naming convention
    # we need to initialize with built in method called __init__(self)
    # self refers to current class
    def __init__(self): # we declare attributes in our last init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True`

    def breathe(self):
        return "Keep breathing to stay alive! "

    def eat(self):
        return "Time to eat "

    def move(self):
        return "move left and right to stay awake "
# We need to create an obkect of this class in order to use any methods
cat = Animal()  # Creating an object of Animal class
# for cat as auser the functionality inside Animal class and the method to breathe is abstracted
# print(cat.breathe())
# print(cat.eat())

# Let's move onto our step two

# Let's create a class to inherit Animal class
from animal import Animal # if the file is not in the directory the absolute path is need

class Reptile(Animal): # inheriting from Animal class

    def __init__(self):
        super().__init__() # Super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]


    def seek_heat(self):
        return "It's really chilly looking have fun in the sun"

    def hunt(self):
        return "Keep working hard to find food"

    def use_venom(self):
        return " If i have it I will use it"
# Let's create an object of Reptile class
`smart_reptile =Reptile()
print(smart_reptile.breathe()) # breathe method is inherited from Animal class
print(smart_reptile.hunt()) # hunt() is available in Reptile class
print(smart_reptile.eat())
print(smart_reptile.move())
print(smart_reptile.hunt())`

# Lets create a class called Snake

`from reptile import Reptile
class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True`


# Let's add some specific methods/behaviours
    def use_tongue_to_smell(self):
        return "If i can touch it I can smell it"
# Let's create an object of Snake class
`smart_snake = Snake()`

 `print(smart_snake.move()) # move() from Animal class print(smart_snake.hunt()) # hunt() is available from Reptile class
print(smart_snake.use_tongue_to_smell()) # from current class`

# Let's create Python class

`from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True`


    def digest_large_prey(self):
        return "I can digest anything without chewing"

    def climb(self):
        return "up we go......."

    def sheds_skin(self):
        return "I'm growing out of my skin"


`fast_python = Python()
print(fast_python.climb())
print(fast_python.hunt())
print(fast_python.move())
print(fast_python.use_tongue_to_smell())
print(fast_python.sheds_skin())
print(fast_python.sheds_skin()) # __ can be used to hide a method (encapsulation)`

