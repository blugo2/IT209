#-------------------------------------------------------------------------+
#Program name: IT209_A9.py                                                |
#Author: Brendon Lugo and William Dugbly                                  |
#Date Written: 4/17/19                                                    |
#Purpose: Assignment 9                                                    |  
#-------------------------------------------------------------------------+
print("Welcome to the start of Assignment 9...")
from os import system, name
import random
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

class Char():
    def __init__(self, Name, Hp, Att, Def, Sp):   #Added Sp for Speical Move funcationality
        self.Name= str(Name)
        self.Hp= int(Hp)
        self.Att= int(Att)
        self.Def= int(Def)
        self.Sp = int(Sp)
        #self.Bag = []                       #Change from UML Char has bag rather than UI

    def __str__(self):
        print("**put ascii drawing here**")

    #def Access_Bag(Bag):
        #for i in bag:
            #print i

    def Use_Ability(Move, Move_Cost, Name, Type):
        if self.Mag >= Move_Cost:
            self.Mag -= Move_Cost
            if Type == "Att":
                self.Att += Move
            if Type == "Hp":
                self.Hp += Move
            print(self.name,' uses ',name,'!')
        else:
            print("You do not have enough Magic for that!")

class Mage(Char):
    def __init__(self, Name, Hp, Att, Def, Sp, Mag, c_type):
        super().__init__(Name, Hp, Att, Def, Sp)
        self.Mag = 4
        self.c_type = 'm'

    def __str__(self):
        print("put drawing in here")

    def Ability(self):
        Name = "FireBall"
        Move = self.Sp + 3
        Move_Cost = 1
        Type = "Att"
        self.Use_Ability(Move, Move_Cost, Name, Type)

class Knight(Char):
    def __init__(self, Name, Hp, Att, Def, Sp, Mag, c_type):
        super().__init__(Name, Hp, Att, Def, Sp)
        self.Mag = 4
        self.c_type = 'k'

    def __str__(self):
        print("put drawing in here")

    def Ability(self):
        Name = "Heal"
        Move = self.Sp + 2
        Move_Cost = 1
        Type = "Hp"
        self.Use_Ability(Move, Move_Cost, Name, Type)

class Archer(Char):
    def __init__(self, Name, Hp, Att, Def, Sp, Mag, c_type):
        super().__init__(Name, Hp, Att, Def, Sp)
        self.Mag = 4
        self.c_type = 'a'

    def __str__(self):
        print("put drawing in here")

    def Ability(self):
        Name = "Rain Arrows"
        Move = self.Sp + 2
        Move_Cost = 1
        Type = "Att"
        self.Use_Ability(Move, Move_Cost, Name, Type)
#---------------Character Class Above, Enemy Below -----------------------------------
class Mob():
    def __init__(self, Hp, Att):   #Added Sp for Speical Move funcationality
        self.Hp= int(Hp)              #Removed Name, mobs dont have uquie names
        self.Att= int(Att)
            
class Dragon(Mob):
    def __init__(self,Hp, Att, ID):
        super().__init__(Hp, Att)
        self.ID = str(ID)
        self.Moves= ["Fire Breath","Dragon's Claw","Tail Whip","Glazing Stare"]
        
    def __str__(self):
        return("put drawing in here")

    def openmsg(self):
        return("An adolesent dragon appears!")

class Wolf(Mob):
    def __init__(self, Hp, Att, ID):
        super().__init__(Hp, Att)
        self.ID = str(ID)
        self.Moves= ["Howlof the pack","Chomp","Claw","Tail Whip"]
        
    def __str__(self):
        return("put drawing in here")

    def openmsg(self):
        return("A wild wolf appears!")

class Zombie(Mob):
    def __init__(self, Hp, Att, ID):
        super().__init__(Hp, Att)
        self.ID = str(ID)
        self.Moves= ["Bite","Claw","Screech","Decaying Burst"]
        
    def __str__(self):
        return("put drawing in here")
        
    def openmsg(self):
        return("A wild zombie appears!")

class Boss(Mob):
    def __init__(self, Hp, Att, ID):
        super().__init__(Hp, Att)
        self.ID = str(ID)
        self.Moves= ["Python Mastery","Lazer Eyes","Fire Breath","One Inch Punch"]
        
    def __str__(self):
        return("put drawing in here")
        
    def openmsg(self):
        return("The rain bends and curves around the figure, creating a sphear of air with no rain. This sphear extends itself towards you and blocks the rain from falling, allowing you to see. \n\n'I am the gurdian of this world, and you have tresspassed here long enough. Its time to send you where you belong.'\n\nNow that you can clearly see, you read the name tag on the figure. It says Professor Shuman, Python Master. Before you have time to speak he attacks!")

#-------------------Enemies Above, Biome Below--------------------
class Biome():
    def __init__(self,Forest_Area, Mountian_Area, Sand_Area, choice):
        self.Forest_Area = Forest_Area
        self.Mountian_Area = Mountian_Area
        self.Sand_Area = Sand_Area
        self.choice = "G"
        
    def PickArea(self, Area):
        if Area == "F":
            self.choice = "F"

        elif Area == "M":
            self.choice = "M"
            
        elif Area == "D":
            self.choice = "D"
        else:
            print("You entered an incorrect choice.")

    def setChoice(self,new):
        self.choice = new
        return self.choice

    def PickAreaEvent(self,choice):
        if choice == "F":
            Event = random.choice(self.Forest_Area)
            print('''
You find yourself in an area that you recognize as''',Event)
        elif choice == "M":
            Event = random.choice(self.Mountian_Area)
            print('''
You find yourself in an area that you recognize as''',Event)
        elif choice == "D":
            Event = random.choice(self.Sand_Area)
            print('''
You find yourself in an area that you recognize as''',Event)
            

        
#---------BIOME CLASS ABOVE, ITEMS CLASS BELOW------------------------
class Items():
    def __init__(self,knightems,archItems,mageItems):
            self.knightems = knightems
            self.archItems = archItems
            self.mageItems = mageItems

    #def PlayerItems(self,Player):
       # if Player.c_type == "k":
        #    worldItems = self.knightems
      ##      return worldItems
      #  elif Player.c_type == "m":
       #     worldItems = self.mageItems
      #      return worldItems
      #  elif Player.c_type == "a":
      #      worldItems = self.archItems
      #      return worldItems

    def getItems(self):
        if Player.c_type == "k":
            print("You find one:",random.choice(list(self.knightems)),"!")
        elif Player.c_type == "m":
            print("You find one:",random.choice(list(self.mageItems)),"!")
        elif Player.c_type == "a":
            print("You find one:",random.choice(list(self.archItems)),"!")
            
gameItems= Items({'Apple':1,"Rubber Chicken":2,"Turkey leg":3, "Dagger":4,"Chipotle":5,"Broadsword":6,"Big Mac":7,"Greataxe":8},
                 {'Apple':1,"Nerf bow":2,"Turkey leg":3, "longbow":4,"Chipotle":5,"Crossbow":6,"Big Mac":7,"Magic bow":8},
                 {'Apple':1,"Useless stick":2,"Turkey leg":3, "Magic wand":4,"Chipotle":5,"Spellbook":6,"Big Mac":7,"Choatic staff":8}
                  )

#---------ITEMS CLASS ABOVE, CONTROLLER CLASS BELOW------------------------

class controller():
    def __init__(self, turnCount, bag, title, choose, Player):
        self.turnCount = 0
        self.bag = []
        self.title = title
        self.choose = choose
        self.Player = ""

    def TriggerItem(self):
        if Player.c_type == "k":
            PlayerItems = {'Apple':1,"Rubber Chicken":2,"Turkey leg":3, "Dagger":4,"Chipotle":5,"Broadsword":6,"Big Mac":7,"Greataxe":8}
        elif Player.c_type == "m":
            PlayerItems = {'Apple':1,"Nerf bow":2,"Turkey leg":3, "longbow":4,"Chipotle":5,"Crossbow":6,"Big Mac":7,"Magic bow":8}
        elif Player.c_type == "a":
            PlayerItems = {'Apple':1,"Useless stick":2,"Turkey leg":3, "Magic wand":4,"Chipotle":5,"Spellbook":6,"Big Mac":7,"Choatic staff":8}
            
        itemPickup = random.randint(1,10)
        if itemPickup%2 == 0:
            pick = random.randint(0,7)
            current_item = []
            current_item.append(list(PlayerItems)[pick - 1])
          
            if pick%2 == 0:
                print("You found a", current_item," that you are now weilding and your attack is now", pick)
                Player.Att += pick
            else:
                print("You found a", current_item," that you consume quicly and gain the following hp:",pick)
                Player.Hp += pick
        else:
            controller.TriggerMob()
    
    def TriggerMob():
        itemPickup = random.randint(1,10)
        if itemPickup in range(1,3):
            zombieMob = Zombie(4,2,"Zombie")
            BattleMob = zombieMob
            controller.TriggerBattle(BattleMob)
        elif itemPickup in range(4,5):
            wolfMob = Wolf(10,2,"Wolf")
            BattleMob = wolfMob
            controller.TriggerBattle(BattleMob)
        elif itemPickup == 6:
            dragonMob = Dragon(10,2,"Dragon")
            BattleMob = dragonMob
            controller.TriggerBattle(BattleMob)
        else:
            print("Oof, bad luck... You didn't find anything.")

    def TriggerBattle(BattleMob):
        BattleMob = BattleMob
        print(BattleMob)
        print(BattleMob.openmsg())
        while BattleMob.Hp > 0:
            BattleMob_Turn = random.randint(1,2)
            if BattleMob_Turn == 1:
                Player.Hp -= BattleMob.Att
                if Player.Hp >0:
                    print("The enemy attacks with",random.choice(BattleMob.Moves),
                                  "- You have", Player.Hp,"health remaining.")
                else:
                    print("The enemy attacks with a",random.choice(BattleMob.Moves),
                                  "- You have 0 health. You died!!")
            else:
                print("The ",BattleMob.ID," attack missed you!")
            if Player.Hp < 1:
                #self.turnCount = 6
                break
            else:
                pass
            print("What will you do?")
            action = input("1. for basic attack 2. to use your special: ") #put validtoin here
            if action == "1":
                BattleMob.Hp -= Player.Att
                print("You attack the",BattleMob.ID,"!")
                
                if BattleMob.Hp <= 0:
                    print("The enemy has lost all its health!!")
                else:
                    print("The enemy now has",BattleMob.Hp,"health remaining.")
            elif action == "2":
                if Player.c_type.lower() == 'm':
                    print("f")
                elif Player.c_type.lower() == 'a':
                    print("f")
                elif Player.c_type.lower() == 'k':
                    print("f")
        if Player.Hp >0:
            print("You defeated a",BattleMob.ID)
        else:
            control.turnCount = 6
        
        
    def PlayerClass(self):
        if self.turnCount == 0:
            print(title)
            time.sleep(1)
            clear()
            print(choose)
            time.sleep(1)

            classType = input('''
            --- Knight
            --- Mage
            --- Archer
            Enter 1 of the above class choices: ''')        
            while classType.lower() not in("knight","mage","archer"):                   #Validation for which class
                print("Please Enter a Valid Class")
                classType = input('''
            --- Knight
            --- Mage
            --- Archer
            Enter 1 of the above class choices: ''')
            Char.name = input("What is your name?: ")
            if classType.lower() == "knight":
                PlayerK = Knight(name,20,3,4,5,2,'k')
                self.Player = PlayerK
                return self.Player
            elif classType.lower() == "archer":
                PlayerA = Archer(name,2,3,4,5,2,'a')
                self.Player = PlayerA
                return self.Player
            elif classType.lower() == "mage":
                PlayerM = Mage(name,2,3,4,5,2,'m')
                self.Player = PlayerM
                return self.Player
            
    def startWorld(self):
        clear()

        print("Welcome, ",self.Player.name,"...")
        print('''
        Before you, you see mountains made of a dark black rock. They look dangerous,
        but the reward has to be worth it... right?
        To the left you notice an large forest. Probably some cute squirrels or something
        To your right you see a desert in the distance. Looks dry. I bet there's a nice
        tanning spot down this way.
        ''')
        choice = input(
        '''
        -- Mountains
        -- Forest
        -- Desert
        Would you like to go to the mountains, forest, or desert?(F,M,D): ''')
        while choice.upper() not in("F","M","D"):                                           #Validation for which area
            print("Please pick a valid choice:")
            choice = input(
            '''
            -- Mountains
            -- Forest
            -- Desert
            Would you like to go to the mountains, forest, or desert?(F,M,D): ''')
        if choice.upper() == "F":                                                         #Valor text about which area to choose
            cloud = "Forest"
            print("""
            With the wind in your hair and bugs chittering around you, you head towards the 
            large forest. You have spent some time travelling along the well worn dirt path
            beneath your feat when your senses spot something. That cute squireel perhaps?
            You stop and gather in your surroundings...""")
                
        elif choice.upper() == "M":
            cloud = "Mountains"
            print("""
            You decide to head towards the mountain made of dark rock. As you get closer you
            spot a winding trail that grips to the mountains edge. By the time you have made it
            to the begining of the trail, the air is cold and stale. Something about this
            mountain makes your skin crawl. You decied to stop, catch your breath, and take
            in your surroundings...
            """)
        elif choice.upper() == "D":
            cloud = "Desert"
            print("""
            You trod down the slopes towards the desert. With the sand blowing past your
            face and the sun beating down your neck you feel confident in your choice.
            As you walk, you begin to notice high dunes besides you and you wonder how
            long they have stood. In the distance you hear a sharp jackle and your hair
            stands on edge. Perhaps someone, or something, is also wandering among the
            dunes. You stand at ease and being to take in your surroundings...
            """)
            
        CloudMsg = [("As you continue along your journey,  you stop to gaze up upon the clouds. A curious thing catchs your eye. In the distance you can see waht you can only describe as a faint, dark object on the horizen. You blink and its gone, hopefully it was nothing."),
                    ("Having progessed further along towards your destination you stop to take a rest. Before your eyes fully close you note that the object on the horizion you saw eariler has reappeared, bigger in size yet still quit some distance away. You note that it may be a strom, but quickly dirft to sleep."),
                    ("Now that you have made considerable progress through the area you are suddenly aware of a dark presence near you. You look up and realize that the dark object from before was indeed a storm, a big one too as it apears. Hopefully you reach your destination before it hits you..."),
                    ("The storm is making quick  time, and you feel the air around get colder. The air tastes moist, and the sky is grey. You quickly push on towards the center of this area!"),
                    ("The storm is upon you! The edge of the storm is quickly gaining ground on you, try as you might you are not able to outrun it. The sky turns dark around you, and thick heavy droplets press against your skin. Lighting crackles and momentairy lights your path. You breifly see a figure standing before you, it seems to be the epicentor of the storm..."),
                    ("Death greets you"),
                    ("The clouds clear up")]
        
        GameWorld = Biome(['Red Wood National Park','The Spooky Woods','Hidden Grove',"The Witch's Hut"],
                ['Mount Denali National Park','The Snowy Peaks','The Raging River','The Abandoned Cabin'],
                ['The Grand Canyon','The Oasis',"Mars' Dunes",'The Hidden Cave'],'G')
        GameWorld.PickArea(choice)
        self.turnCount += 1
        run = True
        while run == True:
            #while self.turnCount <= 5:
                if self.turnCount != 5:
                    GameWorld = Biome(['Red Wood National Park','The Spooky Woods','Hidden Grove',"The Witch's Hut"],
                        ['Mount Denali National Park','The Snowy Peaks','The Raging River','The Abandoned Cabin'],
                        ['The Grand Canyon','The Oasis',"Mars' Dunes",'The Hidden Cave'],'G')
                    GameWorld.PickAreaEvent(choice)
                    fobjects = ["a hollowed out log","a patch of mushrooms","some brush","some small bush","a thorn patch","tall grass"]
                    dobjects = ["a tumble weed","a colorful cactus","a spikey cactus","a small dune","a patch of dead grass","an antelope skull","a large boulder"]
                    mobjects = ["a jagged rock","a smooth stone","a puddle","crevace","a patch of weeds","a mound of gravel","a mossy stone"]
                    entry = input("\nTo your left you see "+random.choice(fobjects)+ ". To your right you see "+random.choice(fobjects)+". Which do you search?: ")
                    print("\n")
                    controller.TriggerItem(Player)
                    input("Hit Enter to Move on...")
                    time.sleep(2)
                    clear()
                    print("\n\n",CloudMsg[self.turnCount - 1].strip("'"),"\n\n")
                    self.turnCount += 1
                    input("Hit Enter to Move on...")
                    
                elif self.turnCount == 5:
                    controller.endGame()
                    
                elif self.turnCount == 6:
                    print("game over")
                    
                elif self.turnCount == 7:
                   print("put end game credits here")

    def endGame():
        Professor_Shuman = Boss(10,2,"Professor_Shuman")
        BattleMob = Professor_Shuman
        controller.TriggerBattle(BattleMob)

#-------------Openning Credits-------------------------------
import time
import random
#import pygame



creditPage = '''
   Written by Billy Duggleby and Brendon Lugo
for IT209 at George Mason University, Spring 2019.
Ascii art wizard created by Morfina at www.asciiart.eu
Ascii art knight created by fsc at http://ascii.co.uk
Ascii art archer created by Erorppn Xrzavgm at http://ascii.co.uk
Ascii art dragon created by Joan at asciiart.website//joan/www.geocities.com
'''


choose = '''
      * ***      *                                                                                                          
    *  ****  * **                                                                                                           
   *  *  ****  **                                                                                                           
  *  **   **   **                                                                                                           
 *  ***        **           ****       ****       ****                 **   ****         ****    **   ****     ***  ****    
**   **        **  ***     * ***  *   * ***  *   * **** *    ***        **    ***  *    * ***  *  **    ***  *  **** **** * 
**   **        ** * ***   *   ****   *   ****   **  ****    * ***       **     ****    *   ****   **     ****    **   ****  
**   **        ***   *** **    **   **    **   ****        *   ***      **      **    **    **    **      **     **         
**   **        **     ** **    **   **    **     ***      **    ***     **      **    **    **    **      **     **         
**   **        **     ** **    **   **    **       ***    ********      **      **    **    **    **      **     **         
 **  **        **     ** **    **   **    **         ***  *******       **      **    **    **    **      **     **         
  ** *      *  **     ** **    **   **    **    ****  **  **            **      **    **    **    **      **     **         
   ***     *   **     **  ******     ******    * **** *   ****    *      *********     ******      ******* **    ***        
    *******    **     **   ****       ****        ****     *******         **** ***     ****        *****   **    ***       
      ***       **    **                                    *****                ***                                        
                      *                                                   *****   ***                                       
                     *                                                  ********  **                                        
                    *                                                  *      ****                                          
                   *                                                                                                        
                                                                                                                            
                                                                                                                            
                   ***                           *                                                                                          
                 ** ***    *                   **            *                                                                              
                **   ***  ***                  **           **                                                                              
                **         *                   **           **                                                                              
                **                             **         ********           ***  ****                                                      
                ******   ***         ****      **  ***   ********     ***     **** **** *                                                   
                *****     ***       *  ***  *  ** * ***     **       * ***     **   ****                                                    
                **         **      *    ****   ***   ***    **      *   ***    **                                                           
                **         **     **     **    **     **    **     **    ***   **                                                           
                **         **     **     **    **     **    **     ********    **                                                           
                **         **     **     **    **     **    **     *******     **                                                           
                **         **     **     **    **     **    **     **          **                                                           
                **         **     **     **    **     **    **     ****    *   ***                                                          
                **         *** *   ********    **     **     **     *******     ***                                                         
                 **         ***      *** ***    **    **             *****                                                                  
                                          ***         *                                                                                     
                                     ****   ***       *                                                                                      
                                    *******  **       *                                                                                       
      	                           *     ****        * 
'''

title = '''
                                                                                                                             
     ***** *    **   ***              ***                                                                                    
  ******  *  *****    ***              ***                                                                                   
 **   *  *     *****   ***              **                                                                                   
*    *  **     * **      **             **                                                                                   
    *  ***     *         **             **                  ****                                                             
   **   **     *         **    ***      **       ****      * ***  * *** **** ****       ***                                  
   **   **     *         **   * ***     **      * ***  *  *   ****   *** **** ***  *   * ***                                 
   **   **     *         **  *   ***    **     *   ****  **    **     **  **** ****   *   ***                                
   **   **     *         ** **    ***   **    **         **    **     **   **   **   **    ***                               
   **   **     *         ** ********    **    **         **    **     **   **   **   ********                                
    **  **     *         ** *******     **    **         **    **     **   **   **   *******                                 
     ** *      *         *  **          **    **         **    **     **   **   **   **                                      
      ***      ***      *   ****    *   **    ***     *   ******      **   **   **   ****    *                               
       ******** ********     *******    *** *  *******     ****       ***  ***  ***   *******                                
         ****     ****        *****      ***    *****                  ***  ***  ***   *****                               
                                                                                             *                            
                                                                                             *                           
                                                                                            *                           
                                                                                                                          
                                                                                                                             
                                                                                                                             
        **             **                                                                                                    
     *****              **                                           *                                                       
    *  ***              **   **                                     **                                                       
       ***              **   **                                     **                                                       
      *  **             **    **    ***                           ******** **   ****     ***  ****              ***  ****    
      *  **         *** **     **    ***     ***    ***  ****    ********   **    ***  *  **** **** *    ***     **** **** * 
     *    **       *********   **     ***   * ***    **** **** *    **      **     ****    **   ****    * ***     **   ****  
     *    **      **   ****    **      **  *   ***    **   ****     **      **      **     **          *   ***    **         
    *      **     **    **     **      ** **    ***   **    **      **      **      **     **         **    ***   **         
    *********     **    **     **      ** ********    **    **      **      **      **     **         ********    **         
   *        **    **    **     **      ** *******     **    **      **      **      **     **         *******     **         
   *        **    **    **     **      *  **          **    **      **      **      **     **         **          **         
  *****      **   **    **      *******   ****    *   **    **      **       ******* **    ***        ****    *   ***        
 *   ****    ** *  *****         *****     *******    ***   ***      **       *****   **    ***        *******     ***       
*     **      **    ***                     *****      ***   ***                                        *****                
*                                                                                                                            
 **
'''

knightImg = '''
                          ,dM
                         dMMP
                        dMMM'
                        \\MM/
                        dMMm.
                       dMMP'_\\---.
                      _| _  p ;88;`.
                    ,db; p >  ;8P|  `.
                   (``T8b,__,'dP |   |
                   |   `Y8b..dP  ;_  |
                   |    |`T88P_ /  `\;
                   :_.-~|d8P'`Y/    /
                    \\_   TP    ;   7`\\
         ,,__        >   `._  /'  /   `\\_
         `._ """"~~~~------|`\\;' ;     ,'
            """~~~-----~~~'\\__[|;' _.-'  `\\
                    ;--..._     .-'-._     ;
                   /      /`~~"'   ,'`\\_ ,/
                  ;_    /'        /    ,/
                  | `~-l         ;    /
                  `\\    ;       /\\.._|
                    \\    \\      \\     \\
                    /`---';      `----'
                   (     / 
                    `---'
'''

wizardImg ='''
                    / \\
                  .'* */
               __/_*_*(_
              / _______ \\
             _\\_)/___\\(_/_ 
            / _((\\0-0/))_ \\
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \\
           / _ \ - | - /_  \\
          (   ( .;""";. .)  )
         _\\"__ /(    )\\ __"/_
            \\/  \\'  ' /  \\/
             ( ' '...' ' )
              / /  |  \\ \\
             / .   .   . \\
            /   .     .   \\
           /   /   |   \\   \\
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._ 
 _.-'       |      BBb       '-.  '-. 
(___________\____.dBBBb.________)____)
'''

archerImg = '''
                                                       \\. 
                                                      /|.
                                                   /   |.
                                                 /     |.
                                               /       |.
                                             /         |.
                                          /            |.
        -\\                              /              |.
          \\\                          /                |.
           \\\                       /                  |.
            \\|                    /                    |\\
              \\#####\\           /                      ||
          ==###########>      /                        ||
           \\##==      \\     /                          ||
      ______ =       =|___/__                          ||
  ,--' ,----`-,__ ___/'  --,-`-========================##==========>
 \\               '        ##______ ____ ____,--,_____,=##,__
  `,    __==    ___,-,__,--'#'  ==='   `-'           | ##,-/
    `-,____,---'       \\####\\          |     ____,---\_##,/
        #_              |##   \\  __,--==,__,--'        ##
         #              ]===--==\\                      ||
         #,             ]         \\                    ||
          #_            |           \\                  ||
           ##_       __/'             \\                ||
            ####='     |                \\              |/
             ###       |                  \\            |.
             ##       _'                    \\          |.
            ###=======]                       \\        |.
           ///        |                         \\      |.
           //         |                           \\    |.
                                                    \\  |.
                                                      \\|.
                                                       /.
'''

dragon = '''\
                                                    ___
                                                  .~))>>
                                                 .~)>>
                                               .~))))>>>
                                             .~))>>             ___
                                           .~))>>)))>>      .-~))>>  
                                         .~)))))>>       .-~))>>)>
                                       .~)))>>))))>>  .-~)>>)>
                   )                 .~))>>))))>>  .-~)))))>>)>
                ( )@@*)             //)>))))))  .-~))))>>)>
              ).@(@@               //))>>))) .-~))>>)))))>>)>
            (( @.@).              //))))) .-~)>>)))))>>)>
          ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>
       ((  ((@@@.@@             |/))))) //)))))>>)))>>)>
      )) @@*. )@@ )   (\\_(\\-\\b  |))>)) //)))>>)))))))>>)>
    (( @@@(.@(@ .    _/`-`  ~|b |>))) //)>>)))))))>>)>
     )* @@@ )@*     (@) (@)  /\b|))) //))))))>>))))>>
   (( @. )@( @ .   _/       /  \b)) //))>>)))))>>>_._
    )@@ (@@*)@@.  (6,   6) / ^  \b)//))))))>>)))>>   ~~-.
 ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \b/)>>))))>>      _.     `,
  ((@@ @@@*.(@@ .   \^^^/' (  ^   \b)))>>        .'         `,
   ((@@).*@@ )@ )    `-'   ((   ^  ~)_          /             `,
     (@@. (@@ ).           (((   ^    `\\        |               `.
       (*.@*              / ((((        \\        \      .         `.
                         /   (((((  \\    \\    _.-~\     Y,          \\
                        /   / (((((( \\    \\.-~   _.`" _.-~`,        ;
                       /   /   `(((((()    )    (((((~      `,      ;
                     _/  _/      `"""/   /'                  ;     ;
                 _.-~_.-~           /  /'                _.-~   _.'
               ((((~~              / /'              _.-~ __.--~
                                  ((((          __.-~ _.-~
                                              <.~~~.~'
'''



            


control = controller(0,0,title,choose,0)
Player = control.PlayerClass()
control.startWorld()

#Comment turn counter increase dark clouds recycle strs with while loop
