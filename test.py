from draw_card import *

def test0():
	deck1 = [0.9, 0.1]
	deck2 = [0.1, 0.9]
	assert(data_is_correct([deck1, deck2]))

def test1():
	deck1 = [0.2,0.6,0.2,1.0]
	deck2 = [0.8,0.4,0.8,0.0]
	n_cards_deck_1 = sum(deck1)
	n_cards_deck_2 = sum(deck2)
	draw_card_unknown(deck1, deck2)
	assert(deck1 == [0.1,0.3,0.1,0.5])
	assert(deck2 == [0.9,0.7,0.9,0.5])

def test2():
	deck1 = [0.25,0.25,0.25,0.25]
	deck2 = [0.75,0.75,0.75,0.75]
	draw_card_unknown(deck1, deck2, draw = 1)
	assert(deck1 == [0,0,0,0])
	assert(deck2 == [1,1,1,1])

def test_known_1():
	deck1 = [0.4, 0.4, 0.2]
	deck2 = [0.6, 0.6, 0.8]
	draw_card_known(deck1, deck2, 0, 1)
	assert(deck1 == [0.0, 0.0, 0.0])
	assert(deck2 == [1.0, 1.0, 1.0])

def test_known_2():
	deck1 = [0.1, 0.1, 0.1, 0.4, 0.6, 0.7]
	deck2 = [0.9, 0.9, 0.9, 0.6, 0.4, 0.3]
	draw_card_known(deck1, deck2, 0, 4, 3)
	assert(deck1 == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
	assert(deck2 == [1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

def test_known_3():
	deck1 = [0.5, 0.9, 0.6]
	deck2 = [0.5, 0.1, 0.4]
	draw_card_known(deck1, deck2, 0, 2)
	assert(deck1[2] == 0.0)
	assert(deck2[2] == 1.0)

def test_data():
	deck1 = [0.1, 0.1, 0.1, 0.4, 0.6, 0.7]
	deck2 = [0.9, 0.9, 0.9, 0.6, 0.4, 0.3]
	data_is_correct([deck1, deck2])
	
if __name__ == '__main__':
	test0()
	test1()
	test2()
	test_known_1()
	test_known_2()
	test_known_3()
	test_data()
