#!/usr/bin/env python

'''
010.py: https://projecteuler.net/problem=10

Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

@see 007.py for brute force attempt at finding nth prime
'''
import os
import pytest
import math


def sum_of_primes(n):
	'''Returns the summation of primes under n.'''
	max_sqrt = math.sqrt(n)
	numbers = [True] * n
	# we use array index to keep track of number, 1 is not 
	# prime but we never test so we manually eliminate here
	numbers[1] = False 

	# build sieve
	for i in range(2, math.ceil(max_sqrt)):
		if numbers[i]:
			for j in range(i+i, n, i):
				numbers[j] = False
	# sum the primes in sieve
	sum = 0
	for i in range(n):
		if numbers[i]:
			sum += i
	return sum


def test_sum_of_primes():
	'''Test'''
	assert 17 == sum_of_primes(10)


def main():
	'''Main runner, delegates to solution.'''
	print(sum_of_primes(2000000))


if __name__ == '__main__':
	main()