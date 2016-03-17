#!/usr/bin/env python

'''
009.py: https://projecteuler.net/problem=9

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import os
import pytest

from math import ceil


def find_pythagorean_triplet(x):
	'''Finds the Pythagorean triplet where a + b + c = 1000, returns their product.'''
	for a in range(1, ceil(x/3)):
		for b in range(a, ceil(x/2)):
			c = x - a - b
			if (pow(a, 2) + pow(b, 2)) == pow(c, 2):
				return a * b * c
	return -1


def test_find_pythagorean_triplet():
	'''Test'''
	assert 60 == find_pythagorean_triplet(12) # a=3, b=4, c=5


def main():
	'''Main runner, delegates to solution.'''
	print(find_pythagorean_triplet(1000))


if __name__ == '__main__':
	main()