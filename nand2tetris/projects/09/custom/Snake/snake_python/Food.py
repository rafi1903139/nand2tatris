import random
from game_config import *


# construct the food object 
class Food:
    def __init__(self, canvas):
        x = self.get_point()
        y = self.get_point()
        self.coordinate = [x, y]
        self.create_food(canvas)

    # return a random location based on gamewidth and height
    def get_point(self):
        point = random.randint(0, game_config['GAME_WIDTH'] / game_config['SPACE_SIZE'] - 1) * game_config['SPACE_SIZE']
        
        return point

    # display food on the screen
    def create_food(self, canvas):
        x = self.coordinate[0]
        y = self.coordinate[1]
        food_size = game_config['SPACE_SIZE']

        canvas.create_oval(x, y, x+food_size, y+food_size, fill=game_config['FOOD_COLOR'], tag='food')