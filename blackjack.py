import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_deal = True
end_game = False
def deal_card():
    card_picked = random.choice(cards)
    print(card_picked)
    return card_picked

while end_game == False:
    user_cards = []
    computer_cards = []
    print("Computer draws: ")
    computer_cards.append(deal_card())
    print("Your cards are: ")
    user_cards.append(deal_card())
    user_cards.append(deal_card())

    print(f"The current sum is {sum(user_cards)}")
    while user_deal == True:
        if sum(user_cards) < 21:
            user_choice = input("Hit or stay?")
            if user_choice == 'hit':
                user_cards.append(deal_card())
                if sum(user_cards)>21:
                    for card in user_cards:
                        if card == 11:
                            user_cards[user_cards.index(11)] = 1
                print(sum(user_cards))
                continue
            else:
                user_cards
                user_deal == False
                break
        elif sum(user_cards) == 21:
            user_deal == False
            break
        elif sum(user_cards) > 21:
            print("You lose.")
            end_game == True

    #computer_cards.append(deal_card())
    print(f"Dealer currently has {sum(computer_cards)}")
    while sum(computer_cards) < sum(user_cards) and sum(computer_cards)<21:
        computer_cards.append(deal_card()) 
        if sum(computer_cards)>21:
            for card in computer_cards:
                if card == 11:
                    computer_cards[computer_cards.index(11)] = 1
                else:
                    pass
            print(f"Dealer has {sum(computer_cards)}. You win.")
        elif sum(computer_cards) > sum(user_cards) and sum(computer_cards)<21:
            print(f"Dealer has {sum(computer_cards)}. You lose")
        elif sum(computer_cards) == sum(user_cards):
            print(f"Dealer has {sum(computer_cards)}. Nobody wins")

