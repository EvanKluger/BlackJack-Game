#This is the code for a BlackJack Game to be played on the terminal
import random 

cards = {
'2 Hearts': 2,
'2 Spades': 2,
'2 Clubs': 2,
'2 Diamonds': 2,
'3 Hearts': 3,
'3 Spades': 3,
'3 Clubs': 3,
'3 Diamonds': 3,

'4 Hearts': 4,
'4 Spades': 4,
'4 Clubs': 4,
'4 Diamonds': 4,

'5 Hearts': 5,
'5 Spades': 5,
'5 Clubs': 5,
'5 Diamonds': 5,

'6 Hearts': 6,
'6 Spades': 6,
'6 Clubs': 6,
'6 Diamonds': 6,

'7 Hearts': 7,
'7 Spades': 7,
'7 Clubs': 7,
'7 Diamonds': 7,

'8 Hearts': 8,
'8 Spades': 8,
'8 Clubs': 8,
'8 Diamonds': 8,

'9 Hearts': 9,
'9 Spades': 9,
'9 Clubs': 9,
'9 Diamonds': 9,

'10 Hearts': 10,
'10 Spades': 10,
'10 Clubs': 10,
'10 Diamonds': 10,

'Jack Hearts': 10,
'Jack Spades': 10,
'Jack Clubs': 10,
'Jack Diamonds': 10,

'Queen Hearts': 10,
'Queen Spades': 10,
'Queen Clubs': 10,
'Queen Diamonds': 10,

'King Hearts': 10,
'King Spades': 10,
'King Clubs': 10,
'King Diamonds': 10,

'Ace Hearts': 11,
'Ace Spades': 11,
'Ace Clubs': 11,
'Ace Diamonds': 11,
}

def play():
    print(' \n Welcome to BlackJack Terminal Game \n')
    play = 'y'
    while play == 'y':
        player = []
        dealer = []

        player_first_card = random.choice(list(cards.keys()))
        player_second_card = random.choice(list(cards.keys()))

        player.append(player_first_card)
        player.append(player_second_card)

        dealer_first_card = random.choice(list(cards.keys()))
        dealer_second_card = random.choice(list(cards.keys()))

        dealer.append(dealer_first_card)
        dealer.append(dealer_second_card)
        
        player_score = 0
        dealer_score = 0
        for card in player:
            player_score += cards[card]
        for card in dealer:
            dealer_score += cards[card]

        print("Your cards are " + player[0] + " and a " + player[1] + ' for a score of '+ str(player_score) +'\n')
        print("The dealer is showing a " + dealer[0] + '\n')

        choice = ''
        ace_count = 0
        while choice != 'stand' and player_score < 22:
            choice = input("Would you like to hit or stand   ")
            if choice.lower() == 'hit':
                new_card = random.choice(list(cards.keys()))
                player.append(new_card)
                player_score += cards[new_card]
            if player_score > 21:
                ace_count_temp = 0
                for card in player:
                    if "Ace" in card:
                        ace_count_temp += 1
                player_score -= ((ace_count_temp - ace_count)* 10)
                ace_count = ace_count_temp
            print("Your cards are " + str(player) + ' for a score of '+ str(player_score) +'\n')
        print('The dealer flips his second card and is showing a ' + str(dealer) + ' for a score of '+ str(dealer_score) + '\n')
        while dealer_score < 17:
            new_card = random.choice(list(cards.keys()))
            dealer.append(new_card)
            dealer_score += cards[new_card]
            print("The dealer hits and has " + str(dealer) + ' for a score of '+ str(dealer_score) + '\n')
            
        if player_score > 21:
            print("Sorry the dealer has won \n")
            play = input("Would you like to play another hand - type y    ").lower()
            print('\n \n')
            continue

        if dealer_score > 21:
            print('You have won \n')
            play = input("Would you like to play another hand - type y    ").lower()
            print('\n \n')
            continue

        if dealer_score < player_score:
            print('You have won \n')
            play = input("Would you like to play another hand - type y    ").lower()
            print('\n \n')
            continue
        else:
            print("Sorry the dealer has won \n")
            play = input("Would you like to play another hand - type y   ").lower()
            print('\n \n')
            continue
        
play()

