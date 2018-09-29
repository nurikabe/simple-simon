import os
import random
import time
import colorama
import sys


class Player:
    """Player model"""

    def __init__(self):
        self.score = 0

    def increment_score(self):
        self.score = self.score + 1


class Simon:
    """Simon model"""

    def __init__(self):
        self.history = []
        self.colors = [
            ('r', colorama.Fore.RED + 'Red'),
            ('y', colorama.Fore.YELLOW + 'Yellow'),
            ('g', colorama.Fore.GREEN + 'Green'),
            ('b', colorama.Fore.BLUE + 'Blue')
        ]

    def add_random_color(self):
        random_color = random.choice(self.colors)
        self.history.append(random_color)

    def get_level_number(self):
        return len(self.history)


class Game:
    """Game controller"""

    def __init__(self):
        self.simon = Simon()
        self.player = Player()
        self.over = False

    def clear_screen(self):
        os.system('clear')  # Un*x
        os.system('cls')  # Windows

    def next_level(self):
        """Advance to the next level"""

        self.simon.add_random_color()
        self.print_level()

        if self.test_player():
            self.player.increment_score()
        else:
            self.over = True

    def print_level(self):
        """Print round, score, and colors for the current level"""

        # Clear screen when starting
        self.clear_screen()

        # Show the round number and score
        print(colorama.Fore.WHITE + "Level #{}".format(self.simon.get_level_number()), end=" ")
        print("[{} points]".format(self.player.score))

        # Briefly show each color
        for color in self.simon.history:
            print(color[1], end=' ')
            sys.stdout.flush()  # Force newline
            time.sleep(1)

        # Clear screen when done
        self.clear_screen()

    def test_player(self):
        """Ask player for the next guess"""

        print(colorama.Fore.WHITE + "Level #{}".format(self.simon.get_level_number()), end=" ")
        print("[{} points]".format(self.player.score))

        for count, color in enumerate(self.simon.history):
            key = input("Color #{} [r, g, b, y]: ".format(count + 1))
            if key != color[0]:
                return False

        return True


game = Game()
while not game.over:
    game.next_level()

print("You scored {} points!".format(game.player.score))
