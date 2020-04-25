#!/usr/bin/python

def setBase():
	s1=set()
	s2=set()

	l1 = input("1st list : ")

	for i in l1.split(','):
		i=i.replace(" ", "")
		i=i.lstrip('[')
		i=i.rstrip(']')
		if(i.isdecimal()): s1.add(int(i))
	
	l2 = input("2nd list : ")
	for i in l2.split(','):
		i=i.replace(" ", "")
		i=i.lstrip('[')
		i=i.rstrip(']')
		if(i.isdecimal()): s2.add(int(i))

	uni=list(s1.union(s2))
	uni.sort()
	ins=list(s1.intersection(s2))
	ins.sort()

	print("=>Union ", uni)
	print("=>intersection ", ins)
