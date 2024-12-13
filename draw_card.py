#!/bin/python3
import numpy as np
from typing import List

decks = {}

def size_of(deck):
	return round(sum(deck), 5)

def data_is_correct(decks: List) -> bool:
	"""
	The data is defined like this :
	all decks must be of the same size.
	Each index represents a card and the value is the probability of it to be in the deck.
	All values of probability additionned together is the amount of cards in the deck.
	For one card (index), all of the decks must have 1 if the probabilities of one card for all decks are additionned.
	"""
	decks_np = np.array(decks)
	sums = np.sum(decks_np, axis = 1) # y axis
	return np.count_nonzero(sums != 1) == 0 # only 1 in sums

def draw_card_unknown(deck_from, deck_to, draw=1):
	"""
	Changes the probabilities of the cards to belong to one deck if we don't know which card has been drawn.

	Keywords arguments:
	deck_from -- list : the probability of each card (represented by index) to be in the first deck 	
	deck_from -- list : the probability of each card (represented by index) to be in the target deck 	
	draw -- int : the number of cards that we want to draw.
	"""
	n_cards_from = size_of(deck_from)
	while draw > 0:
		if n_cards_from < 1:
			return
		for card, prob in enumerate(deck_from):
			prob_draw_card = (prob / n_cards_from)
			deck_from[card] -= prob_draw_card
			deck_to[card] += prob_draw_card
		n_cards_from = size_of(deck_from)
		draw -= 1

def draw_card_known(deck_from, deck_to, other_decks=0, *cards):
	"""
	Changes the probabilities of the cards to be in one deck if we know which card has been drawn.

	Keywords arguments:
	deck_from -- list : the probability of each card (represented by index) to be in the first deck 	
	deck_to -- list : the probability of each card (represented by index) to be in the target deck 	
	other_decks -- list : list of decks to which we will also apply probability absorption
	*cards -- *int : the cards that has been drawn

	"""
	print(size_of(deck_from))
	
	for card in cards:
		if (size_of(deck_from) < 1.0):
			print(size_of(deck_from))
			print(deck_from)
			print("Not enough cards in deck to draw a card.")
			return
		proba_from = deck_from[card] # 0.1
		print("probba_from = ", proba_from)
		percent_to_rem = (1 - proba_from) #/ (0.9)
		size_from = size_of(deck_from)
		current_size_from = size_from - proba_from #2 - 0.1 = 1.9
		for i, card_proba in enumerate(deck_from):
			deck_from[i] = round(card_proba - percent_to_rem * card_proba / current_size_from, 5)
		if isinstance(other_decks, list):
			for deck in other_decks:
				for i, card_proba in enumerate(deck):
					deck_from[i] = round(card_proba - percent_to_rem * card_proba / current_size_from, 5)
		deck_from[card] = 0.0

		print("deck to before:", deck_to)
		proba_to = deck_to[card]
		percent_to_add = 1 - proba_to
		print("percent to add:", percent_to_add)
		size_to = size_of(deck_to)
		current_size_to = size_to + proba_to
		print("current_size_to:", current_size_to)
		for i, card_proba in enumerate(deck_to):
			# deck_to[i] = round(card_proba + percent_to_add * (1 - card_proba) / (len(deck_to) - current_size_to - 1), 5)
			if i == card:
				continue
			deck_to[i] += percent_to_add * (deck_to[i]) # TODO
		deck_to[card] = 1.0
