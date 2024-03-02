# Program to display the Fibonacci sequence up to n-th term
range = int(input("How many terms? "))
# n1 and n2 are first two terms
n1, n2, n3 = 0, 1, 0
count = 0
# Checking the range is valid or not
if range <= 0:
   print("Please enter a positive integer")
# If the range is 1 then print n1
elif range == 1:
   print("Fibonacci sequence upto",range,":")
   print(n1)
# Generating Fibonacci Series
else:
   print("Fibonacci sequence:")
   while count < range:
       print(n1,end=" ")
       n3 = n1 + n2
       # update values
       n1 = n2
       n2 = n3
       count += 1