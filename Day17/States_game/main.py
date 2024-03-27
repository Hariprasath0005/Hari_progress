import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S states gaame")
image = "./Day17/States_game/india_map.gif"
screen.setup(width = 700, height = 700)
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./Day17/States_game/states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states)<29:
    ans_states = screen.textinput(title=f"{len(guessed_states)}/29 states correct",prompt="What's another state's name?").title()
    print(ans_states)
    if ans_states == "Exit":
        missed_states = [i for i in all_states if i not in guessed_states]
        states_dict = {"Missed states":missed_states}
        pandas.DataFrame(states_dict).to_csv("./Day17/States_game/missed_states.csv")
        break
    if ans_states in all_states:
        guessed_states.append(ans_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state ==ans_states]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())



