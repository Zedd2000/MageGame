################################
#                               #
#   PSI Battle                  #
#   20201002 -                  #
#   Zed & JHarttech             #
#                               #
################################

import random
from os import system, name

#psiList = ["eshot","bes","tele","abs","pyro"]
#enemypsi = (psiList[random.randint(0,4)])

#helpList = ["1) Energy Shot    : ","2) Beserker       : ","3) Telekinesis    : ","4) Absorbtion     : ","5) Pyrokenesis :"]
#helpinfo = ["Energy Shot Info","Beserker Info","Telekinesis Info","Absoption Info","Pyrokenesis Info"]

# Distant TODO # Battle System
# Distant TODO # Class abilities
# Distant TODO # Item System
# Distant TODO # Gooey GUI

def clear():

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux
        else:
            _ = system('clear')

#Player Character
class Player:
    def __init__(self, charName, psi, stats):  #The Player character is created
        # Name and class are collected during creation
        self.charName = input("Name : ")
        self.psi = input("PSI : ") # TODO # Selective data input
        CR = input("Would you like Custom or Random stats? (C/R) : ")
        self.stats = {
            "stre": [int(0),"Strength"],
            "inte": [int(0),"Intelligence"],
            "perc": [int(0),"Perception"],
            "fort": [int(0),"Fortitude"],
            "char": [int(0),"Charisma"],
            "quic": [int(0),"Quickness"],
            "luck": [int(0),"Luck"]
            }
        if(CR == "r" or CR == "R"): # Player has chosen to randomize their stats
            minmax = False
            total = 0
            while(minmax == False):
                for stat in self.stats:
                    vals = self.stats[stat] # Temporarily making into an accessable list
                    total += vals[0]
                    vals[0] = random.randint(1,10) # TODO # Add min/max amount of points to be allocated
                    self.stats[stat] = vals # Moving changes back into dictionary entry
                print(total)
                if(35 < total < 60):
                    minmax = True
                else:
                    total = 0
        elif(CR == "c" or CR == "C"): # Player has chosen to customize thier stats
            pool = 50
            while(pool > 0): # Loop while points are still available
                for stat in self.stats:
                    clear()
                    self.statPrint()
                    print("Pool : " + str(pool))
                    print("")
                    vals = self.stats[stat] # Temporarily making into an accessable list
                    delta = None # made to exist for the next loop
                    while(delta == None): # used to catch stats that go to high/low, and a negative pool
                        delta = int(input("Change " + vals[1] + " : "))
                        if(vals[0] + delta < 1 or vals[0] + delta > 10): # The stat is too big/small
                            print("Stats must be between 1 and 10")
                            delta = None
                        else:
                            vals[0] += delta
                            self.stats[stat] = vals
                            pool -= delta
                        if(pool < 0):
                            print("Not enough points!\n")
                            pool += delta
                            vals[0] -= delta
                            self.stats[stat] = vals
                            delta = None
                        if(pool == 0):
                            print("You are out of points")
                            break
                if(pool == 0):
                    print("You are out of points")
                    break

    def statPrint(self):
        print("=" * 25)
        for stat in self.stats:
            vals = self.stats[stat]
            one = vals[1]
            two = str(vals[0])
            print( ' {:<20s} {:<10s}'.format(one, two) )
        print("=" * 25)


#Non-Playable Character
class NPC:
    def __init__(self, npcName, stats):
        self.npcName = "Randomized Enemy NPC" # TODO # Create collection of names to randomly select from
        self.psi = (psiList[random.randint(0,4)]) # enemy is assigned a random class
        print(self.psi) # Temporary, for my sake
        self.stats = {
            "stre": [random.randint(1,10)],
            "inte": [random.randint(1,10)],
            "perc": [random.randint(1,10)],
            "fort": [random.randint(1,10)], # All stats are randomized
            "char": [random.randint(1,10)], # TODO # Create tiers of enemies with varying min/max stat levels
            "quic": [random.randint(1,10)], #      # EX: Weakling, mid-grade, boss, endgame
            "luck": [random.randint(1,10)]
            }



#================================================#

def main():
    clear()

    p1 = Player(None,None,None) # This is all collected when the player character object is created

    #clear()
    print("############## Player Info ###############")
    print("Name : " + p1.charName)
    print("PSI : " + p1.psi)
    Player.statPrint(p1)
main()
