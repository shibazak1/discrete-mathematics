
def query(y):
    x=4
    if y==x:
        return "equal"
    elif y>x:
        return "grater"
    elif y<x:
        return "smaller"



def guess(lower,upper):
    
    midel = (upper+lower)//2
    answer = query(midel)
    print(f"x={midel} answer is {answer}")
    if answer=="equal":
        return
    elif answer=="grater":
        guess(lower,midel-1)
    elif answer=="smaller":
        guess(midel+1,upper)


        
