# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smorphet <smorphet@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:17:25 by smorphet          #+#    #+#              #
#    Updated: 2024/06/10 10:17:27 by smorphet         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #




# You need to modify the string of each data object to display the following greetings:
# "Hello World", "Hello «country of your campus»", "Hello «city of your campus»", "Hello
# «name of your campus»"/


ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}



ft_list[1] = "World"

new_list = list(ft_tuple)
new_list[1]= "Finland"
ft_tuple = tuple(new_list)


ft_set.remove("tutu!")
ft_set.add("Helsinki!")

ft_dict["Hello"] = "Hive"



print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)