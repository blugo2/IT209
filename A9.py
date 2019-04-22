#-------------------------------------------------------------------------+
#Program name: IT209_A9.py                                                |
#Author: Brendon Lugo and William Dugbly                                  |
#Date Written: 4/17/19                                                    |
#Purpose: Assignment 9                                                    |  
#-------------------------------------------------------------------------+
print("Welcome to the start of Assignment 9...")
import random
class Char():
    def __init__(Name, Hp, Att, Def, Sp):   #Added Sp for Speical Move funcationality
        self.Name= str(Name)
        self.Hp= int(Hp)
        self.Att= int(Att)
        self.Def= int(Def)
        Self.Sp = int(Sp)
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
    def __init__(Name, Hp, Att, Def, Mag, Sp)
        super().__init__(Name, Hp, Att, Def, Sp):
        self.Mag = Mag

    def __str__(self):
        print("put drawing in here")

    def Ability():
        Name = "FireBall"
        Move = self.Sp + 3
        Move_Cost = 1
        Type = "Att"
        self.Use_Ability(Move, Move_Cost, Name, Type)

class Knight(Char):
    def __init__(Name, Hp, Att, Def, Mag, Sp)
        super().__init__(Name, Hp, Att, Def, Sp):
        self.Mag = Mag

    def __str__(self):
        print("put drawing in here")

    def Ability():
        Name = "Heal"
        Move = self.Sp + 2
        Move_Cost = 1
        Type = "Hp"
        self.Use_Ability(Move, Move_Cost, Name, Type)

class Archer(Char):
    def __init__(Name, Hp, Att, Def, Mag, Sp)
        super().__init__(Name, Hp, Att, Def, Sp):
        self.Mag = Mag

    def __str__(self):
        print("put drawing in here")

      def Ability():
        Name = "Rain Arrows"
        Move = self.Sp + 2
        Move_Cost = 1
        Type = "Att"
        self.Use_Ability(Move, Move_Cost, Name, Type)
#---------------Character Class Above, Enemy Below -----------------------------------
class Mob():
    def __init__(Hp, Att):   #Added Sp for Speical Move funcationality
        self.Hp= int(Hp)              #Removed Name, mobs dont have uquie names
        self.Att= int(Att)
            
class Dragon(Mob):
    def __init__(Hp, Att, ID, Moves)  
        super().__init__(Hp, Att):
        self.ID = int(ID)
        Moves= ["Fire Breath","Dragons Claw","Tail Whip","Glazing Stare"]
        
    def __str__(self):
        print("put drawing in here")

class Wolf(Mob):
    def __init__(Hp, Att, Def, ID, Moves)  
        super().__init__(Hp, Att):
        self.ID = int(ID)
        Moves= ["Howel","Chomp","Claw","Tail Whip"]
        
    def __str__(self):
        print("put drawing in here")

class Zombie(Mob):
    def __init__(Hp, Att, Def, ID, Moves)  
        super().__init__(Hp, Att):
        self.ID = int(ID)
        Moves= ["Bite","Claw","Screech","Decaying Burst"]
        
    def __str__(self):
        print("put drawing in here")


class Boss(Mob):
    def __init__(Hp, Att, Def, ID, Moves)  
        super().__init__(Hp, Att):
        self.ID = int(ID)
        Moves= ["Python Mastery","Lazer Eyes","Fire Breath","One Inch Punch"]
        
    def __str__(self):
        print("put drawing in here")
#-------------------Enemies Above, Biome Below--------------------
class Biome():
    def __init__(Forest_Area, Mountian_Area, Deseart_Area, choice):
        self.Forest_Area = ['Red Wood National Park','Spooky Woods','Hidden Grove','Forest Hut']
        self.Mountian_Area = ['Mount Denali National Park','Snowy Peaks','Raging River','Log Cabin']
        self.Deseart_Area = ['Grand Cayone','Ososis','Dunes','Hidden Cave']
        self.choice = None
        
    def PickArea(Area):
        if Area == "F":
            self.choice = "F"

        elif Area == "M":
            self.choice = "M"
            
        elif Area == "D":
            self.choice = "D"

    def PickAreaEvent():
        if choice = "F":
            Event = random.choice(self.Forest_Area)
        elif choice = "M":
            Event = random.choice(self.Mountian_Area)
        elif choice = "D":
            Event = random.choice(self.Deseart_Area)
        
#Comment turn counter increase dark clouds recycle strs with while loop



        
