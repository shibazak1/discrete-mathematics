
#written for fun during study made to understand euclidean algorithm for computing GCD of tow number
# by the Greate viibug

#in 2024/8/22



def add_recursive(a,b):

    if b==0:
        return a
    else:
        return(1+add_recursive(a,b-1))






a,b = map(int,input("enter a ,b").split())

print(add_recursive(a,b))
