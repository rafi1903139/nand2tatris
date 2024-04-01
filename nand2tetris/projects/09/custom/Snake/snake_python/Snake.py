from game_config import *
# construct the snake object and 
# controls it in the canvas

class Snake:
    def __init__(self, canvas):
      self.body_size = game_config['BODY_PARTS'] 
      self.coordinates = []
      self.squares = []

      block_size = game_config['SPACE_SIZE']
      # initialize snake body parts location
      for i in range(self.body_size):
         self.coordinates.append([0,0])
    
      # construct body parts of the snake
      for x, y in self.coordinates:
         square = canvas.create_rectangle(
            x, y, x+block_size, y+block_size, fill=game_config['SNAKE_COLOR'], tag="snake"
         )

         self.squares.append(square)

   