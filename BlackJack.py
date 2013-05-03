#coding:utf-8
import random

def init_cards(cards):
	for color in ("♠", "♥", "♣", "♦"):
		for rank in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):
			cards.append(color + rank)
	random.shuffle(cards)

def init_deal(cards, dealer, player):
	player.append(cards.pop())
	player.append(cards.pop())
	dealer.append(cards.pop())
	dealer.append(cards.pop())
	print "Player(You) got cards: ",
	for card in player:
		print card,
	print
	print "Dealer(PC) got cards: ",
	print dealer[0], "unknown"

if __name__ == '__main__':
	cards = []
	player = []
	dealer = []
	init_cards(cards)
	init_deal(cards, dealer, player)