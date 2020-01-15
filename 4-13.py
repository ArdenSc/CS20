foods = ('bread', 'potato', 'chicken', 'beef', 'soup')

for food in foods:
    print(food)

try:
    foods[0] = 'toast'
except TypeError:
    print("Tuple value editing failed")

foods = ('toast', 'potato', 'chicken', 'beef', 'stew')

for food in foods:
    print(food)
