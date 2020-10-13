#!/usr/bin/env python3

dictionary = {						#defines dictionary data structure
	"class"			:	"Astr 119",	
	"prof"			:	"Brant",
	"awesomeness"	:	10
}
print(type(dictionary));			#prints the data type of dictionary

course = dictionary["class"];		#obtains a value from a key in dictionary
print(course);						#prints the value

dictionary["awesomeness"] += 1;		#modifies a value from a key in dictionary

print(dictionary);					#prints dictionary

for x in dictionary.keys():			#for each element in dictionary
	print(x, dictionary[x]);			#prints current element