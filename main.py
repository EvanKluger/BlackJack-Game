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
    #Setting up the Game and the anount the Player Bets
    total_winnings = 0
    print(' \n Welcome to BlackJack Terminal Game \n')
    
    play = 'y'
    
    #While loop that runs the game over and over again until player choses to stop
    while play == 'y':
        bet = int(input('How much would you like to bet \n'))
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
        if dealer_score > 21:
            dealer_score -= 20
        
        print("Your cards are " + player[0] + " and a " + player[1] + ' for a score of '+ str(player_score) +'\n')
        print("The dealer is showing a " + dealer[0] + '\n')
        
        choice = ''
        ace_count_player = 0
        ace_count_dealer = 0
        first_hand_score = 0
        second_hand_score = 0
        if(cards[player_first_card] == cards[player_second_card]):
            choice = input("Would you like to double down or split? Enter double or split. If not type no   ").lower()

            if choice == 'double':
                new_card = random.choice(list(cards.keys()))
                player.append(new_card)
                player_score += cards[new_card]
                print("Your cards are " + str(player) + ' for a score of '+ str(player_score) +'\n')

            if choice == 'split':
                split_choice_1 = ''
                split_choice_2 = ''
                first_hand = []
                second_hand = []
                first_hand.append(player_first_card)
                first_hand.append(random.choice(list(cards.keys())))
                second_hand.append(player_second_card)
                second_hand.append(random.choice(list(cards.keys())))

                while split_choice_1 != 'stand' and first_hand_score < 22:
                    split_choice_1 = input(" Your first hand is a " + str(first_hand) + "Would you like to hit or stand   ")
                    if split_choice_1.lower() == 'hit':
                        new_card = random.choice(list(cards.keys()))
                        first_hand.append(new_card)
                        first_hand_score += cards[new_card]
                    print("Your cards are " + str(first_hand) + ' for a score of '+ str(first_hand_score) +'\n')
                
                while split_choice_2 != 'stand' and second_hand_score < 22:
                    split_choice_2 = input(" Your second hand is a " + str(second_hand) + "Would you like to hit or stand   ")
                    if split_choice_2.lower() == 'hit':
                        new_card = random.choice(list(cards.keys()))
                        second_hand.append(new_card)
                        second_hand_score += cards[new_card]
                    print("Your cards are " + str(second_hand) + ' for a score of '+ str(second_hand_score) +'\n')
                
            else:
                while choice != 'stand' and player_score < 22:
                    choice = input("Would you like to hit or stand   ")
                    if choice.lower() == 'hit':
                        new_card = random.choice(list(cards.keys()))
                        player.append(new_card)
                        player_score += cards[new_card]
                    if player_score > 21:
                        ace_count_temp_player = 0
                        for card in player:
                            if "Ace" in card:
                                ace_count_temp_player += 1
                        player_score -= ((ace_count_temp_player - ace_count_player)* 10)
                        ace_count_player = ace_count_temp_player
                    print("Your cards are " + str(player) + ' for a score of '+ str(player_score) +'\n')

            print('The dealer flips his second card and is showing a ' + str(dealer) + ' for a score of '+ str(dealer_score) + '\n')
            
        else:
            choice = input("Would you like to double down? Enter double. If not type no   ").lower()

        if choice == 'double':
            new_card = random.choice(list(cards.keys()))
            player.append(new_card)
            player_score += cards[new_card]
            print("Your cards are " + str(player) + ' for a score of '+ str(player_score) +'\n')
            
        else:
            while choice != 'stand' and player_score < 22:
                choice = input("Would you like to hit or stand   ")
                if choice.lower() == 'hit':
                    new_card = random.choice(list(cards.keys()))
                    player.append(new_card)
                    player_score += cards[new_card]
                if player_score > 21:
                    ace_count_temp_player = 0
                    for card in player:
                        if "Ace" in card:
                            ace_count_temp_player += 1
                    player_score -= ((ace_count_temp_player - ace_count_player)* 10)
                    ace_count_player = ace_count_temp_player
                print("Your cards are " + str(player) + ' for a score of '+ str(player_score) +'\n')
        
        print('The dealer flips his second card and is showing a ' + str(dealer) + ' for a score of '+ str(dealer_score) + '\n')
        
        while dealer_score < 17:
            new_card = random.choice(list(cards.keys()))
            dealer.append(new_card)
            dealer_score += cards[new_card]
            ace_count_temp_dealer = 0

            if dealer_score > 21:
                for card in dealer:
                    if "Ace" in card:
                        ace_count_temp_dealer += 1
                dealer_score -= ((ace_count_temp_dealer - ace_count_dealer)* 10)
                ace_count_dealer = ace_count_temp_dealer
            print("The dealer hits and has " + str(dealer) + ' for a score of '+ str(dealer_score) + '\n')
        
        if first_hand_score != 0:
            if first_hand_score > 21 and second_hand_score > 21:
                print("Sorry the dealer has won both hands \n")
                total_winnings -= bet
                total_winnings -= bet
                print("Your total winnings are " + str(total_winnings) +'\n')
                play = input("Would you like to play another hand - type y    ").lower()
                print('\n \n')
                continue
            if dealer > 21 and first_hand_score < 21 and second_hand_score < 21:
                print("You have won both hands \n")
                total_winnings += bet
                total_winnings += bet
                print("Your total winnings are " + str(total_winnings) +'\n')
                play = input("Would you like to play another hand - type y    ").lower()
                print('\n \n')
                continue

            if dealer_score > 21 and (first_hand_score < 21 or second_hand_score < 21):
                print('You have split with the dealer \n')
                print("Your total winnings are " + str(total_winnings) +'\n')
                play = input("Would you like to play another hand - type y    ").lower()
                print('\n \n')
                continue

            if dealer_score < first_hand_score and dealer_score < second_hand_score:
                print('You have won both hands \n')
                total_winnings += bet
                total_winnings += bet
                print("Your total winnings are " + str(total_winnings) +'\n')
                play = input("Would you like to play another hand - type y    ").lower()
                print('\n \n')
                continue
            else: 
                print('You have split with the dealer \n')
                print("Your total winnings are " + str(total_winnings) +'\n')
                play = input("Would you like to play another hand - type y    ").lower()
                print('\n \n')
                continue
        else:
            if choice == 'double':
                if player_score > 21:
                    print("Sorry the dealer has won \n")
                    total_winnings -= bet
                    total_winnings -= bet
                    print("Your total winnings are " + str(total_winnings) +'\n')
                    play = input("Would you like to play another hand - type y    ").lower()
                    print('\n \n')
                    continue

                if dealer_score > 21:
                    print('You have won \n')
                    total_winnings += bet
                    total_winnings += bet
                    print("Your total winnings are " + str(total_winnings) +'\n')
                    play = input("Would you like to play another hand - type y    ").lower()
                    print('\n \n')
                    continue

                if dealer_score < player_score:
                    print('You have won \n')
                    total_winnings += bet
                    total_winnings += bet
                    print("Your total winnings are " + str(total_winnings) +'\n')
                    play = input("Would you like to play another hand - type y    ").lower()
                    print('\n \n')
                    continue
                else:
                    print("Sorry the dealer has won \n")
                    total_winnings -= bet
                    total_winnings -= bet
                    print("Your total winnings are " + str(total_winnings) +'\n')
                    play = input("Would you like to play another hand - type y   ").lower()
                    print('\n \n')
                    continue
            else:
                if player_score > 21:
                    print("Sorry the dealer has won \n")
                    total_winnings -= bet
                    print("Your total winnings are " + str(total_winnings) +'\n')
                    play = input("Would you like to play another hand - type y    ").lower()
                    print('\n \n')
                    continue

                if dealer_score > 21:
                    print('You have won \n')
                    total_winnings += bet
                    print("Your total winnings are " + str(total_winnings) +'\n')
                    play = input("Would you like to play another hand - type y    ").lower()
                    print('\n \n')
                    continue

                if dealer_score < player_score:
                    print('You have won \n')
                    total_winnings += bet
                    print("Your total winnings are " + str(total_winnings) +'\n')
                    play = input("Would you like to play another hand - type y    ").lower()
                    print('\n \n')
                    continue
                else:
                    print("Sorry the dealer has won \n")
                    total_winnings -= bet
                    print("Your total winnings are " + str(total_winnings) +'\n')
                    play = input("Would you like to play another hand - type y   ").lower()
                    print('\n \n')
                    continue
        
play()

