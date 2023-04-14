import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

score = 0
states_list = []
while score != 50:
    user_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another states name?").title()
    if user_answer == "Exit":
        missing_states = [state for state in data["state"].tolist() if state not in states_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_lean.csv")
        break
    if user_answer in data["state"].tolist() and user_answer not in states_list:
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        state_row = data[data["state"] == user_answer]
        new_state.goto(x=int(state_row.x), y=int(state_row.y))
        new_state.write(user_answer)
        states_list.append(user_answer)
        score += 1




