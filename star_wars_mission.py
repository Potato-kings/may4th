import random


characters = [
    "Jedi Knight",
    "Padawan",
    "Rebel Pilot",
    "Mandalorian",
    "Smuggler",
    "Clone Trooper",
    "Resistance Spy"
]

planets = [
    "Tatooine",
    "Hoth",
    "Endor",
    "Naboo",
    "Coruscant",
    "Dagobah",
    "Mustafar"
]

missions = [
    "rescue a captured droid",
    "recover stolen battle plans",
    "escape an Imperial base",
    "protect a hidden Jedi temple",
    "deliver a secret message",
    "destroy a Sith weapon",
    "find a lost lightsaber"
]

enemies = [
    "Darth Vader",
    "a Sith Inquisitor",
    "stormtroopers",
    "bounty hunters",
    "a crime lord",
    "battle droids",
    "the First Order",
    "Kylo Ren",
    "Darth Sidious",
    "Count Dooku"
]

allies = [
    "R2-D2",
    "Chewbacca",
    "Ahsoka Tano",
    "Obi-Wan Kenobi",
    "BB-8",
    "a group of Ewoks",
    "a mysterious rebel informant"
]

ships = [
    "Millennium Falcon",
    "X-wing",
    "TIE fighter",
    "Naboo starfighter",
    "Razor Crest",
    "Jedi starfighter",
    "Corellian freighter",
    "Millennium Falcon",
    "Death Star",
    "Tantive IV"
]

lightsaber_colors = [
    "Red",
    "Blue",
    "Purple",
    "White",
    "Yellow",
    "Green"
]

code_words_1 = ["Shadow", "Red", "Jedi", "Echo", "Rebel", "Nova"]
code_words_2 = ["Falcon", "Saber", "Moon", "Strike", "Temple", "Droid"]

def display_mission_type():
    mission_type = random.choice(["rescue", "battle", "spy", "escape"])
    
    if mission_type == "rescue":
        print("This is a rescue mission. Move quickly and protect the target.")
    elif mission_type == "battle":
        print("This is a combat mission. Prepare for heavy resistance.")
    elif mission_type == "spy":
        print("This is a stealth mission. Do not get caught.")
    else:
        print("This is an escape mission. Get out before it is too late.")


def draw_lightsaber():
    print(""
    "\n           /--/" \
    "\n          /  /" \
    "\n         /  /" \
    "\n        /  /" \
    "\n       /  /" \
    "\n     =/==/=" \
    "\n     /  /" \
    "\n    /--/")

def generate_mission():
    character = random.choice(characters)
    planet = random.choice(planets)
    mission = random.choice(missions)
    enemy = random.choice(enemies)
    ally = random.choice(allies)
    ship = random.choice(ships)
    color = random.choice(lightsaber_colors)
    difficulty = random.randint(1, 10)
    code_name = random.choice(code_words_1) + " " + random.choice(code_words_2)  

    print("\n<=---------------------------=>")
    print("   STAR WARS MISSION BRIEFING")
    print("<=---------------------------=>")

    display_mission_type()

    print("Mission Code Name:", code_name)  
    print("Character:", character)
    print("Planet:", planet)
    print("Mission:", mission)
    print("Enemy:", enemy)
    print("Ally:", ally)
    print("Ship:", ship)
    print("Lightsaber Color:", color)
    print("Difficulty:", difficulty)

    print("\nBriefing:")
    print(f"A {character} must travel to {planet} aboard the {ship} on mission {code_name}.")
    print(f"With help from {ally} and their {color} lightsaber, they must {mission} before {enemy} stops them.")

    if difficulty <= 3:
        print("This should be an easy mission.")
    elif difficulty <= 7:
        print("This mission will be dangerous.")
    else:
        print("This mission is extremely risky. I have a bad feeling about this.")

    success_chance = random.randint(1, 100)

    print("\nSuccess Chance:", success_chance, "%")

    if success_chance >= 75:
        print("The Force is strong with this mission.")
    elif success_chance >= 40:
        print("This mission is risky, but possible.")
    else:
        print("The odds are not good.")

    print("May the Force be with you.")


print("Welcome to the Star Wars Mission Generator!")
draw_lightsaber()

side = input("Choose your side: Jedi, Rebel, Sith, or Bounty Hunter: ").lower()

if side == "jedi":
    print("You have chosen the path of the Jedi.")
elif side == "sith":
    print("The dark side grows stronger...")
elif side == "rebel":
    print("The Rebellion needs your help.")
elif side == "bounty hunter":
    print("This mission is all about the credits.")
else:
    print("You are a mysterious traveler.")
        

while True:

    choice = input("\nGenerate a new mission? yes/no: ").lower()

    if choice == "yes":
        generate_mission()
    elif choice == "no":
        print("Goodbye, young Jedi.")
        break
    else:
        print("Please type yes or no.")

# Reflection Questions:
# 1. What does random.choice() do?
# It picks a random value from a list

# 2. What does random.randint() do?
# Returns a random integer between two imputed integer (inclusive)

# 3. Why are lists useful in this project?
# It helps group similar items together for readabilty and for selecting using random.choice()

# 4. Why did we put the mission generator inside a function?
# helps sort code and for easier use in while loop

# 5. What custom list or feature did you add?
# added extra ships, extra villans, and new lightsaber colors and ASCII lightsaber, Mission code name, sucsess chance, and chosing sides.

# 6. What was your favorite mission your program created?
# See below

# Welcome to the Star Wars Mission Generator!

#            /--/
#           /  /
#          /  /
#         /  /
#        /  /
#      =/==/=
#      /  /
#     /--/
# Choose your side: Jedi, Rebel, Sith, or Bounty Hunter: jedi
# You have chosen the path of the Jedi.

# Generate a new mission? yes/no: yes

# <=---------------------------=>
#    STAR WARS MISSION BRIEFING
# <=---------------------------=>
# This is a rescue mission. Move quickly and protect the target.
# Mission Code Name: Shadow Temple
# Character: Smuggler
# Planet: Tatooine
# Mission: find a lost lightsaber
# Enemy: a Sith Inquisitor
# Ally: a group of Ewoks
# Ship: Tantive IV
# Lightsaber Color: Green
# Difficulty: 10

# Briefing:
# A Smuggler must travel to Tatooine aboard the Tantive IV on mission Shadow Temple.
# With help from a group of Ewoks and their Green lightsaber, they must find a lost lightsaber before a Sith Inquisitor stops them.
# This mission is extremely risky. I have a bad feeling about this.

# Success Chance: 31 %
# The odds are not good.
# May the Force be with you.

# Generate a new mission? yes/no: no
# Goodbye, young Jedi.