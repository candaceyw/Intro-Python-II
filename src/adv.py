import textwrap
from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Candace", room['outside'])

# Write a loop that:
#

while True:
    # * Prints the current room name
    print(f'{player1.name} you are currently in {player1.location}')


# * Prints the current description (the textwrap module might be useful here).
    for line in textwrap.wrap(player1.location.print_description()):
        print('\n', line)


    command = input("What do you want to do?")
    if command == "n":
        if player1.location.n_to == None:
            print("Wrong way! Turn back and try again")
        else:
            player1.location = player1.location.n_to
            print("Nice, you went North!")

    elif command == "s":
        if player1.location.s_to == None:
            print("Wrong way! Turn back and try again")
        else:
            player1.location = player1.location.s_to
            print("Nice, you went South!")

    elif command == "e":
        if player1.location.e_to == None:
            print("Wrong way! Turn back and try again")
        else:
            player1.location = player1.location.e_to
            print("Nice, you went East!")

    elif command == "w":
        if player1.location.w_to == None:
            print("Wrong way! Turn back and try again")
        else:
            player1.location= player1.location.w_to
            print("Nice, you went West!")

    elif command == "q":
        print("You have exited the game")
        quit()



