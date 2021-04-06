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
            "stre": int(0),
            "inte": int(0),
            "perc": int(0),
            "fort": int(0),
            "char": int(0),
            "quic": int(0),
            "luck": int(0)
            }
        if(CR == "r" or CR == "R"): # Player has chosen to randomize thier stats
            for stat in self.stats:
                self.stats[stat] = random.randint(1,10) # TODO # Add min/max amount of points to be allocated
        elif(CR == "c" or CR == "C"): # Player has chosen to customize thier stats
            pool = 50
            while(pool > 0): # Loop while points are still available
                for stat in self.stats:
                    print(self.stats) # TODO # Make pretty
                    print("Pool : " + str(pool))
                    print("")
                    delta = None # made to exists for the next loop
                    while(delta == None): # used to catch stats that go to high/low, and a negative pool
                        delta = int(input("Change " + stat + " : "))
                        if(self.stats[stat] + delta < 1 or self.stats[stat] + delta > 10): # The stat is too big/small
                            print("Stats must be between 1 and 10")
                            delta = None # Loop back without moving to next stat
                        else:
                            self.stats[stat] += delta # Change is applied to the stat
                            pool -= delta # Same change is applied to the point pool
                        if(pool < 0): # The stat has become negative
                            print("Not enough points!\n")
                            pool += delta # Reverting change that made pool negative
                            self.stats[stat] -= delta # Reverting change that made pool negative
                            delta = None # Loop back without moving to next stat
                if(pool == 0 and sum(self.stats.values()) == 50):
                    print("You are out of points")
                    break


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

    clear()
    print(p1.charName)
    print(p1.psi)
    print(p1.stats)

main()
