"""
https://adventofcode.com/2020/day/3

Thoughts:
- just walk through with given slope
- clue is that the repeated pattern is horizontal
- when we get the right edge, just mod to get us to next pattern 
"""
import helpers

def main():	
	matrix = []
	with open(helpers.get_data_file_path(__file__)) as reader:
		for line in reader.readlines():
			matrix.append([c == '#' for c in line.strip()])
	print(matrix)


if __name__ == "__main__":
	main()

