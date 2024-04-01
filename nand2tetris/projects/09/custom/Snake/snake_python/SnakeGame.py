from tkinter import *
from game_config import *
from helper import *
import Snake 
import Food
# initialize all the configuration of the game
# set the stage for the player to play

class SnakeGame:
    def __init__(self):
        # initialize fields
        self.score = 0
        self.direction = 'down'
        self.canvas = None
        self.label = None

        # craete game window
        self.window = Tk()

    def create_screen(self):
        self.window.title(game_config['TITLE'])
        self.window.resizable(False, False)

        self.label = Label(
            self.window,
            text="Score:{}".format(self.score),
            font=(game_config['FONT'], game_config['FONT_SIZE']),
        )


        self.canvas = Canvas(
            self.window, 
            bg = game_config['BACKGROUND_COLOR'], 
            width=game_config['GAME_WIDTH'],
            height=game_config['GAME_HEIGHT'],
            )
        
        
        # bind the widgets to the window
        self.label.pack()
        self.canvas.pack()
        
        #center_screen(self.window)



    def run(self):
        # initialize display
        self.create_screen()

        # create game objects
        self.snake = Snake.Snake(self.canvas)
        self.food = Food.Food(self.canvas) 

        # move the snake
        self.next_turn()

        # control the objects
        control_snake(self.window, self.change_direction)



        self.window.mainloop()


    def next_turn(self):
        x, y = self.snake.coordinates[0]

        # modify the coordinate of the snake for the next turn
        if self.direction == 'up':
            y -= game_config['SPACE_SIZE']
        elif self.direction == 'down':
            y += game_config['SPACE_SIZE']
        elif self.direction == 'left':
            x -= game_config['SPACE_SIZE']
        elif self.direction == 'right':
            x += game_config['SPACE_SIZE']

        self.snake.coordinates.insert(0, (x, y))

        # create body part for the new coordinate
        square = self.canvas.create_rectangle(
            x, y, x+game_config['SPACE_SIZE'], y+game_config['SPACE_SIZE'], fill=game_config['SNAKE_COLOR']
        )
        self.snake.squares.insert(0, square)

        # check if snake gets the food 
        if x == self.food.coordinate[0] and y == self.food.coordinate[1]:
            self.score += 1
            self.label.config(text="Score:{}".format(self.score))
            self.canvas.delete('food')
            self.food = Food.Food(self.canvas)
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]
        
        if self.check_collision():
            self.game_over()
        else:
            # update window
            self.window.after(game_config['SPEED'], self.next_turn)

    def change_direction(self, new_direction):
       if new_direction == 'left' and self.direction != 'right':
          self.direction = new_direction
       elif new_direction == 'right' and self.direction != 'left':
          self.direction = new_direction
       elif new_direction == 'up' and self.direction != 'down':
          self.direction = new_direction
       elif new_direction == 'down' and self.direction != 'up':
          self.direction = new_direction
    

    def check_collision(self):
        x, y = self.snake.coordinates[0]
        if x < 0 or x >= game_config['GAME_WIDTH']:
            return True 
        elif y < 0 or y >= game_config['GAME_HEIGHT']:
            return True 
        else:
            for body_part in self.snake.coordinates[1:]:
                if x == body_part[0] and y == body_part[1]:
                    return True
        return False 

    def game_over(self):
        text_width = int(self.canvas.winfo_width() / 2)
        text_height = int(self.canvas.winfo_height() / 2)
        self.canvas.delete(ALL)
        self.canvas.create_text( text_width, text_height, text="GAME OVER", fill='#FF0000' )