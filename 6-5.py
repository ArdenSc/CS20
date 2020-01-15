rivers = {
    'nile': 'egypt',
    'amazon river': 'bolivia, peru, columbia, venezuela, brazil, and ecuador',
    'yangtze': 'china'
}

for k, v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}")

for k in rivers:
    print(k.title())

for k in rivers:
    print(rivers[k].title())
