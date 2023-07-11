import time
from itertools import cycle

lights= [
    ('Green', 2),
    ('Yellow', 0.5),
    ('Red', 2)
]
colors = cycle(lights)

while True:
    color, second = next(colors)
    print(color)
    time.sleep(second)