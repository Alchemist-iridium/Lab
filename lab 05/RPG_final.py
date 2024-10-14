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
    def ownership(self, owner):
        self._ownership = owner #setter


    def pick_up(self, owner=""):
        self.ownership = owner
        print (f"{self.name} has been picked up by {self.ownership}.")

    def throw_away(self):
        self.ownership = "" #ownership is set to empty string.
        print(f"{self.name} has been thrown away.")

    def use(self):
        if self.ownership == "":
            print(f"Error, {self.name} has not been owned.")
        else:
            print(f"{self.name} has been used.")
    
    def view(self):
        for item in self:
            if item.rarity == "legendary":
                print(f"{item.name} is a legendary item.")  #if item is legendary, print it
        
    
class Weapon(Item):
    def __init__(self, name, description = "", rarity = "", type = "", damage = float):
        super().__init__(name, description, rarity)
        self.rarity = rarity
        self.damage = damage
        self.type = type

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
        
    #attack movements functions based on weapon type

    def _slash(self):
        print(f"{self.name} has been used to slash.")
        return "slash"
    def _spin(self):
        print(f"{self.name} has been used to spin.")
        return "spin"
    def _stab(self):
        print(f"{self.name} has been used to stab.")
        return "stab"
    def _shoot(self):
        print(f"{self.name} has been used to shoot.")
        return "shoot"


    def use(self):
        if not self.equip(verbose=False):
            print(f"{self.name} is unable to be used for attack.") 
            #if weapon has not been equipped or owned, it cannot be used for attack
        else:

            #first construct the attack movement based on weapon category
            #classify the weapon type based on the category

            category = {
                "sword" : "Single-handed weapon",
                "katana" : "Double-handed weapon",
                "spear" : "Pike",
                "bow" : "Ranged weapon"
            }
            self.category = category[self.type]

            match self.category:
                case "Single-handed weapon":
                    self.attack_movement = self._slash()
                case "Double-handed weapon":
                    self.attack_movement = self._spin()
                case "Pike":
                    self.attack_movement = self._stab()
                case "Ranged weapon":
                    self.attack_movement = self._shoot()
                case _:
                    print("Invalid weapon type.")

            #the attack damage is calculated based on the damage and attack modifier

            self.attack_power = self.damage * self._attack_modifier #attack power is calculated based on damage and attack modifier
            print(f"{self.name} has been used to attack with {self.attack_power} damage.")
            super().use() #calls the use method from the parent class
    
class Shield(Item):
    def __init__(self, name, description = "", rarity = "", defense = float ,broken = False):  #broken set as not broken, default for shield
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
        self.ownership = owner
    
    def use(self):
        if self.ownership == "":
            print(f"Error, {self.name} has not been owned.")    #if potion has not been owned, it cannot be used
        else:
            if self.type == "attack":
                print(f"{self.name} has been used to increase {self.value} attack for {self.time}.")
                self.ownership = ""    #after successful use, ownership is set to empty string
            elif self.type == "defense":
                print(f"{self.name} has been used to increase {self.value} defense for {self.time}.")
                self.ownership = ""
            elif self.type == "HP":
                print(f"{self.name} has been used to increase {self.value} HP for {self.time}.")
                self.ownership = ""
            else:
                print(f"Error, {self.name} is not defined for any type of potion.")


class Inventory():
    def __init__(self, owner = None):
        self.ownership = owner
        self.items = []

    #add item to inventory
    def add_item(self,item):

        self.items.append(item)

        if self.ownership:
            item.ownership = self.ownership

        print(f"{item.name} has been added to the inventory.")

    #view items in inventory

    def view(self, type = None, item = None):
        if type == None:
            for item in self.items:
                print(f"{item.name} is in the inventory.")
        elif item:
            if item in self.items:
                print(f"{item.name} is in the inventory.")
            else:
                print(f"{item.name} is not in the inventory.")
        else:
            for item in self.items:
                if isinstance(item, Weapon) and item.type == type:
                    print(f"{item.name} is a {type} weapon.")
                elif isinstance(item, Shield):
                    print(f"{item.name} is a shield.")
                elif isinstance(item, Clothes):
                    print(f"{item.name} is a clothes.")
                elif isinstance(item, Potion) and item.type == type:
                    print(f"{item.name} is a {type} potion.")

    #drop item from inventory

    def drop_item(self, item):
        self.items.remove(item)

        if self.ownership:
            item.ownership = ""

        print(f"{item.name} has been dropped from the inventory.")
    
    def __iter__(self):
        # Make the Inventory class iterable by returning an iterator over the items list
        return iter(self.items)
    

#test

#single-handed weapon:

master_sword = Weapon(name = "master sword", rarity = "legendary", damage = 300, type = 'sword')

#double-handed weapon:

muramasa = Weapon(name = "muramasa",rarity= "legendary", damage = 580, type = "katana")

#Pike

gungnir = Weapon(name= "gungnir", rarity = "legendary", damage = 290, type = "spear")

#Ranged weapon:

belthronding = Weapon(name = "belthronding", rarity= "legendary", damage= 500, type = "bow")

#shield

round_shield = Shield(name = "round shield", rarity = "legendary", defense = 200)
broken_pot_lid = Shield(name = "broken pot lid", rarity = "common", defense = 100, broken = True)

#potions

hp_potion = Potion(name = "hp potion", type = "HP")

beleg_backpack = Inventory(owner = 'Beleg')


beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(hp_potion)
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.add_item(muramasa)
beleg_backpack.add_item(gungnir)
beleg_backpack.add_item(round_shield)
beleg_backpack.view(type = 'shield')
beleg_backpack.view()
beleg_backpack.drop_item(broken_pot_lid)
if master_sword in beleg_backpack:
    master_sword.equip()
    print(master_sword)
# message to show off your legendary item
    master_sword.use()
# Beleg slash using master sword
# master sword is used dealing 345 damage
for item in beleg_backpack:
    if isinstance(item, Weapon):
        beleg_backpack.view(item = item)
