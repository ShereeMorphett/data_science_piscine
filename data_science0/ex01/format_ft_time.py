# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smorphet <smorphet@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:17:15 by smorphet          #+#    #+#              #
#    Updated: 2024/06/10 10:35:57 by smorphet         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #




# Allowed functions : time, datetime or any other library that allows to
# receive the date
# Write a script that formats the dates this way, of course your date will not be mine
# as in the example but it must be formatted the same.
# Expected output:
# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $

import time
from datetime import date

today = date.today()


seconds_since = time.time()


print(f"Seconds since January 1, 1970: {seconds_since:,} or {seconds_since:.2E} in scientific notation.")
print(today.strftime("%B %d %Y"))