hotbar = [
    'Torch',
    'Rock',
    'Potion',
    'Sword',
    'Shield'
]

index = hotbar.index('Sword')
item = hotbar.pop(index)
hotbar.insert(0, item)
print(hotbar)
