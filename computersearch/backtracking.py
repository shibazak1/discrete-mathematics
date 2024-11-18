
def can_be_extend(perm):
    print(perm)
    i = len(perm)-1
    print(i)
    return all(abs(i-j)!= abs(perm[i]-perm[j]) for j in range(i))


def extend(perm,n):
    if len(perm)==n:
        print(perm)
        return
    print("this for of extend {}".format(perm))
    for i in range(n):
        print("iteration number {} call with {}".format(i,perm+[i]))
        extend(perm+[i],n)


def extend2(perm,n):
    if len(perm)==n:
        print(perm)
        exit()
    for i in range(n):
        if i not in perm:
            if can_be_extend(perm+[i]):
                extend2(perm+[i],n)
            


extend2([],4)


