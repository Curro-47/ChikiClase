
################ BASICS ##############################################################################################

######## Variables and data types
int = 1
float = 1.2
string = "Hello"
boolean = True

######## Operators
op_add =       4 + 2.12 + int
op_substract = 1 - 4.1 - float 
op_multiply =  2 * 2.2 * int
op_divide =    3 / 2.12 / float
op_modulus =   2 % 3.1 % int

op_concatenation = "Hello " + "World, " + string

op_and =   True and boolean
op_or =    False or boolean
op_equals =     1 == int
op_not_equals = 1 != int
op_greater =    1 > int
op_lesser =     1 < int
op_great_or_equals = 1 >= int
op_less_or_equals =  1 <= int

######## Transforming data types
int("12")     # = 12
float("32.1") # = 32.1
str(12)       # = "12"

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

