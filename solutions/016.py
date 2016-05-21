#!/usr/bin/env python

'''
016.py: https://projecteuler.net/problem=16

Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
import os
import pytest
import time
import math


def power_digit_sum(N, P):
	"""
	Calculates the sum of digits for a number 'N' raise to power 'P'. Basic
	algorithm is to apply long multiplication, storing the results in two
	arrays, one for current digits, and other a tmp. 

	N must be between 2 <= N <= 9
	"""
	# To calculate the size of the array that can hold all our digits, I used
	# the following formula (P * Log10(N))
	if N > 9 or N < 2 or P < 1:
		return None

	d_size = math.ceil(P * math.log(N, 10))
	digits = [None] * d_size
	tmp_digits = [None] * d_size

	# Set our ones column for long multiplication, and assign our first value
	ones_place = d_size - 1
	digits[ones_place] = N

	# Multiply N P-1 times, since we set our initial N in ones_place
	for i in range(1, P):
		j = ones_place
		carry = 0
		while digits[j] != None and j >= 0:
			product = carry + (digits[j] * N)
			if product >= 10:
				tmp_digits[j] = product % 10
				carry = math.floor(product / 10)
				tmp_digits[j-1] = carry
			else:
				tmp_digits[j] = product
				carry = 0
			j -= 1

		tmp = digits
		digits = tmp_digits
		tmp_digits = tmp

	return sum(filter(None, digits))


def test_solution():
	'''Test'''
	assert 25 == power_digit_sum(5, 8)
	assert 26 == power_digit_sum(2, 15)

def main():
	'''Main runner, delegates to solution.'''
	#4,782,969
	# 5, 3, 1, 4, 4, 1
	print(power_digit_sum(2, 1000))


if __name__ == '__main__':
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
