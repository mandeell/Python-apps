import turtle as t
from turtle import Turtle, Screen
import pandas

# Setup screen and image
screen = Screen()
screen.setup(900, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

# Load state data
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states =[]

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} States Correct",
        prompt="What's another state's name?")
    # Exit game if user types 'exit'
    if answer_state is None or answer_state.title() == "Exit":
        break
    answer_state = answer_state.title()
    # check if the answer is correct
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = states_data[states_data.state == answer_state]
        t= Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state,align="center", font=("Arial", 4, "normal"))

missing_states = [state for state in all_states if state not in guessed_states]
pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")

screen.mainloop()
