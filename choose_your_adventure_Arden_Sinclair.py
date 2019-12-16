from random import randint


def fight(hp, enemy, enemy_hp):
    print(f"You are approached by a fearsome {enemy}, what do you do?")
    while True:
        choice = input("Attack or run?\n").lower()
        if choice == "attack":
            while hp > 0 and enemy_hp > 0:
                print(f"You have {hp} health, the {enemy} has {enemy_hp} health.")
                while True:
                    print("What do you do?")
                    choice = input("Light attack, heavy attack, or heal?\n").lower()
                    if choice == ("heavy" or "heavy attack"):
                        if randint(0, 1) == 0:
                            print("Your heavy attack missed!")
                        else:
                            damage = randint(3, 5)
                            enemy_hp -= damage
                            enemy_hp = enemy_hp if enemy_hp > 0 else 0
                            print(f"Your heavy attack did {damage} damage!")
                        break
                    elif choice == ("light" or "light attack"):
                        damage = randint(1, 3)
                        enemy_hp -= damage
                        enemy_hp = enemy_hp if enemy_hp > 0 else 0
                        print(f"Your light attack did {damage} damage!")
                        break
                    elif choice == "heal":
                        hp += 1
                        print("You heal yourself by 1 health.")
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
print("Welcome to the dungeon!")
while True:
    print("You are confronted with three tunnels. Which will you take?")
    choice = input("Left, center, or right?\n").lower()
    if choice == "left":
        print("You follow the tunnel, holding you torch out in front of you for light.\n"
              "Something runs quickly past your side. A sense of danger looms.\n"
              "It runs back towards you. You can now see that it's a massive rat!")
        if randint(0, 1) == 0:
            print("The rat squeaks and runs behind you. It didn't want to bite such a fearsome foe.")
        else:
            hp = fight(hp, "Rat", 4)
    elif choice == "right":
        pass
    elif choice == "center":
        pass
    else:
        print("Invalid choice, try again.")
