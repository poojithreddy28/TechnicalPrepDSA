# Problem 1: New Horizons
# Step 1: Copy the following code into your IDE.

# Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

# The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []
#         self.items = []
#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
#     def set_catchphrase(self, new_catchphrase):
#         if len(new_catchphrase) < 20 and all(char.isalpha() or char.isspace() for char in new_catchphrase):
#             print("Catchphrase updated")
#             self.catchphrase = new_catchphrase
#         else:
#             print("Invalid catchphrase")
#     def add_item(self, item_name):
#         self.furniture.append(item_name)

#     def print_inventory(self):
#         if not self.items:
#             print("Inventory empty")
#         else:
#             inventory = {}
#             for i in self.items:
#                 if i in inventory:
#                     inventory[i] += 1
#                 else:
#                     inventory[i] = 1
#             for i in inventory:
#                 print(f"{i}: {inventory[i]}, ", end="")
        
# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)

# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# alice.print_inventory()

# alice.items = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()

# Instantiate your villager here
# Example Usage:
# apollo = Villager("Apollo", "Eagle", "pah")
# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 
# print(apollo.greet_player("Tram"))
# Example Output:

# Apollo
# Eagle
# pah
# []

# Problem 2: Greet Player
# Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

       
# Step 2: Create a second instance of Villager in a variable named bones.

# The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
# Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.

# Example Usage:

# print(bones.name)
# print(bones.species)  
# print(bones.catchphrase) 
# print(bones.furniture) 
# Example Output:

# Bones
# Dog
# yip yip
# []



# Problem 3: Update Catchphrase
# In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

# Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".

# Example Usage:

# print(apollo.greet_player("Samia"))
# Example Output:

# Bones: Hey there, Samia! How's it going, ruff it up!


# Problem 4: Set Character
# In the previous exercise, we accessed and modified a player’s catchphrase attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

# Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

# If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
# Otherwise, it should print out "Invalid catchphrase".
# Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.

# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
# 		self.catchphrase = catchphrase
#         self.furniture = []
	
# 	def set_catchphrase(self, new_catchphrase):
# 		pass
# Example Usage:

# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)
# Example Output:

# Example 1:
# Catchphrase Updated!
# sweet dreams
# Invalid catchphrase
# sweet dreams

# Problem 5: Add Furniture
# Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

# Update the Villager class with a new method add_item() that takes in one parameter, item_name.

# The method should validate the item_name.

# If the item is valid, add item_name to the player’s furniture attribute.
# The method does not need to return any values.
# item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".

# class Villager:
#     # ... methods from previous problems
	
#     # New method
#     def add_item(self, item_name):
#         pass
# Example Usage:

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)
# Example Output:

# []
# ["acoustic guitar"]
# ["acoustic guitar", "cacao tree"]
# ["acoustic guitar", "cacao tree"]



# Problem 6: Print Inventory
# Update the Villager class with a method print_inventory() that accepts no parameters except for self.

# The method should print the name and quantity of each item in a villager’s furniture list.

# The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" for however many unique items exist in the villager's furniture list
# If the player has no items, the function should print "Inventory empty".
# class Villager():
#     # ... methods from previous problems
    
#     def print_inventory(self):
#         # Implement the method here
#         pass
# Example Usage:

# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.items = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()
# Example Output:

# Inventory empty
# acoustic guitar: 1, ironwood kitchenette: 1, kotatsu: 2

# Problem 7: Group by Personality
# The Villager class has been updated below to include the new string attribute personality representing the character's personality type.

# Outside of the Villager class, write a function of_personality_type(). Given a list of Villager instances townies and a string personality_type as parameters, return a list containing the names of all villagers in townies with personality personality_type. Return the names in any order.

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.items = []
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(char.isalpha() or char.isspace() for char in new_catchphrase):
            print("Catchphrase updated")
            self.catchphrase = new_catchphrase
        else:
            print("Invalid catchphrase")
    def add_item(self, item_name):
        self.furniture.append(item_name)

    def print_inventory(self):
        if not self.items:
            print("Inventory empty")
        else:
            inventory = {}
            for i in self.items:
                if i in inventory:
                    inventory[i] += 1
                else:
                    inventory[i] = 1
            for i in inventory:
                print(f"{i}: {inventory[i]}, ", end="")
    
def of_personality_type(townies, personality_type):
    if personality_type in [i.personality for i in townies]:
        return [i.name for i in townies if i.personality == personality_type]
    else:
        return []    
# Example Usage:

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
# Example Output:

# ["Bob", "Stitches"]
# []


# Problem 8: Telephone
# The Villager constructor has been updated to include an additional attribute neighbor. A villager's neighbor is another Villager instance and represents their closest neighbor. By default, a Villager's neighbor is set to None.

# Given two Villager instances start_villager and target_villager, write a function message_received() that returns True if you can pass a message from the start_villager to the target_villager through a series of neighbors and False otherwise.

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    # ... methods from previous problems

    
def message_received(start_villager, target_villager):
    if start_villager.neighbor == None:
        return False
    else:
        print(start_villager.name)
        start_villager = start_villager.neighbor
        print(start_villager.name)
        if start_villager == target_villager:
            return True
        else:
            return message_received(start_villager, target_villager)
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))
print(message_received(tom_nook, isabelle))
# Example Output:

# True
# Example 1 Explanation: Isabelle can pass a message to her neighbor, Tom Nook. Tom Nook can then pass the 
# message to his neighbor, KK Slider. KK Slider is the target, therefore the function should return True.


# False
# Example 2 Explanation: KK Slider doesn't have a neighbor, so you cannot pass a message to Isabelle from KK Slider.
