# The print() function is a way to send output to standard output devices like monitor.
# syntax is print()
# print consists of objects separated by commas
print("Welcome to my class")        # a string
print(45)                           # an integer 


print("I'm",12+5,"year old.")       # multiple comma separated expression
print("I\'m",12+8,"year old.")

# Let us do some examples.
# Example1
print('My birthday is','on 25th January')
print('Sum of 4 and 6 is', 4+6)         # Here, 4+6 is evaluated and result printed as 10

#Example2
a = 8
print('Double of',a,'is', a*a)          # will print the output (a*2 is evaluated and result printed as 64)

# sep argument: sep'' 
# sep argument specifies the separator character. if you don't give sep'' argument,
# then by default print() will add to it automatically while printing the items.
# consider this example
print('India', 'is', 'my', 'country.')

print('India', 'is', 'my', 'country.', sep = '...')

# end argument 
# Normally the print() automatically takes value of end argument as '\n' - new line character
# on giving the  end argument with a print() function. The print() function will print the line with string specified
# with the given end argument. 
# Let us do some examples
print("Asia is a continent.",end='$' )                  # the $ will aslo get printed with the line.
print("India is the largest growing economy in Asia.")

#Another example
print("Asia is a continent.",end='' )                  # space end='' will aslo get printed with the line.
print("India is the largest growing economy in Asia.")

# the end character  given with spaces (i.e., end=' ') so the ('\n') character is not appended at the end of line. 
print('My name is alex.', end = ' ')    
print('I am 12 yr old.') 

#Example 3
a,b = 20,50
print("a=",a, end =' ')
print("b=",b)

#Example 4
Name = "Arjun."
print("Hello",'dear', end=' ')
print(Name)
print("Where are you?")

#Example 5                 # you can break any statement by putting a \ (backlash) in the end and pressing enter key
print('Hello',\
end= '. ')
print("I'm a kid.")

# Write a program with welcome message and print it.

message= input('Enter a welcome message:')
print()                                         # here print() will give space to the ouput message line 62.
print("Hi!", message)