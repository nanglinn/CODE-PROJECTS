import random,re

#-------------------------------------------------------------------------------
class Knight:
    def __init__(self, shield =5, weapon =5):
        self.weapon = weapon
        self.shield = shield
        self.health = 30
        
    
    def Kstrike(self):
        u = self.weapon*0.7
        return u
    
    def Kshield(self):
        u = self.weapon*0.5
        return u
    def changeHealth(self,a):
        self.health = self.health - a
        return a
#-------------------------------------------------------------------------------
class Mage:
    def __init__(self, shield =5, weapon=5):
        self.weapon = weapon
        self.shield = shield
        self.health = 30

    
    def Mstrike (self):
        u= self.weapon*0.4
        return u
    
    def Mshield (self):
        u = self.shield*0.2
        return u

    def changeHealth(self,a):
        self.health = self.health - a
        return a

    def Mheal (self):
        self.health = self.health + 2
        print (f'You have healed yourself by 2.')
#-------------------------------------------------------------------------------
class imp:
    def __init__(self,):
        self.health = 45
    
    def changeHealthImp(self,a):
        self.health = self.health - a
        return 
    
    def impFightOne(self):
        return random.randint(1,3)

    def impFightTwo(self):
        return random.randint(4,6)
    
    def impFightThree(self):
        return random.randint(6,8)
#-------------------------------------------------------------------------------

impHealth = 45
impFight = random.randint(1,3)
impFight2 = random.randint(4,6)
impFight2 = random.randint(6,8)
chance = 0
turn = 1
act = 0
t1 = 0
t2 = 0 
t3 = 0 
tot= 0

print (f'----------------------------------------------------------------------------------------------------------------')
# TITLE SEQUENCE

print (f'\t\t\t\t\tWelcome to Dungeon Quest!\n\t\tYou will play as an adventurer that traverses through dungeons to collect treasure.\
    \n\tHowever there will be imps crawling through the dungoen attempting to hinder your progress, so beware!\n')
print(f'----------------------------------------------------------------------------------------------------------------')
print(f"FOR THE PURPOSE OF THE PROJECT, THE ENTIRE PROGRAM HAS NOT BEEN CODED TO REMAIN MEDIUM IN SCALE, EXPECTED TO BE MUCH LARGER.\nCURRENTLY KNIGHT AND DUNGEON 1 ARE FUNCTIONAL.\n")
playerName = str(input(f'You will first need to enter your name: '))
validName = r'([A-Z]{1})([a-z]{2,})'
match = re.fullmatch(validName,playerName)

while match == None:
    print(f'Your name must be capitalized and at least three letters.')
    playerName = str(input(f'Enter your name: '))
    match = re.fullmatch(validName,playerName)
print(f'\n\n')
#regex to ensure that there are no numbers in the name, only letters.

answer = int(input(f'O brave {playerName}, what kind of adventurer are you going to become?\n1)A knight (slight strength and shield advantage).\n2)A mage (healing).\n'))
while answer < 1 or answer > 2:
    print('Invalid response... Enter a following number to be a part of that division:')
    answer = int(input(f'What kind of adventurer are you going to become?\n1) A knight.\n2) A mage.\n'))
print(f'\n------------------------------------------------------------------------------------------------------------------')

if answer == 1:
    playerType = 'knight'
else:
    playerType = 'mage'

print (f'You are hereby {playerName}, the {playerType}!\nNext you must strengthen your weapon and shield before venturing into the dungeon.\n\
You have 10 mana points available to strengthen either one.')
s = int(input(f'How many points for your shield?: '))
while (s > 10):
    s = int(input(f'You only have 10 mana points to use. Try again: '))
print(f'\n')
p = int(input(f'How many points for your weapon?: '))
while (s+p >10):
    p = int(input(f'Not enough mana points. You currently have {10-s} mana points. Try again: \n'))
print(f'\n\n')


#gameplay for a knight character
if answer == 1:
    player = Knight(s,p)

    while (tot < 3): #while not all the treasures have been found
        print(f'Which dungeon would you like to enter next?\n')
        resp = int(input(f'1)Dungeon 1\n2)Dungeon 2\n3)Dungeon 3\n'))
        if resp == 1:
            print(f"\n◉ The imp of this dungeon approaches holding a treasure! ◉")
            while t1 == 0:
                while turn %2 != 0: #the players turn
                    if (player.health <= 0):
                        print(f"\t\tYou have been attacked too much by the imp, and fainted..\n\t\t\t\tGAME OVER")
                        exit()
                    act = int(input(f"What would you like to do?\n1) Attack the imp.\nOR\n2) Block their next attack.\n"))
                    while act < 1 or act > 2:
                        act = int(input(f"You may only do one of the following..\n 1) Attack the imp!\nOR\n2) Block their next attack!?\n"))
                    if act == 1:
                        print(f'You swung your sword at the imp!')
                        impHealth = impHealth- player.Kstrike()
                        print(f"Your current health is {player.health:.2f}.\nYour enemy's health is {impHealth:.2f}\n-------------------")
                        turn +=1
                    if act == 2:
                        chance = random.randint(1,2)
                        if chance == 1:
                                print("Your block did not work! You were attacked by the imp.")
                                player.changeHealth(impFight-player.Kshield())
                                turn+=1
                        if chance == 2:
                                print("Your block worked!")
                                turn+=1

                while turn %2 == 0: #the imps turn
                    if (impHealth <= 0 ):
                        print("You beat the first imp and retireved the treasure!")
                        t1 = 1
                        tot +=1
                        exit()
                    player.changeHealth(impFight)
                    print(f'The imp scratched you!\nYour health is now {player.health:.2f}')
                    turn+=1


        if resp == 2:
            while t2 == 0:
                print("The imp of this dungeon approaches!")
                print(f'\nUNDER CONSTRUCTION.')
        if resp == 3:
            while t3 == 0:
                print("The imp of this dungeon approaches!")
                print(f'\nUNDER CONSTRUCTION.')
    
#gameplay of a mage character
elif answer == 2:
    player = Mage(s,p)

    while (tot < 3):
        print(f'You go through the enterance of the dungeon and enter the first dungeon down below.\n\Which dungeon would you like to enter first?\n')
        resp = int(input(f'1)Dungeon 1\n2)Dungeon 2\n3)Dungeon 3\n'))
        if resp == 1:
            while t1 == 0:
                print("The imp of this dungeon approaches!")
                print(f'\nUNDER CONSTRUCTION.')

        if resp == 2:
            while t2 == 0:
                print("The imp of this dungeon approaches!")
                print(f'\nUNDER CONSTRUCTION.')
        if resp == 3:
            while t3 == 0:
                print("The imp of this dungeon approaches!")
                print(f'\nUNDER CONSTRUCTION.')

