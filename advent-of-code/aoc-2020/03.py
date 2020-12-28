"""
https://adventofcode.com/2020/day/3

Thoughts:
- just walk through with given slope
- clue is that the repeated pattern is horizontal
- when we get the right edge, just mod to get us to next pattern 
"""
import helpers

def count_trees_in_path(matrix, start, slope):
	"""Given a slice of a larger repeating matrix, and a slope for 
	a path through the matrix, count the number of trees in the path.

	:param matrix: 2D array representing slice of larger matrix
	:param start: tuple of starting position
	:param slope: tuple of run/rise (right and down)
	"""
	trees = 0
	bottom = len(matrix)
	x = start[0] + slope[0]
	y = start[1] + slope[1]
	while y < bottom:
		if matrix[y][x]:
			trees += 1
		x = (x + slope[0]) % len(matrix[y])
		y += slope[1]
	return trees

def main():	
	matrix = []
	with open(helpers.get_data_file_path(__file__)) as reader:
		for line in reader.readlines():
			matrix.append([c == '#' for c in line.strip()])
	print(count_trees_in_path(matrix, [0,0], [3,1]))


if __name__ == "__main__":
	main()

