#!/usr/bin/env python3

def flow_control(k):	#defines flow control function
	if(k == 0):												#if k equals 0
		st = "Variable k = %d equals 0." % k;					#string states that k equals 0
	elif(k == 1):											#else if k equals 1
		st = "Variable k = %d equals 1." % k;					#string states that k equals 1
	else:													#else if k does not equal 0 or 1
		st = "Variable k = %d does not equal 0 or 1." % k;		#string states that k does not equal 0 or 1

	print(st);	#prints st

def main():
	i = 0;	#initializes integer variable

	flow_control(i);	#calls flow_control function with i as parameter
	i = 1;				#sets i to 1
	flow_control(i);	#calls flow_control function with i as parameter
	i = 2;				#sets i to 2
	flow_control(i);	#calls flow_control function with i as parameter

if __name__ == "__main__":	#runs main function
	main();