from hangman.game import render_display,render_summary,is_won,is_lost,init_state,apply_guess,validate_guess
from hangman.words import select_a_word
from hangman.io import prompt_guess,print_result,print_status
from data.tests import data


def play(words: list[str], max_tries: int = 2) -> None:
    word = select_a_word(words)
    print(word)
    dict_status = init_state(word,max_tries)
    win = False
    while not win:
        while dict_status["wrong_guesses"] != dict_status["max_tries"]:
            print_status(dict_status)
            print(dict_status["display"])
            render_display(dict_status)
            char = prompt_guess()
            check1 = validate_guess(char,dict_status["guessed"])
            if check1 == (True, " You already guessed it."):
                break
            if check1 ==(False, "ist not in guessed"):
                check2 = apply_guess(dict_status,char)
                if check2:
                    print("A good guess")
                    break
                else:
                    print("Bad guess, try again.")
                    break
        check_win = is_won(dict_status)
        if check_win:
            win = True
            break
        if dict_status["wrong_guesses"] == dict_status["max_tries"]:
            break

    print(render_summary(dict_status))
    check_lose = is_lost(dict_status)
    if check_lose:
        print("you win! \n Summary: ",print_result(dict_status))
    else:
        print("you lose! \n Summary: ",print_result(dict_status))








if __name__ == "__main__":
    play(data)