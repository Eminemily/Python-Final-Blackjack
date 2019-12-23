import random

#create deck of cards
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
          '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':1}

#deal card function
def deal_card():
    dealt_card = cards.pop()
    cards.remove(dealt_card)
    return dealt_card

#Menu
print ("Welcome to Emily's Blackjack Game!")

#begin a hand
dealer_hand = []
while len(dealer_hand) != 2:
    dealer_hand.append(deal_card())
    if len(dealer_hand) == 2:
        print("Dealer shows ", (dealer_hand[1]))
player_hand = []
while len(player_hand) != 2:
    player_hand.append(deal_card())
    if len(player_hand) == 2:
        print("Your hand is ", *player_hand)

#play game
def check_hand (who, hand):
    cards_total = sum(map(value.get, hand))
    total = [cards_total] + [item for item in range(cards_total+10, cards_total+10*hand.count('A')+1, 10) if item <=21]
    return total

pl, cp = check_hand('Player', player_hand), check_hand('Dealer', dealer_hand)

while pl:
    option = input ('Enter "h" to Hit or Enter "s" to Stay: ').lower()
    if option == "h":
        print ('You hit.')
        player_hand.append(deal_card())
        print ('Your hand is ', *player_hand)
        new_hand = check_hand('Player', player_hand)
        if new_hand[-1] > 21:
            print ('***** You bust. *****')
            break
        
    elif option == "s":
        print ('You stand.')
        break
    
    
while cp[-1] < 16:
    print ('Dealer hits.')
    dealer_hand.append(deal_card())
    break
    
while 1:
    pl, cp = check_hand('Player', player_hand), check_hand('Dealer', dealer_hand)

    print ('Player:', *player_hand)
    print ('Dealer: ', *dealer_hand)
    if pl[-1] > 21:
        print ('***** You bust. Dealer wins. *****')
    elif cp[-1] > 21:
        print ('***** Dealer Busts. You win! *****')
    elif pl[-1] == 21 and  cp[-1] != 21:
        print ('***** You have 21! You win! *****')
    elif cp[-1] == 21 and pl[-1] != 21:
        print ('***** Dealer has 21. Dealer wins. *****')
    elif pl[-1] > cp[-1]:
        print ('***** You win! *****')
    elif pl[-1] < cp[-1]:
        print ('***** Dealer wins. *****')
    elif pl[-1] == cp[-1]:
            print ('***** You push. *****')
    break

