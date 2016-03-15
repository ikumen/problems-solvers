#!/usr/bin/env python

'''
004.py: https://projecteuler.net/problem=4

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import os
import pytest


def largest_palindrom_product(num_digits):
	'''Finds the largest palindromic product of numbers of num_digits long.'''
	# create list of all numbers that are num_digits in length
	numbers = _create_n_digit_numbers(num_digits)
	largest = 0
	# get product of every number vs other numbers
	for i in numbers:
		for j in numbers:
			n = i * j
			if _isPalindromic(n):
				# keep track of largest palindromic number
				largest = max(largest, n)
	return largest


def _isPalindromic(n):
	'''Checks if number n is palindromic. First convert number to 
	string then checks if it's equal to reversed.'''
	s = str(n)
	s_len = len(s)
	i = 0
	# only need to check half way
	while i < s_len / 2:
		if s[i] != s[s_len-i-1]:
			return False
		i += 1
	return True


def _create_n_digit_numbers(n):
	'''Helper for creating a list of numbers that a n digits in length.'''
	numbers = []
	start = int('1' + ('0' * (n-1)))
	for d in range(start, start * 10):
		numbers.append(d)
	return numbers


def test_largest_palindrom_product():
	'''Test'''
	assert 9009 == largest_palindrom_product(2)


def main():
	'''Main runner, delegates to solution.'''
	print(largest_palindrom_product(3))


if __name__ == '__main__':
	main()