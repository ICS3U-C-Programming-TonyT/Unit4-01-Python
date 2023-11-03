#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Nov. 3, 2023
# This program will give you the sum of your number.


def main():
    user_num = str(input("Give me a number:\n"))
    try:
        user_num = int(user_num)
    except ValueError:
        print(f"{user_num} is invalid")
    else:
        if user_num < 0:
            print(f"{user_num} has to be positive.")
        else:
            sum = 0
            counter = 0
            while user_num >= counter:
                sum = sum + counter
                counter = counter + 1
                print(f"Has loop'd {counter} times")
            print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
