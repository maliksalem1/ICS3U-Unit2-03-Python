#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Sept 2022
# This program calculates the circumference of a circle
# with user input


import constants


def main():
    # This function calculates circumference

    # Input
    radius = int(input("Enter radius of the circle (mm): "))

    # Process
    circumference = constants.TAU * radius

    # Output
    print("Circumference is {} mm2.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
