import art
import random
print(art.logo)

def blackjack():

  deck = [11,2,3,4,5,6,7,8,9,10,10,10]
  
  player_cards = []
  player_cards.append(random.choice(deck))
  player_cards.append(random.choice(deck))
  player_score = player_cards[0] + player_cards[1]
  plus_player_card = 2
  print(f'Your cards: {player_cards} Your current score: {player_score}')
  
  computer_cards = []
  computer_cards.append(random.choice(deck))
  computer_score = computer_cards[0]
  plus_computer_card = 1
  print(f'Computer score {computer_score}')
  
  if player_score == 21:
    print('Player wins')
  
  def player_winning(player,computer):
    if player > computer:
      return True
    else:
      return False
  
  def is_Ace(card):
    if card == 11:
      return True
  
  player_still_playing = True
  computer_still_playing = True
  another_game = True
  
  
  
  while another_game:
    while player_still_playing:
      first_play = input('Play another card? y or n \n').lower()
      if first_play == 'y':
        player_cards.append(random.choice(deck))
        player_score += player_cards[plus_player_card]
        plus_player_card += 1
        print(f'Your cards: {player_cards} Your current score: {player_score}')
        if is_Ace(player_cards[-1]) and player_score >= 22:
          player_cards[-1] = 1
        if not is_Ace(player_cards[-1]) and player_score >= 22:
          print(f'Your cards: {player_cards}, players score is {player_score} computer wins')
          computer_still_playing = False
          break
      else:
        player_still_playing = False
      
    if len(player_cards) == 5 and player_score <= 21:
      print('player wins')
      
      
    while computer_still_playing:
      if is_Ace(computer_cards[-1]) and computer_score >= 22:
        player_cards[-1] = 1
      if not is_Ace(computer_cards[-1]) and computer_score >= 22:
        print(f'computers score is {computer_score} player wins')
        computer_still_playing = False
      elif not player_winning(player_score,computer_score) and computer_score < 22:
        print(f' players score is {player_score} but computers score is {computer_score} computer wins')
        computer_still_playing = False
      else:
        computer_cards.append(random.choice(deck))
        computer_score += computer_cards[plus_computer_card]
        plus_computer_card += 1
        print(f'computer cards:{computer_cards}, computer score: {computer_score}')
    
    play_again = input("Play again? 'y' for yes, 'n' for no\n")
    if play_again == 'y':
      another_game = True
      blackjack()
    else:
      another_game = False

blackjack()