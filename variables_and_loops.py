#!/usr/bin/env python3

import numpy as num #imports numpy library

def main():
	i = 0;		#initializes first integer variable
	j = 10;		#initializes second integer variable
	x = 119.0;	#initializes float variable

	y = num.zeros(j, dtype = float);	#declares an array of 10 zeroes as floats

	for i in range(j):					#loops through array
		y[i] = 2.0 * float(i) + 1;			#sets current element to 2i + 1 as a float

	for y_element in y:		#iterates through array
		print(y_element);		#prints current element

if __name__ == "__main__":	#runs main function
	main();