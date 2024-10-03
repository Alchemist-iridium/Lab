class Item:
    def __init__(self, name, description="", rarity="common"): #common set as default for rarity
        self.name = name
        self.description = "" #empty string set as default
        self.rarity =  rarity
        self._ownership = "" #empty string set as default, this is a private attribute
    
    @property
    def ownership(self):
        return self._ownership #getter
    
    @ownership.setter
    def ownership(self, character):
        self._ownership = character.name #setter


    def pick_up(self, character):
        self._ownership = character.name

    def throw_away(self):
        self._ownership = "" #ownership is set to empty string.

    def use(self):
        print(f"{self.name} has been used.")
    
class Weapon(Item):
    def __init__(self, name, description, rarity, type):
        super().__init__(name, description, rarity)
        self.type = type
         
    
    def equip(self):
            #check if clothes has been equipped for any further use
            #no ownership means it has not been equipped by any character
        if self.ownership == "":
            print(f"{self.name} has not been owned.")
            return False
        else:
            print(f"{self.name} has been equipped.")
            return True

    def use(self):
        if self.equip() == False:
            print(f"{self.name} is unable to be used for attack.") #if weapon has not been equipped or owned, it cannot be used for attack
        else:
            self.attack_power = self.damage * self._attack_modifier #attack power is calculated based on damage and attack modifier
            print(f"{self.name} has been used to attack with {self.attack_power} damage.")
            super().use() #calls the use method from the parent class
    
class Sheid(Item):
    def __init__(self, name, description, rarity, defense,broken = False):  #broken set as not broken, default for shield
        super().__init__(name, description, rarity)
        self.defense = defense
        self.broken = broken
        
        #attack modifier based on shield broken status and rarity

        if self.broken == True:
            self._defense_modifier = 0.5    #first check if shield is broken, if it is, defense modifier is set to 0.5
        elif self.rarity == "uncommon":
            self._defense_modifier = 1.0
        elif self.rarity =="common": 
            self._defense_modifier = 1.0
        elif self.rarity == "epic":
            self._defense_modifier = 1.0
        elif self.rarity == "legendary":
            self._defense_modifier = 1.10            
        else:
            return "Invalid weapon type."  
    
    def equip(self):
            #check if shield has been equipped for any further use
            #no ownership means it has not been equipped by any character
        if self.ownership == "":
            print(f"{self.name} has not been owned.")
            return False
        else:
            print(f"{self.name} has been equipped.")
            return True

    def use(self):
        if self.equip() == False:
            print(f"{self.name} is unable to be used for defense.") #if shield has not been equipped or owned, it cannot be used for defense
        else:
            self.defense_power = self.defense * self._defense_modifier #defense power is calculated based on damage and attack modifier
            print(f"{self.name} has been used to defense with {self.defense_power} damage.")
            super().use() #calls the use method from the parent class

class Clothes(Item):
    def __init__(self, name, description, rarity):
        super().__init__(name, description, rarity)

        
    def equip(self):
            #check if weapon has been equipped for any further use
            #no ownership means it has not been equipped by any character
        if self.ownership == "":
            print(f"{self.name} has not been owned.")
            return False
        else:
            print(f"{self.name} has been equipped.")
            return True

    def use(self):
        if self.equip() == False:
            print(f"{self.name} is unable to be used.") #if weapon has not been equipped or owned, it cannot be used for attack
        else:
            super().use() #calls the use method from the parent class
    



        
