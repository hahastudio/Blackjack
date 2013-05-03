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
	show_cards(player)
	print "Dealer(PC) got cards: ",
	print dealer[0], "unknown"

def show_cards(someone):
	for card in someone:
		print card,
	print

def sum_cards(someone):
	sum = 0
	ace = 0
	for card in someone:
		rank = card[-1]
		if rank in ("0", "J", "Q", "K"):
			sum += 10
		elif rank == "A":
			sum += 11
			ace += 1
		else:
			sum += int(rank)
	while sum > 21 and ace > 0:
		sum -= 10
		ace -= 1
	return sum

def is_blackjack(someone):
	if sum_cards(someone) == 21 and len(someone) == 2:
		return True
	return False

def ask_decision(player):
	decision = raw_input("Hit or Stand? (H/S)>")
	decision = decision.upper()
	while decision not in ("H", "S"):
		decision = raw_input("Invalid input. Please input \"H\" or \"S\" >")
	return decision

def hit(cards, someone):
	someone.append(cards.pop())

if __name__ == '__main__':
	cards = []
	player = []
	dealer = []
	init_cards(cards)
	init_deal(cards, dealer, player)
	print "Player's(Your) card totals: %d" % sum_cards(player)
	if is_blackjack(player):
		print "And Player(You) got a BlackJack!!!"
	else:
		while sum_cards(player) < 21:
			if ask_decision(player) == "H":
				hit(cards, player)
				print "Player(You) got cards: ",
				show_cards(player)
				sum_player = sum_cards(player)
				print "Player's(Your) card totals: %d" % sum_player
				if sum_player > 21:
					print "Busted!"
					break
			else:
				break
	