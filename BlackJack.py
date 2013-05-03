#coding:utf-8
import random

def init_cards(cards):
	for color in u"♠♥♣♦":
		for rank in u"A23456789JQK":
			cards.append(color + rank)
	random.shuffle(cards)

if __name__ == '__main__':
	cards = []
	init_cards(cards)
	for card in cards:
		print card.encode("utf-8"),