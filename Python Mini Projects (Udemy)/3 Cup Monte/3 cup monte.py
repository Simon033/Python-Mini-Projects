def shuffle_list(mylist):
    # Take in list, and returned shuffle versioned
    from random import shuffle
    shuffle(mylist)
    
    return mylist
    
def player_guess():
    
    guess = ''
    
    while guess not in ['1','2','3']:
        
        # Recall input() returns a string
        guess = input("Pick a number: 1, 2 or 3:  ")
    
    return int(guess)    

def check_guess(mylist,guess):
    if mylist[guess-1] == 'O':
        print('Correct Guess!')
        print(mylist)
    else:
        print('Wrong! Better luck next time')
        print(mylist)

game_list = [' ','O',' ']

mixedup=shuffle_list(game_list)

guess = player_guess()

check_guess(mixedup,guess)

