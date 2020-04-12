#!/usr/bin/python

numN = int(input("How many numbers will you enter?"))
sum = 0

print("Input num")

num = [int(x)for x in input().split()]

for i in range(0,numN):
	sum = num[i] + sum

total = sum/numN

print("Average : ", total)

