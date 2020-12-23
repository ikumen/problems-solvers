import os

def get_data_file_path(filepath):
	return os.path.join(
		os.path.dirname(filepath),
		f"{os.path.splitext(os.path.basename(filepath))[0]}.txt")
