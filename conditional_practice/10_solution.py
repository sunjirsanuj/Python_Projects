
print("\n***** TEAM WIN TESTING PROGRAM *****\n")

teamA_name = input("Enter name of team A: ")
teamA_score = int(input("Enter team A's score: "))
teamB_name = input("\nEnter name of team B: ")
teamB_score = int(input("Enter team B's score: "))

print("Score of",teamA_name,":",teamA_score)
print("Score of",teamB_name,":",teamB_score)

if teamA_score == teamB_score:
    print("Draw!")
elif teamA_score > teamB_score:
    print(teamA_name,"has won the game.")
else:
    print(teamB_name,"has won the game.")