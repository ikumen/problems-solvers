#!/usr/bin/env python

'''
005.py: https://projecteuler.net/problem=5

Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all 
of the numbers from 1 to 20?
'''
import os
import pytest


def smallest_multiple(n1, n2):
	'''Returns the smallest positive number that is evenly 
	divisble by all numbers from n1 to n2.'''
	i = 2
	while True:
		# get multiples of n2, then see if all numbers leading up to 
		# n2 evenly divide into the multiple
		multiple = n2 * i
		for n in range(n1, n2):
			if not multiple % n == 0:
				break
			if n == n2 - 1: 
				# numbers up to this point are all multiples
				return multiple
		i += 1


def test_smallest_multiple():
	'''Test'''
	assert 2520 == smallest_multiple(1, 10)

def main():
	'''Main runner, delegates to solution.'''
	print(smallest_multiple(1, 20))


if __name__ == '__main__':
	main()