#!/usr/bin/env python3

import numpy as num #imports numpy library
import sys			#imports sys library

def power(x):			#defines exponent function
	return num.exp(x);	#returns e^x

def print_power(n):				#defines print function
	for i in range(n):			#loops from 0 to n - 1
		print(power(float(i)));		#prints result of power function with i as parameter

def main():
	n = 10;	#initializes n to 10

	if(len(sys.argv) > 1):		#checks if a command line argument is provided
		n = int(sys.argv[1]);		#if so, uses argument for n

	print_power(n);	#calls print_power function with n as parameter

if __name__ == "__main__":	#runs main function
	main();