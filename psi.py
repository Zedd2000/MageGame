################################
#                               #
#   Working Name : PSI Battle   #
#   20201002 -                  #
#   Zed                         #
#                               #
#   Special Thanks              #
#   --------------              #
#                               #
#   JHarttech                   #
#   Popspy76                    #
#                               #
################################

import random
from os import system, name

psiList = ["eshot","bes","tele","abs","pyro"]
tierlist = ["Weakling", "Midling", "Boss", "Endgame"]

# Think of the PSI as the character class. Ex: Pyro, Heavy, Scout from tf2
classList = ["1) Energy Shot    : ","2) Beserker       : ","3) Telekinesis    : ","4) Absorbtion     : ","5) Pyrokenesis    : "]
classInfo = ["Energy Shot Class Info","Beserker Class Info","Telekinesis Class Info","Absorbtion Class Info","Pyrokenesis Class Info\n"]

# Distant TODO # Battle System
# Distant TODO # Class abilities
# Distant TODO # Item System
# Distant TODO # Gooey GUI
# TODO # Non-input, calculated stats

def clear(): # Clears the screen. Thanks Stackoverflow
        if name == 'nt':
            _ = system('cls') # for windows
        else:
            _ = system('clear') # for mac and linux

def rand_line(fname): #grabs random line of text file
    lines = open(fname).read().splitlines()
    return random.choice(lines)

#Player Character
class Player:
    def __init__(self, charName, psi, stats, calcStats):  # The Player character is created
        self.charName = ""
        while(not self.charName.strip()): # Making sure name is not set to an empty string
            self.charName = input("Name : ")
            clear()

        while(True): # Making sure psi selection is with an int
            try:
                for x,y in zip(classList,classInfo): # Printing names and info of the psi classes
                    print(x,y)
                self.psi = int(input("PSI : "))
                if(not 0< self.psi < 6):
                    int("Intentional ValueError") # input is out of the expected range, force a ValueError
            except ValueError:
                clear()
                print("Please enter a number given\n") # input was not an expected int, loop back
            else:
                break

        clear()

        self.stats = {
            "stre": [int(0),"Strength"],
            "inte": [int(0),"Intelligence"],
            "perc": [int(0),"Perception"],
            "fort": [int(0),"Fortitude"],
            "char": [int(0),"Charisma"],
            "quic": [int(0),"Quickness"],
            "luck": [int(0),"Luck"]
            }

        CR = None
        while(not CR in ["c","r","C","R"]):
            CR = input("Would you like Custom or Random stats? (C/R) : ")
            clear()
            if(CR in ["r","R"]): # Player has chosen to randomize their stats
                total = 0
                while(True):
                    for stat in self.stats:
                        vals = self.stats[stat] # Temporarily making into an accessable list
                        vals[0] = random.randint(1,10)
                        total += vals[0]
                        self.stats[stat] = vals # Moving changes back into dictionary entry
                    if(44 < total < 66):
                        break
                    else:
                        total = 0
            elif(CR in ["c","C"]): # Player has chosen to customize thier stats
                pool = 50
                while(pool > 0): # Loop while points are still available
                    for stat in self.stats:
                        clear()
                        self.statPrint()
                        print("Pool : " + str(pool)+"\n")
                        vals = self.stats[stat] # Temporarily making into an accessable list
                        delta = None # made to exist for the next loop
                        while(delta == None): # used to catch stats that go to high/low, and a negative pool
                            while(True):
                                try:
                                    if(pool == 0): # if the points pool is empty, break out of the loop.
                                        delta = 0
                                        break
                                    delta = int(input("Change " + vals[1] + " : ")) # collect how much to add/sub from the stat
                                    if(vals[0] + delta < 1 or vals[0] + delta > 10 or pool - delta < 0):
                                        int("Intentional ValueError") # The stat is too big/small or it goes past the point limit, so throw an error
                                except ValueError: # Player entered a string/an int out of the accepted range
                                    clear()
                                    self.statPrint()
                                    print("Pool : " + str(pool)+"\n")
                                    print("Stats must be between 1 and 10, with a total no greater than 50.") # input is undesirable. loop back
                                else:
                                    break # input is good. break out of loop
                            vals[0] += delta # temp variable is set to the input
                            self.stats[stat] = vals # stat is set to the temp variable
                            pool -= delta # The input is subtracted from the point pool.
                            if(pool == 0): # Out of point, break the loop
                                break

    def statPrint(self): # prints a nice, formatted list of stats
        print("=" * 25)
        total = 0
        for stat in self.stats:
            vals = self.stats[stat]
            total += vals[0]
            one = vals[1]
            two = str(vals[0])
            print( ' {:<20s} {:<10s}'.format(one, two) )
        print("-" * 25)
        print( ' {:<20s} {:<10s}'.format("Stat Total", str(total)) )
        print("=" * 25)

#Non-Playable Character
class NPC:
    def __init__(self, npcName, psi, stats,tiernum):
        self.tiernum = random.randint(0,3)
        self.npcName = rand_line(".randname") # TODO # Create cool collection of names to randomly select from
        self.psi = random.choice(psiList) # enemy is assigned a random class
        tmodmin = {0 : 1, 1 : 10, 2 : 20, 3 : 40}
        tmodmax = {0 : 10, 1 : 20, 2 : 30, 3 : 50}
        self.stats = {
            "stre": [random.randint(tmodmin.get(self.tiernum),tmodmax.get(self.tiernum)), "Strength"],
            "inte": [random.randint(tmodmin.get(self.tiernum),tmodmax.get(self.tiernum)), "Intelligence"],
            "perc": [random.randint(tmodmin.get(self.tiernum),tmodmax.get(self.tiernum)), "Perception"],
            "fort": [random.randint(tmodmin.get(self.tiernum),tmodmax.get(self.tiernum)), "Fortitude"], # All stats are semi-randomized due to tiers
            "char": [random.randint(tmodmin.get(self.tiernum),tmodmax.get(self.tiernum)), "Charisma"],
            "quic": [random.randint(tmodmin.get(self.tiernum),tmodmax.get(self.tiernum)), "Quickness"],
            "luck": [random.randint(tmodmin.get(self.tiernum),tmodmax.get(self.tiernum)), "Luck"]
            }

#================================================#

def main():
    clear()

    p1 = Player(None,None,None,None) # This is all collected when the player character object is created
    enemy = NPC(None,None,None,None)

    clear()
    print("############## Player Info ###############")
    print("Name : " + p1.charName)
    print("PSI : " + psiList[int(p1.psi - 1)])
    Player.statPrint(p1)

    print("")

    print("############## Enemy Info ###############")
    print("Name : " + enemy.npcName)
    print("PSI : " + enemy.psi)
    print("Tier : " + tierlist[int(enemy.tiernum)])
    Player.statPrint(enemy)
main()
