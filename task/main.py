
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(hand):
    score = sum(hand)

    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score


play_again = True

while play_again:
    user_decks = [random.choice(cards) for _ in range(2)]
    computer_decks = [random.choice(cards) for _ in range(2)]

    user_score = calculate_score(user_decks)
    computer_score = calculate_score(computer_decks)

    print(art.logo)
    print(f"Your cards: {user_decks}, score: {user_score}")
    print(f"Computer's first card: {computer_decks[0]}")

    while user_score < 21:
        another_card = input("Type 'y' to draw or 'n' to pass: ")

        if another_card == "y":
            user_decks.append(random.choice(cards))
            user_score = calculate_score(user_decks)
            print(f"Your cards: {user_decks}, score: {user_score}")
        else:
            break

    while computer_score < 17:
        computer_decks.append(random.choice(cards))
        computer_score = calculate_score(computer_decks)

    print(f"Your final hand: {user_decks}, score: {user_score}")
    print(f"Computer's hand: {computer_decks}, score: {computer_score}")

    if user_score > 21:
        print("You lose!")
    elif computer_score > 21:
        print("Computer busts. You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")

    want_continue = input("Play again? Type 'y' or 'n': ")
    if want_continue != "y":
        play_again = False

print("Game exited.")