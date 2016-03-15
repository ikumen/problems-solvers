#!/usr/bin/env python

'''
003.py: https://projecteuler.net/problem=3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import os
import pytest


def largest_prime_factor(n):
	largest = 0
	factor = 2
	while n > 1:
		while n % factor == 0:
			largest = max(largest, factor)
			n /= factor
		factor += 1
	return largest

def test_largest_prime_factor():
	'''Test'''
	assert 29 == largest_prime_factor(13195)

def main():
	'''Main runner, delegates to solution.'''
	print(largest_prime_factor(600851475143))


if __name__ == '__main__':
	main()