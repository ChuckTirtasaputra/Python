# Binary Sequence without consecutive 1's

def generateAllStringsUtil(num, binary, n):
	# print binary string without consecutive 1's
	if (n == num):
		# terminate binary string
		print(*binary[:n], sep = "", end = "\n") 
		return
	
	# if previous character is '1' then we put only 0 at end of string
	# example str = "01" then new string be "000"
	if (binary[n-1] == '1'):
		binary[n] = '0'
		generateAllStringsUtil (num, binary, n + 1)
		
	# if previous character is '0' than we put both '1' and '0' at end of string
	# example str = "00" then new string "001" and "000"
	if (binary[n-1] == '0'):
		binary[n] = '0'
		generateAllStringsUtil(num, binary, n + 1)
		binary[n] = '1'
		generateAllStringsUtil(num, binary, n + 1)
		
# function generate all binary string without
# consecutive 1's
def generateAllStrings(num):
	
	# Base case
	if (num <= 0):
		return
	
	# One by one stores every
	# binary string of length K
	binary = [0] * num
	
	# Generate all Binary string starts with '0'
	binary[0] = '0'
	generateAllStringsUtil (num, binary, 1)
	
	# Generate all Binary string starts with '1'
	binary[0] = '1'
	generateAllStringsUtil (num, binary, 1)

# num determines the length of the binary number
num = 3
generateAllStrings(num)

'''
# Driver code
x = True

while x == True:
	num = int(input("Number: "))
	generateAllStrings(num)
	conn = input("Continue? (y/n) \n")
	if conn.lower() == "y":
		x = True
	else:
		x = False
'''
