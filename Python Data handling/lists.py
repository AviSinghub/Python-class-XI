# Lists : A list represents the comma-separated values of any datatypes between square brackets.

a = [1,2,4,6,8,10,11,16,18,21,44,56,72,88,92,101]
print(a)

# in lists value can be change.
a[0] = 20         # Now from the above list, the first index value is replaced or changed by value 20.
print(a)

a[2]= 48
print(a)          # Here the inedex value of 2 is changed by value 48.

a[4] = 36
print(a,'\n')

print("Length of the list: ",len(a))        # len() function is use to get the length of list.