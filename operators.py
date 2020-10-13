#!/usr/bin/env python3

i = 9;	#initializes first integer variable
j = 3;	#initializes second integer variable

print(i + j);	#prints sum of i and j
print(i - j);	#prints j subtracted from i
print(i * j);	#prints i multiplied by j
print(i / j);	#prints i divided by j
print(i % j);	#prints the remainder of i divided by j
print(i ** j);	#prints i to the power of j

i = 9.191823;
print(i // j);	#prints i divided by j (floor division)

i = 9;		#sets i to 9
i += 3;		#increments i by 3
print(i);
i = 9;		#sets i to 9
i -= 3;		#decrements i by 3
print(i);
i *= 3;		#multiplies i by 3
print(i);
i /= 3;		#divides i by 3
print(i);
i **= 3;	#raises i to the power of 3
print(i);

i = 9;			#sets i to 9
j = 3;			#sets j to 3
print(i == j);	#true if i equals j, false otherwise
print(i != j);	#true if i does not equal j, false otherwise
print(i > j);	#true if i is greater than j, false otherwise
print(i < j);	#true if i is less than j, false otherwise
print(i >= j);	#true if i is greater than or equal to j, false otherwise
print(i <= j);	#true if i is less than or equal to j, false otherwise