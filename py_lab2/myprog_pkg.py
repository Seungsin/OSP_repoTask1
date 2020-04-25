#!/usr/bin/python
import my_pkg 

if __name__=='__main__':
	menu='1'
	while(menu != '3'):
		menu=input("Select menu : 1)conversion 2)union/intersection 3) exit ? ")
		if(menu == '1'): my_pkg.base()
		elif(menu == '2'): my_pkg.setBase()
		elif(menu == '3'): print("Exit the program...")
		else : print("You entered the wrong menu No.")
	exit()
