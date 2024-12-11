# Write a Python program that takes a string as input and checks if it is a
# palindrome. If it is, the program should print "Palindrome", and if it is not, the
# program should print "Not a Palindrome".


# Palindrome means the string reads the same forwards and backwards. For example, "racecar" is a palindrome.
# To check if a string is a palindrome, we can compare the string to its reverse. If the string is equal to its reverse, it is a palindrome.

def main():
    string = input("Enter a string to check if it is a palindrome: ")

    # Check if the input is a string
    if string.isalpha():
        if is_palindrome(string):
            print("Palindrome")
        else:
            print("Not a Palindrome")
    else:
        print("Invalid input. Please enter a valid string.")


def is_palindrome(string):
    # reverse the string
    reverse = string[::-1]
    print("reverse is: " + reverse)
    if string == reverse:
        return True
    else:
        return False


main()