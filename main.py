
# Warrior Castle Adventure
# A text-based adventure game built with Python

def show_instructions():
    print("=" * 50)
    print("       WARRIOR CASTLE ADVENTURE")
    print("=" * 50)
    print("Welcome, brave warrior!")
    print()
    print("An evil wizard has taken control of the castle.")
    print("Your mission is to explore the castle,")
    print("collect all six magical items, and defeat him!")
    print()
    print("Commands:")
    print("  go North, go South, go East, go West")
    print("  get Item Name")
    print("  exit")
    print("=" * 50)


show_instructions()


# Castle rooms and their connections
rooms = {
    "Gate House": {
        "North": "Royal Hall",
        "East": "Training Arena"
    },
    "Royal Hall": {
        "South": "Gate House",
        "East": "Library",
        "West": "Armory",
        "North": "Wizard Sanctum"
    },
    "Training Arena": {
        "West": "Gate House",
        "North": "Alchemy Lab"
    },
    "Armory": {
        "East": "Royal Hall",
        "South": "Dungeon"
    },
    "Library": {
        "West": "Royal Hall"
    },
    "Alchemy Lab": {
        "South": "Training Arena"
    },
    "Dungeon": {
        "North": "Armory"
    },
    "Wizard Sanctum": {
        "South": "Royal Hall"
    }
}


# Magical items hidden throughout the castle
items = {
    "Gate House": "Map",
    "Training Arena": "Shield",
    "Armory": "Sword",
    "Library": "Spell Book",
    "Alchemy Lab": "Strength Potion",
    "Dungeon": "Torch"
}

# Player starting information
current_room = "Gate House"
inventory = []

# Number of items required to defeat the wizard
required_items = 6


# Move the player between castle rooms
def move_player(direction):
    global current_room

    direction = direction.capitalize()

    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        print(f"\nYou entered the {current_room}!")
    else:
        print("\nYou cannot go that direction!")


# Allow the player to collect items
def collect_item(item_name):
    if current_room in items:
        room_item = items[current_room]

        if item_name.lower() == room_item.lower():
            inventory.append(room_item)
            del items[current_room]
            print(f"\nYou collected the {room_item}!")
        else:
            print("\nThat item is not in this room!")
    else:
        print("\nThere are no items to collect here!")


# Main gameplay loop
def play_game():
    global current_room

    while True:
        print("\n" + "=" * 40)
        print(f"Current Room: {current_room}")
        print(f"Inventory ({len(inventory)}/{required_items}): {', '.join(inventory) if inventory else 'Empty'}")

        if current_room in items:
            print(f"You see a {items[current_room]}.")

        print("Available directions:",
              ", ".join(rooms[current_room].keys()))

        # Check whether the player reached the wizard
        if current_room == "Wizard Sanctum":
            if len(inventory) == required_items:
                print("\nYou defeated the evil wizard!")
                print("Congratulations! You saved the castle!")
            else:
                print("\nThe evil wizard has defeated you!")
                print("You needed all six magical items!")
            break

        command = input("\nEnter your command: ").strip()

        if command.lower() == "exit":
            print("\nThanks for playing!")
            break

        elif command.lower() == "help":
            show_instructions()
            
        elif command.lower().startswith("go "):
            direction = command[3:].strip()
            move_player(direction)

        elif command.lower().startswith("get "):
            item_name = command[4:].strip()
            collect_item(item_name)

        else:
            print("\nInvalid command! Try again.")


# Start the adventure
play_game()
