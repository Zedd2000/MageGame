################################
#                               #
#   PSI Battle                  #
#   20201002 -                  #
#   Zed & JHarttech             #
#                               #
################################

import random
from os import system, name

psiList = ["eshot","bes","tele","abs"]
enemypsi = (psiList[random.randint(0,3)])

helpList = ["Enerny Shot    : ","Beserker       : ","Telekinesis    : ","Absorbtion     : "]
helpinfo = ["Energy Shot Info","Beserker Info","Telekinesis Info","Absoption Info"]

def clear():

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux
        else:
            _ = system('clear')

#Player Character
class Char:
    def __init__(self, player, psi):
        self.player = player
        self.psi = psi

class NPC:
    def __init__(self, npcName, stats):
        self.npcName = name
        slef.stats = stats


#================================================#

nameChoice = input("Name: ")
psiChoice = input("PSI: ")

p1 = Char(nameChoice, psiChoice)

print(p1.player)
print(p1.psi)
