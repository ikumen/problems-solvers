#!/usr/bin/env python

'''
015.py: https://projecteuler.net/problem=15

Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''
import os
import pytest
import time


def find_num_of_paths(w, h):
	'''finds the number of paths through a grid of w x h size. Constraints are,
	you can only move right to down. Starting position is [0][0], ending at [w][h].'''
	if w <= 0 or h <= 0:
		return 0

	matrix = [[1]*(w+1) for i in range(h+1)]
	for n in range(w+1):
		for m in range(h+1):
			if m == 0 and n == 0:
				pass
			elif n-1 < 0:
				matrix[n][m] = matrix[n][m-1]
			elif m-1 < 0:
				matrix[n][m] = matrix[n-1][m]
			else:
				matrix[n][m] = (matrix[n-1][m] + matrix[n][m-1])
	return matrix[w][h]


def test_find_num_of_paths():
	'''Test'''
	assert 2 == find_num_of_paths(1, 1)
	assert 6 == find_num_of_paths(2,2)
	assert 0 == find_num_of_paths(0, 0)


def main():
	'''Main runner, delegates to solution.'''
	print(find_num_of_paths(20, 20))


if __name__ == '__main__':
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
