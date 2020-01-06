from random import choice as randchoice
from random import randint


def fight(hp, enemy, enemy_hp, running_allowed=True):
    print(f"You are approached by a {randchoice(('fearsome', 'ferocious', 'evil', 'crazy'))} {enemy}, what do you do?")
    while True:
        choice = input("Attack or run?\n").lower()
        if choice == "attack":
            while hp > 0 and enemy_hp > 0:
                print(f"You have {hp} health, the {enemy} has {enemy_hp} health.")
                while True:
                    print("What do you do?")
                    choice = input("Light attack, heavy attack, or heal?\n").lower()
                    if choice in ("heavy", "heavy attack"):
                        if randint(0, 4) == 0:
                            print("Your heavy attack missed!")
                        else:
                            damage = randint(3, 5)
                            if randint(0, 1) == 0:
                                damage *= 2
                            enemy_hp -= damage
                            enemy_hp = enemy_hp if enemy_hp > 0 else 0
                            print(f"Your heavy attack did {damage} damage!")
                        break
                    elif choice in ("light", "light attack"):
                        damage = randint(1, 3)
                        enemy_hp -= damage
                        enemy_hp = enemy_hp if enemy_hp > 0 else 0
                        print(f"Your light attack did {damage} damage!")
                        break
                    elif choice == "heal":
                        heal = randint(1, 3)
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
                    print(f"The {enemy} jumped forward and tried to hit you, but fell to the ground.")
            if hp == 0:
                print(f"You died to {'an' if enemy[0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'} {enemy}, really?")
                print("Game Over.")
                exit()
            elif enemy_hp == 0:
                print(f"You have slain the {enemy}, well done! You have {hp} health.")
            break
        elif choice == "run":
            if not running_allowed:
                print(f"You can't run from the {enemy}, there's nowhere to go!")
                continue
            if randint(0, 1) == 0:
                print("You ran away.")
            else:
                damage = randint(1, 5)
                hp -= damage
                hp = hp if hp > 0 else 0
                print(f"The {enemy} struck you from behind, dealing {damage} damage!")
                if hp == 0:
                    print("You died!")
                    print("Game Over.")
                    exit()
                print(f"You ran away, wounded from the slash with {hp} health remaining.")
            break
        else:
            print("Invalid choice, try again.")
    return hp


hp = 20
print("Welcome to the dungeon adventure!")
while True:
    print("You are confronted with a cave opening. Will you go in and see what's inside?")
    choice = input("Enter the cave or run away?\n").lower()
    if choice in ("enter the cave", "enter", "go in", "cave"):
        print("You follow the tunnel, holding your torch out in front of you for light.\n"
              "Something runs quickly past your side. A sense of danger looms.\n"
              "It runs back towards you. You can now see that it's a massive rat!")
        if randint(0, 1) == 0:
            print("The rat squeaks and runs behind you. It didn't want to bite such a fearsome foe.")
        else:
            hp = fight(hp, "Rat", 4)
        print("You continue on, finding a skeleton leaned against the wall.\n"
              "One of its bones looks weird and shiny. What do you do?")
        while True:
            choice = input("Grab the bone or leave it?\n").lower()
            if choice in ("grab the bone", "grab it", "grab"):
                print("The wall behind you creaks and splits, revealing a secret passage!\n"
                      "There is a skeleton guarding the passage with a sword and shield!")
                hp = fight(hp, "Skeleton", 15)
                print("With the skeleton gone, you trudge on, encountering\n"
                      "a fork in the path. Where do you go?")
                while True:
                    choice = input("Left or right?\n").lower()
                    if choice == "left":
                        print("You walk through the left passage. A metal door falls from above,\n"
                              "blocking the way back. You hear a massive RRRRRROOOOOAAAAARRRRR!\n"
                              "A giant Ogre appears out of the smoke in front of you!")
                        hp = fight(hp, "Ogre", 50, False)
                        print("With his dying breath, the Ogre pulls out a key from his pocket.\n"
                              "You see a door behind him with a keyhole about the same size as the key.\n"
                              "You can try the key and see what's behind. What do you do?")
                        while True:
                            choice = input("Try the key or run away?\n").lower()
                            if choice in ("try the key", "key"):
                                print("The key fits and turns, revealing a room full of gold and gems!\n"
                                      "Congratulations, you win!")
                                exit()
                            elif choice in ("run away", "run"):
                                print("You run away from the door in fear of a trap. You find yourself back\n"
                                      "at the start of the cave.")
                                break
                            else:
                                print("Invalid choice, try again.")
                        break
                    elif choice == "right":
                        print("You go through the right passage. From all around you, different foes appear!")
                        hp = fight(hp, "Zombie", 5, False)
                        hp = fight(hp, "Poisonous Bat", 10, False)
                        hp = fight(hp, "Troll", 20, False)
                        print("With the trio dealt with, you find a key lying on the ground beside them.\n"
                              "You see a door behind with a keyhole about the same size as the key.\n"
                              "You can try the key and see what's behind. What do you do?")
                        while True:
                            choice = input("Try the key or run away?\n").lower()
                            if choice in ("try the key", "key"):
                                print("The key fits and turns, revealing a room full of gold and gems!\n"
                                      "Congratulations, you win!")
                                exit()
                            elif choice in ("run away", "run"):
                                print("You run away from the door in fear of a trap. You find yourself back\n"
                                      "at the start of the cave.")
                                break
                            else:
                                print("Invalid choice, try again.")
                        break
                    else:
                        print("Invalid choice, try again.")
            elif choice in ("leave it", "leave"):
                print("You ignore the skeleton, walking further into the tunnel.\n"
                      "The tunnel opens up into a room full of lava and spikes. Looks like this wasn't\n"
                      "the path you wanted. You turn back and leave, soon finding yourself at the start\n"
                      "of the cave.")
                break
            else:
                print("Invalid choice, try again.")
    elif choice in ("run away", "run"):
        print("You run away from the cave, too scared of what awaits you inside.")
        print("Game over.")
        exit()
    else:
        print("Invalid choice, try again.")
