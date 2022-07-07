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
    #Setting up the Game 
    total_winnings = 0
    print(' \n Welcome to BlackJack Terminal Game \n')
    
    play = 'y'
    
    #While loop that runs the game over and over again until player choses to stop
    while play == 'y':
        bet = int(input('How much would you like to bet \n'))
        bet_side = int(input('How much would you like to bet on the Perfect Pair side bet. Type 0 if you do not want to. \n'))
        
        #Player and Dealer Lists that hold the player and dealer's cards 
        player = []
        dealer = []

        #Dealing the first two cards to the Player and Dealer
        player_first_card = random.choice(list(cards.keys()))
        player_second_card = random.choice(list(cards.keys()))

        player.append(player_first_card)
        player.append(player_second_card)

        dealer_first_card = random.choice(list(cards.keys()))
        dealer_second_card = random.choice(list(cards.keys()))

        dealer.append(dealer_first_card)
        dealer.append(dealer_second_card)
        
        #Score to keep track of how many points is in each player and dealer's hands
        player_score = 0
        dealer_score = 0
        ace_count_player = 0
        ace_count_dealer = 0
        perfect_pair = 'no'
        mixed_pair = 'no'
        for card in player:
            player_score += cards[card]
        for card in dealer:
            dealer_score += cards[card]
        if dealer_score > 21:
            dealer_score -= 20
            ace_count_dealer += 2
        
        if player_score > 21:
            player_score -= 20
            ace_count_player += 2
        
        print("Your cards are " + player[0] + " and a " + player[1] + ' for a score of '+ str(player_score) +'\n')
        print("The dealer is showing a " + dealer[0] + '\n')
        
        #If statements to track whether player has won the side bet or not off the first two cards
        if player_first_card == player_second_card and bet_side != 0:
            print('Congrats your cards are suited pairs. You win 30x your side bet \n')
            perfect_pair = 'yes'
            total_winnings += (30*bet_side)
        
        if (cards[player_first_card] == cards[player_second_card]) and ('Hearts' in player_first_card or 'Diamonds' in player_first_card) and ('Hearts' in player_second_card or 'Diamonds' in player_second_card) and perfect_pair == 'no':
            if cards[player_first_card] != 10:
                print('Congrats your cards are coloured pairs. You win 10x your side bet \n')
                mixed_pair = 'yes'
                total_winnings += (10*bet_side)
            else: 
                if ('Jack' in player_first_card and 'Jack' in player_second_card) or ('Queen' in player_first_card and 'Queen' in player_second_card) or ('King' in player_first_card and 'King' in player_second_card):
                    print('Congrats your cards are coloured pairs. You win 10x your side bet \n')
                    mixed_pair = 'yes'
                    total_winnings += (10*bet_side)
                else:
                    print('Sorry you lose your side bet \n')
                    total_winnings -= bet_side

        if (cards[player_first_card] == cards[player_second_card]) and ('Spades' in player_first_card or 'Clubs' in player_first_card) and ('Spades' in player_second_card or 'Clubs' in player_second_card) and perfect_pair == 'no':
            if cards[player_first_card] != 10:
                print('Congrats your cards are coloured pairs. You win 10x your side bet \n')
                mixed_pair = 'yes'
                total_winnings += (10*bet_side)
            else: 
                if ('Jack' in player_first_card and 'Jack' in player_second_card) or ('Queen' in player_first_card and 'Queen' in player_second_card) or ('King' in player_first_card and 'King' in player_second_card):
                    print('Congrats your cards are coloured pairs. You win 10x your side bet \n')
                    mixed_pair = 'yes'
                    total_winnings += (10*bet_side)
                else:
                    print('Sorry you lose your side bet \n')
                    total_winnings -= bet_side

        if (cards[player_first_card] == cards[player_second_card]) and perfect_pair == 'no' and mixed_pair == 'no' and bet_side != 0:
            if cards[player_first_card] != 10:
                print('Congrats your cards are regular pairs. You win 5x your side bet \n')
                total_winnings += (5*bet_side)
            else:
                if ('Jack' in player_first_card and 'Jack' in player_second_card) or ('Queen' in player_first_card and 'Queen' in player_second_card) or ('King' in player_first_card and 'King' in player_second_card):
                    print('Congrats your cards are regular pairs. You win 5x your side bet \n')
                    total_winnings += (5*bet_side)
                else:
                    print('Sorry you lose your side bet \n')
                    total_winnings -= bet_side
        if (cards[player_first_card] != cards[player_second_card]) and (player_first_card != player_second_card) and bet_side != 0:
            print('Sorry you lose your side bet \n')
            total_winnings -= bet_side

        #If statement to check whether player has BlackJack
        if player_score == 21:
            print('Congrats you got BlackJack you have won 1.5 times your bet')
            total_winnings += (bet*1.5)
            print("Your total winnings are " + str(total_winnings) +'\n')
            play = input("Would you like to play another hand - type y    ").lower()
            print('\n \n')
            continue
        
        
        choice = ''
        ace_count_split_1 = 0
        ace_count_split_2 = 0
        first_hand_score = 0
        second_hand_score = 0
        first_hand_done = 'no'
        
        #Case when Player has option to split cards
        if(cards[player_first_card] == cards[player_second_card]):
            choice = input("Would you like to double down or split? Enter double or split. If not type no   ").lower()

            #Player doubles down when there is oppurtunity to split
            if choice == 'double':
                new_card = random.choice(list(cards.keys()))
                player.append(new_card)
                player_score += cards[new_card]
                if player_score > 21:
                        ace_count_temp_player = 0
                        for card in player:
                            if "Ace" in card:
                                ace_count_temp_player += 1
                        player_score -= ((ace_count_temp_player - ace_count_player)* 10)
                print("Your cards are " + str(player) + ' for a score of '+ str(player_score) +'\n')

            #Player splits when has the option to split
            if choice == 'split':
                
                split_choice_1 = ''
                split_choice_2 = ''
                
                #List holding the first and second split hands
                first_hand = []
                second_hand = []
                first_hand.append(player_first_card)
                first_hand.append(random.choice(list(cards.keys())))
                second_hand.append(player_second_card)
                second_hand.append(random.choice(list(cards.keys())))
                
                for card in first_hand:
                    first_hand_score += cards[card]   
                
                for card in second_hand:
                    second_hand_score += cards[card]
                #While loop to define how a player plays the first hand
                if first_hand_score == 22:
                    first_hand_score -= 20
                    ace_count_split_1 += 2
                
                if second_hand_score == 22:
                    second_hand_score -= 20
                    ace_count_split_2 += 2
                
                while split_choice_1 != 'stand' and first_hand_score < 22:
                    split_choice_1 = input("\n Your first hand is a " + str(first_hand) + ' for a score of '+ str(first_hand_score) +  " \n Would you like to hit or stand   ")
                    
                    if split_choice_1.lower() == 'hit':
                        new_card = random.choice(list(cards.keys()))
                        first_hand.append(new_card)
                        first_hand_score += cards[new_card]
                    
                    if first_hand_score > 21:
                        ace_count_temp_split_1 = 0
                        for card in first_hand:
                            if "Ace" in card:
                                ace_count_temp_split_1 += 1
                        first_hand_score -= ((ace_count_temp_split_1 - ace_count_split_1)* 10)
                        ace_count_split_1 = ace_count_temp_split_1
                    if first_hand_score > 21:
                        print('You have busted the first hand with a ' + str(first_hand) + ' for a score of '+ str(first_hand_score) + '\n')
    
                
                #While loop to define how a player plays the second hand
                while split_choice_2 != 'stand' and second_hand_score < 22:
                    split_choice_2 = input(" Your second hand is a " + str(second_hand) + ' for a score of '+ str(second_hand_score) +  " \n Would you like to hit or stand   ")
                    if split_choice_2.lower() == 'hit':
                        new_card = random.choice(list(cards.keys()))
                        second_hand.append(new_card)
                        second_hand_score += cards[new_card]
                    if second_hand_score > 21:
                        ace_count_temp_split_2 = 0
                        for card in first_hand:
                            if "Ace" in card:
                                ace_count_temp_split_2 += 1
                        second_hand_score -= ((ace_count_temp_split_2 - ace_count_split_2)* 10)
                        ace_count_split_2 = ace_count_temp_split_2
                    if second_hand_score > 21:
                        print('You have busted the second hand with a ' + str(second_hand) + ' for a score of '+ str(second_hand_score) + '\n')
            
            #If player chooses not to split or double down when he/she has option to split  
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
        
        #Case when player has cards that can not be split
        else:
            choice = input("Would you like to double down? Enter double. If not type no   ").lower()

            #Player choses to double down
            if choice == 'double':
                new_card = random.choice(list(cards.keys()))
                player.append(new_card)
                player_score += cards[new_card]
                if player_score > 21:
                        ace_count_temp_player = 0
                        for card in player:
                            if "Ace" in card:
                                ace_count_temp_player += 1
                        player_score -= ((ace_count_temp_player - ace_count_player)* 10)
                print("Your cards are " + str(player) + ' for a score of '+ str(player_score) +'\n')
                
            #Player choses to not double down 
            else:
                #while loop for how a player plays his/her hand
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
        
        #Dealer flips second card and plays hand according to dealer rules
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
        

        #Keeping track of who wins in cases of spliting
        if first_hand_score != 0:
            if first_hand_score > 21:
                first_hand_done = 'yes'
                print("Sorry the dealer has won the first hand \n")
                total_winnings -= bet
                
            if dealer_score > 21 and first_hand_score < 22 and first_hand_done == 'no':
                first_hand_done = 'yes'
                print("You have won the first hand \n")
                total_winnings += bet

            if dealer_score >= first_hand_score and first_hand_done == 'no':
                first_hand_done = 'yes'
                print("Sorry the dealer has won the first hand \n")
                total_winnings -= bet

            if first_hand_score > dealer_score and first_hand_done == 'no':
                first_hand_done = 'yes'
                print("You have won the first hand \n")
                total_winnings += bet
            
            if second_hand_score > 21 :
                print("Sorry the dealer has won the second hand \n")
                total_winnings -= bet
                print("Your total winnings are " + str(total_winnings) +'\n')
                play = input("Would you like to play another hand - type y    ").lower()
                print('\n \n')
                continue
                
            if dealer_score > 21 and second_hand_score < 22:
                print("You have won the second hand \n")
                total_winnings += bet
                print("Your total winnings are " + str(total_winnings) +'\n')
                play = input("Would you like to play another hand - type y    ").lower()
                print('\n \n')
                continue

            if dealer_score >= second_hand_score:
                print("Sorry the dealer has won the second hand \n")
                total_winnings -= bet
                print("Your total winnings are " + str(total_winnings) +'\n')
                play = input("Would you like to play another hand - type y    ").lower()
                print('\n \n')
                continue

            if second_hand_score > dealer_score:
                print("You have won the second hand \n")
                total_winnings += bet
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