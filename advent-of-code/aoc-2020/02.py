import os
import helpers

def _parse_policy(policy):
	mnmx, char = policy.split(' ')
	mn, mx = [int(n) for n in mnmx.split('-')]
	return mn, mx, char

def is_valid_passwords(policy, password):
	mn, mx, char = _parse_policy(policy)
	cnt = password.count(char)
	return cnt <= mx and cnt >= mn
	# cnt = 0
	# for c in password:
	# 	if c == char:
	# 		cnt += 1
	# 	if cnt > mx:
	# 		return False
	# return cnt >= mn

def is_valid_password_part2(policy, password):
	i, k, char = _parse_policy(policy)
	truths = 0
	if password[i-1] == char:
		truths += 1
	if k <= len(password) and password[k-1] == char:
		truths += 1
	return truths == 1

def main():	
	with open(helpers.get_data_file_path(__file__)) as reader:
		valid_cnt = 0
		valid_cnt2 = 0
		for line in reader.readlines():
			policy, password = line.split(":")
			password = password.strip()
			if is_valid_passwords(policy, password):
				valid_cnt += 1
			if is_valid_password_part2(policy, password):
				valid_cnt2 += 1

		print(valid_cnt)
		print(valid_cnt2)


if __name__ == "__main__":
	main()
