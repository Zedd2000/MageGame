################################
#                               #
#   Working Name : PSI Battle   #
#   File:   Character Creator   #
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
import core

psiList = ["eshot","bes","tele","abs","pyro"]
tierList = ["Weakling", "Midling", "Boss", "Endgame"]

# Think of the PSI as the character class. Ex: Pyro, Heavy, Scout from tf2
classList = ["1) Energy Shot    : ","2) Beserker       : ","3) Telekinesis    : ","4) Absorbtion     : ","5) Pyrokenesis    : "]
classInfo = ["High damage in bursts, needs to recharge after using up thier energy.","Balanced stats, can activate Rage to greatly increase damage and decrease defense.","Medium-low stats, high speed, uses telekinesis to buff themself, and debuff enemies.","High defense and low damage, can absorb incoming damage and release it, dealing damage based on how much was stored.","Low damage, but can use fire to deal high amounts of damge over time.\n"]

#Player Character
class Player:
    def __init__(self, charName, psi, stats, calcStats):  # The Player character is created
        self.charName = ""
        while(not self.charName.strip()): # Making sure name is not set to an empty string
            self.charName = input("Name : ")
            core.clear()

        while(True): # Making sure psi selection is with an int
            try:
                for x,y in zip(classList,classInfo): # Printing names and info of the psi classes
                    print(x,y)
                self.psi = int(input("PSI : "))
                if(not 0< self.psi < 6):
                    int("Intentional ValueError") # input is out of the expected range, force a ValueError
            except ValueError:
                core.clear()
                print("Please enter a number given\n") # input was not an expected int, loop back
            else:
                break

        core.clear()

        self.stats = {
            "stre": [int(0),"Strength"],        #Str 0
            "inte": [int(0),"Intelligence"],    #Int 1
            "perc": [int(0),"Perception"],      #Per 2
            "fort": [int(0),"Fortitude"],       #frt 3  ##index values for easy referencing
            "char": [int(0),"Charisma"],        #chr 4
            "spee": [int(0),"Speed"],           #spe 5
            "luck": [int(0),"Luck"]             #luk 6
            }

        CR = None
        while(not CR in ["C","R"]):
            CR = input("Would you like Custom or Random stats? (C/R) : ").upper()
            core.clear()
            if(CR == "R"): # Player has chosen to randomize their stats
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
            elif(CR == "C"): # Player has chosen to customize thier stats
                pool = 50
                while(pool > 0): # Loop while points are still available
                    for stat in self.stats:
                        core.clear()
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
                                    core.clear()
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
        self.calcStats = Player.setCalcStats(self.stats)

    def setCalcStats(stats): #Calculates non-direct-input stats
        stre = stats.get("stre")[0]
        inte = stats.get("inte")[0]
        perc = stats.get("perc")[0]
        fort = stats.get("fort")[0]
        char = stats.get("char")[0]
        spee = stats.get("spee")[0]
        luck = stats.get("luck")[0]

        calcStats = {
                "crit": [int(luck),"Critical Chance"], #Luck stat + Accuracy Runoff
                "mxHP": [int((fort * 10) + (stre / 2)),"Max. HP"], #Fortitude * 10 + Strength / 2
                "accu": [int((perc * 11)),"Accuracy"], #Perception * 11, anything over 100 goes to crit
                "pote": [int((char * inte)),"Potency"], #Charisma * Intelligence
                "dodg": [int(((spee * 2) + luck) / (fort - (fort / 3))),"Dodge"] #((Speed*2)+luck)/(2/3) * Fortitude))
                }
        return calcStats

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

    def calcStatPrint(self):
        for cstat in self.calcStats:
            vals = self.calcStats[cstat]
            one = vals[1]
            two = str(vals[0])
            print( ' {:<20s} {:<10s}'.format(one, two) )
        print("-" * 25)


#Non-Playable Character
class NPC:
    def __init__(self, npcName, psi, stats, calcStats, tierNum):
        self.tierNum = random.randint(0,3)
        self.npcName = core.rand_line("data/.randname") # sets enemy name; Thanks to Rae Elliot (Barely Hare Books) for the list of names
        self.psi = random.choice(psiList) # enemy is assigned a random class
        tModMin = {0 : 1, 1 : 8, 2 : 26, 3 : 41}
        tModMax = {0 : 7, 1 : 25, 2 : 40, 3 : 75}
        self.stats = {
            "stre": [random.randint(tModMin.get(self.tierNum),tModMax.get(self.tierNum)), "Strength"],
            "inte": [random.randint(tModMin.get(self.tierNum),tModMax.get(self.tierNum)), "Intelligence"],
            "perc": [random.randint(tModMin.get(self.tierNum),tModMax.get(self.tierNum)), "Perception"],
            "fort": [random.randint(tModMin.get(self.tierNum),tModMax.get(self.tierNum)), "Fortitude"], # All stats are semi-randomized due to tiers
            "char": [random.randint(tModMin.get(self.tierNum),tModMax.get(self.tierNum)), "Charisma"],
            "spee": [random.randint(tModMin.get(self.tierNum),tModMax.get(self.tierNum)), "Speed"],
            "luck": [random.randint(tModMin.get(self.tierNum),tModMax.get(self.tierNum)), "Luck"]
            }
        self.calcStats = Player.setCalcStats(self.stats)
