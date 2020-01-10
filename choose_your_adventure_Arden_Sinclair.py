# CS20 - P4
# Arden Sinclair
# Jan. 06, 2020
# Chart: https://github.com/ArdenSinclair/CS20/blob/master/CYOA%20Flowchart.png
# Dungeon adventure game

from random import choice
from random import randint


def fight(hp, dmg_multiplier, enemy, enemy_hp, running_allowed=True):
    """Allows the player to engage in combat against an enemy.
    hp is the health of the player at the start of the fight
    enemy is the name of the enemy to be fought
    enemy_hp is the health of the enemy at the start of the fight
    running_allowed allows or disallows the player to run from a fight
    """
    print(f"You are approached by a "
          f"{choice(('fearsome', 'ferocious', 'evil', 'crazy'))} "
          f"{enemy}, what do you do?")
    while True:
        selection = input("Attack or run?\n").lower()
        if selection == "attack":
            while hp > 0 and enemy_hp > 0:
                print(f"You have {hp} health, the {enemy} has {enemy_hp}"
                      f" health.")
                while True:
                    print("What do you do?")
                    selection = input("Light attack, heavy attack, "
                                      "or heal?\n").lower()
                    if selection in ("heavy", "heavy attack"):
                        if randint(0, 4) == 0:
                            print("Your heavy attack missed!")
                        else:
                            damage = round(randint(3, 5) * dmg_multiplier)
                            if randint(0, 1) == 0:
                                damage *= 2
                            enemy_hp -= damage
                            enemy_hp = enemy_hp if enemy_hp > 0 else 0
                            print(f"Your heavy attack did {damage} damage!")
                        break
                    elif selection in ("light", "light attack"):
                        damage = round(randint(1, 3) * dmg_multiplier)
                        enemy_hp -= damage
                        enemy_hp = enemy_hp if enemy_hp > 0 else 0
                        print(f"Your light attack did {damage} damage!")
                        break
                    elif selection == "heal":
                        heal = randint(2, 4)
                        hp += heal
                        print(f"You heal yourself by {heal} health.")
                        break
                    else:
                        print("Invalid choice, try again.")
                if enemy_hp > 0:
                    damage = randint(1, 3)
                    hp -= damage
                    hp = hp if hp > 0 else 0
                    print(f"The {enemy} hit you for {damage} damage!")
                else:
                    print(f"The {enemy} jumped forward and tried to hit you, "
                          f"but fell to the ground.")
            if hp == 0:
                a_or_an = 'an' if enemy[0].lower() in \
                                  ['a', 'e', 'i', 'o', 'u'] else 'a'
                print(f"You died to {a_or_an} {enemy}, really?")
                print("Game Over.")
                return hp
            elif enemy_hp == 0:
                print(f"You have slain the {enemy}, well done! You have {hp}"
                      f" health.")
            break
        elif selection == "run":
            if not running_allowed:
                print(f"You can't run from the {enemy}, "
                      f"there's nowhere to go!")
                continue
            if randint(0, 1) == 0:
                print("You ran away.")
            else:
                damage = randint(1, 5)
                hp -= damage
                hp = hp if hp > 0 else 0
                print(f"The {enemy} struck you from behind, dealing {damage}"
                      f" damage!")
                if hp == 0:
                    print("You died!")
                    print("Game Over.")
                    return hp
                print(f"You ran away, wounded from the slash with {hp}"
                      f" health remaining.")
            break
        else:
            print("Invalid choice, try again.")
    return hp


def game(hp, dmg_multiplier):
    """Contains the story and choices of the adventure game
    hp is the player's starting health
    """
    print("Welcome to the dungeon adventure!")
    while True:
        print("You are confronted with a cave opening. Will you go in and "
              "see what's inside?")
        selection = input("Enter the cave or run away?\n").lower()
        if selection in ("enter the cave", "enter", "go in", "cave"):
            print("You follow the tunnel, holding your torch out in front of "
                  "you for light.\n"
                  "Something runs quickly past your side. A sense of danger "
                  "looms.\n"
                  "It runs back towards you. You can now see that it's a "
                  "massive rat!")
            if randint(0, 1) == 0:
                print("The rat squeaks and runs behind you. It didn't want "
                      "to bite such a fearsome foe.")
            else:
                hp = fight(hp, dmg_multiplier, "Rat", 4)
                if hp == 0:
                    return
            print("You continue on, finding a skeleton leaned against the "
                  "wall.\n"
                  "One of its bones looks weird and shiny. What do you do?")
            while True:
                selection = input("Grab the bone or leave it?\n").lower()
                if selection in ("grab the bone", "grab it", "grab"):
                    print("The wall behind you creaks and splits, revealing "
                          "a secret passage!\n"
                          "There is a skeleton guarding the passage with a "
                          "sword and shield!")
                    hp = fight(hp, dmg_multiplier, "Skeleton", 15)
                    if hp == 0:
                        return
                    print("With the skeleton gone, you trudge on, "
                          "encountering\n"
                          "a fork in the path. Where do you go?")
                    while True:
                        selection = input("Left or right?\n").lower()
                        if selection == "left":
                            print("You walk through the left passage. A "
                                  "metal door falls from above,\n"
                                  "blocking the way back. You hear a massive "
                                  "RRRRRROOOOOAAAAARRRRR!\n"
                                  "A giant Ogre appears out of the smoke in "
                                  "front of you!")
                            hp = fight(hp, dmg_multiplier, "Ogre", 50, False)
                            if hp == 0:
                                return
                            print("With his dying breath, the Ogre pulls out "
                                  "a key from his pocket.\n"
                                  "You see a door behind him with a keyhole "
                                  "about the same size as the key.\n"
                                  "You can try the key and see what's "
                                  "behind. What do you do?")
                            while True:
                                selection = input("Try the key or "
                                                  "run away?\n").lower()
                                if selection in ("try the key", "key", "try",
                                                 "try it"):
                                    print("The key fits and turns, revealing "
                                          "a room full of gold and gems!\n"
                                          "Congratulations, you win!")
                                    return
                                elif selection in ("run away", "run"):
                                    print("You run away from the door in "
                                          "fear of a trap. You find yourself "
                                          "back\n"
                                          "at the start of the cave.")
                                    break
                                else:
                                    print("Invalid choice, try again.")
                            break
                        elif selection == "right":
                            print("You go through the right passage. From "
                                  "all around you, different foes appear!")
                            hp = fight(hp, dmg_multiplier, "Zombie", 5, False)
                            if hp == 0:
                                return
                            hp = fight(hp, dmg_multiplier, "Poisonous Bat", 10,
                                       False)
                            if hp == 0:
                                return
                            hp = fight(hp, dmg_multiplier, "Troll", 20, False)
                            if hp == 0:
                                return
                            print("With the trio dealt with, you find a key "
                                  "lying on the ground beside them.\n"
                                  "You see a door behind with a keyhole "
                                  "about the same size as the key.\n"
                                  "You can try the key and see what's "
                                  "behind. What do you do?")
                            while True:
                                selection = input("Try the key or "
                                                  "run away?\n").lower()
                                if selection in ("try the key", "key",
                                                 "try it", "try"):
                                    print("The key fits and turns, revealing "
                                          "a room full of gold and gems!\n"
                                          "Congratulations, you win!")
                                    return
                                elif selection in ("run away", "run"):
                                    print("You run away from the door in "
                                          "fear of a trap. You find yourself "
                                          "back\n"
                                          "at the start of the cave.")
                                    break
                                else:
                                    print("Invalid choice, try again.")
                            break
                        else:
                            print("Invalid choice, try again.")
                    break
                elif selection in ("leave it", "leave"):
                    print("You ignore the skeleton, walking further into the "
                          "tunnel.\n"
                          "The tunnel opens up into a room full of lava and "
                          "spikes. Looks like this wasn't\n"
                          "the path you wanted. You turn back and leave, "
                          "soon finding yourself at the start\n"
                          "of the cave.")
                    break
                else:
                    print("Invalid choice, try again.")
        elif selection in ("run away", "run"):
            print("You run away from the cave, too scared of what awaits you "
                  "inside.")
            print("Game over.")
            return
        else:
            print("Invalid choice, try again.")


def main():
    """Calls the function to play the game and requests if the player wants
    to play again """
    while True:
        # Starts the game and gives the player a starting health of 20
        while True:
            print("Choose a character:\n"
                  "Ogre: 30HP, 75% damage\n"
                  "Human: 20HP, 100% damage\n"
                  "Elf: 15HP, 125% damage")
            selection = input("Ogre, Human, or Elf?\n").lower()
            if selection == "ogre":
                game(30, 0.75)
                break
            elif selection == "human":
                game(20, 1)
                break
            elif selection == "elf":
                game(15, 1.25)
                break
            else:
                print("Invalid choice, try again.")
        while True:
            selection = input("Would you like to play again? Yes or no?\n"). \
                lower()
            if selection == "yes":
                print("Sure. Lets play another round, shall we?")
                break
            elif selection == "no":
                print("Alright. Hope you had fun!")
                exit()
            else:
                print("Invalid choice, try again.")


main()
