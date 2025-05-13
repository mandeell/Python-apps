class GameController:
    """Manages game start and replay prompts for the coffee machine program."""

    def start_game(self):
        """Prompts user to start the game, returns True for 'y', False for 'n'."""
        while True:
            play_game = input(
                "Do you want to play this game? Type 'y' or 'n': ").lower()
            if play_game in ['y', 'n']:
                return play_game == 'y'
            print("Invalid input. Please type 'y' or 'n'.")

    def play_again(self):
        """Prompts user to play again, returns True for 'y', False for 'n'."""
        while True:
            response = input(
                "\nDo you want to play again? Type 'y' or 'n': ").lower()
            if response in ['y', 'n']:
                return response == 'y'
            print("Invalid input. Please type 'y' or 'n'.")

    def run(self, main_func, clear_screen_func):
        """Runs the game loop, calling main and clear_screen functions."""
        if self.start_game():
            while True:
                clear_screen_func()
                main_func()
                if not self.play_again():
                    break
