
"""
TITLE - Assignment 1: Bouncy Ball

This python script accepts values for an initial height,
a minimum height, and a bouncieness coefficient.
It then returns the number of bounces completed above the
minimum height, and the time elapsed.

Lewis Zigante 27/10/2020
"""
import sys
ACCELERATION = 9.81


def height_calculation(start_height, min_height, bounce_coefficient):
    """
    Calculates the number of bounces above a given minimum height
    and the time taken to complete these bounces

    Parameters
    ----------
    start_height : float
    The height the ball begins at

    min_height : float
    The minimum height the ball must reach
    for the bounce to be counted

    bounce_coefficient : float
    The fraction of energy lost with
    each bounce (the efficiency)
    ----------
    Returns the number of bounces and the time taken
    """
    new_height = start_height
    time = 0
    exponent = 1
    bounces = 0
    time_initial = (2 * new_height / ACCELERATION) ** 0.5
    while new_height > min_height:
        time += time_calculation(new_height)
        new_height = start_height * bounce_coefficient ** exponent
        bounces += 1
        exponent += 1

    bounces = bounces - 1
    time = time - time_initial
    return (bounces, time)


def time_calculation(new_height):
    """
    Calculates the time for each bounce

    Parameters
    ----------
    new_height : float
    The height of the ball for this iteration
    ----------
    Returns the time for this height
    """
    time_add = 2 * (2 * new_height / ACCELERATION) ** 0.5
    return time_add


def input_check(start_height, height_min, bounciness_coefficient):
    """
    Checks if user's inputs are correct. If they are invalid,
    the code is terminated

    Parameters
    ----------
    start_height : float
    The height the ball begins at

    height_min : float
    The minimum height the ball must reach
    for the bounce to be counted

    bounciness_coefficient : float
    The fraction of energy lost with
    each bounce (the efficiency)
    -------
    """



    if start_height <= 0 or height_min <= 0:
        print('---INVALID INPUT---')
        print('Start height and minimum height must be greater than 0')

    elif start_height <= height_min:
        print('---INVALID INPUT---')
        print('Minimum height must be less than start height')

    elif bounciness_coefficient <= 0 or bounciness_coefficient >= 1:
        print('---INVALID INPUT---')
        print('Bounciness coefficient must be between 0 and 1')

    else:
        return None

    sys.exit()


START_HEIGHT = input("Enter the starting height: ")
HEIGHT_MIN = input("Enter the minimum height: ")
BOUNCINESS_COEFFICIENT = (input("Enter the coefficient for the "
                                "bounciness (between 0 and 1): "))
try:
    START_HEIGHT = float(START_HEIGHT)
    HEIGHT_MIN = float(HEIGHT_MIN)
    BOUNCINESS_COEFFICIENT = float(BOUNCINESS_COEFFICIENT)

except ValueError:
    print('---INVALID INPUT(S)---')
    print('Inputs must be float')
    sys.exit()

input_check(START_HEIGHT, HEIGHT_MIN, BOUNCINESS_COEFFICIENT)

BOUNCES, TIME = height_calculation(START_HEIGHT, HEIGHT_MIN, BOUNCINESS_COEFFICIENT)
print("Number of bounces completed =", BOUNCES)
print("Time elapsed = {0:.2f} seconds".format(TIME))
