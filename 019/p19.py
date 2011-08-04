#!/usr/bin/python

import sys

# for the months, we only need to keep number of days mod 7 (for day of the week)
months = [3,0,3,2,3,2,3,3,2,3,2,3]
months_leap = [3,1,3,2,3,2,3,3,2,3,2,3]

def isleap(n):
	if((n%4==0 and n%100!=0) or (n%400 == 0)):
		return 1
	return 0

def main():
	(year, day, i) = (1901, 2, 0)
	while year < 2001:
                day %= 7
		if isleap(year):
			for month in months_leap:
				day += month
				print day
				if day%7 == 0:
					i+=1
		else:
			for month in months:
				day += month
				print day
				if day%7 == 0:
					i+=1
		year+=1
	print i

if __name__ == "__main__":
	main()
