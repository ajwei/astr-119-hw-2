#!/usr/bin/env python3

arr = [0.0, 3.0, 5.0, 2.5, 3.7];	#declares an array
print(type(arr));					#prints the data type of arr

arr.pop(2);			#removes the third element of arr
print(arr);			#prints the contents of arr

arr.remove(2.5);	#removes the element equivalent to 2.5
print(arr);			#prints the contents of arr

arr.append(1.2);	#adds 1.2 to the end of arr
print(arr);			#prints the contents of arr

arr_copy = arr.copy();		#makes a copy of arr
print(arr_copy);			#prints the contents of arr_copy

print(arr_copy.count(0.0));	#prints the number of elements in arr_copy equal to 0.0

print(arr_copy.index(3.7));	#prints the index of arr_copy with the value 3.7

arr_copy.sort();	#sorts arr_copy so that its contents are in numerical order
print(arr_copy);	#prints the contents of arr_copy

arr_copy.reverse();	#reverses the order of arr_copy's contents
print(arr_copy);	#prints the contents of arr_copy

arr_copy.clear();	#erases all content in arr_copy
print(arr_copy);	#prints the contents of arr_copy