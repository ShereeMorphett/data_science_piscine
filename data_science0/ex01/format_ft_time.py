import time
from datetime import date

today = date.today()

seconds_since = time.time()
print(f"Seconds since January 1, 1970: {seconds_since:,}")
print(f"or {seconds_since:.2E} in scientific notation.")
print(today.strftime("%B %d %Y"))
