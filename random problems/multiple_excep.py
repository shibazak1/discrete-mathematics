
'''
def funny_div(divisore):
    try:
    
        if divisore == 13:

            raise ValueError("13 is not allowble")

        100/divisore
    except(ZeroDivisionError,TypeError):
        print("try another number")




for i in (2,"hellow",13,0):

    print("testing {}".format(i),end="")
    print(funny_div(i))

'''

def funny_div(number):

    try:
       if number == 13:
           raise ValueError("13 not good number")
       return 100/number

    except ZeroDivisionError:
        print("try other then Zero")
    except TypeError:
        print("this is not a number")
    except ValueError:
        raise


for val in (2,"hellow",0,13):

    print("testing {} :".format(val),end="")
    print(funny_div(val))
