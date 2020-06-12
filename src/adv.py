import textwrap
from room import Room
from player import Player
from item import Item

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

# Items
flashlight = Item('flashlight', 'a bright shiny thing to help you see')
sword = Item('sword', 'a sharp stabby thing')
apple = Item('apple', 'one a day keeps the doctor away')
paper = Item('paper', 'useless garbage, should probably leave it')
gold = Item('gold', 'arg matey, I found the treasure!')

room['outside'].add_item(flashlight)
room['foyer'].add_item(sword)
room['overlook'].add_item(apple)
room['narrow'].add_item(paper)
room['treasure'].add_item(gold)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Candace", room['outside'])
player1.location.print_description()
# Write a loop that:
#

while True:
    # * Prints the current room name
    print(f'{player1.name} you are currently in {player1.location}')
    print('\nItems in inventory ', player1.items, '\n')

# * Prints the current description (the textwrap module might be useful here).
    for line in textwrap.wrap(player1.location.print_description()):
        print('\n', line)

        command = input(
            "What do you want to do? To pick up items use 'p0', 'p1', etc...  To drop items use 'd0', 'd1', "
            "etc...('q' or 'quit' to quit) ")

        if command in ['n', 's', 'e', 'w']:
            player1.location = player1.move_to(command, player1.location)
            continue

        elif command[0] == 'p':
            item = int(command[1:])
            if 0 <= item < len(player1.location.items):
                print('\n', player1.name, ' picks up ', player1.location.items[item])
                player1.add_item(player1.location.items[item])
                player1.location.remove_item(item)
            else:
                print('that item does not exist')

        elif command[0] == 'd':
            item = int(command[1:])
            if 0 <= item < len(player1.items):
                print('\n', player1.name, ' drops ', player1.items[item])
                player1.location.add_item(player1.items[item])
                player1.remove_item(item)
            else:
                print('that item does not exist')

        elif command == 'q' or command == 'quit':
            done = True

        else:
            print(
                'Wrong way! Turn back and try again \n')

    # command = input("What do you want to do?").split(' ')
    # if command[0] == "n":
    #     if player1.location.n_to is None:
    #         print("Wrong way! Turn back and try again")
    #         player1.location.print_items()
    #     else:
    #         player1.location = player1.location.n_to
    #         print("Nice, you went North!")
    #         continue
    # elif command[0] == 'p':
    #     item = int(command[1:])
    #     if item >= 0 and item < len(player1.location.items):
    #         print('\n', player1.name, ' picks up ', player1.location.items[item])
    #         player1.add_item(player1.location.items[item])
    #         player1.location.remove_item(item)
    #     else:
    #         print('that item does not exist')
    #
    # elif command[0] == "s":
    #     if player1.location.s_to is None:
    #         print("Wrong way! Turn back and try again")
    #     else:
    #         player1.location = player1.location.s_to
    #         print("Nice, you went South!")
    #
    # elif command[0] == "e":
    #     if player1.location.e_to is None:
    #         print("Wrong way! Turn back and try again")
    #     else:
    #         player1.location = player1.location.e_to
    #         print("Nice, you went East!")
    #
    # elif command[0] == "w":
    #     if player1.location.w_to is None:
    #         print("Wrong way! Turn back and try again")
    #     else:
    #         player1.location = player1.location.w_to
    #         print("Nice, you went West!")
    #
    # elif command[0] == "q":
    #     print("You have exited the game")
    #     quit()
    #
    #
    #
