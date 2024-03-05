a = int(input("Enter the number to check whether it's a prime number or not: "))

# Entered number is greate than one or not
if a > 1:
    # Checking for factors
    for i in range(2, a):
        if (a % i) == 0:
            print(a, "is not a prime number.")
            break
    else:
        print(a, "is a prime number.")
else:
    print(a, "is not a prime number.")


