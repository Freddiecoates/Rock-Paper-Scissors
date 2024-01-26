import random

def play_rock_paper_scissors():
    computer_choice = random.randint(1, 3)

    player_choice = input("Type 'OK' if you want to play Rock, Paper, Scissors: ").upper()

    if player_choice == "OK":
        player_choice = random.randint(1, 3)

    if computer_choice == player_choice:
        print(f"We both chose {get_choice_name(computer_choice)}! It's a tie. Let's try again.")
    else:
        winner = determine_winner(computer_choice, player_choice)
        print(f"I chose {get_choice_name(computer_choice)}, you chose {get_choice_name(player_choice)}: {winner}")

    play_again = input("Do you want to play again? (Type 'YES' to play again): ").upper()
    if play_again == "YES":
        play_rock_paper_scissors()

def determine_winner(computer, player):
    if (computer == 1 and player == 2) or (computer == 2 and player == 3) or (computer == 3 and player == 1):
        return "You WIN!"
    else:
        return "You LOSE!"

def get_choice_name(choice):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return choices[choice]

if __name__ == "__main__":
    play_rock_paper_scissors()
    print("Goodbye!")
