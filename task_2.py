"""
Task 2: Palindrome Checker
"""

from collections import deque

def is_palindrome(input_string):
    """
    Check if the given string is a palindrome.
    """

    input_string = input_string.lower().replace(" ", "")
    string_deque = deque(input_string)

    while len(string_deque) > 1:
        if string_deque.popleft() != string_deque.pop():
            print(f"The line is not a palindrome : {input_string}")
            return False
    print(f"The line is a palindrome : {input_string}")
    return True


def main():
    """
    Main function to handle user input and check for palindrome.
    """
    user_input = input("Enter your line here: ")
    is_palindrome(user_input)

if __name__ == "__main__":
    main()
