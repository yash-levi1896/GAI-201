import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'q']:
            return user_choice
        else:
            print("Invalid choice. Please choose from rock, paper, or scissors.")
            
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif user_choice == 'rock':
        return 'user' if computer_choice == 'scissors' else 'computer'
    elif user_choice == 'scissors':
        return 'user' if computer_choice == 'paper' else 'computer'
    elif user_choice == 'paper':
        return 'user' if computer_choice == 'rock' else 'computer'

def display_score(user_wins, computer_wins, draws):
    print(f"User Wins: {user_wins}, Computer Wins: {computer_wins}, Draws: {draws}")

def main():
    user_wins = 0
    computer_wins = 0
    draws = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'q':
            print("Thanks for playing. Final Score:")
            display_score(user_wins, computer_wins, draws)
            break
        
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        
        result = determine_winner(user_choice, computer_choice)
        if result == 'draw':
            print("It's a draw!")
            draws += 1
        elif result == 'user':
            print("Congratulations! You win this round.")
            user_wins += 1
        else:
            print("Computer wins this round.")
            computer_wins += 1
        
        display_score(user_wins, computer_wins, draws)
        print("-------------------------------------------------")

if __name__ == "__main__":
    main()
