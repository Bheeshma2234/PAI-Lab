def minimax_guess(low, high):
    """
    Minimax strategy for number guessing.
    Always choose the midpoint to minimize worst-case range.
    """
    return (low + high) // 2


def play_game():
    print("Think of a number.")
    low = int(input("Enter lower bound: "))
    high = int(input("Enter upper bound: "))

    print(f"\nThink of a number between {low} and {high}.")
    print("Respond with:")
    print("'h' if guess is too high")
    print("'l' if guess is too low")
    print("'c' if correct\n")

    attempts = 0

    while low <= high:
        guess = minimax_guess(low, high)
        attempts += 1

        print(f"\nAI guesses: {guess}")
        feedback = input("Your response (h/l/c): ").lower()

        if feedback == 'c':
            print(f"🎉 AI found your number in {attempts} moves!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input.")

    else:
        print("Something went wrong. Were the answers consistent?")


play_game()
