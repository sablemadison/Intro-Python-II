# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    def __str__(self):
        return f'{self.name}, {self.description}'

    def add_item(self, item):
        self.items.append(item)
    def check_room(self):
       if self.items == 0:
           print(f'Room empty')
       else:
            print(f'Room contents:')
            for item in self.items:
                print(item)

    
    

        