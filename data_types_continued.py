#!/usr/bin/env python3

st = "I am a string.";	#intializes string variable
print(type(st));		#prints the data type of st

y = True;		#initializes true boolean variable
print(type(y));	#prints the data type of y

n = False;		#initializes false boolean variable
print(type(n));	#prints the data type of n

alpha_list = ["a", "b", "c"];	#initializes list
print(type(alpha_list));		#prints the data type of alpha_list
print(type(alpha_list[0]));		#prints the data type of the first element of alpha_list
alpha_list.append("d");			#appends "d" to the end of alpha_list
print(alpha_list);				#prints the contents of alpha_list

alpha_tuple = ("a", "b", "c");	#initializes tuple
print(type(alpha_tuple));		#prints the data type of alpha_tuple

try:											#attempts the following line
	alpha_tuple[2] = "d";							#checks end of alpha_tuple for "d"
except TypeError:								#when a TypeError is received
	print("We can'd add elements to tuples!");		#prints error message
print(alpha_tuple);								#prints the contents of alpha_tuple