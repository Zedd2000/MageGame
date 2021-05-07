################################
#                               #
#   Working Name : Mage Battle  #
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

# TODO # Battle System
# TODO # High-level Stat rebalance
# TODO # Class ability mechanics
# TODO # Passive Item System
# TODO # Active Item System
# Distant TODO # Gooey GUI

import CharacterCreator as char
from CharacterCreator import classList, tierList, classNameList, classInfo
import random
import core
from os import system, name

def main():
    core.clear()

    p1 = char.Player(None,None,None,None) # This is all collected when the player character object is created
    enemy = char.NPC(None,None,None,None,None)

    core.clear()
    print("############## Player Info ###############")
    print("Name : " + p1.charName)
    print("Class : " + classList[int(p1.mageClass - 1)])
    char.Player.statPrint(p1)
    char.Player.calcStatPrint(p1)

    print("")

    print("############## Enemy Info ###############")
    print("Name : " + enemy.npcName)
    print("Class : " + enemy.mageClass)
    print("Tier : " + tierList[int(enemy.tierNum)])
    char.Player.statPrint(enemy)
    char.Player.calcStatPrint(enemy)
main()
