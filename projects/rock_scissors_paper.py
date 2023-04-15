import random

def play():
    user = input("r for rock p for papper s for scissors: " )
    computer = random.choice(['r','s','p'])
    print(computer)
    if user == computer:
        return "tie"
    return is_win(user,computer)
    # r > s
    # p > r
    # s > p 
    
def is_win(player, opponent):
    if player == 'r' and opponent == 's':
        return "you won"
    elif player == 'p' and opponent == 'r':
        return "you won"
    elif player == 's' and opponent == 'p':
        return "you won"
    else:
        return "you lost"
    
print(play())

