import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_deal = True
new_game = True

def deal_card():
    card_picked = random.choice(cards)
    return card_picked

while new_game == True:
    user_cards = []
    computer_cards = []

    computer_cards.append(deal_card())
    print(f"Computer draws: {computer_cards}")
    for _ in range(2):
        user_cards.append(deal_card())
    print(f"Your cards are: {user_cards}. The current sum is {sum(user_cards)}")

    while user_deal == True:
        if sum(user_cards) < 21:
            user_choice = input("Hit or stay? ")
            if user_choice == "hit":
                user_cards.append(deal_card())
                if sum(user_cards)>21:
                    for card in user_cards:
                        if card == 11:
                            user_cards[user_cards.index(11)] = 1
                print(sum(user_cards))
                continue
            else:
                user_deal == False
                break
        elif sum(user_cards) == 21:
            user_deal == False
            break
        elif sum(user_cards) > 21:
            print("You lose.")
            break

    if sum(user_cards)<=21:
    #computer_cards.append(deal_card())
        print(f"Dealer cards: {computer_cards} with a sum of {sum(computer_cards)}")

        while sum(computer_cards) < sum(user_cards) and sum(computer_cards)<=21:
            computer_cards.append(deal_card()) 
            print(f"Dealer got {deal_card()}. All cards are: {computer_cards}")
            if sum(computer_cards)>21:
                for card in computer_cards:
                    if card == 11:
                        computer_cards[computer_cards.index(11)] = 1
                    else:
                        pass
                print(f"Dealer has {sum(computer_cards)}. You win.")
            elif sum(computer_cards) > sum(user_cards) and sum(computer_cards)<=21:
                print(f"Dealer has {sum(computer_cards)}. You lose")
            elif sum(computer_cards) == sum(user_cards):
                print(f"Dealer has {sum(computer_cards)}. Nobody wins")
    else:
        pass
        
    play_again = input("Do you want to play again? Y/N ")
    if play_again == "y":
        new_game == True
    else:
        break
    