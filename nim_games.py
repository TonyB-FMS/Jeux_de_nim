def get_player_move(player, remaining_matches):
    """
    Prompts the player to remove a certain number of matches and validates the input.

    Args:
        player (str): The name of the current player.
        remaining_matches (int): The number of matches remaining.

    Returns:
        int: The number of matches the player removes.
    """
    while True:
        try:
            move = int(input(f"{player}, combien d'allumettes voulez-vous enlever (1-4)? "))
            if 1 <= move <= 4 and move <= remaining_matches:
                return move
            else:
                print(f"Entrez un nombre entre 1 et 4, et pas plus que le nombre d'allumettes restantes (reste {remaining_matches}).")
        except ValueError:
            print("Invalide. Entrez un nombre.")

def get_computer_move(player_move):
    """
    Calculates the computer's move based on the player's move.

    Args:
        player_move (int): The number of matches removed by the player.

    Returns:
        int: The number of matches the computer removes.
    """
    return 5 - player_move

def play_nim_game():
    """
    Manages the execution of the Nim game between a human player and the computer.

    This function:
    - Asks for the human player's name.
    - Asks who starts the game.
    - Executes a game loop where the human player and the computer take turns removing matches.
    - Displays the number of matches remaining after each turn.
    - Declares the loser (the one who has to remove the last match).
    """
    # Game initialization
    total_matches = 21
    player = input("Nom du joueur: ")
    starting_player = input(f"Qui commence, {player} ou l'ordinateur? ")

    # Main game loop
    while total_matches > 0:
        print(f"\nIl reste {total_matches} allumettes.")

        if starting_player == player:
            # Player's turn
            move = get_player_move(player, total_matches)
            total_matches -= move

            # Check if the game continues
            if total_matches == 0:
                print(f"\nIl ne reste plus d'allumettes. {player} a perdu!")
                break

            # Computer's turn
            computer_move = get_computer_move(move)
            print(f"L'ordinateur enlève {computer_move} allumettes.")
            total_matches -= computer_move

            # Check if the game continues
            if total_matches == 0:
                print("\nIl ne reste plus d'allumettes. L'ordinateur a perdu!")
                break
        else:
            # Computer's turn to start the game
            if total_matches == 21:
                computer_move = 1
            else:
                computer_move = get_computer_move(player_move)
            print(f"L'ordinateur enlève {computer_move} allumettes.")
            total_matches -= computer_move

            # Check if the game continues
            if total_matches == 0:
                print("\nIl ne reste plus d'allumettes. L'ordinateur a perdu!")
                break

            # Player's turn
            player_move = get_player_move(player, total_matches)
            total_matches -= player_move

            # Check if the game continues
            if total_matches == 0:
                print(f"\nIl ne reste plus d'allumettes. {player} a perdu!")
                break

# Start the game
if __name__ == "__main__":
    play_nim_game()
