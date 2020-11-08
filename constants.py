ROWS = 20
COLS = 10

SQUARE_SIZE = 30

PREVIEW_HEIGHT = SQUARE_SIZE * 3

WIDTH = COLS * SQUARE_SIZE
HEIGHT = ROWS * SQUARE_SIZE + PREVIEW_HEIGHT

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
AUQUA = (0, 255, 255)
PURPLE = (255, 0, 255)

WINDOW_TITLE = "Tetris"


MOVE_DELAY = 500  # ms


F_SHAPE = [
    [[0, 1, 0],
     [0, 1, 1],
     [0, 1, 0]],

    [[0, 1, 0],
     [1, 1, 1],
     [0, 0, 0]],

    [[0, 1, 0],
     [1, 1, 0],
     [0, 1, 0]],

    [[0, 0, 0],
     [1, 1, 1],
     [0, 1, 0]]
]
F_COLOR = GREEN

L_SHAPE = [
    [[0, 0, 0, 0],
     [0, 0, 0, 1],
     [1, 1, 1, 1],
     [0, 0, 0, 0]],

    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 1, 0]],

    [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [1, 0, 0, 0],
     [0, 0, 0, 0]],

    [[0, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 0]]
]
L_COLOR = BLUE

Z_SHAPE = [
    [[1, 1, 0],
     [0, 1, 1],
     [0, 0, 0]],

    [[0, 1, 0],
     [1, 1, 0],
     [1, 0, 0]]
]
Z_COLOR = YELLOW

I_SHAPE = [
    [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [1, 1, 1, 1],
     [0, 0, 0, 0]],

    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0]]
]
I_COLOR = AUQUA


O_SHAPE = [
    [[1, 1],
     [1, 1]]
]
O_COLOR = PURPLE
