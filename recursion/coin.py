

def change(amount):
    
    if amount==8:
        print("this is how to add 8")
        return [5,3]
    elif amount==9:
        print("this is how to add 9")
        return [3,3,3]
    elif amount==10:
        print("this is how to add 10")
        return [5,5]


    print(f"we compute how to add up {amount-3}")
    coins = change(amount-5)
    coins.append(5)
    print(f"this is how to add {amount} {coins}")
    return coins


amount = 14
result = change(amount)

print(f"{amount}={'+'.join(map(str,result))}")

def change2(amount):
    if amount==7:
        return [7]
    elif amount==5:
        return [5]
    elif amount==24:
         return [7,7,5,5]
    elif amount==25:
        return [5,5,5,5,5]
    elif amount==26:
        return [7,7,5,7]

    coins = change2(amount-7)
    coins.append(7)
    return coins

