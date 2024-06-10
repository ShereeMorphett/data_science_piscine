# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smorphet <smorphet@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:38:00 by smorphet          #+#    #+#              #
#    Updated: 2024/06/10 12:35:00 by smorphet         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



# Create a script that takes a number as argument, checks whether it is odd or even,
# and prints the result.
# If more than one argument is provided or if the argument is not an integer, print an
# AssertionError.
# Expected output:

# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# Assert


import sys


    
try: 
    argc = len(sys.argv)
    assert argc <= 2, "more than one argument is provided"
    assert argc == 2
    
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as msg: 
    print(msg)