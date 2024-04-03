"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()





def jump():
    """"
    pre-condition:Karel is on the left side of the wall,facing South.
    post-condition: Karel is facing North

    turn_left()
    #facing North
    while not front_is_clear():
        move()
    """
    up()
    cross()
    down()

def up():
    """"
    Pre-condition:Karel is at the upper right,facing South
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()


def cross():
    """
    Pre-condition:Karel is facing North
    Post-condition:Karel is at the upper right,facing South
    """
    move()
    turn_right()


def down():
    while front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
