import random
def number_game(in_val):
	number_range = [x for x in range(1,101)]
	rand_num = random.choice(number_range)
	if int(in_val) == rand_num:
		print("Amazing how did this happen")
	else:
		diff_num = int(in_val) - rand_num
		if diff_num < 0:
			print("You are just {} behind".format(diff_num * -1))
			print("I have choosen {}".format(rand_num))
		else:
			print("You are just {} ahaead".format(diff_num))
			print("I have choosen {}".format(rand_num))
def main():
	while True:
		user_option = raw_input("Do you want to play a Game (Yes/No): ")
		if user_option in ['Yes','Y','y','yes']:
			user_val = raw_input("Please guess a number between 1 to 100: ")
			number_game(user_val)
			continue
		else:
			break
    
if __name__ == '__main__':
    main()
