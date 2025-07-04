import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(name = image)

turtle.shape(image)

# def get_mouse_click_cords(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cords)
# turtle.mainloop()
# screen.exitonclick()

states = pd.read_csv("50_states.csv")
all_states = states["state"].to_list()
total_states = len(states)
guessed_states = []
print(total_states)

while len(guessed_states) <= total_states:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/{total_states} States Correct", prompt = "What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = {"state": []}

        for state in all_states:
            if state not in guessed_states:
                missing_states["state"].append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # If answer state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        new_x = states[states["state"] == answer_state]["x"].to_list()[0]
        new_y = states[states["state"] == answer_state]["y"].to_list()[0]

        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(new_x, new_y)
        new_turtle.write(arg = answer_state)

# states_to_learn.csv

