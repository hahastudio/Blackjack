#coding:utf-8
import random

def init_cards(cards):
	for color in u"♠♥♣♦":
		for rank in (u"A", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"J", u"Q", u"K"):
			cards.append(color + rank)
	random.shuffle(cards)



if __name__ == '__main__':
	cards = []
	init_cards(cards)
	for card in cards:
		print card.encode("utf-8"),