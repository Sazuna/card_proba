#!/bin/python3
from typing import List

from draw_card import draw_card_known, draw_card_unknown, size_of
from enum import Enum
import random

SIZE = 52
NB_DECKS = 4
DECKS = []

PLAYERS = 3
CAN_SEE_DECK = [[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]]

PROBA_PLAYERS = []

class Visibility(Enum):
	HIDDEN = 0
	VISIBLE = 1
	SELF = 2
	SOME = 3

class Player():
	idx = 0
	def __init__(self):
		self.idx = idx
		idx += 1

class Deck():
	idx = 0
	size = 0
	def __init__(self,
		 n_cards = -1
		 visibility: Visibility = Visibility.HIDDEN,
		):
		if n_cards == 0:
			raise ValueError("Can not have 0 cards in a Deck.")
		elif n_cards > size:
			if size == 0:
				size = n_cards
			else:
				raise ValueError("Can not have a deck that is not the same size as other decks.")
		elif n_cards < 0 and size == 0:
			raise ValueError("Size of a deck can not be a negative number.")
		self.idx = idx
		idx += 1
		self.cards = [0] * size

class ProbaPlayers():
	def __init__(self,
		players: List[Player],
		decks: List[Deck]):
		self.proba_players = [[[0] * len(players)] * len(decks)] * len(decks[0])
		self.visibility_by_player_deck = [[Visibility.HIDDEN] * len(players)] * len(decks)

	def add_visibility(player: Player, deck: Deck, visibility: Visibility):
		self.visibility[player.idx][deck.idx] = visibility
		
		


def draw_cards(from_deck: Deck,
		to_deck: Deck,
		n_cards: int,
		known: bool = False # if known : every player knows which card. Else: only the players who have access to one of the decks know.
	):
	"""
	known -- bool : if True, every player knows which card. Else: only the players who have access to one of the decks know.
	"""
	for _ in range(n_cards):
		idx = [i for i, a in enumerate(from_deck) if a == 1]
		idx = random.choice(idx)
		from_deck[idx] = 0
		to_deck[idx] = 1
		

def empty_decks(n_decks, n_cards) -> List[Deck]:
	for n in range(n_decks):
		d = Deck(n_cards)

"""
def init_probas():
	for i, player in enumerate(CAN_SEE_DECK):
		for j, can_see in enumerate(CAN_SEE_DECK[i]):
			continue
			if can_see:
				PROBA_PLAYERS[j][i] = DECKS[j] # 3 dimensions memory
			else:
				size_deck = size_of(DECKS[i])
				PROBA_PLAYERS[j][i] = size_deck / SIZE
"""

def main():
	decks = empty_decks(n_decks = NB_DECKS, n_cards = SIZE)
	# init_probas()
	draw_cards(0, 1, 1)
	player1 = Player()
	print(player1.idx)
	player2 = Player()
	print(player2.idx)

if __name__ == "__main__":
	main()
