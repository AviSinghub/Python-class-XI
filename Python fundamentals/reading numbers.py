# Strings cant be used as a airthmetic or other numeric operations. 
# For theese operations interger and float is needed.
# Python offers int()  and  float() to be used as an input(). which converts the values received from intput() 
# into int() and float() types.
# lets see the examples below.

marks = float(input('Enter marks:'))        #the function float() around input() converts the read value into float type. 
print(type(marks))

age = int(input('Enter age:'))              #the function int() around input() converts the read value into integer type. 
print(type(age))

# this is a output with print() function, we use print()  

profit = float(input('Enter the profit percentage:'))
print(type(profit))                                    #   simplified syntax:  print()                                                                               