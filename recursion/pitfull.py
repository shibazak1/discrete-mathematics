
def strange(n):
    if n==10:
        return 9
    else:
        return n*strange(n+1)
