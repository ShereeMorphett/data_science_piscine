# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smorphet <smorphet@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 13:11:03 by smorphet          #+#    #+#              #
#    Updated: 2024/06/10 14:16:44 by smorphet         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# This time you have to make a real autonomous program, with a main, which takes
# a single string argument and displays the sums of its upper-case characters, lower-case
# characters, punctuation characters, digits and spaces.
# • If None or nothing is provided, the user is prompted to provide a string.
# • If more than one argument is provided to the program, print an AssertionError.

# $>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backwardcompatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 8 punctuation marks
# 25 spaces
# 15 digits
# (the carriage return counts as a space, if you don’t want to return
# one use ctrl + D)
# $>python building.py
# What is the text to count?
# Hello World!
# The text contains 13 characters:
# 2 upper letters
# 8 lower letters
# 1 punctuation marks
# 2 spaces
# 0 digits
# $>

import sys

def pr_light_purple(skk): print("\033[94m{}\033[00m" .format(skk))
def pr_cyan(skk): print("\033[96m{}\033[00m" .format(skk))
def pr_purple(skk): print("\033[95m{}\033[00m" .format(skk))
def pr_green(skk): print("\033[92m{}\033[00m" .format(skk))

def create_data(user_input):
    """Takes the string and creates a data output

    Parameters:
    arg1 (str): Takes the user input

    Returns: Outputs the results to console"""  
    uppercase = 0
    lowercase = 0
    punctuation_marks = 0
    whitespace = 0
    digit = 0
    
    for i in user_input:
        if i.isdigit():
            digit += 1
        elif i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
        elif i.isspace():
            whitespace += 1
        else:
            punctuation_marks += 1


    print(f"The text contains {len(user_input)} characters:")
    print(f"{uppercase} upper letters\n{lowercase} lower letters\n{punctuation_marks} punctuation marks\n{whitespace} spaces\n{digit} digits")


def main():
# your tests and your error handling

    """_summary_
        Takes user input from either the command line or prompts for user input if none is give at program execution.
        calls create_data() and runs basic test for create_data function

    Raises:
        AssertionError: Raises assertion if the user input is incorrect
    """
    try:
        try:
            if len(sys.argv) == 1:
                user_input = input("What is the text to count?  ")
                user_input += '\r'
            else:
                user_input = sys.argv[1]
        except EOFError:
            raise AssertionError("Incorrect input")
            
        assert len(user_input) >= 1, "Incorrect input"
        
        # print(create_data.__doc__)
    except AssertionError as msg: 
        print(msg)
    
    pr_green("\nStarting testing\n")
    user_input =  "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
    
    pr_cyan(user_input)
    pr_light_purple("Expected Output: \n")
    pr_cyan("The text contains 171 characters:\n2 upper letters\n121 lower letters\n8 punctuation marks\n25 spaces\n15 digits\n")
    create_data(user_input)
    # print(main.__doc__)
    # print(create_data.__doc__)
    
    



if __name__ == "__main__":
    main()
