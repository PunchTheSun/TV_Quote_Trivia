from backend.tv_Trivia import *
from frontend.menu_utils import *


if __name__ == "__main__":
    round_number = 0
    user_points = 0
    strikes = 3
    still_playing = True
    welcome_message()
    while still_playing:
        round_number += 1
        quotes = get_requests()
        answers = present_quotes_return_names(quotes, round_number)
        user_win_round = answer_attempt(answers)
        user_points, strikes = present_answers(answers, user_win_round, round_number, user_points, strikes)
        still_playing = check_still_playing(strikes)
    end_message(user_points, round_number)
