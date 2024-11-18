

def day_required(amount,target_money,earning_percentage,day):

    amount = amount+amount*(earning_percentage )//100
    if amount>=target_money:
        print(f"you got it {amount}")
        return amount
    else:
        print(f"after {day} we got {amount} from {target_money}")
        
        day_required(amount,target_money,earning_percentage,day+1)
    




day_required(1000,1000000,2,1)
