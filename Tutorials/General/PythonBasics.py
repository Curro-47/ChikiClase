
################ BASICS ##############################################################################################

######## Variables and data types
int = 1
float = 1.2
string = "Hello"
boolean = True

######## Operators
op_add =       4 + 2.12 + int       # Adds 2 numbers (int / float)
op_substract = 1 - 4.1 - float      # Substracts 2 numbers (int / float)
op_multiply =  2 * 2.2 * int        # Multiplies 2 numbers (int / float)
op_divide =    3 / 2.12 / float     # Divides 2 numbers (int / float)
op_modulus =   2 % 3.1 % int        # Gets the remainder of the division of 2 numbers (int / float)

op_concatenation = "Hello " + "World, " + string   # Joins 2 strings

op_and =   True and boolean         # Checks if both bool are true
op_or =    False or boolean         # Checks if any bool is true
op_equals =     1 == int            # Checks if 2 values are equals
op_not_equals = 1 != int            # Checks if 2 values are DIFFERENT
op_greater =    1 > int             # Checks if a number is greater than another one
op_lesser =     1 < int             # Checks if a number is lesser than another one
op_great_or_equals = 1 >= int       # Checks if a number is greater or equal than another one
op_less_or_equals =  1 <= int       # Checks if a number is lesser or equal than another one

######## Transforming data types
int("12")     # = 12                # Turns another data type into an int
float("32.1") # = 32.1              # Turns another data type into a float
str(12)       # = "12"              # Turns another data type into a string

######## Basic functions
print("Hello "+string)
string_variable = input("Input some text:")

######## Example code of all previous
months_in_year = 12
current_month = int(input("Input current month: "))

remaining_months = months_in_year - current_month
print(remaining_months + " months remaining on the year")

is_month_january = current_month == 1
print("Is month January? " + is_month_january)








################ CONDITIONALS AND LOOPS ######################################################################

######## If statements
if True:                            # You can use direct booleans
    print("Always executes")
if boolean:                         # Or boolean variables (line.8)
    print("Executes if boolean = True")
if 1 == int:                        # Or boolean operators (line.19-26)
    print("Executes if int = 1")

######## While loops
while False:
    print("This will never execute")
while boolean:
    print("This is an infinite loop while boolean = True")
while int == 10:
    print("While int = 10 this will run forever")

######## Loop and Conditional actions
while True:
    pass # Does literally nothing (Used if you want an empty loop)
    break # Breaks out of the loop (Skips to the end and continues with the next code)
    continue # Skips to the end of the loop and starts again

######## Example code of all previous
counter = 20

while counter > 0:
    if counter % 2 == 0:
        print(str(counter) + " Is even")

    counter = counter - 1








################ FUNCTIONS ##############################################################################

######## Simplified
def function_name():    # Defining a function, you create it with a name and code inside to execute later
    pass

function_name()         # Executing the function and whatever is inside of it when defining it

#### Example
def say_hi():
    print("hi")

say_hi()
say_hi()
say_hi()
# This will say hi 3 times




######## Arguments
def fun_params(a, b, c):        # You define any information you want to pass to the function in the parenthesis
    print(a, b, c)                        

fun_params("1", "2", "3")    # When executing the function you pass the parameters defined (of any type)

#### Example
def say_texts(text1, text2):
    print(text1+text2)

say_texts("Hello", " World")
say_texts("Wow", "Yippie")
# This will print:
# Hello World
# WowYippie




######## Return
def fun_return():           
    return "something"      # When using return you can send values as an output of a function

var = fun_return()          # And store them in a variable or use them directly
# Var = "something"

#### Example
def get_power(num):
    return num **2

power_of_num = get_power(4) # power of num is now 16
print(power_of_num) # You can use the variable
print(get_power(3)) # Or use the function directly, this prints 9

def is_even(num):
    return num % 2 == 0 # Returns True or False

if is_even(2):      # You can even use them directly as any data type, this is an example with bools
    print("2 is even")