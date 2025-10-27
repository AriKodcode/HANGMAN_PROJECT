from hangman.words import select_a_word
from data.tests import data


def init_state(secret: str, max_tries: int) -> dict:
    display = []
    for char in secret:
        display.append("_")
    result = {
        "secret": secret,
        "display": display,
        "guessed": [],
        "wrong_guesses": 0,
        "max_tries": max_tries
    }

    return result

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) == 1:
        if ch in guessed:
            return True, " You already guessed it."
        else:
            return False, "ist not in guessed"
    else:
        return False, "press only one char"


def apply_guess(state: dict, ch: str) -> bool:
    count = 0
    change = False
    for char in state["secret"]:
        if ch == char:
            state["display"][count] = char
            state["guessed"] += char
            change = True
        count += 1
    if change:
        return True
    else:
        state["wrong_guesses"] += 1
        return False



def is_won(state: dict) -> bool:
    check = ""
    for char in state["display"]:
        check += char
    if check == state["secret"]:
        return True
    else:
        return False

def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    else:
        return False


def render_display(state: dict) -> str:
    return state["display"]

def render_summary(state: dict) -> str:
    new = str(state["guessed"])
    return "the secret word its: " + state["secret"] + "and the char guessed its: " + new
