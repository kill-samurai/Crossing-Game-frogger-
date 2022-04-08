from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.setpos(-280, 260)
        self.starting_point = 0
        self.write_board()
        self.hideturtle()


    def write_board(self):
        self.clear()
        self.write(f"Level: {self.starting_point}", align="left", font=FONT)

    def add_point(self):
        self.starting_point += 1
        self.write_board()

    def lost_game(self):
        self.setpos(0, 0)
        self.write("Game Over.", align="center", font=FONT)
