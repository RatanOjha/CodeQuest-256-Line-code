import random

MAX_STEPS = 20
MINIMUM_FUEL = 10
MONEY_HIGH_SCORE=100

player = {
    "name": "",
    "location": "Space",
    "fuel": 100,
    "steps": 0,
    "inventory": [],
    "role": "",
    "money":0
}

locations = {
    "Space": "You are the captain of the starship 'Odyssey' on a mission to explore the cosmos.",
    "Asteroid Field": "Navigating through this asteroid field is dangerous, but it might yield valuable discoveries.",
    "Space Station": "The space station offers refueling and trading. Make wise decisions to succeed.",
    "Alien Planet": "You land on an alien planet with lush forests and strange creatures. It's a world of mysteries.",
    "Black Hole": "You've encountered a black hole! Its immense gravity is pulling you in.",
    "Ancient Ruins": "You stumble upon the ruins of an ancient civilization. What secrets do they hold?",
    "Space Pirates": "You encounter a band of space pirates! They demand a ransom or a fight.",
    "Deep Space": "You find yourself in the depths of space, far from any celestial objects. An eerie calm surrounds you.",
    "Lost in Nebula": "Your ship is enveloped in a colorful nebula. Visibility is low, and navigation is challenging.",
    "Space Wormhole": "A swirling wormhole opens before you, offering a mysterious shortcut through space and time."
}

items = {
    "Oxygen Tank": "A portable oxygen tank that could be vital in emergencies.",
    "Alien Artifact": "A mysterious alien artifact with unknown powers.",
    "Medikit": "A medical kit to heal injuries and ailments.",
    "Exploration Robot": "A robot companion to assist in exploring unknown terrains.",
    "Quantum Key": "A high-tech key that can unlock advanced alien technologies.",
    "Star Map": "A detailed star map revealing hidden secrets of the cosmos.",
    "Laser Blaster": "A powerful laser blaster for defense against threats.",
    "Translator Device": "A device that can decipher alien languages.",
    "Ancient Scroll": "An ancient scroll with cryptic inscriptions.",
    "Energy Crystal": "A glowing energy crystal that pulses with power.",
    "Time Capsule": "A time capsule containing messages from a bygone era."
}

def check_game_conditions():
    if player["fuel"] <= 0:
        return "You've run out of fuel! Game over."
    elif player["steps"] >= MAX_STEPS:
        return "Congratulations! You've completed your mission by reaching the maximum number of steps with money-->"+str(player["money"])
    return None

def refuel():
    cost = random.randint(10, 30)
    if player["fuel"] >= 100 - cost:
        player["fuel"] = 100
    else:
        player["fuel"] += cost
    return f"You refueled your spaceship at the space station. Current fuel: {player['fuel']}"


def change_location(new_location):
    player["location"] = new_location

locations_options = {
    "Space": {
        "1": "Explore nearby asteroid field",
        "2": "Refuel at space station",
        "3": "Check inventory",
        "4": "Quit"
    },
    
    "Asteroid Field": {
        "1": "Attempt asteroid navigation",
        "2": "Check Fuel",
        "3": "Check inventory",
        "4": "Quit"
    },
    "Space Station": {
        "1": "Refuel your spaceship",
        "2": "Trade with the station",
        "3": "Leave the station",

    },
    "Alien Planet": {
        "1": "Explore the planet's forests",
        "2": "Check Fuel",
        "3": "Check inventory",
        "4": "Quit"
    },
    "Black Hole": {
        "1": "Attempt to escape the black hole's grasp",
        "2": "Check Fuel",
        "3": "Check inventory",
        "4": "Quit"
    },
    "Ancient Ruins": {
        "1": "Investigate the ruins",
        "2": "Check Fuel",
        "3": "Check inventory",
        "4": "Quit"
    },
    "Space Pirates": {
        "1": "Continue diving deep by sniffing away from pirates",
        "2": "Check Fuel",
        "3": "Check inventory",
        "4": "Quit"
    },
    "Deep Space": {
        "1": "Continue drifting through deep space",
        "2": "Check Fuel",
        "3": "Check inventory",
        "4": "Quit"
    },
    "Lost in Nebula": {
        "1": "Navigate carefully through the nebula",
        "2": "Check Fuel",
        "3": "Check inventory",
        "4": "Quit"
    },
    "Space Wormhole": {
        "1": "Avoid the wormhole and continue your current course",
        "2": "Check Fuel",
        "3": "Check inventory",
        "4": "Quit"
    }
}

def change_to_random_location():
    new_location = random.choice(["Space Station","Alien Planet", "Asteroid Field", "Black Hole", "Ancient Ruins", "Space Pirates", "Deep Space", "Lost in Nebula", "Space Wormhole"])
    change_location(new_location)

def print_player_profile():
    print(f"Player: {player['name']}")
    print(f"Location: {player['location']}")
    print(f"Fuel: {player['fuel']}")
    print(f"Steps: {player['steps']} / {MAX_STEPS}")
    print(f"Inventory: {player['inventory']}")
    print(f"Money: {player['money']}")
    print("\n")


def setup_player():
    print("Welcome to the Space Adventure Game!")
    while True:
        role = input("Do you want to be the captain or a crew member? Enter 'captain' or 'crew': ").strip().lower()
        if role in ['captain', 'crew']:
            player["role"] = role
            break
        else:
            print("Invalid role. Please enter 'captain' or 'crew'.")

    player["name"] = input("Enter your name: ")

def fuel_steps():
    player["steps"] += 1
        # Decrease fuel randomly between 0 and 15 units
    #fuel_decrease = random.randint(0, 15)
    fuel_decrease = random.randint(2, 4) * 5  # Selects a number between 10 and 30 in increments of 5

    player["fuel"] -= fuel_decrease

    # Ensure that fuel doesn't go below 0
    if player["fuel"] < 0:
        player["fuel"] = 0


while True:
    #print(MONEY_HIGH_SCORE)
    #setup_player()
    if player["role"] =="":
        setup_player()
    location_description = locations[player["location"]]
    print(f"-------------------------------------------------------------------------------------------")
    print(f"\nLocation: {player['location']}")
    print(location_description)
    print_player_profile()


    game_result = check_game_conditions()
    if game_result:
        print(game_result)
        if player["money"]>MONEY_HIGH_SCORE:
            print("You also broke record")
        break

    options = locations_options[player["location"]]
    print("Options:")
    for key, value in options.items():
        print(f"{key}: {value}")
    choice = input("Enter your choice: ")
    if player["location"] == "Space Station":
        if choice == "1":
            print(refuel())
        elif choice=="2":
            if player["inventory"]:
                # If the inventory is not empty, randomly remove an item
                removed_item = random.choice(player["inventory"])
                player["inventory"].remove(removed_item)
                add_money = random.choice([10,20,30,40,55,34,98,76,34,22,34,56,100,87,56,45,22,45,80,96])
                print(f"You traded {removed_item} with the space station.")
                player['money']+=add_money;
            else:
                # If the inventory is empty, inform the player
                print("You have nothing to trade.")
        elif choice =="3":
            print("Changing location...............")
            change_to_random_location()
            new_item = random.choice(item_keys)
            player["inventory"].append(new_item)
            fuel_steps()
    elif player["location"]=="Space":
        if choice == "1":
            item_keys = [
                "Oxygen Tank",
                "Alien Artifact",
                "Medikit",
                "Exploration Robot",
                "Quantum Key",
                "Star Map",
                "Laser Blaster",
                "Translator Device",
                "Ancient Scroll",
                "Energy Crystal",
                "Time Capsule"
            ]
            change_to_random_location()
            new_item = random.choice(item_keys)
            player["inventory"].append(new_item)
            fuel_steps()
        elif choice=="2":
            player["location"]="Space Station"
            fuel_steps()
        elif choice == "3":
            # Check inventory
            print("Inventory:", player["inventory"])
        elif choice == "4":
            # Quit the game
            print("Thanks for playing!")
            break

    elif choice in options:
        if choice == "1":
            # Explore nearby asteroid field (random location change)
            item_keys = [
                "Oxygen Tank",
                "Alien Artifact",
                "Medikit",
                "Exploration Robot",
                "Quantum Key",
                "Star Map",
                "Laser Blaster",
                "Translator Device",
                "Ancient Scroll",
                "Energy Crystal",
                "Time Capsule"
            ]
            change_to_random_location()
            new_item = random.choice(item_keys)
            player["inventory"].append(new_item)
            fuel_steps()
        elif choice == "2":
            # Return to space (location change)
            #change_location("Space")
            print("Fuel:", player["fuel"])
        elif choice == "3":
            # Check inventory
            print("Inventory:", player["inventory"])
        elif choice == "4":
            # Quit the game
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    else:
        print("Invalid choice. Please choose a valid option.")
