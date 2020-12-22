#!/usr/bin/env python
import os


def build_path(basedir, file_name):
	return os.path.join(os.path.dirname(basedir), file_name)


def load_matrix(path):
	grid = []
	with open(path) as input:
		for line in input.readlines():
			grid.append(list(map(int, line.strip().split())))
	return grid