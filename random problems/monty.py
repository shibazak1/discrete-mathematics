from random import randint , seed


def initial_choice():
    return randint(1,3)


def keep(choice,opened):
    return choice

def randomize(choice,opened):
    doors = [1,2,3];
    doors.remove(opened)
    return doors[randint(0,1)]

def change(choice,opened):
    return 6-choice - opened


def success_frequency(strategy,number_of_exp):

    wins = 0
    for i in range(number_of_exp):
        
        choice = initial_choice()
        car = randint(1,3)

        if choice == car:
            doors = [1,2,3]
            doors.remove(choice)
            opened = doors[randint(0,1)]
            
        else:
            opened = 6-choice-car


        new_choice = strategy(choice,opened)

        if new_choice == car:
            wins+=1

    return wins/number_of_exp

print(success_frequency(keep, 100000))
print(success_frequency(randomize, 100000))
print(success_frequency(change, 100000))
            

    
