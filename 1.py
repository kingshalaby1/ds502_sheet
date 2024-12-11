# Write a Python program that takes an integer as input and prints "Even" if the
# number is even, and "Odd" if the number is odd.


def main():
    num = input("Enter a number to check: ")

    # Check if the input is a number
    if num.isdigit():
        num = int(num)
        if is_even(num):
            print("Even")
        else:
            print("Odd")
    else:
        print("Invalid input. Please enter a valid number.")

def is_even(number):
    
    # if the number is divisible by 2 and the remainder/modulus == 0, it is even
    if number % 2 == 0:
        return True
    else:
        return False


main()