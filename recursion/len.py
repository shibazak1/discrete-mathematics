

def length(lst):
    print(f"computing the lenght of the list {lst}")
    if not lst:
        print("the lenght of the list is 0")
        return 0


    else:
        shorter_lst = lst[1:]
        result = 1+length(shorter_lst)
        print(f"the length of the lst is {result}")
        return result
    

length([1,3,4,5,6,7,8])
