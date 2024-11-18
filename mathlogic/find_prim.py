# check what a gavin number is prime

def is_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


for n in range(100):
    if not is_prime(n**2 +n +41):
        print(n)
        exit()
