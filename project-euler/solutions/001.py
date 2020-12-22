#!/usr/bin/env python

'''
001.py: https://projecteuler.net/problem=1

Multiples of 3 and 5 

If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
import os
import pytest


def sum_of_multiples(n):
	sum = 0
	for i in range(1, n):
		if (i % 3 == 0) or (i % 5 == 0):
			sum += i
	return sum

def test_sum_of_multiples():
	'''Test'''
	assert 23 == sum_of_multiples(10)


def main():
	'''Main runner, delegates to solution.'''
	print(sum_of_multiples(1000))


if __name__ == '__main__':
	main()