#!/usr/bin/env python3

try:							#attempts the following line
	print(a);						#prints a
except:							#if exception is thrown
	print("a is not defined!");		#prints error message

try:										#attempts the following line
	print(a);									#prints a
except NameError:							#if a NameError exception is thrown
	print("a is still not defined!");			#prints error message
except:										#if another exception is thrown
	print("Something else went wrong.");		#prints error message

print(a);	#prints a