#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: April 2021
# This program calculates the area and perimeter of a circle
#    with radius inputted from the user

import math


def main():
    # this function calculates the area and perimeter of a circle

    # input
    radius_of_circle = int(input("Enter radius of a circle (mm): "))

    # process
    area_of_circle = math.pi * radius_of_circle ** 2
    perimeter_of_circle = 2 * math.pi * radius_of_circle

    # output
    print("")
    print("Area is {0} mm².".format(area_of_circle))
    print("Perimeter is {0} mm.".format(perimeter_of_circle))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
