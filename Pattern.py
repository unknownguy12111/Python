# Pattern 
def triangle(n):
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces and values change according to the requirements
		for j in range(0, k):
			print(end=" ")
	
		# Decrementing K after every loop
		k = k - 1
	
		# inner loop to handle number of columns and values change according to the outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("*", end=" ")

		print("\r")

# Driver Code
n = int(input("Enter the range: "))
triangle(n)
