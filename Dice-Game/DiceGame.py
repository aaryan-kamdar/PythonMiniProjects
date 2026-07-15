import numpy as np

def roll():
    min_value=1
    max_value=6
    value=np.random.randint(min_value,max_value)
    return value
    
max_score=50

while True:
    noofplayers=int(input("Enter the number of players "))
    while noofplayers>4 and noofplayers<2:
        print("No of players should be more than 2 and less than 4")
        noofplayers=int(input("Enter the number of players ")) 
    if noofplayers<=4 or noofplayers>=2:
        break
        
scores=[0 for i in range(noofplayers)]

while max(scores)<max_score:
    for player_idx in range(noofplayers):
        print("\n Player Name ",player_idx+1 , "turn started ")
        print("Your total score is: " ,scores[player_idx])
        current_score=0
        while True:    
            choice=input("Do you still want to continue").lower()
            if choice=="y":
                user_score=roll()
                if user_score==1:
                    current_score=0
                    break
                else:
                    current_score+=user_score
                    print(f"Your rolled value is {user_score}")
            else:
                scores[player_idx]+=current_score
                print("Your total score is ", scores[player_idx])
                break
                
max_score=max(scores)

winning_idx=scores.index(max_score)

print("Player numner ", winning_idx+1,"is the winner with max score", max_score)
    
