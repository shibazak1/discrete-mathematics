
def binary_search(a,lst):

    print(f"searching for {a} in {lst}")
    middel = len(lst)//2
    

    if a==lst[middel]:
        return "found"
    elif a>lst[middel]:
        return binary_search(a,lst[middel+1:])
    elif a<lst[middel]:
        return binary_search(a,lst[:middel])
        
        
