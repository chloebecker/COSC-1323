##### Assignment 10
##### Chloe Becker 


# =================================================================
# AlienSpacecraft Class
# =================================================================
class AlienSpacecraft(object):
    
    # Constructor
    # Creates an AlienSpacecraft and initializes class variables
    #
    def __init__(self):
        
        print("A alien spacecraft has been born!")
        self.velocity = 0
        self.direction = "north"
        self.ammunitionLevel = 0  
    
    # setVelocity()
    # Sets the velocity of the alien spacecraft
    # Valid values are 0 - 10
    # raises ValueError if velocity is out of range
    #    
    def setVelocity(self, velocity) :
        
        if (velocity < 0 or (velocity + self.velocity) > 10 ) :
            raise ValueError("Error: velocity must be between 0 and 10")
        
        self.velocity = velocity
        
        print("Moving ", self.direction, "at velocity of ", self.velocity)
    
    # getVelocity()
    # returns the current spacecraft velocity
    #    
    def getVelocity(self) :
        return self.velocity
    
    # setDirection()
    # Sets the direction of the spacecraft
    # Valid directions are north, south, east or west
    # Raises a ValueError for an invalid direction
    def setDirection(self, direction) :
        
        allDirections = ["north", "south", "east", "west"]
        
        if (direction not in allDirections ) :
            raise ValueError("Error: directon must be north, south, east or west")
        
        self.direction = direction
        
        print("Direction set to ", self.direction)
    
    # getDirection()
    # Returns the current direction
    #
    def getDirection(self):
        
        return self.direction
    
    # setAmmunitionLevel()
    # Sets the ammunitionLevel of the spacecraft
    # Valid values are 0 - 10
    # Raises a ValueError if for an invalid ammunitionLevel
    #
    def setAmmunitionLevel(self, ammunitionLevel):
        
        if (ammunitionLevel < 0 or ammunitionLevel > 10) :
            raise ValueError("AmmunitionLevel must be between 0 and 10")
    
        self.ammunitionLevel = ammunitionLevel
        
        print("AmmunitionLevel set to ", self.ammunitionLevel)

    # getAmmunitionLevel()
    # Returns the current ammumition level
    #
    def getAmmunitionLevel(self):
        
        return self.ammunitionLevel

    # fireWeapons()
    # Fires the alien spacecraft weapons.
    # Decrements ammunitionlevel by 1
    # Prints error message if weapons fired and there is no
    # ammunition
    def fireWeapons(self):
        
        if (self.ammunitionLevel ==  0) :
            print("No Ammunition!  Rats, we're done for!")
            return
        else :
            self.ammunitionLevel -= 1
            print("Weapons fired!")

    # printCurrentValues()
    # Prints current values of object attributes
    #
    def printCurrentValues(self):
        
        print("\nCurrent Values:\n-------------------")
        print("Velocity: ", self.getVelocity())
        print("Directon: ", self.getDirection())
        print("Ammunition Level: ", self.getAmmunitionLevel())
        print("\n\n")
        
##########################################################################
######################### MY CODE ########################################

def get_num(message):
    loop = True
    num = 0
    while loop == True:
        try:
            num = int(input(message))
            loop = False
        except:
            print("\nInvalid input! Try again.")
    return num
       
def main():
    #instantiating object...
    alien = AlienSpacecraft()
    num = None
    
    while num != 6:
        #menu 
        print("""
                     This is what you can do:
                     
                     1) Add ammunition (0 - 10) 
                     2) Set velocity (0 - 10) 
                     3) Set direction (north, south, east west) 
                     4) Fire weapons 
                     5) Print current values 
                     6) Exit
                     """)
        #makes sure the number the user enters is an option on the menu
        num = None
        while num not in [1,2,3,4,5,6]:
            num = get_num("Choose an action from the menu (1-9): ")
            print("")

        ####option 1
        if num == 1:
            loop = True
            #uses a loop to keep asking the user if the program throws an error
            #****See the bottom for notes on alternate ways******
            while loop == True:
                level = get_num("\nEnter the amount of ammo to add (between 0 and 10): ")
                try:
                    alien.setAmmunitionLevel(level)
                    loop = False            
                except:
                    print("Error! Not a valid input.")
                    
        ####option 2
        elif num == 2:
            loop = True
            while loop == True:
                velocity = get_num("What velocity would you like to set your\
spaceship at? ")
                try:
                    alien.setVelocity(velocity)
                    loop = False
                except ValueError: #in case user enters something that's not an int
                    print("\nError! Your value needs to be a number in the range [0-10].")

        ####option 3
        elif num == 3:
            loop = True
            while loop == True:
                direction = input("Would you like to go north, east, south, or west? ")
                try:
                    direction = direction.lower()
                    alien.setDirection(direction)
                    loop = False 
                except ValueError:
                    print("\nYour direction needs to be either north, east, south, or west!")
                except:
                    print("Not a valid direction")
 
        ####option 4
        elif num == 4:
            alien.fireWeapons()
 
        ####option 5
        elif num == 5:
            alien.printCurrentValues()
 
        ####if #6 is chosen, the program exits


    
## Main code
    
main()


## NOTES!!***
#
#loop = True
#while loop == True:
#   try:
#       value = int(input("enter num"))
#       try:
#           alien.setAmmo(value)
#       except:
#           print("invalid")
#   except TypeError:
#       print("not an int- needs to be a number")







