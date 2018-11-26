#!/bin/python3
#### Task #####
# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February. 
# In the Gregorian calendar three criteria must be taken into account to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
# Source: https://www.timeanddate.com/date/leapyear.html

class HackerRank():
    def check_leapyear(self, year):
        self.year = year

        return ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0))

def main():
    year = int(input())

    hkr_inst = HackerRank()
    print(hkr_inst.check_leapyear(year))

if __name__ == '__main__':
    main()