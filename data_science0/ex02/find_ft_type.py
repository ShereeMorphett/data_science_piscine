# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smorphet <smorphet@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:31:42 by smorphet          #+#    #+#              #
#    Updated: 2024/06/10 10:56:47 by smorphet         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Write a function that prints the object types and returns 42.
# $>python tester.py | cat -e
# List : <class 'list'>$
# Tuple : <class 'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# Brian is in the kitchen : <class 'str'>$
# Toto is in the kitchen : <class 'str'>$
# Type not found$
# 42$
# $>


def all_thing_is_obj(object: any) -> int:
    if type(object) is list:
        print(f"List : {type(object)}")
    elif type(object) is tuple:
        print(f"Tuple : {type(object)}")
    elif type(object) is set:
        print(f"Set : {type(object)}")
    elif type(object) is dict:
        print(f"Dict : {type(object)}")
    elif type(object) is str:
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42