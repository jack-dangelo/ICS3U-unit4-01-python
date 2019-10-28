#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: October 2019
# This program adds user number input from 0


def main():
    # this program adds user number from 0
    # asks user again if input is invalid
    while True:
        try:
            # list to add numbers from counter
            numbers = []

            # increments until number reaches input
            loop_counter = 0

            # input
            integer = int(input("Please enter a number: "))
            print()

            # process
            while loop_counter <= integer:
                numbers.append(loop_counter)
                loop_counter += 1

            # output
            print(sum(numbers))

        # prevents crash of input is invalid
        except ValueError:
            print()
            print("Invalid Number")
            print()
            continue

        # breaks out of loop
        else:
            break


if __name__ == "__main__":
    main()
