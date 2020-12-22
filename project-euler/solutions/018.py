#!/usr/bin/env python

'''
018.py: https://projecteuler.net/problem=18

Maximum Path Sum I

By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                     75
                    95 64
                  17 47 82
                 18 35 87 10
               20 04 82 47 65
              19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
         41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
      53 71 44 65 25 43 91 52 97 51 14
     70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by 
trying every route. However, Problem 67, is the same challenge with a triangle 
containing one-hundred rows; it cannot be solved by brute force, and requires 
a clever method! ;o)
'''
import os
import pytest
import time

from helpers import load_matrix, build_path


def max_path_sum(tree):
	'''Finds the max total for path through given tree. NOTE: tree is in the 
	form of a 2d matrix (with no padding).'''
	return _collapse_tree(tree, len(tree)-1)


def _collapse_tree(t, l):
	'''Starts at the bottom of tree and collapses tree by solving
	the bottom most sub-trees.''' 
	if l == 0:
		return t[l][0]
	else:
		for i in range(l):
			t[l-1][i] = t[l-1][i] + max(t[l][i], t[l][i+1])
		return _collapse_tree(t, l-1)


def test_max_path_sum():
	'''Test'''
	tree = load_data_file('data/018b.txt')
	assert 23 == max_path_sum(tree)	
	tree = load_data_file('data/067.txt')
	assert 7273 == max_path_sum(tree)


def load_data_file(file_name):
	tree = []
	with open(os.path.join(os.path.dirname(__file__), file_name)) as input:
		for line in input.readlines():
			tree.append(list(map(int, line.strip().split())))
	return tree	


def main():
	'''Main runner, delegates to solution.'''
	#tree = load_data_file('data/018.txt')
	tree = load_matrix(build_path(__file__, 'data/018.txt'))
	print(max_path_sum(tree))


if __name__ == '__main__':
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
