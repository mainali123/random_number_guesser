import random
hard_try = 5
easy_try = 10
random_number = random.choice(range(0, 101))

def easy():
    global easy_try
    global random_number
    if easy_try == 0:
        return_ = f"You lost! The answer was {random_number}"
        exit(return_)

    print(f"You have {easy_try} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == random_number:
        return_ = f"You got it! The answer was {random_number}"
        exit(return_)
    elif guess > random_number:
        print("Too high.")
        if guess != 1:
            print("Guess again.")
        easy_try -= 1
        easy()
    elif guess < random_number:
        print("Too low.")
        if guess != 1:
            print("Guess again.")
        easy_try -= 1
        easy()
    else:
        pass

def hard():
    global hard_try
    global random_number
    if hard_try == 0:
        return_ = f"You lost! The answer was {random_number}"
        exit(return_)

    print(f"You have {hard_try} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == random_number:
        return_ = f"You got it! The answer was {random_number}"
        print(return_)
        return
    if guess > random_number:
        print("Too high.")
        if guess != 1:
            print("Guess again.")
        hard_try -= 1
        hard()
    elif guess < random_number:
        print("Too low.")
        if guess != 1:
            print("Guess again.")
        hard_try -= 1
        hard()
    else:
        pass


def main():
    user_input = input("Choose a dificulty. Type 'easy' or 'hard': ")
    if user_input == 'easy':
        print(easy())
    elif user_input == 'hard':
        print(hard())
    else:
        print("Invalid input. Please enter again")
        main()


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    main()