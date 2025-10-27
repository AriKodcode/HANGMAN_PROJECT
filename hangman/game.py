from hangman.words import select_a_word
from data.tests import data


def init_state(secret: str, max_tries: int) -> dict:
    display = []
    for char in secret:
        display.append("_")
    result = {
        "secret": secret,
        "display": display,
        "guessed": set[str],
        "wrong_guesses": int,
        "max_tries": max_tries
    }

    return result

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) == 1:
        if ch not in guessed:
            return tuple(True, "Correct guess")
        else:
            return tuple(False, "You already guessed")
    else:
        return tuple(False, "press only one char")


def apply_guess(state: dict, ch: str) -> bool:
    if ch in state["guessed"]:
        return True
    else:
        return False



def is_won(state: dict) -> bool:
    if state["guessed"] == state["secret"]:
        return True
    else:
        return False

def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    else:
        return False


def render_display(state: dict) -> str:
    summary = state["display"]
    return summary

def render_summary(state: dict) -> str;
