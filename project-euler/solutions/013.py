#!/usr/bin/env python

'''
013.py: https://projecteuler.net/problem=13

Large Sum

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
...
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690

'''
import os
import pytest
import time


def first_ten_digits_of_sum(n, numbers):
	'''Finds the first n digits of the sum of numbers list.'''
	return (str(sum(numbers)))[:10]

def test_first_ten_digits_of_sum():
	'''Test'''
	assert '5537376230' == first_ten_digits_of_sum(10, load_numbers())


def load_numbers():
	with open(os.path.join(os.path.dirname(__file__), 'data/013.txt')) as input:
		return list(map(int, input.readlines()))


def main():
	'''Main runner, delegates to solution.'''
	print(first_ten_digits_of_sum(10, load_numbers()))


if __name__ == '__main__':
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
