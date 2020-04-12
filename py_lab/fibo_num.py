#!/usr/bin/python

n = int(input("Enter the number of Fibonacci to generate : "))

fibo = [1,1]

for i in range(2, n):
	fibo.append(fibo[i-1]+fibo[i-2])

print(fibo)
print("F",n," = ",fibo[n-1], sep='')
