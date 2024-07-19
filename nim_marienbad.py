def display_matches(multiple_piles):
    """
    Displays the current state of matches in a visual format.

    Args:
        multiple_piles (list of int): List representing the number of matches in each pile.
    """
    for i, pile in enumerate(multiple_piles):
        print(f"Tas {i + 1}: {'|' * pile}")


def get_player_move(player, piles):
    """
    Prompts the player to remove a certain number of matches from a chosen pile and validates the input.

    Args:
        player (str): The name of the current player.
        piles (list of int): List representing the number of matches in each pile.

    Returns:
        tuple: The chosen pile and the number of matches the player removes.
    """
    while True:
        try:
            pile_choice = int(input(f"{player}, choisissez un tas (1-{len(piles)}): ")) - 1
            if 0 <= pile_choice < len(piles) and piles[pile_choice] > 0:
                move = int(input(f"{player}, combien d'allumettes voulez-vous enlever (1-{piles[pile_choice]})? "))
                if 1 <= move <= piles[pile_choice]:
                    return pile_choice, move
                else:
                    print(f"Entrez un nombre entre 1 et {piles[pile_choice]}.")
            else:
                print(f"Choisissez un tas valide avec des allumettes restantes (1-{len(piles)}).")
        except ValueError:
            print("Entrée invalide. Entrez un nombre.")


def compute_nim_sum(piles):
    """
    Computes the Nim-sum of the given piles.

    Args:
        piles (list of int): List representing the number of matches in each pile.

    Returns:
        int: The Nim-sum of the piles.
    """
    nim_sum = 0
    for pile in piles:
        nim_sum ^= pile
    return nim_sum


def get_computer_move_marienbad(piles):
    """
    Calculates the computer's move using the winning strategy for Marienbad.

    Args:
        piles (list of int): List representing the number of matches in each pile.

    Returns:
        tuple: The chosen pile and the number of matches the computer removes.
    """
    nim_sum = compute_nim_sum(piles)
    if nim_sum == 0:
        # If the Nim-sum is 0, make a random valid move (fallback)
        for i, pile in enumerate(piles):
            if pile > 0:
                return i, 1
    else:
        for i, pile in enumerate(piles):
            target_pile = pile ^ nim_sum
            if target_pile < pile:
                return i, pile - target_pile


def play_game(piles, player1, player2, is_computer, starting_player):
    """
    Manages the execution of the Nim game or Marienbad between two players or player and computer.

    Args:
        piles (list of int): List representing the initial state of matches in each pile.
        player1 (str): The name of the first player.
        player2 (str): The name of the second player or "Computer".
        is_computer (bool): True if player2 is the computer, False if it is another human player.
        starting_player (str): The name of the player who starts the game.
    """
    current_player = starting_player
    while any(piles):
        print("\nÉtat actuel des allumettes:")
        display_matches(piles)

        if current_player == player1 or not is_computer:
            pile_choice, move = get_player_move(current_player, piles)
        else:
            pile_choice, move = get_computer_move_marienbad(piles)
            print(f"L'ordinateur enlève {move} allumette(s) du tas {pile_choice + 1}.")

        piles[pile_choice] -= move

        if not any(piles):
            print(f"\nÉtat actuel des allumettes:")
            display_matches(piles)
            print(f"\nIl ne reste plus d'allumettes. {current_player} a perdu!")
            break

        current_player = player2 if current_player == current_player == player1 else player1


def main():
    """
    Main function to choose the game version and mode, and start the game.
    """
    while True:
        print("Choisissez la version du jeu:")
        print("1. Jeu de Nim (version simple)")
        print("2. Jeu de Marienbad")
        version_choice = input("Entrez 1 ou 2: ")

        if version_choice not in ['1', '2']:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
            continue

        print("\nChoisissez le mode de jeu:")
        print("1. Joueur contre Joueur")
        print("2. Joueur contre Ordinateur")
        mode_choice = input("Entrez 1 ou 2: ")

        if mode_choice not in ['1', '2']:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
            continue

        player1 = input("Nom du joueur 1: ")
        if mode_choice == '1':
            player2 = input("Nom du joueur 2: ")
            is_computer = False
        else:
            player2 = "Ordinateur"
            is_computer = True

        starting_player = input(f"Qui commence, {player1} ou {player2}? ")

        if version_choice == '1':
            piles = [21]
        else:
            piles = [1, 3, 5, 7]

        print(f"\n{starting_player} commence la partie.")
        play_game(piles, player1, player2, is_computer, starting_player)
        break


if __name__ == "__main__":
    main()
