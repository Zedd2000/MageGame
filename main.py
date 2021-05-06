################################
#                               #
#   Working Name : PSI Battle   #
#   File: Main                  #
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

# Distant TODO # Battle System
# Distant TODO # Class abilities
# Distant TODO # Passive Item System
# Distant TODO # Active Item System
# Distant TODO # Gooey GUI
# TODO # Non-input, calculated stats

import CharacterCreator as char
from CharacterCreator import psiList, tierList, classList, classInfo
import random
import core
from os import system, name

def main():
    core.clear()

    p1 = char.Player(None,None,None,None) # This is all collected when the player character object is created
    enemy = char.NPC(None,None,None,None)

    core.clear()
    print("############## Player Info ###############")
    print("Name : " + p1.charName)
    print("PSI : " + psiList[int(p1.psi - 1)])
    char.Player.statPrint(p1)

    print("")

    print("############## Enemy Info ###############")
    print("Name : " + enemy.npcName)
    print("PSI : " + enemy.psi)
    print("Tier : " + tierList[int(enemy.tierNum)])
    char.Player.statPrint(enemy)
main()
