from tkinter import *

# centers the window
def center_screen(window):
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int( screen_width / 2 - window_width / 2)
    y = int( screen_height / 2 - window_height / 2)

    window.geometry(f"{window_width}*{window_height}+{x}+{y}")


# setting up control
def control_snake(window, change_direction):
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))