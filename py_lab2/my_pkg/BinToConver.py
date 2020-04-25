#!/usr/bin/python

def conBin(bin):
	num=0
	size=len(bin)-1
	for i in range(0,size):
		if(bin[i]=='1'): num+= 2**(size-i)
	if(size==0):
		if(bin[size]=='1'): num = 1
	return(num)
def OCT(num):
	print("=>OCT> %0o" %(num))
def DEC(num):
	print("=>DEC> ", num)
def HEX(num):
	print("=>HEX> %X" %(num))

def base():
	bin=input("input binary number :")
	num = conBin(bin)
	OCT(num)
	DEC(num)
	HEX(num)
