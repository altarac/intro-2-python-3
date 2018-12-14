# Challenge 1 solution:
from turtle import *

sides = int(input('How many sides? '))

angle = 360/sides

for i in range(sides):
    forward(100)
    right(angle)



# ------------------------------------------ #


# Challenge 2 solution:
import random

sides = random.randint(3, 10)

angle = 360/sides

for i in range(sides):
    forward(100)
    right(angle)
