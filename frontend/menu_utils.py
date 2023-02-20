import random


def present_quotes_return_names(quotes: list[dict[str]], round_number: int) -> dict:
    series_names = []
    series_names_dict = {}
    random.shuffle(quotes)
    print(f"\n*********************************************************"
          f"\n                      ROUND {round_number}:"
          f"\n*********************************************************")
    for i, quote in enumerate(quotes):
        key = iter(quote.keys()).__next__()
        series_names.append(key)
        print(f"Quote {i+1}: {quote[key]}")
    for j, name in enumerate(series_names):
        series_names_dict[j+1] = name
    print()
    return series_names_dict


def answer_attempt(answers: dict) -> bool:
    answers_attempt = []
    series_names = ["The Office", "The Simpsons", "Breaking Bad"]
    valid_answers = 0
    while True:
        not_valid_number = True
        while not_valid_number:
            current_attempt = input(f'Enter the quote number for the quote taken from the show "{series_names[valid_answers]}": ')
            if current_attempt.isnumeric():
                if int(current_attempt) in [1, 2, 3] and int(current_attempt) not in answers_attempt:
                    answers_attempt.append(int(current_attempt))
                    valid_answers += 1
                    not_valid_number = False
                elif int(current_attempt) not in [1, 2, 3]:
                    print("Invalid input, Please enter a number between 1 to 3 only")
                else:
                    print("Already selected that number, Please try a different one")
            else:
                print("Invalid input, Please enter numbers only")
        if valid_answers == 3:
            break
    translate_back = {answers_attempt[0]: "the_office", answers_attempt[1]: "the_simpsons", answers_attempt[2]: "breaking_bad"}
    for user_answer in answers_attempt:
        if translate_back[user_answer] != answers[user_answer]:
            return False
    return True


def present_answers(answers: dict, user_win: bool, round_number: int, user_points: int, user_strikes: int) -> (int, int):
    answers_translate_dict = {"the_office": "The Office", "the_simpsons": "The Simpsons", "breaking_bad": "Breaking Bad"}
    print("\nAnd now the answers: ")
    for i, answer in enumerate(answers.values()):
        print(f'Quote number {i+1} is from the TV Series: "{answers_translate_dict[answer]}"')
    if user_win:
        print(f"\nCongratulations! you answered correctly\n+{round_number*10} points!")
        user_points += round_number*10
        print(f"Current points: {user_points}")
    else:
        user_strikes -= 1
        print(f"\nSorry! you answered wrong\nStrikes left: {user_strikes}")
    return user_points, user_strikes


def check_still_playing(user_strikes: int) -> bool:
    check_playing_dict = {'y': True, 'n': False}
    if user_strikes <= 0:
        return False
    while True:
        user_input = input("Continue playing? (Y/N): ")
        if user_input.lower() in ['y', 'n']:
            return check_playing_dict[user_input.lower()]
        else:
            print("Invalid input, Please only enter 'Y' for yes or 'N' for no")


def welcome_message():
    print("Welcome to TV-Trivia!!\nEveryone's favorite TV quote guessing show\n"
          "\nThe rules are simple:\n3 Quotes will appear on the screen"
          "\nGuess from which TV Series each quote is taken from to win points!"
          "\nGuess wrong and you'll get a strike - 3 Strikes and you'rrrrrrreeeee OUT!!"
          "\nGood luck! and lets get guessing!!")


def end_message(user_points: int, user_rounds: int):
    print(f"\nThank you for playing TV-Trivia!\nYour score: {user_points}\nRounds played: {user_rounds}")
