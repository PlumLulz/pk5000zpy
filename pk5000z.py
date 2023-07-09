import argparse

def pk5000z(seed):
	charset = "23456789abcdefghijkmnpqrstuvwxyz"
	password = [None] * 14
	for i in range(0, 14):
		seed = seed * 0x41c64e6d + 0x3039
		l_pos = seed >> 0x10 & 0x1f
		password[i] = charset[l_pos]
	password = "".join(password)
	print(password)


parser = argparse.ArgumentParser(description='PK5000Z Keygen')
parser.add_argument('seed', help='Seed', type=int)
args = parser.parse_args()

pk5000z(args.seed)