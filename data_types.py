#!/usr/bin/env python3

import numpy as num #imports numpy library

i = 10;			#initializes integer variable
print(type(i));	#prints the data type of i

arr_i = num.zeros(i, dtype = int);	#declares an array of 10 zeroes as integers
print(type(arr_i));					#prints the data type of arr_i
print(type(arr_i[0]));				#prints the data type of the first element of arr_i

x = 119.0;		#initializes first float variable
print(type(x));	#prints the data type of x

y = 1.19e2;		#intializes second float variable
print(type(y));	#prints the data type of y

arr_fl = num.zeros(i, dtype = float);	#declares an array of 10 zeroes as floats
print(type(arr_fl));					#prints the data type of arr_fl
print(type(arr_fl[0]));					#prints the data type of the first element of arr_fl