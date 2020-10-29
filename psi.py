################################
#                               #
#   PSI Battle                  #
#   20201002 -                  #
#   Zed & JHarttech             #
#                               #
################################
#   Back Burner                 #
#                               #
#   Pyrokinesis -poison         #
#   GUI                         #
#                               #
###############################
#   Known Issues                #
#   ************                #
#                               #
#   pType() loop is funky       #
#                               #
#                               #
#


import random
from os import system, name

psiList = ["eshot","bes","tele","abs"]
enemypsi = (psiList[random.randint(0,3)])

helpList = ["Enerny Shot    : ","Beserker       : ","Telekinesis    : ","Absorbtion     : "]
helpinfo = ["Energy Shot Info","Beserker Info","Telekinesis Info","Absoption Info"]

class Engine():

    def start():
        print("Welcome.\n")
        print("Would you like to create a new game")
        nl = input("or Load a saved one? : ")
        onepass = False
        while(onepass == False):
            while(nl.lower() not in ("load","new")):
                nl = input("(new / load) : ")
            if(nl.lower() == "load"):
                onepass = True
                print("\nLoad function goes here")
                Engine.clear()
                Char.name()
            elif(nl.lower() == "new"):
                onepass = True
                print("\n## New Game ##")
                Engine.clear()
                Char.name()

    def clear():

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux
        else:
            _ = system('clear')

class Char():

    def name():
        pName = ""
        while(not pName.strip()):
                pName = input("What is your name? : ")
                Engine.clear()
        pName = str(pName)
        Engine.clear()
        Char.pType()

    def intcheck():
        while(True):
            try:
                psi = int(input("Please enter a number given : "))
            except(ValueError):
                psi = int(input("Please enter a number given : "))
            else:
                while(psi == 5):
                    for x,y in zip(helpList,helpinfo):
                        print(x,y)
                    input("Continue")
                    Engine.clear
                    Char.intcheck()


    def pType():
        psi = None
        print("""What Type of Psychic Power do you Desire?\n
                (1) Energy Shot     (2) Beserker
                (3) Telekinesis     (4) Absorption
                (5) Help\n""")
        Char.intcheck()

        print("#######", psiList[int(psi)-1])
        print("####### Enemy =", enemypsi)
        input("#######dev pause for info")
        Engine.clear()
        Char.cr()

    def cr():
        global initChoice
        choiceTest = None
        while(choiceTest == None):
            print("Customize (C), Randomize (R)")
            initChoice = input("Would you like to customize a character or have one randomized for you?: ")
            if(initChoice.lower() == "c" or initChoice.lower() == "r"):
                choiceTest = True
            else:
                print("\n###############################################################")
                print("# Please enter either a C to customize, or an R to randomize. #")
                print("###############################################################")
        if(initChoice.lower() == "c"):
            Engine.clear()
            Char.custom()
        else:
            Engine.clear()
            Char.randChar()

    def statTable():
        if(pool > 0):
            print("You have", pool," character points left to spend.")
            print("\nName         : ", pName)
            print("Strength     : ", stre)
            print("Awareness    : ", awar)
            print("Fortitude    : ", fort)
            print("Charisma     : ", char)
            print("Intellect    : ", inte)
            print("Quickness    : ", quic)
            print("Luck         : ", luck)
        else:
            print("Name         : ", pName)
            print("\nStrength     : ", stre)
            print("Awareness    : ", awar)
            print("Fortitude    : ", fort)
            print("Charisma     : ", char)
            print("Intellect    : ", inte)
            print("Quickness    : ", quic)
            print("Luck         : ", luck)

    def custom():
        #stats are given a base stat of 5, and the player can put up to 5 extra points into each stat.
        global stre
        global awar
        global fort
        global char
        global inte
        global quic
        global luck
        pool = 5
        stre = 5
        awar = 5
        fort = 5
        char = 5
        inte = 5
        quic = 5
        luck = 5
        while(pool > 0):
            netPoints = stre + awar + fort + char + inte + quic + luck
            print("Stats must be between 1 and 10")
            Char.statTable()
            Char.calcStats()
            print("Total        : ",netPoints)
            #player is given the option to add to a stat or subtract from one.
            addsub = input("\nWould you like to add or subtract form a stat? (+/-): ")
            if(addsub == "+"):
                #player is chosing what stat to add to.
                stat = input("\nWhat stat? (First Letter): ")
                if(stat == "s" or stat == "S"):
                    stre += 1
                    pool -= 1
                    if(stre == 11):
                        stre -= 1
                        pool += 1
                elif(stat == "a" or stat == "A"):
                    awar += 1
                    pool -= 1
                    if(awar == 11):
                        perc -= 1
                        pool += 1
                elif(stat == "f" or stat == "F"):
                    fort += 1
                    pool -= 1
                    if(fort == 11):
                        fort -= 1
                        pool += 1
                elif(stat == "c" or stat == "C"):
                    char += 1
                    pool -= 1
                    if(char == 11):
                        char -= 1
                        pool += 1
                elif(stat == "i" or stat == "I"):
                    inte += 1
                    pool -= 1
                    if(inte == 11):
                        inte -= 1
                        pool += 1
                elif(stat == "q" or stat == "Q"):
                    quic += 1
                    pool -= 1
                    if(quic == 11):
                        agil -= 1
                        pool += 1
                elif(stat == "l" or stat == "L"):
                    luck += 1
                    pool -= 1
                    if(luck == 11):
                        luck -= 1
                        pool += 1
                else:
                    print("\n##########################################")
                    print("# Please use the first letter of a stat. #")
                    print("##########################################")
            elif(addsub == "-"):
                #player is chosing what stat to subtract from.
                stat = input("\nWhat stat? (First Letter): ")
                if(stat == "s" or stat == "S"):
                    stre -= 1
                    pool += 1
                    if(stre == 0):
                        stre += 1
                        pool -= 1
                elif(stat == "a" or stat == "A"):
                    awar -= 1
                    pool += 1
                    if(perc == 0):
                        perc += 1
                        pool -= 1
                elif(stat == "f" or stat == "F"):
                    fort -= 1
                    pool += 1
                    if(fort == 0):
                        fort += 1
                        pool -= 1
                elif(stat == "c" or stat == "C"):
                    char -= 1
                    pool += 1
                    if(char == 0):
                        char += 1
                        pool -= 1
                elif(stat == "i" or stat == "I"):
                    inte -= 1
                    pool += 1
                    if(inte == 0):
                        inte += 1
                        pool -= 1
                elif(stat == "q" or stat == "Q"):
                    quic -= 1
                    pool += 1
                    if(quic == 0):
                        agil += 1
                        pool -= 1
                elif(stat == "l" or stat == "L"):
                    luck -= 1
                    pool += 1
                    if(luck == 0):
                        luck += 1
                        pool -= 1
                else:
                    print("\n##########################################")
                    print("# Please use the first letter of a stat. #")
                    print("##########################################")
            else:
                print("\n##############################")
                print("# Please enter either + or - #")
                print("##############################")
        Char.statTable()
        Char.calcStats()
        Char.saveChar()
        print("\nThis is now your character.")
        input("\nPress Enter to exit.")


    def randChar():
        global stre
        global awar
        global fort
        global char
        global inte
        global quic
        global luck
        test = False
        while(test != True):
            stre = random.randint(1,10)
            awar = random.randint(1,10)
            fort = random.randint(1,10)
            char = random.randint(1,10)
            inte = random.randint(1,10)
            quic = random.randint(1,10)
            luck = random.randint(1,10)
            netPoints = stre + awar + fort + char + inte + quic + luck
            if(netPoints >= 30 and netPoints <= 45):
                test = True
            elif(netPoints == 60):
                #That's a 0.00001% chance of rolling max stats
                test = True
        print("Name         : ", pName)
        print("Level        : ", pLevel)
        print("Strength     : ", stre)
        print("Awareness    : ", awar)
        print("Fortitude    : ", fort)
        print("Charisma     : ", char)
        print("Intellect    : ", inte)
        print("Quickness    : ", quic)
        print("Luck         : ", luck)
        print("Total        : ", netPoints)

    def calcStats():
        global maxHP
        global pHP
        global maxEnergy
        global energy
        global critChance
        global critDam
        global meleeDam
        global physDef
        global spDef
        maxHP = fort * 10
        #
        #if class == bes then maxhp = fort * 15
        #
        pHP = maxHP
        maxStam = int((fort * quic) / 2)
        stam = maxStam
        maxMana = int((inte * char) / 2)
        mana = maxMana
        skillRate = int(10 + (inte / 2))
        maxCarry = (150 + (stre * 10))
        critChance = int(luck / 100)
        critDam = 2
        meleeDam = int(stre / 2)
        physDef = 0
        spDef = 0
        print("\nHP           : ", pHP,"/", maxHP)
        print("Stamina      : ", stam,"/", maxStam)
        print("Mana         : ", energy,"/", maxEnergy)
        print("         ____________")
        print("        |TEMP DEV BOX|")
        print("=============================")
        print("Skill Rate   : ", skillRate)
        print("Carry Weight : ", maxCarry)
        print("Crit Chance  : ", critChance, "%")
        print("Crit Damage  : ", critDam)
        print("Melee Damage : ", meleeDam)
        print("Phys. Def.   : ", physDef)
        print("Psi Def.     : ", spDef)
        print("=============================")

    def saveChar():
        save = open(pName + ".txt", "a+")
        save.write(str(pName) + ":")
        save.write(str(stre) + ":")
        save.write(str(awar) + ":")
        save.write(str(fort) + ":")
        save.write(str(char) + ":")
        save.write(str(inte) + ":")
        save.write(str(quic) + ":")
        save.write(str(luck) + ":")
        save.write(str(maxHP) + ":")
        save.write(str(pHP) + ":")
        save.write(str(maxStam) + ":")
        save.write(str(stam) + ":")
        save.write(str(maxMana) + ":")
        save.write(str(mana) + ":")
        save.write(str(critChance) + ":")
        save.write(str(critDam) + ":")
        save.write(str(meleeDam) + ":")
        save.write(str(physDef) + ":")
        save.write(str(spDef) + "\n")
        save.close()


Engine.clear()
Engine.start()
