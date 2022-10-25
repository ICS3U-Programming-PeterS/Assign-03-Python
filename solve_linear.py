#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: October 24, 2022
# This program is a linear calculator, it solves linear equations
import os
import time


# ------------------- Functions ------------------------
# function solves for y
def solve_for_y(m, x, b):
    solve_y = m * x + b
    print(
        "The value of y is "
        + str(solve_y)
        + "."
        + "\n"
        + "The equation is y = "
        + str(m)
        + "x + "
        + str(b)
        + "."
        + "\n" * 2
    )


# function solves for y if b is a negative
def solve_for_y2(m, x, b):
    solve_y2 = m * x - b
    print(
        "The value of y is "
        + str(solve_y2)
        + "."
        + "\n"
        + "The equation is y = "
        + str(m)
        + "x - "
        + str(abs(b))
        + "."
        + "\n" * 2
    )


# function solves for x
def solve_for_x(y, b, m):
    solve_x = (y - b) / m
    print(
        "The value of x is "
        + str(solve_x)
        + "."
        + "\n"
        + "The equation is y = "
        + str(m)
        + "x + "
        + str(b)
        + "."
        + "\n" * 2
    )


# function solves for x if b is negative
def solve_for_x2(y, b, m):
    solve_x2 = (y + b) / m
    print(
        "The value of x is "
        + str(solve_x2)
        + "."
        + "\n"
        + "The equation is y = "
        + str(m)
        + "x + "
        + str(abs(b))
        + "."
        + "\n" * 2
    )


# function solves for m
def solve_for_m(y, b, x):
    m = (y - b) / x
    print(
        "The value of m is "
        + str(m)
        + "."
        + "\n"
        + "The equation is y = "
        + str(m)
        + "x + "
        + str(b)
        + "."
        + "\n" * 2
    )


# function solves for m if b is a negative
def solve_for_m2(y, b, x):
    m = (y + b) / x
    print(
        "The value of m is "
        + str(m)
        + "."
        + "\n"
        + "The equation is y = "
        + str(m)
        + "x + "
        + str(abs(b))
        + "."
        + "\n" * 2
    )


# function solves for b
def solve_for_b(y, m, x):
    solve_b = y - (m * x)
    if 0 <= solve_b:
        print(
            "The value of b is "
            + str(solve_b)
            + "."
            + "\n"
            + "The equation is y = "
            + str(m)
            + "x + "
            + str(solve_b)
            + "."
            + "\n" * 2
        )
    else:
        print(
            "The value of b is "
            + str(solve_b)
            + "."
            + "\n"
            + "The equation is y = "
            + str(m)
            + "x - "
            + str(abs(solve_b))
            + "."
            + "\n" * 2
        )


# ------------------- Main ---------------------------
def main():
    # set use again to y
    use_again = "y"

    # make while loop and make it run as long as use again is y
    while use_again == "y":

        # set operation check to false and stop time to display message
        operation_check = False
        os.system("clear")
        print("Welcome to the world's greatest calculator!")
        time.sleep(2.5)

        # while loop that runs as long as operation check is false
        while operation_check == False:
            os.system("clear")

            # display choices to the user
            print("Choose from one of the following options:")
            print(
                "\t [1]"
                " Solve for y -- y=mx+b \n \t [2] Solve for x -- x=(y-b)/m"
                " \n \t"
                + " [3] Solve for m -- m=(y-b)/x \n \t "
                + "[4] Solve for b -- b=y-mx"
            )

            # get operation from user
            operation = input("Enter your selection: ")

            # try to make sure no value or operation other than 1-5 is accepted
            try:
                check = int(operation)
                if check >= 1 and check <= 5:
                    operation_check = True
                else:
                    operation_check = False
            except ValueError:
                operation_check = False

        # select case to determine what code should run
        match check:
            case 1:
                os.system("clear")
                print("******************")
                print("To solve for y, you need m, x and b.")

                # get values for m, x and b
                m_as_a_string = input("Enter a value for m: ")
                x_as_a_string = input("Enter a value for x: ")
                b_as_a_string = input("Enter a value for b: ")

                # try catch to make sure inputs show no errors
                try:
                    m = float(m_as_a_string)
                    x = float(x_as_a_string)
                    b = float(b_as_a_string)

                    # if statement to check if 0 is greater than b
                    if 0 > b:
                        solve_for_y2(m, x, b)
                    else:
                        solve_for_y(m, x, b)
                except TypeError:
                    print("Enter a valid value.")

            # case #2
            case 2:
                os.system("clear")
                print("******************")
                print("To solve for x, you need y, b and m.")

                # Get input for y, b and m
                y_as_a_string = input("Enter a value for y: ")
                b_as_a_string = input("Enter a value for b: ")
                m_as_a_string = input("Enter a value for m: ")

                # try catch to make sure inputs show no errors
                try:
                    y = float(y_as_a_string)
                    b = float(b_as_a_string)
                    m = float(m_as_a_string)

                    # if statement to make sure m = 0 as thats an error
                    if m == 0:
                        print("\nYour m cannot be 0.")
                    else:

                        # if statement to check if b is negative or positive
                        if 0 > b:
                            solve_for_x2(y, b, m)
                        else:
                            solve_for_x(y, b, m)
                except TypeError:
                    print("Enter a valid value.")

            # case #3
            case 3:
                os.system("clear")
                print("******************")
                print("To solve for m, you need y, b and x.")

                # get user input for value y, b and x
                y_as_a_string = input("Enter a value for y: ")
                b_as_a_string = input("Enter a value for b: ")
                x_as_a_string = input("Enter a value for x: ")

                # try catch to make sure values have no errors
                try:
                    y = float(y_as_a_string)
                    b = float(b_as_a_string)
                    x = float(x_as_a_string)

                    # if statement to make sure x doesn't equal 0
                    if x == 0:
                        print("\nYour x cannot be 0.")
                    else:

                        # if statement to check if b is negative or positive
                        if 0 > b:
                            solve_for_m2(y, b, x)
                        else:
                            solve_for_m(y, b, x)
                except TypeError:
                    print("Enter a valid value.")

            # case #4
            case 4:
                os.system("clear")
                print("******************")
                print("To solve for b, you need y, m and x.")

                # get input for values y, m and x
                y_as_a_string = input("Enter a value for y: ")
                m_as_a_string = input("Enter a value for m: ")
                x_as_a_string = input("Enter a value for x: ")

                # Try catch to make sure no errors in values
                try:
                    y = float(y_as_a_string)
                    m = float(m_as_a_string)
                    x = float(x_as_a_string)

                    # function to solve for b
                    solve_for_b(y, m, x)
                except TypeError:
                    print("Enter a valid value.")

        # defining use_again to see if user wants to use again or stop
        use_again = input("\n" * 2 + "Do you want to use it again? (y/n): ")

        # if statement that stops the program if use again != y
        if not use_again == "y":
            os.system("clear")
            print("Mrs. Raffin is the best computer science teacher.")
            break


if __name__ == "__main__":
    main()
