## Jorge Vallejo Ortega 
## 23/05/2019
## Written and tested in QPython3. 

"""This is a very simple program that
I wrote with the objective of practicing
basic Python and to get used to code
in mobile phone environment.
"""

"""This script calculates volumes of
geometric figures so you don't have to. 
"""

import math # For using pi.


# This message is for ValueError. 
v_error ="Use only numbers, please."

pi = math.pi

def carry_on(): # Pauses the main loop. 
    input ("\nPress Enter to continue...")

# Here all the formulae for calculating
# the different geometric figures. 

def cone():
    # The try-except blocks will
    # handle the cases in which the
    # user enters input not expected
    # by the program. 
    try:
        radius = float(input("Radius: "))
        height = float(input("Height: ")) 
        volume = (pi * height * (radius ** 2))/3
        result = ("\nThe volume of a cone of\n" 
    	    "radius %f units and height %f units\n" 
    	    "is %f cubic units." 
    	    % (radius, height, volume)) 
        return result
    except ValueError:
        return (v_error)

def cube():
    try:
        side = float(input("Side of the cube: "))
        volume = side ** 3
        result = ("\nThe volume of a cube of\n" 
    	    "side %f units is %f cubic units." 
    	    % (side, volume)) 
        return result
    except ValueError:
        return (v_error)
        
def cylinder():
    try:
        radius = float(input("Radius: "))
        height = float(input("Height: ")) 
        volume = pi * height * (radius ** 2)
        result = ("\nThe volume of a cylinder of\n" 
    	    "radius %.3f units and height %.3f units\n" 
    	    "is %.3f cubic units." 
    	    % (radius, height, volume)) 
        return result
    except ValueError:
        return (v_error)
        
def rectangular_solid():
    try:
        length = float(input("Length: "))
        width = float(input("Width: "))
        height = float(input("Height: "))
        volume = length * width * height
        result = ("\nThe volume of a rectangular \n" 
        	"solid of %.3f by %.3f by %.3f is\n"
        	"%.3f cubic units." 
    	    % (length, width, height, volume)) 
        return result
    except ValueError:
        return (v_error)
        
def pyramid():
    try:
        length = float(input("Length of base: "))
        width = float(input("Width of base: "))
        height = float(input("Height: "))
        volume = (length * width * height)/3
        result = ("\nThe volume of a pyramid \n" 
        	"of %.3f by %.3f by %.3f height is\n"
        	"%.3f cubic units." 
    	    % (length, width, height, volume)) 
        return result
    except ValueError:
        return (v_error)    
        
def sphere():
    try:
        radius = float(input("Radius: "))
        volume = (4 * pi * 
        	(radius ** 3)) / 3 
        result = ("\nThe volume of a sphere of\n" 
    	    "radius %.3f units is %.3f cubic units." 
    	    % (radius, volume)) 
        return result
    except ValueError:
        return (v_error)
        
# Menu. This is the main block
       # of the program. 

while True:
    print() 
    print("Choose the geometric figure\n"
	" for which you want the volume:\n"
	"1: Cone\n"
	"2: Cube\n"
	"3: Cylinder\n"
	"4: Pyramid\n"
	"5: Rectangular solid\n"
	"6: Sphere\n"
	"q: Quit") 
    print() 
    selection = input("Your selection: ") 
	
# Calling the right function
    if selection == "1":
    	    print(cone())
    	    carry_on()
    elif selection == "2":
    	    print(cube())
    	    carry_on()
    elif selection =="3":
        print(cylinder())
        carry_on()
    elif selection =="4":
        print(pyramid())
        carry_on()
    elif selection =="5":
        print(rectangular_solid())
        carry_on()
    elif selection =="6":
        print(sphere())
        carry_on()
    elif selection == ("q" or "Q"):
        print("You selected 'Quit'. Goodbye")
        break
    else:
        print("Your selection is not in the menu") 