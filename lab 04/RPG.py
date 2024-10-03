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
        self._ownership = character #setter


    def pick_up(self, character=""):
        self._ownership = character
        print (f"{self.name} has been picked up by {self.ownership}.")

    def throw_away(self):
        self._ownership = "" #ownership is set to empty string.
        print(f"{self.name} has been thrown away.")

    def use(self):
        if self.ownership == "":
            print(f"Error, {self.name} has not been owned.")
        else:
            print(f"{self.name} has been used.")
    
class Weapon(Item):
    def __init__(self, name, description="", rarity="", type="", damage=0):
        super().__init__(name, description, rarity)
        self.rarity = rarity
        self.damage = damage

        if self.rarity == "uncommon":
            self._attack_modifier = 1.0
        elif self.rarity =="common": 
            self._attack_modifier = 1.0
        elif self.rarity == "epic":
            self._attack_modifier = 1.0
        elif self.rarity == "legendary":
            self._attack_modifier = 1.15
        else:
            return "Invalid weapon rarity."
         
    
    def equip(self,verbose=True):
            #check if weapon has been equipped for any further use
            #no ownership means it has not been equipped by any character
        if self.ownership == "":
            if verbose:
                print(f"{self.name} has not been owned.")
            return False
        else:
            if verbose:
                print(f"{self.name} has been equipped.")
            return True

    def use(self):
        if not self.equip(verbose=False):
            print(f"{self.name} is unable to be used for attack.") #if weapon has not been equipped or owned, it cannot be used for attack
        else:
            self.attack_power = self.damage * self._attack_modifier #attack power is calculated based on damage and attack modifier
            print(f"{self.name} has been used to attack with {self.attack_power} damage.")
            super().use() #calls the use method from the parent class
    
class Shield(Item):
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
            return "Invalid weapon rarity."  
    
    def equip(self, verbose=True):
            #check if shield has been equipped for any further use
            #no ownership means it has not been equipped by any character
        if self.ownership == "":
            if verbose:
                print(f"{self.name} has not been owned.")
            return False
        else:
            if verbose:
                print(f"{self.name} has been equipped.")
            return True

    def use(self):
        if not self.equip(verbose=False):
            print(f"{self.name} is unable to be used for defense.") #if shield has not been equipped or owned, it cannot be used for defense
        else:
            self.defense_power = self.defense * self._defense_modifier #defense power is calculated based on damage and attack modifier
            print(f"{self.name} has been used to defense with {self.defense_power} damage.")
            super().use() #calls the use method from the parent class
    
    def throw_away(self):
        if not self.equip(verbose=False):
            print(f"{self.name} is unable to be thrown away.")
        else:
            super().throw_away() #calls the throw_away method from the parent class

class Clothes(Item):
    def __init__(self, name, description, rarity):
        super().__init__(name, description, rarity)

        
    def equip(self, verbose=True):
            #check if clothes has been equipped for any further use
            #no ownership means it has not been equipped by any character
        if self.ownership == "":
            if verbose:
                print(f"{self.name} has not been owned.")
            return False
        else:
            if verbose:
                print(f"{self.name} has been equipped.")
            return True

    def use(self):
        if self.equip() == False:
            print(f"{self.name} is unable to be used.") #if weapon has not been equipped or owned, it cannot be used for attack
        else:
            super().use() #calls the use method from the parent class

class Potion(Item):
    def __init__(self, name, owner="", description="", rarity="common", type = "NaN"):
        super().__init__(name, description, rarity)
        self.type = type
        self.value = 50
        self.time = 30
        self._ownership = owner
    
    def use(self):
        if self.ownership == "":
            print(f"Error, {self.name} has not been owned.")    #if potion has not been owned, it cannot be used
        else:
            if self.type == "attack":
                print(f"{self.name} has been used to increase {self.value} attack for {self.time}.")
                self._ownership = ""    #after successful use, ownership is set to empty string
            elif self.type == "defense":
                print(f"{self.name} has been used to increase {self.value} defense for {self.time}.")
                self._ownership = ""
            elif self.type == "HP":
                print(f"{self.name} has been used to increase {self.value} HP for {self.time}.")
                self._ownership = ""
            else:
                print(f"Error, {self.name} is not defined for any type of potion.")


#testing

belthronding = Weapon(name='Belthronding', rarity='legendary', damage= 5000, type = 'bow')
belthronding.pick_up('Beleg') # Belthronding is now owned by Beleg
belthronding.equip() # Belthronding is equipped by Beleg
belthronding.equip() # Belthronding is equipped by Beleg
belthronding.use() # Belthronding is used, dealing 5750 damage

broken_pot_lid = Shield(name='wooden lid', description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield', defense = 5, broken = True, rarity="common")

#rarity should be specified as common, epic, legendary, or uncommon, but the test doesn't check for this, I add the functionality in the code

broken_pot_lid.pick_up('Beleg') # wooden lid is now owned by Beleg
broken_pot_lid.equip() # wooden lid is equiped by Beleg
broken_pot_lid.use() # wooden lid is used, blocking 2.5 damage
broken_pot_lid.throw_away() # wooden lid is thrown away
broken_pot_lid.use() # NO OUTPUT


attack_potion = Potion(name='atk potion temp', owner ='Beleg', type='attack')
attack_potion.use() # Beleg used atk potion temp, and attack increase 50 for 30s
attack_potion.use() # NO OUTPUT

print(isinstance(belthronding, Item)) # True
print(isinstance(broken_pot_lid, Shield)) # True
print(isinstance(attack_potion, Weapon)) # False