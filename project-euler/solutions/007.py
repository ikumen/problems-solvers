#!/usr/bin/env python

'''
007.py: https://projecteuler.net/problem=7

10001st Prime Number

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can 
see that the 6th prime is 13.

What is the 10001st prime number?
'''
import os
import pytest


def find_nth_prime(nth_prime):
	# keep list of primes, initialize with first prime
	primes = [2]
	# we only care about odds numbers, as all even 
	# are divisble by our first prime
	number = 3
	while len(primes) < nth_prime:
		isPrime = True
		for prime in primes:
			if number % prime == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(number)
		# check only odd numbers
		number += 2
	# nth prime was last added prime
	return primes[-1]


def test_find_nth_prime():
	'''Test'''
	assert 13 == find_nth_prime(6)
	assert 2 == find_nth_prime(1)
	assert 3 == find_nth_prime(2)


def main():
	'''Main runner, delegates to solution.'''
	print(find_nth_prime(10001))


if __name__ == '__main__':
	main()