def prompt_guess() -> str:
    char = input("guess a char")
    return char

def print_status(state: dict) -> None:
    print("guessed: " ,state["guessed"], "wrong_guesses: ", state["wrong_guesses"])


def print_result(state: dict) -> None:
    print(state)
