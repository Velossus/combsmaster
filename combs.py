import hashlib
import logging
from string import digits, ascii_letters
from itertools import product

def main(): #made into function for ease of termination
	logging.basicConfig(filename="logfilename.log", level=logging.INFO)
	chars = digits + ascii_letters

	match = '0badbeef'

	for n in range(1, 20): #I don't think it'll ever hit 62^20 honestly
		for comb in product(chars, repeat=n):
			testing = ''.join(comb) + "d470d406"
			hash = hashlib.md5(testing.encode('ascii')).hexdigest()
			if match in hash:
				logging.info('Match:' + testing + ', md5:' + hash)
				return 0; 
			#print(testing) #can be added back for testing

main()
