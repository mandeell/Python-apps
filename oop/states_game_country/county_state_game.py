import turtle
import pandas as pd
from turtle import Turtle, Screen


class CountryStatesGame:
    def __init__(self, country_name, map_image, states_csv):
        self.country_name = country_name
        self.map_image = map_image
        self.states_csv = states_csv
        self.states_data = pd.DataFrame()
        self.all_states = []
        self.guessed_states = []
        self.screen = Screen()
        self.setup_game()

    def setup_game(self):
        """Initialize game screen and load data"""
        self.screen.title(f"{self.country_name} States Game")
        self.screen.addshape(self.map_image)
        turtle.shape(self.map_image)
        self.states_data = pd.read_csv(self.states_csv)
        self.all_states = self.states_data.state.to_list()

    def check_answer(self, answer):
        """Check if the answer is correct and plot on the map"""
        state_data = self.states_data[self.states_data.state == answer]
        if not state_data.empty:
            t = Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            t.write(answer, align="center", font=("Arial", 5, "normal"))
            return True
        return False

    def run_game(self):
        """Main game loop"""
        while len(self.guessed_states) < len(self.all_states):
            answer = self.screen.textinput(
                title=f"{len(self.guessed_states)}/{len(self.all_states)} States",
                prompt="Name a state:").title()

            if answer in ["Exit", None]:
                break

            if answer in self.all_states and answer not in self.guessed_states:
                if self.check_answer(answer):
                    self.guessed_states.append(answer)

        self.save_missing_states()
        self.screen.mainloop()

    def save_missing_states(self):
        """Generate CSV of states not guessed"""
        missing = [s for s in self.all_states if s not in self.guessed_states]
        pd.DataFrame(missing).to_csv(f"missing_{self.country_name.lower()}_states.csv")