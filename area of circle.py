from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

filename = input('input the filename :')
file_= filename.split('.')
print('The extension of the file is:' +repr(file_[-1]))
