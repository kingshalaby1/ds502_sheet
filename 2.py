# Write a Python program that takes two integers as input and prints the larger
# of the two numbers.

def main():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Check if the input is a number
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        if num1 == num2:
            print("The numbers are equal.")
        else:
            larger = compare(num1, num2)
            print("The larger number is: ", larger)
    else:
        print("Invalid input. Please enter valid numbers.")


def compare(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


main()