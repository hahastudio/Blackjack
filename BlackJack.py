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
		decision = decision.upper()
	return decision

def ask_play_again():
	decision = raw_input("Do you want to play again? (Y/N)>")
	decision = decision.upper()
	while decision not in ("Y", "N"):
		decision = raw_input("Invalid input. Please input \"Y\" or \"N\" >")
		decision = decision.upper()
	return decision	

def hit(cards, someone):
	someone.append(cards.pop())

def dealer_decision(cards, dealer):
	while sum_cards(dealer) < 17:
		hit(cards, dealer)
		print "Dealer(PC) got cards: ",
		show_cards(dealer)
		print "Dealer's(PC) card totals: %d" % sum_cards(dealer)

def player_win():
	print "Player(You) wins!!!"

def dealer_win():
	print "Dealer(PC) wins."

def drawn():
	print "Drawn."

def win(dealer, player):
	if is_blackjack(player):
		if is_blackjack(dealer):
			drawn()
		else:
			player_win()
	else:
		if is_blackjack(dealer):
			dealer_win()
		else:
			sum_player = sum_cards(player)
			sum_dealer = sum_cards(dealer)
			if sum_player > 21:
				if sum_dealer > 21:
					drawn()
				else:
					dealer_win()
			else:
				if sum_dealer > 21:
					player_win()
				else:
					if sum_player > sum_dealer:
						player_win()
					elif sum_player == sum_dealer:
						drawn()
					else:
						dealer_win()

if __name__ == '__main__':
	while True:
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
		print "It's Dealer(PC)'s turn."
		print "Dealer(PC) got cards: ",
		show_cards(dealer)
		print "Dealer's(PC) card totals: %d" % sum_cards(dealer)
		if is_blackjack(dealer):
			print "And Dealer(PC) got a BlackJack!!!"
		dealer_decision(cards, dealer)
		if sum_cards(dealer) > 21:
			print "Busted!"
		win(dealer, player)
		if ask_play_again() == "N":
			break