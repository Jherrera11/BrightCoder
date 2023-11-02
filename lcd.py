
def one ():
    #section top#
    print ("")
    #section bot#
    for i in range (height):
        print (" "*(width), end="")
        print ("|")
    #section bot#
    for i in range (height):
        print (" "*(width), end="")
        print ("|")


def two ():
    #section top#
    for i in range (width):
        print ("_", end="")
    print("")

    #section mid
    for i in range (height):
        print (" "*(width ), end="")
        print ("|")
    for i in range (width):
        print ("—", end="")
    print(" ")

    #section bot#
    for i in range (height):
        print ("|  ")
    for i in range (width):
        print ("—", end="")

def three ():
    #section top#
    for i in range (width):
        print ("_", end="")
    print("")
    #section mid#
    for i in range (height):
        print (" "*(width), end="")
        print ("|")
    for i in range (width):
        print ("—", end="")
    print("")
    #section mid#
    for i in range (height):
        print (" "*(width), end="")
        print ("|")
    for i in range (width):
        print ("—", end="")

def fourt ():
    #section top#
    print ("")
    #section mid#
    for i in range (height):
        print ("|", end="")
        print (" "*(width - 1), end="")
        print ("|  \n", end="")
    for i in range (width):
        print ("—", end="")
    #section bot#
    print("")
    for i in range (height):
        print (" "*(width - 2), end="")
        print ("  |")

def five ():
    #section top#
    for i in range (width):
        print ("_", end="")    
    print("")
    #section mid#
    for i in range (height):
        print ("|")
    for i in range (width):
        print ("—", end="")
    print("")
    #section bot#
    for i in range (height):
        print (" "*(width - 1), end="")
        print ("|")
    for i in range (width):
        print ("—", end="")

def six ():
    #section top#
    for i in range (width):
        print ("_", end="")    
    print("")
    #section mid#
    for i in range (height):
        print ("|")
    for i in range (width):
        print ("—", end="")
    print("")
    #section bot#
    for i in range (height):
        print ("|", end="")
        print (" "*(width - 1), end="")
        print ("|  \n", end="")
    print ("—"*(width), end="")


def seven ():
    #section top#
    for i in range (width):
        print ("_", end="")    
    print("")
    #section bot#
    for i in range (height):
        print (" "*(width), end="")
        print ("|")
    #section bot#
    for i in range (height):
        print (" "*(width), end="")
        print ("|")

def eight ():
    #section top#
    for i in range (width):
        print ("_", end="")    
    print("")
    #section mid#
    for i in range (height):
        print ("|", end="")
        print (" "*(width - 1), end="")
        print ("|  \n", end="")
    print ("—"*(width), end="")
    print("")
    #section bot#
    for i in range (height):
        print ("|", end="")
        print (" "*(width - 1), end="")
        print ("|  \n", end="")
    print ("—"*(width), end="")

def nine ():
    #section top#
    for i in range (width):
        print ("_", end="")    
    print("")
    #section mid#
    for i in range (height):
        print ("|", end="")
        print (" "*(width-1), end="")
        print ("|  \n", end="")
    print ("—"*(width), end="")
    print("")
    #section bot#
    for i in range (height):
        print (" "*(width), end="")
        print ("|")
    for i in range (width):
        print ("—", end="")    

numero = int(input("Give a number from 1 to 9: "))

height = int(input("Give the height : "))
width  = int(input("Give a width  : "))
match numero:
    case 1:
        one()
    case 2:
        two()
    case 3:
        three()
    case 4:
        fourt()
    case 5:
        five()
    case 6:
        six()
    case 7:
        seven()
    case 8:
        eight()
    case 9:
        nine()
    case _:
        print("ERROR only number 1 to 9")