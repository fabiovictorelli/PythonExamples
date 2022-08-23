# Python3 program to demonstrate 
# working of Kaprekar constant 

# This function checks validity of 
# kaprekar's constant. It returns 
# kaprekar's constant for any four 
# digit number "n" such that all 
# digits of n are not same. 
def kaprekarRec(n, prev): 

	if (n == 0): 
		return 0; 

	# Store current n as previous 
	# number 
	prev = n; 

	# Get four digits of given number 
	digits = [0] * 4; 
	for i in range(4): 
		digits[i] = n % 10; 
		n = int(n / 10); 

	# Sort all four dgits in ascending order 
	# And giet in the form of number "asc" 
	digits.sort(); 
	asc = 0; 
	for i in range(4): 
		asc = asc * 10 + digits[i]; 

	# Get all four dgits in descending order 
	# in the form of number "desc" 
	digits.sort(); 
	desc = 0; 
	for i in range(3, -1, -1): 
		desc = desc * 10 + digits[i]; 

	# Get the difference of two numbers 
	diff = abs(asc - desc);
	
	# Fabio code
	# print ("fazendo para : %s - %s = %s",desc,asc,diff);
	print('fazendo para = ', desc, '- ', asc , '=' , diff)

	# If difference is same as previous, 
	# we have reached kaprekar's constant 
	if (diff == prev): 
		return diff; 

	# Else recur
	
	return kaprekarRec(diff, prev); 

# A wrapper over kaprekarRec() 
def kaprekar(n): 

	rev = 0; 
	return kaprekarRec(n, rev); 

# Driver code 

# Trying few four digit numbers, 
# we always get 6174 
print(kaprekar(1000)); 
print(kaprekar(1112)); 
print(kaprekar(9812)); 

# This code is contributed by mits. 
