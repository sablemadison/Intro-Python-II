from room import Room
from item import Item
from player import Player #imports should happen first;moving up fixed 'inventory arguments' error

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Populate empty rooms

def populate_rooms():
    room['narrow'].add_item(Item("dagger", """Sharp and ready to use; remember to handle carefully!"""))
    room['treasure'].add_item(Item("hammer", """This tool could come in handy"""))
    room['overlook'].add_item(Item("rope", """Exercise, climbing, hunting; be ready for anything with a handy rope"""))
    room['outside'].add_item(Item("4-leaf clover", """Not very useful but pretty to look at!"""))
    room['foyer'].add_item(Item("map", """No GPS? No problem."""))
populate_rooms()

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# player1 = Player('Jack', room['outside'])
# validSession = True

# print(f'Welcome {player.name} \n')
# while validSession == True:
        
#     print(f'You are {player.current_room} \n', room['outside'].description)
#     choice = input(f'Adventure awaits. Which direction would you like to travel in first? \n Enter N, E, S or W or enter Q to quit')
    
#     if choice == 'Q':
#         print(f'Goodbye! See you next time.')
#         break
               














player1 = Player('Bobert', room['outside'].name) 

validGame = True
directions = ['n', 's', 'e', 'w']
actions = ['get', 'drop', 'g', 't']

print(f'Welcome {player1.name} \n')


while validGame:
    print(f'You are {player1.current_room} \n', room['outside'].description)
    choice = input(f'Please choose a direction of travel: n, s, e, or w. Or enter q to quit game.')

    if choice == 'q' or choice  == 'quit':
        print(f'Goodbye! See you next time.')
        break
    elif choice in directions:
        player1.move(choice)
        print(f"""You were in {room['outside']}
        You went {choice}. Now you're in {player1.current_room}""")
        print(f'You can explore the room you are in, c, or choose another direction to travel to')
        if choice in directions:
            player1.move(choice)
            print(f'You went {choice}. Now you are in {player1.current_room}')
            if choice == 'c':
                player1.current_room.check_room()
                item = player1.current_room.items
                print(f'You find {item}. You can use g to get the item and d to drop it again ')
                if choice == 'g':
                    item = player1.current_room.items
                    player1.get(item)
                    print(player1.inventory)
                    print(f'You got {item}')
                    if choice == 'd':
                        item = player1.current_room.items
                        player1.drop(item)
                        print(f'You dropped {item}')
    else: 
        print(f'Invalid command. Please try again.')
    
    print(f'Your journey ends here, traveler')

    choice = input('Choose a new direction: n, s, e, or w. Or enter q to quit.')
 

    

    






