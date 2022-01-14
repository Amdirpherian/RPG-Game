import math
import random as r
import time
import os
import sys
import json
from dataclasses import dataclass
from itertools import accumulate

print("Welcome to Korum'Dah!")


# Set up base classes
class Player:
    def __init__(self, name: str, gender: str, race: str, hp: float, atk: float, critchance: float, critdmg: float,
                 defense: float, helmet: str, chestplate: str, leggings: str, boots: str, ring: str, weapon: str,
                 evasion: float, inventory, goldcoins: int, pclass: str, totalxp: float, level: int):
        self.name = name
        self.gender = gender
        self.race = race
        self.hp = hp
        self.atk = atk
        self.critchance = critchance
        self.critdmg = critdmg
        self.defense = defense
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.ring = ring
        self.weapon = weapon
        self.evasion = evasion
        self.inventory = inventory
        self.goldcoins = goldcoins
        self.pclass = pclass
        self.totalxp = totalxp
        self.level = level

    def duel(self, enemy: str, pclass: str):
        pass

    def gear_menu(self):
        print(f"""
        helmet: {player.helmet}
        chestplate: {player.chestplate}
        leggings: {player.leggings}
        boots: {player.boots}
        ring: {player.ring}
        
        """)

        gValid = False

        while (gValid == False):
            gprompt = input("""
            What would you like to do?
            \'equip\' to equip some gear
            \'exit\' to exit""")

            if (gprompt.lower().strip() == "exit"):
                return None
            elif (gprompt.lower().strip() == "equip"):
                equipValid = False

                while (equipValid == False):
                    eprompt = input("What gear would you like to equip?")

                    # equip gear here from json



    def xp_menu(self, xpearned: int):
        self.totalxp += xpearned
        xpneeded = 0

        for level in range(self.level):
            xpneeded += (0.25 * (level + 300 * 2 ** (level / 7)))

        if (self.totalxp >= xpneeded):
            self.level += 1
            print(f"You reached level {self.level}!")

    def treasure(self, location: str):
        if (location == "fortress"):
            if (self.level <= 20):
                fortresslootobtained1to20 = random.choices(fortressloot1to20, weights=(10, 20, 5, 30, 40, 35, 36, 30, 1), k=1)
                print(f"You found {fortresslootobtained1to20}.")
                alreadyCounted = False  # check if metal was already counted and added to inventory
                for loot in fortresslootobtained1to20:
                    if (player.inventory.get(loot) == None):
                        player.inventory[loot] = minemetals.count(loot)
                        alreadyCounted = True
                    elif (alreadyCounted == False):
                        player.inventory[loot] += minemetals.count(loot)
                        alreadyCounted = True


        elif (location == "religious monument"):
            if (self.level <= 20):
                religiousmonumentlootobtained1to20 = random.choices()


class Weapon:
    def __init__(self, wtype: str, dmg: float):
        self.wtype = wtype
        self.dmg = dmg


class Enemy:
    def __init__(self, race: str, hp: float, atk: float, defense: float, weapon: str):
        self.race = race
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.weapon = weapon


racev, genderv, classv = False, False, False

player = Player(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, {}, 0, None,
                0, 0)

name = input("What is your name? ")
player.name = name

time.sleep(0.75)
print("loading more prompts...")
time.sleep(2)

while (genderv == False):
    genderv = input("What is your gender? (male, female, other) ")
    if (genderv.lower().strip() in ["male", "female", "other"]):
        player.gender = genderv
    else:
        genderv = False

while (racev == False):
    time.sleep(2)
    racev = input("What race do you want to be? The choices are human, orc, elf, werewolf, and dragunius ")
    if (racev.lower().strip() == "human"):
        player.race = "human"
        player.hp = 100
        player.atk = 10
        player.defense = 10
        player.critchance = 0.05
        player.critdmg = 1.5
        player.evasion = 0.05

    elif (racev.lower().strip() == "orc"):
        player.race = "orc"
        player.hp = 150
        player.atk = 7
        player.defense = 15
        player.critchance = 0.04
        player.critdmg = 1.75
        player.evasion = 0.03

    elif (racev.lower().strip() == "elf"):
        player.race = "elf"
        player.hp = 75
        player.atk = 12
        player.defense = 8
        player.critchance = 0.1
        player.critdmg = 2
        player.evasion = 0.15

    elif (racev.lower().strip() == "werewolf"):
        player.race = "werewolf"
        player.hp = 110
        player.atk = 11
        player.defense = 9
        player.critchance = 0.06
        player.critdmg = 1.4
        player.evasion = 0.12

    elif (racev.lower().strip() == "dragunius"):
        player.race = "dragunius"
        player.hp = 115
        player.atk = 11
        player.defense = 10
        player.critchance = 0.02
        player.critdmg = 0.03
        player.evasion = 0.04
    else:
        racev = False

while (classv == False):
    time.sleep(2)
    classv = input("""
    Which class do you want to be?
    -----------------------------

    Warlock: Summons minions to aid in battle
    Mage: Harnesses the elements to devastate enemies
    Warrior: Uses a powerful broadsword to cut down foes
    Paladin: Uses the power of his shield and hammer to wreak havoc while blocking high percentages of damage
    Vampire: Reaps the life essence of enemies, stealing their life to benefit himself
    Rogue: Uses the art of trickery to attack enemies while maintaining stealth
    Shaman: Harnesses the power of totems to buff himself and annihilate his foes
    Executioner: Deals massive damage at the cost of his own health
    Berserker: Deals more damage the weaker and more enraged he is\n
    """)

    if (classv.lower().strip() == "warlock"):
        player.hp += 5
        player.atk += 20
        player.defense += 20
        player.critchance += 0.02
        player.critdmg += 0.3
        player.evasion += 0.02
        print("You chose the Warlock class!")
        player.pclass = "human"

    elif (classv.lower().strip() == "mage"):
        player.hp -= 10
        player.atk += 25
        player.defense += 0
        player.critchance += 0.03
        player.critdmg += 0.35
        player.evasion += 0.03
        print("You chose the Mage class!")
        player.pclass = "human"

    elif (classv.lower().strip() == "warrior"):
        player.hp += 40
        player.atk += 10
        player.defense += 30
        player.critchance += 0.01
        player.critdmg += 0.2
        player.evasion += 0.01
        print("You chose the Warrior class!")
        player.pclass = "human"

    elif (classv.lower().strip() == "paladin"):
        player.hp += 55
        player.atk += 5
        player.defense += 50
        player.critchance += 0
        player.critdmg += 0.01
        player.evasion += 0.01
        print("You chose the Paladin class!")
        player.pclass = "human"

    elif (classv.lower().strip() == "vampire"):
        player.hp += 10
        player.atk += 10
        player.defense += 0
        player.critchance += 0.01
        player.critdmg += 0.2
        player.evasion += 0.01
        print("You chose the Vampire class!")
        player.pclass = "human"

    elif (classv.lower().strip() == "rogue"):
        player.hp -= 40
        player.atk += 25
        player.defense += 0
        player.critchance += 0.2
        player.critdmg += 0.4
        player.evasion += 0.1
        print("You chose the Rogue class!")
        player.pclass = "human"

    elif (classv.lower().strip() == "shaman"):
        player.hp += 20
        player.atk += 15
        player.defense += 10
        player.critchance += 0.02
        player.critdmg += 0.01
        player.evasion += 0
        print("You chose the Shaman class!")
        player.pclass = "human"

    elif (classv.lower().strip() == "executioner"):
        player.hp += 10
        player.atk += 30
        player.defense += 10
        player.critchance += 0.15
        player.critdmg += 0.50
        player.evasion += 0.02
        print("You chose the Executioner class!")
        player.pclass = "human"

    elif (classv.lower().strip() == "berserker"):
        player.hp += 5
        player.atk += 20
        player.defense += 10
        player.critchance += 0.03
        player.critdmg += 0.25
        player.evasion += 0.04
        print("You chose the Berserker class!")
        player.pclass = "human"
    else:
        classv = False

# define resources and resource gathering


logging = ["oak", "spruce", "acacia", "dark oak", "ash", "cedar", "beech", "pine", "maple", "mystical"]
mining = ["gold", "copper", "diamond", "mythril", "quartz", "jade", "silver", "emerald", "amber", "iron", "stone"]
fishing = ["salmon", "cod", "tilapia", "mahi mahi", "tuna", "bluefish", "sunfish", "Shark", "Blue Whale",
           "Colossal Squid", "Leviathin", "Hydra"]
moblist = ["goblin", "mossy golem", "goblin brute", "drunk barbarian", "voodoo goblin", "goblin chief", "imp",
           "hellish imp", "imp archmage", "cyclops", "chimera", "oni", "ogre", "gorgon", "centaur", "centaur chief",
           "dulgarim", "cursedgaze", "7th Bastion death claw",
           "magibolt armor", "megalotragus", "funa yurei", "gravekeeper", "magata kifusa", "onmitsu",
           "magitek dreadnaught"]
fortressloot1to20 = ["tattered treasure map", "mysterious scroll", "gold", "silver", "wine bottle", "old sack",
                     "rusty nail", "mossy key", "aetherial lodestone"]

mobs = [

    {
        "name": "goblin",
        "description": "A small devilish green little creature, full of maliciousness and trickery.",
        "hp": 5,
        "xp_yield": 5,
        "atk": 3,
    }
    ,
    {
        "name": "mossy golem",
        "description": "An old stone golem, covered with moss from his years of existence.",
        "hp": 10,
        "xp_yield": 8,
        "atk": 4,

    }
    ,
    {
        "name": "goblin brute",
        "description": "A large imposing goblin, very dumb yet very violent. Legends say his club weighs as much as 3 humans combined.",
        "hp": 15,
        "xp_yield": 12,
        "atk": 6,

    }
    ,
    {
        "name": "drunk barbarian",
        "description": "A heavily drunk man wielding a axe. Very angry and immune to pain in his drunken state.",
        "hp": 12,
        "xp_yield": 17.5,
        "atk": 12,

    }
    ,
    {
        "name": "voodoo goblin",
        "description": "A frail goblin that practices shamanic rituals. Outcasted by his fellow goblins.",
        "hp": 13,
        "xp_yield": 16,
        "atk": 11,

    }

]

weapons1to20 = [

    {
        "name": "Wooden Sword",
        "description": "A weak and shabby sword. Barely does any damage.",
        "type": "sword",
        "atk": 1,
        "critchance": 0,
        "critdmg": 0,
        "defense": 0,
        "evasion": 0,
        "droprate":40,
    },

{
    "name": "Blunt Club",
    "description": "An awful looking club. Doesn't hurt much.",
    "type": "club",
    "atk": 2,
    "critchance": 0,
    "critdmg": 0,
    "defense": 0,
    "evasion": 0,
    "droprate":30,
},

{
    "name": "Novice Staff",
    "description": "A simple magic staff for novices. Can only cast basic spells. Made of magical wood.",
    "type": "staff",
    "atk": "2",
    "critchance": 0,
    "critdmg": 0.1,
    "defense": 0,
    "evasion": 0,
    "droprate":30,
},

{
    "name": "Stone Axe",
    "description": "A very rudimentary stone axe. Hits like a stick.",
    "type": "axe",
    "atk": 2,
    "critchance": 0,
    "critdmg": 0.1,
    "defense": 0,
    "evasion": 0,
    "droprate":30,
},

{
    "name": "Phantom Dagger",
    "description": "A lightweight dagger, allowing the user to attack rapidly with it.",
    "type": "dagger",
    "atk": 4,
    "critchance": 0.2,
    "critdmg": 0.2,
    "defense": -2,
    "evasion": 0,
    "droprate":25,
},

{
    "name": "Voodoo Doll",
    "description": "A voodoo doll said to contain dangerous and vile dark magic.",
    "type": "misc",
    "atk": 6,
    "critchance": 0.2,
    "critdmg": 0.1,
    "defense": -1,
    "evasion": 1,
    "droprate":15,
},

{
    "name": "Aetherial Ice Staff",
    "description": "A staff with an ice ball imbued in it. Can freeze enemies very easily.",
    "type": "staff",
    "atk": 7.2,
    "critchance": 0,
    "critdmg": 0.1,
    "defense": 0,
    "evasion": 0,  # chance to freeze: base 15%
    "droprate":18,
},

{
    "name": "Titan Broadsword",
    "description": "Heavy and powerful sword. Makes the user cumbersome.",
    "type": "sword",
    "atk": 6,
    "critchance": 0.1,
    "critdmg": 0.13,
    "defense": 10,
    "evasion": -5,
    "droprate":20,
},

{
    "name": "Apprentice's wand",
    "description": "A slightly more sophisticated wand made from fine Ash wood. Can cast damaging spells.",
    "type": "Wand",
    "atk": 5,
    "critchance": 0.1,
    "critdmg": 0.1,
    "defense": 0,
    "evasion": 0,
    "droprate":20,
},

{
    "name": "Smooth Cutlass of the Tide",
    "description": "A smooth medium length blade. It was supposedly smoothed by the tides.",
    "type": "Sword",
    "atk": 10.3,
    "critchance": 0.04,
    "critdmg": 0.136,
    "defense": 0,
    "evasion": 0,
    "droprate":3,
},

{
    "name": "Enhanced Magitek Falchion",
    "description": "Made of steel and enhanced with a bit of magic, this falchion is highly dangerous.",
    "type": "Sword",
    "atk": 11.45,
    "critchance": 0.07,
    "critdmg": 0.21,
    "defense": 0,
    "evasion": 0,
    "droprate":3,
},

{
    "name": "Fine Saber of Forgotten Souls",
    "description": "A long saber that holds desparate solds inside it. You can almost hear them wailing if all is quiet.",
    "type": "Sword",
    "atk":11.3,
    "critchance": 0.05,
    "critdmg": 0.3,
    "defense": 0,
    "evasion": 0,
"   droprate":3,
},

{
    "name": "Pious Longsword",
    "description": "A holy sword, crafted from the finest metals. Has very long reach.",
    "type": "sword",
    "atk": 9.5,
    "critchance": 0.3,
    "critdmg": 0.05,
    "defense": 0,
    "evasion": 0,
    "droprate":5,
},

{
    "name": "Picatrix of Foresight",
    "description": "An ancient picatrix. Tales tell of its ability to divinate the future...",
    "type": "Book",
    "atk": 10.2,
    "critchance": 0.18,
    "critdmg": 0.07,
    "defense":0,
    "evasion":0.2,
    "droprate":4,
},

{
    "name": "Grimoire Infernium",
    "description": "An old and tattered grimoire, rumored to contain potent fire spells in it...",
    "type": "Book",
    "atk": 19.7,
    "critchance": 0.13,
    "critdmg": 0.94,
    "defense": 0,
    "evasion": 0,
    "droprate":2,
},

{
    "name": "Bloodborne Cutlass",
    "description": "A powerful and menacing sword. Legends say it was formed from the first blood oath of Aurim...",
    "type": "sword",
    "atk": 15.4,
    "critchance": 0.21,
    "critdmg": 0.364,
    "defense": 3,
    "evasion": 0,
    "droprate":2,
},

{
    "name": "Luminous Broadsword",
    "description": "A heavy broadsword. Also used to light up dark areas.",
    "type": "sword",
    "atk": 8.1,
    "critchance": 0,
    "critdmg": 0,
    "defense": 10,
    "evasion": 0,
    "droprate":4,
},

{
    "name": "Scepter of Aurima",
    "description:": "A powerful scepter, capable of inflicting great pain. It is said that it draws from the Aetherial energy of the fabric of reality itself.",
    "type": "staff",
    "atk": 20.3,
    "critchance": 0.14,
    "critdmg": 0.276,
    "defense": 2,
    "evasion": 0,
    "droprate":1,
}

]

def log():
    print("You go out into the forests to log some wood")
    print("...")
    time.sleep(2)

    gatheredlogs = r.choices(logging, weights=(2, 2, 2, 2, 2, 2, 2, 2, 2, 1), k=3)
    print(f"You finished logging. You logged {gatheredlogs}.")
    alreadyCounted = False  # check if log was already counted and added to inventory
    for log in gatheredlogs:
        if (player.inventory.get(log) == None):
            player.inventory[log] = gatheredlogs.count(log)
            alreadyCounted = True
        elif (alreadyCounted == False):
            player.inventory[log] += gatheredlogs.count(log)
            alreadyCounted = True


def fish():
    print("You walk down to the closest lake with your fishing rod and throw in your line.")
    print("...")
    time.sleep(2)
    isCatch = r.randint(1, 2)
    if (isCatch == 1):
        failMsg = r.randint(1, 3)
        if (failMsg == 1):
            print("You didn't catch anything. Perhaps your hook is not attractive enough.")

        elif (failMsg == 2):
            print("You didn't catch anything. Maybe you need to be more patient.")

        else:
            print("You didn't catch anything. Maybe your bait isn't tasty enough.")


    else:
        caughtfish = r.choices(fishing, weights=(10, 10, 10, 10, 10, 10, 10, 5, 5, 3, 1, 1), k=1)

        print(f"You finished fishing. You fished up {caughtfish}.")
        alreadyCounted = False  # check if sea creature was already counted and added to inventory
        for seacreature in caughtfish:
            if (player.inventory.get(seacreature) == None):
                player.inventory[seacreature] = caughtfish.count(seacreature)
                alreadyCounted = True
            elif (alreadyCounted == False):
                player.inventory[seacreature] += caughtfish.count(seacreature)
                alreadyCounted = True


def mine():
    print(
        "You grab your pickaxe and begin to hack at the earth, hoping to find some useful minerals, metals, and ores.")
    print("...")
    time.sleep(2)
    minemetals = r.choices(mining, weights=(3, 20, 2, 1, 4, 4, 30, 7, 5, 50, 150), k=3)

    print(f"You finished mining. You mined {minemetals}.")
    alreadyCounted = False  # check if metal was already counted and added to inventory
    for metal in minemetals:
        if (player.inventory.get(metal) == None):
            player.inventory[metal] = minemetals.count(metal)
            alreadyCounted = True
        elif (alreadyCounted == False):
            player.inventory[metal] += minemetals.count(metal)
            alreadyCounted = True


def explore():
    print("You venture out to explore the wild.\n...")
    time.sleep(r.randint(5, 10))

    foundstruct = 1

    match foundstruct:

        case 1: # fortress
            print("You stumbled across some stones\n...")
            time.sleep(2)
            goInside = input(r"""
            [-I-I--II-]
             \ `   '  /
              |[] `__|
              |__   ,|
    \,/     __| ___ ,|_
/`\        [_I__I_I__I_]
           \-\--|-|--/-/
            |[] `    '|
           / \  [] ` .|
          <===>    `  |
          | []|  `    |
          <===>.  `   |
           \_/    .   |
            | []      |
            |    `    |
            |    . '  |
          ./|' . . . .|
       __ ----~    ~`---,
__ ,--~'                  ~~


It appears to be the ancient ruins of some fortress.
Are you daring enough to venture inside? (yes/no) """)
            if (goInside.lower().strip() == "yes"):
                dioforchoice = r.randint(1, 5)
                match dioforchoice:
                    case 1:
                        print("You carefully venture into the ruins. The moss is slippery.")
                    case 2:
                        print(
                            "You venture into the ruins. You think you see a shadow of a demonic figure, but it disappears.")
                    case 3:
                        print("You venture carefully into the ruins. You notice the cracked stones.")
                    case 4:
                        print(
                            "You venture carefully into the abandoned ruins. You hear the soft *pitter patter* of raindrops on the archaic floor.")
                    case 5:
                        print(
                            "You venture carefully into the abandoned ruins. The whistle of the wind seems eerie today...")

                mobencounter = r.randint(1, 3)

                match mobencounter:
                    case 1:
                        print("You encountered a mob while exploring!")
                    case 2:
                        print("You hear a shriek from the shadows and see a hideous beast appear in front of you.")
                    case 3:
                        print("You find a treasure chest!")
                        treasure("fortress")

            else:
                print("You left the ruins.")
                return None

        case 2: # ancient religious monument
            print("""                                                   
            While out exploring, you stumble across some huge pillar stones. They have weird runic inscriptions on them. They seem to be placed in a circle, and you think you see a shiny crystal floating in the center. Perhaps this is just your imagination.
            """)

            goInside = input("Would you like to venture into the circle?")

            if (goInside.lower().strip() == "yes"):
                # varied dialogue while entering
                diomonchoice = r.randint(1,5)
                match diomonchoice:
                    case 1:
                        print("You carefully step into the center of the monument. It seems old, yet you feel an etherial power emanating from it.")
                    case 2:
                        print("You carefully walk into the monument. You feel a powerful magic presence take hold of you.")
                    case 3:
                        print("You carefully step into the center of the monument. The runes on it look mysterious.")
                    case 4:
                        print("")
                    case 5:
                        print("")

                # add mobencounter stuffs
                mobortreasuremonument = r.randint(1,3)

            else:
                print("You left the monument.")
                return None








def profile():
    print(f"""

    {player.name}'s profile
    Race: {player.race}
    Gender: {player.gender}
    Class: {player.pclass}
    Attack: {player.atk}
    Health: {player.hp}
    Defense: {player.defense}
    Crit Chance: {player.critchance*100}%
    Crit Damage: {player.critdmg+100}%
    Evasion: {player.evasion*100}%
    Inventory: {player.inventory}
    Gold Coins: {player.goldcoins}
    Level: {player.level}
    

    """)


def craft():
    pass


def questLog():
    pass


while True:
    time.sleep(5)
    isValid = False

    while (isValid == False):
        action = input("""
    Which action do you want to take?

    \'log\' to go logging
    \'fish\' to go fishing
    \'mine\' to go mining
    \'explore\' to go exploring
    \'profile\' to view your profile
    \'craft\' to view the crafting menu
    \'gear\' to view current gear and gear inventory
    \'questlog\' to view the current quest
    """)

        if (action.lower().strip() == "log"):
            log()
        elif (action.lower().strip() == "fish"):
            fish()
        elif (action.lower().strip() == "mine"):
            mine()
        elif (action.lower().strip() == "log"):
            log()
        elif (action.lower().strip() == "explore"):
            explore()
        elif (action.lower().strip() == "profile"):
            profile()
        elif (action.lower().strip() == "craft"):
            craft()
        elif (action.lower().strip() == "gear"):
            player.gear_menu()
        elif (action.lower().strip() == "questLog"):
            questLog()





































