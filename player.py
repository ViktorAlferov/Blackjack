#Player module


class Player(object):
    """ A player for a game. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

answer = ask_yes_no("\nDo you like Python 3? Please enter 'y' or 'n': ")


answer_2 = ask_number("\nPlease select the number from 1 to 6: ", low=1, high=6)

input("\n\nPress the enter key to exit.")

"""if __name__ == "__main__":
    print("This module imports. But you run it directly.")
    input("\n\nPress the enter key to exit.")"""
