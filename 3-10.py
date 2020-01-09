# CS20 - P4
# Arden Sinclair
# Jan. 8, 2020
# Solutions to Python Crash Course 3-10

from random import shuffle


def print_flavors():
    print(f"Ice cream flavors: {', '.join(ice_cream)}")


print("Starting list")
ice_cream = ["vanilla", "chocolate", "coconut", "brownie", "cookies and cream",
             "fudge", "candy cane", "cake"]
print_flavors()

print("\nAdding mint to list")
ice_cream.append("mint")
print_flavors()

print("\nAdding caramel as the second flavor")
ice_cream.insert(1, "caramel")
print_flavors()

print("\nRemoving the second last flavor")
del ice_cream[-2]
print_flavors()

print(
    f"\nRemoving the 3rd item, which is {ice_cream.pop(4)}, from the flavors")
print_flavors()

print("\nRemoving candy cane from the flavors")
ice_cream.remove("candy cane")
print_flavors()

print("\nSorting the flavors alphabetically")
ice_cream.sort()
print_flavors()

print("\nScrambling the list")
shuffle(ice_cream)
print_flavors()

print(f"\nShowing flavors in alphabetical order without changing the list")
print(f"Ice cream flavors: {', '.join(sorted(ice_cream))}")
print("Actual list")
print_flavors()

print("\nReversing the list")
ice_cream.reverse()
print_flavors()

print(f"\nThe list of flavors is {len(ice_cream)} long")
