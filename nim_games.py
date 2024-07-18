#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux de nim
variante simple et de Marienbad
"""


def get_player_move(player, remaining_turns):
    """
    Ask the player the number of matches to remove and validates.

    Args :
        player : actual player name.
        remaining_turns : number of matches still in game.

    Returns :
        int : number of matches to remove.
    """
    while True:
        try:
            move = int(input(f"{player}, combien d'allumettes voulez-vous enlever (1-4) ?"))
            if 1 <= move <= 4 and move <= remaining_turns:
                return move
            else:
                print(f"Entrez un nombre entre 1 et 4 (pas plus que ce qu'il reste: {remaining_turns}")
        except ValueError:
            print("Invalide, entrez un nombre.")


def play_nim_game():
   """
   Execute the game between 2 human players.

    - Demande les noms des deux joueurs.
    - Demande quel joueur commence.
    - Exécute une boucle de jeu où les joueurs enlèvent des allumettes à tour de rôle.
    - Affiche le nombre d'allumettes restantes après chaque tour.
    - Déclare le perdant (celui qui doit enlever la dernière allumette).
   """
    # Initialisation du jeu
    total_matches = 21
    player1 = input("Nom du joueur 1: ")
    player2 = input("Nom du joueur 2: ")
    current_player = input(f"Qui commence, {player1} ou {player2}? ")

    # Vérification du joueur initial
    if current_player not in [player1, player2]:
        print(f"Le joueur initial doit être {player1} ou {player2}. Par défaut, {player1} commence.")
        current_player = player1

    # Boucle principale du jeu
    while total_matches > 0:
        print(f"\nIl reste {total_matches} allumettes.")
        move = get_player_move(current_player, total_matches)
        total_matches -= move

        # Changement de joueur
        if total_matches > 0:
            current_player = player2 if current_player == player1 else player1

    # Fin du jeu, détermination du perdant
    print(f"\nIl ne reste plus d'allumettes. {current_player} a perdu!")

# Lancement du jeu
if __name__ == "__main__":
    play_nim_game()