import random
def diceroll(user_entry):
    dice_list = [x for x in range(1,7)]
    while user_entry not in ['No','no','n']:
        print(random.choice(dice_list))
        user_entry = raw_input('Do want to Roll the Dice?(yes/no): ')
        if user_entry == "No":
            break
        else:
            continue
        
            
def main():
    user_entry = raw_input('Do want to Roll the Dice?(yes/no): ')
    diceroll(user_entry)
if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        raise e
