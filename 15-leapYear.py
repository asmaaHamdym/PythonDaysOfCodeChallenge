# Create a program that checks if a year is a leap year
import re

while True:
    year = input('Enter the year you want to check: ').strip()
    if re.match(r"^\d{4}$", year) and 1 <= int(year) <= 9999:
        break
    print("This is not valid year!")
    
if (int(year) % 4) == 0:
    print(f"Current year {year} is a leap year")
else:
    print(f"Current year {year} is a not leap year")
