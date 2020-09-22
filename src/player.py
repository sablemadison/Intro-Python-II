# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        
    
    def __str__(self):
        return f"{self.name} is in {self.current_room}."
    
    def move(self, dir):
        new_room = hasattr(self.current_room, f"{dir}_to")
        if new_room == False:
            self.current_room = new_room
        else:
            self.current_room = self.current_room.dir_to
            print(f'Movement not allowed. Try another direction')
    def get(self, item):
        if item.name == item:
            self.inventory.append(item)
            self.current_room.items.remove(item) #should not exist in room AND inventory
            print(f'You got {item}')
        else: 
            print(f'{item} not found. \n Try searching in a different room.')

    def drop(self, item):
        if item.name == item:
            self.inventory.remove(item)
            self.current_room.items.append(item) 
            print(f'You dropped {item}.')

        else: 
            print(f'{item} not found. Not sure what you are carrying? Try checking your inventory')

    def check_inventory(self):
        if len(self.inventory) == 0:
            print(f'Inventory empty')
        else: 
            print(f'Checking inventory:')
            for item in self.inventory: #missing self.
                print(f'{item.name}: {item.description}')
    
    def select_item(self, item):
        for i in self.current_room.items:
            if i.name.lower() == str(item).lower():
                return i
            else:
                print(f'{item} does not exist')
                return None

   # def check_inventory():
    