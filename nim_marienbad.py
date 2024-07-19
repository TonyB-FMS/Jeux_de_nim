"""
Explications générales :

    Demander qui commence à chaque partie :
        - La variable starting_player est demandée à chaque début de partie pour déterminer qui commence.
            Précision sur le choix du joueur qui commence :
               - L'invite de saisie pour le joueur qui commence donne des instructions claires sur ce qu'il faut entrer
                    pour valider (le nom du joueur pour le joueur humain ou 'o' pour l'ordinateur).
               - Le choix est rendu non sensible à la casse en utilisant ".lower()" sur les entrées
                    et les vérifications.

    Fonction "compute_nim_sum(piles)" :
        - Calcule la somme de Nim des piles données en utilisant l'opération XOR.

    Fonction "get_computer_move_marienbad(piles)" :
        - Calcule le mouvement de l'ordinateur en utilisant la stratégie gagnante pour Marienbad.
        - Si la somme de Nim est 0 (une position perdante pour le joueur suivant),
            l'ordinateur fait un mouvement aléatoire valide comme solution de repli.
        - Sinon, l'ordinateur choisit un mouvement pour rendre la somme de Nim 0 pour le joueur suivant,
            ce qui est une position gagnante pour l'ordinateur.

    Fonction "play_game(piles, player1, player2, is_computer, starting_player)" :
        - Gère l'exécution du jeu (Nim ou Marienbad) entre deux joueurs ou un joueur et l'ordinateur.
        - Alterne les tours entre les joueurs, affiche l'état actuel des allumettes et déclare le perdant.

    Fonction main() :
        - Menu principal pour choisir la version du jeu et le mode de jeu.
        - Initialise le jeu en demandant les noms des joueurs et en définissant l'état initial des piles.
        - Demande à chaque fois qui commence la partie.
        - Lance le jeu en appelant play_game().
        - Ajout de la vérification et de l'affichage des instructions pour le choix du joueur qui commence,
            incluant la gestion de la casse.
"""


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
            print("Invalide. Entrez un nombre.")


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

        # Switch players
        current_player = player2 if current_player == player1 else player1


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

        starting_player = input(
            f"Qui commence, {player1} (entrez {player1.lower()}) ou {player2} (entrez {player2.lower()[0]})? ").lower()

        if starting_player not in [player1.lower(), player2.lower()[0]]:
            print(f"Choix invalide. Veuillez entrer {player1.lower()} ou {player2.lower()[0]}.")
            continue

        if starting_player == player1.lower():
            starting_player = player1
        else:
            starting_player = player2

        if version_choice == '1':
            piles = [21]
        else:
            piles = [1, 3, 5, 7]

        print(f"\n{starting_player} commence la partie.")
        play_game(piles, player1, player2, is_computer, starting_player)
        break


if __name__ == "__main__":
    main()
