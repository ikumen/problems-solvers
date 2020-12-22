#!/usr/bin/env python

'''
014.py: https://projecteuler.net/problem=14

Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 
terms. Although it has not been proved yet (Collatz Problem), it is thought that 
all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import os
import pytest
import time

chains = {}

def longest_collatz(n):
	start_num = 0
	longest_chain = 0
	for i in range(n):
		chain_len = compute_chain(i)
		if longest_chain < chain_len:
			longest_chain = chain_len
			start_num = i
	return start_num

def compute_chain(n):
	k = n
	count = 1
	while k > 1:
		if k % 2 == 0:
			k = k / 2
		else:
			k = (3 * k) + 1
		if k in chains:
			chains[n] = count + chains[k]
			return chains[n]
		count += 1
		
	chains[n] = count
	return count



def test_solution():
	'''Test'''
	num_with_longest_chain = longest_collatz(13)
	assert 9 == num_with_longest_chain


def main():
	'''Main runner, delegates to solution.'''
	n = 999999
	print(longest_collatz(n))

if __name__ == '__main__':
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
