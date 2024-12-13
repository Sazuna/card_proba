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
		self.idx = Player.idx
		Player.idx += 1

class Deck():
	idx = 0
	size = 0
	filled = False
	def __init__(self,
		 n_cards: int = -1,
		 visibility: Visibility = Visibility.HIDDEN,
		 full: bool = False
		):
		"""
		Keywords arguments:

		n_cards -- int : how many cards are in the decks, first Deck created will fix a value for the next decks. Default: -1
		visibility -- Visibility : which player can see the deck. Default: HIDDEN
		full -- bool : if True, the deck is initialized with all cards in it. Can only be full once.
		"""
		if n_cards == 0:
			raise ValueError("Can not have 0 cards in a Deck.")
		elif n_cards > Deck.size:
			if Deck.size == 0:
				Deck.size = n_cards
			else:
				raise ValueError("Can not have a deck that is not the same size as other decks.")
		elif n_cards < 0 and Deck.size == 0:
			raise ValueError("Size of a deck can not be a negative number.")
		self.idx = Deck.idx
		Deck.idx += 1
		if full and not Deck.filled:
			self.cards = [1] * Deck.size
			Deck.filled = True # TODO fill the memory as well.
		else:
			self.cards = [0] * Deck.size

	def __len__(self):
		return len(self.cards)

	def __getitem__(self, i: int):
		return(self.cards[i])

	def __setitem__(self, i: int, card: int):
		self.cards[i] = card

	def __str__(self):
		return str(self.cards)

	def __repr__(self):
		return str(self)

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
	known -- bool : if True, every player knows which card. Else: only the players who have visibility upon one of the decks know.
	"""
	for _ in range(n_cards):
		idx = [i for i in range(len(from_deck)) if from_deck[i] == 1]
		idx = random.choice(idx)
		from_deck[idx] = 0
		to_deck[idx] = 1
		

def empty_decks(n_decks, n_cards) -> List[Deck]:
	decks = []
	for n in range(n_decks):
		decks.append(Deck(n_cards))
	return decks

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
	decks = empty_decks(n_decks = NB_DECKS - 1, n_cards = SIZE)
	main_deck = Deck(full = True)
	decks.insert(0, main_deck)
	# init_probas()
	draw_cards(main_deck, decks[1], 1)
	print(decks)
	player1 = Player()
	print(player1.idx)
	player2 = Player()
	print(player2.idx)

if __name__ == "__main__":
	main()
