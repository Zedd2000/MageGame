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

helpList = ["1) Energy Shot    : ","2) Beserker       : ","3) Telekinesis    : ","4) Absorbtion     : ","5) Pyrokenesis :"]
helpinfo = ["Energy Shot Info","Beserker Info","Telekinesis Info","Absoption Info","Pyrokenesis Info"]

def clear():

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux
        else:
            _ = system('clear')

#Player Character
class Player:
    def __init__(self, charName, psi, stats):
        self.charName = charName
        self.psi = psi
        self.stats = stats

#Non-Playable Character
class NPC:
    def __init__(self, npcName, stats):
        self.npcName = npcName
        self.stats = stats

class StatBlock:
    def __init__(self, stats):
        self.stats = stats[stre,inte,perc,fort,char,quic,luck]


#================================================#

def main():
    nameChoice = ""
    psiChoice = ""
    STATSPLACEHOLDER = ""

    clear()

    while(not nameChoice.strip()):
        nameChoice = input("Name? : ")
        clear()
    stats = StatBlock(stats)
    p1 = Player(nameChoice, psiChoice, STATSPLACEHOLDER)

    print(p1.charame)
    print(p1.psi)




main()
