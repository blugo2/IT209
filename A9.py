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
        print("put ascit drawing here")

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
            print("You do not have enough Magic!")

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
    def __init__(self,Hp, Att, ID, Moves):
        super().__init__(Hp, Att)
        self.ID = int(ID)
        Moves= ["Fire Breath","Dragons Claw","Tail Whip","Glazing Stare"]
        
    def __str__(self):
        print("put drawing in here")

class Wolf(Mob):
    def __init__(self, Hp, Att, Def, ID, Moves):
        super().__init__(Hp, Att)
        self.ID = int(ID)
        Moves= ["Howel","Chomp","Claw","Tail Whip"]
        
    def __str__(self):
        print("put drawing in here")

class Zombie(Mob):
    def __init__(self, Hp, Att, Def, ID, Moves):
        super().__init__(Hp, Att)
        self.ID = int(ID)
        Moves= ["Bite","Claw","Screech","Decaying Burst"]
        
    def __str__(self):
        print("put drawing in here")


class Boss(Mob):
    def __init__(self, Hp, Att, Def, ID, Moves):
        super().__init__(Hp, Att)
        self.ID = int(ID)
        Moves= ["Python Mastery","Lazer Eyes","Fire Breath","One Inch Punch"]
        
    def __str__(self):
        print("put drawing in here")
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
You find yourself in and area that you recognize as''',Event)
        elif choice == "M":
            Event = random.choice(self.Mountian_Area)
            print('''
You find yourself in and area that you recognize as''',Event)
        elif choice == "D":
            Event = random.choice(self.Sand_Area)
            print('''
You find yourself in and area that you recognize as''',Event)
            

        
#---------BIOME CLASS ABOVE, ITEMS CLASS BELOW------------------------
class Items():
    def __init__(self,knightems,archItems,mageItems):
            self.knightems = knightems
            self.archItems = archItems
            self.mageItems = mageItems

    def getItems(self,player):
        if player.c_type == "k":
            print("You find one:",random.choice(list(self.knightems)),"!")
        elif player.c_type == "m":
            print("You find one:",random.choice(list(self.mageItems)),"!")
        elif player.c_type == "a":
            print("You find one:",random.choice(list(self.archItems)),"!")
            
gameItems= Items({"Dagger":1,"Broadsword":2,"Greataxe":2,"Rubber Chicken":3,'Apple':1,"Turkey leg":2,"Chipotle":3},
                 {"Yew longbow":2,"Nerf bow":1,"Magic bow":3,"Crossbow":2,'Apple':1,"Turkey leg":2,"Chipotle":3},
                 {"Choatic staff":3,"Spellbook":2,"Useless stick":1,"Magic wand":2,'Apple':1,"Turkey leg":2,"Chipotle":3})
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

turnCount = 1

print(title)
time.sleep(5)
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
    Player = Knight(name,2,3,4,5,2,'k')
elif classType.lower() == "archer":
    Player = Archer(name,2,3,4,5,2,'a')
elif classType == "mage":
    Player = Mage(name,2,3,4,5,2,'m')

GameWorld = Biome(['Red Wood National Park','The Spooky Woods','Hidden Grove',"The Witch's Hut"],
                  ['Mount Denali National Park','The Snowy Peaks','The Raging River','The Abandoned Cabin'],
                  ['The Grand Canyon','The Oasis',"Mars' Dunes",'The Hidden Cave'],'G')
clear()
print("Welcome, ",Char.name,"...")
print('''
Before you, you see mountains made of a dark black rock. They look dangerous,
but the reward has to be worth it... right?
To the left you notice an large forest. Probably some cute squirrels or something
To your right you see a desert in the distance. Looks dry. I bet there's a nice
tanning spot down this way.
''')
choice = input(
'''-- Mountains
-- Forest
-- Desert
Would you like to go to the mountains, forest, or desert?(F,M,D): ''')
while choice.upper() not in("F","M","D"):                                           #Validation for which area
    print("Please pick a valid choice:")
    choice = input(
'''-- Mountains
-- Forest
-- Desert
Would you like to go to the mountains, forest, or desert?(F,M,D): ''')
if choice.upper() == "F":                                                         #Valor text about which area to choose
    print("""
    With the wind in your hair and bugs chittering around you, you head towards the 
    large forest. You have spent some time travelling along the well worn dirt path
    beneath your feat when your senses spot something. That cute squireel perhaps?
    You stop and gather in your surroundings...""")
    
elif choice.upper() == "M":
    print("""
    You decide to head towards the mountain made of dark rock. As you get closer you
    spot a winding trail that grips to the mountains edge. By the time you have made it
    to the begining of the trail, the air is cold and stale. Something about this
    mountain makes your skin crawl. You decied to stop, catch your breath, and take
    in your surroundings...
    """)
elif choice.upper() == "D":
    print("""
    You trod down the slopes towards the desert. With the sand blowing past your
    face and the sun beating down your neck you feel confident in your choice.
    As you walk, you begin to notice high dunes besides you and you wonder how
    long they have stood. In the distance you hear a sharp jackle and your hair
    stands on edge. Perhaps someone, or something, is also wandering among the
    dunes. You stand at ease and being to take in your surroundings...

    """)
GameWorld.PickArea(choice)
GameWorld.PickAreaEvent(choice)
#itemPickup = input
fobjects = ["a hollowed out log","a patch of mushrooms","some brush","some small bush","a thorn patch","tall grass"]
dobjects = ["a tumble weed","a colorful cactus","a spikey cactus","a small dune","a patch of dead grass","an antelope skull","a large boulder"]
mobjects = ["a jagged rock","a smooth stone","a puddle","crevace","a patch of weeds","a mound of gravel","a mossy stone"]
entry = input("\nTo your left you see  "+random.choice(fobjects)+
              ". To your right you see "+random.choice(fobjects)+". Which do you search?: ")
print("\n")
itemPickup = random.randint(1,10)
if itemPickup%2 == 0:
    gameItems.getItems(Player)
else:
    print("Oof, bad luck... You didn't find anything.")

#-----GLOBAL CODE BELOW----------------------------------------
#player = Mage('billy',2,3,4,5,2,'m')
#gameItems.getItems(player)
        

#Comment turn counter increase dark clouds recycle strs with while loop

