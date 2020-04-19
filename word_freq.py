#!/usr/bin/python
import sys

filename = sys.argv[1]
num = int(sys.argv[2])

count = []
word = []
D = {}

fp = open(filename, 'r')
lines = fp.readlines()
for itr in lines:
	itr = itr.rstrip("\n")
	for words in itr.split(' '):
		words = words.lower()
		if(words in word):
			count[word.index(words)]+=1
		else:
			word.append(words)
			count.append(1)

for i in range(0, len(word)):
	D[word[i]] = count[i]

pt = 0;
for y in sorted(D, reverse = True):
	if(pt==num): break
	print("{:<10}".format(y), end=' ')
	print("{:>10}".format(D[y]))
	pt+=1
