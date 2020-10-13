#!/usr/bin/env python3

def main():
	i = 0;					#initializes integer variable
	x = 119.0;				#initializes float variable

	for i in range(120):	#loops i from 0 to 119, inclusive
		if((i % 2) == 0):	#if i is even
			x += 3;				#increments x by 3
		else:				#else if i is odd
			x -= 5;				#decrements x by 5

	st = "%3.2e" % x;		#initializes string variable containing x with scientific notation to two decimal places
	print(st);				#prints st

if __name__ == "__main__":	#runs main function if it exists
	main();