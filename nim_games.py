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
