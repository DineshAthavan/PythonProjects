import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.pencolor("black")
writer.speed("fastest")


state_data = pandas.read_csv("50_states.csv")
states_list = state_data.state.to_list()
missed_states = states_list
game_on = True
num_guesses = 0
corr_guess = 0
guessed_states = []

while game_on:
    user_input = screen.textinput(title=f"Guesses the State  Guesses:{num_guesses}/50", prompt="Enter State name:")
    if user_input == "exit":
        game_on = False
        break
    for state in states_list:
        if state.lower() == user_input.lower():
            state_details = state_data[state_data.state == state]
            if user_input.lower() not in guessed_states:
                writer.goto(int(state_details.x.to_string(index=False)), int(state_details.y.to_string(index=False)))
                writer.pendown()
                writer.write(state_details.state.to_string(index=False), False, align="center", font=("arial", 8, "normal"))
                writer.penup()
                corr_guess += 1
                missed_states.remove(state)
            break
    num_guesses += 1
    guessed_states.append(user_input.lower())
    if num_guesses == 50:
        game_on = False
        print(f"You guessed {corr_guess}/50 states correctly")

print(f"Missed states list:\n{missed_states}")



