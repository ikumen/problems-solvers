#!/usr/bin/env python

'''
006.py: https://projecteuler.net/problem=6

Sum Square Difference

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''
import os
import pytest


def sum_square_diff(n):
	return _square_of_sums(n) - _sum_of_squares(n)


def _sum_of_squares(n):
	'''Returns the sum of the squares of integers from 1 to n.'''
	if n == 1:
		return n
	elif n > 1:
		return (n * n) + _sum_of_squares(n-1) 


def _square_of_sums(n):
	'''Returns the square of the sum of integers from 1 to n.'''
	sum = 0
	for i in range(1, n+1):
		sum += i
	return sum * sum


def test_sum_square_diff():
	'''Test'''
	assert 2640 == sum_square_diff(10)


def main():
	'''Main runner, delegates to solution.'''
	print(sum_square_diff(100))


if __name__ == '__main__':
	main()