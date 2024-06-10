# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smorphet <smorphet@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:58:05 by smorphet          #+#    #+#              #
#    Updated: 2024/06/10 11:33:10 by smorphet         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# $>python tester.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>



def NULL_not_found(object) -> int:
    null_types = {
        'Nothing': None,
        'Garlic': float('NaN'),
        'Zero': 0,
        'Empty': '',
        'Fake': False
    }
    
    for name, value in null_types.items():
        if object is value or (isinstance(object, float) and isinstance(value, float) and str(object) == str(value)):
            print(f"{name}: {value} {type(object)}")
            return 0
    
    print("Type not Found")
    return 1