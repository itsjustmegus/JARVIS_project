"""
    Name: utils.py
    Author: Augustus Allred
    Created: 9/26/22
    Purpose: A utility module with commonly used functions
"""


def title(program_title):
    """
        Takes in a string argument
        returns a string with ascii decorations    
    """
    # Get the length of the statement
    text_length = len(program_title)

    # Create the title string by concantenation

    title_string = "+--" + "-" * text_length + "--+\n"
    title_string = title_string + "|  " + program_title + "  |\n"
    title_string = title_string + "+--" + "-" * text_length + "--+\n"

    return title_string

def get_float(prompt :str):
    """
        Get an float from the user with try catch
        The prompt string parameter is used to ask the user
        for the type of input needed
    """
    # Declare local variable
    num = 0

    # Ask the user for an input based on the prompt string parameter
    num = input(prompt)

    # If the input is numeric, convert to int and return value
    try:
        return float(num)

    # If the input is not numberic,
    # Inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a number.")
        print(f"Let's try that again.\n")

        # Call function from the beginning
        # This is a recursive function call
        return get_float(prompt)