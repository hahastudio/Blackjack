#coding:utf-8
import random

def init_cards(cards):
	for color in ("♠", "♥", "♣", "♦"):
		for rank in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):
			cards.append(color + rank)
	random.shuffle(cards)

if __name__ == '__main__':
	cards = []
	init_cards(cards)
	for card in cards:
		print card,