# find smallest  counterexample for ((2)^2)^n +1  for n>=0 is prime

def is_prime(n):

    for i in range(2,n):
        return n%i !=0
    

    



def cal():
    l = [30,60,90]
    for i in l:
        print(i)
        for n in range(i,i+1):
            if is_prime(2**2**n +1):
                pass
            else:
                print(n)
    



    
    
