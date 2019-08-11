def getinteger():
    return int(input("Enter a number : "))

def primeornot(x):
    if x<=1:
        return False
    for i in range(2, x-1):
        if x%i==0:
            return False
    return True

n = getinteger()
result = primeornot(n)
if result == True:
    print("It is a prime number.")
else:
    print("It is not a prime number.")
