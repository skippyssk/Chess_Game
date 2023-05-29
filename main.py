import pygame
import os

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 1065, 760
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
PIECE_WIDTH, PIECE_HEIGHT = 15, 15
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 40

FPS = 60
CHESS_GREY = (64, 66, 76)

pygame.display.set_caption("AI CHESS")
# Padding around the board
PADDING = 4 * 6  # Scaled

# Size of the board without the padding
BOARD_SIZE = 128 * 6 - 2 * PADDING  # Scaled
# Size of one square on the chessboard
SQUARE_SIZE = BOARD_SIZE // 8
# The top-left position of the chessboard
BOARD_POSITION = (PADDING, PADDING)

FILES = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
RANKS = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}

# Adjust the values to be the top-left corner of each square
FILES = {file: pos * SQUARE_SIZE + PADDING for file, pos in FILES.items()}
RANKS = {rank: pos * SQUARE_SIZE + PADDING for rank, pos in RANKS.items()}

chess_board = pygame.image.load(os.path.join('Assets', 'set_regular', 'board_empty.png'))

SPRITE_SHEET_WHITE = pygame.image.load(
    os.path.join('Assets', 'set_regular', 'pieces_white_1.png'))

SPRITE_SHEET_BLACK = pygame.image.load(
    os.path.join('Assets', 'set_regular', 'pieces_black_1.png'))

SPRITE_SHEET_MENU = pygame.image.load(os.path.join('Assets', 'GUI', 'buttons.png'))

# GUI Class
class GUI:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # draw gui on screen
    def draw(self):
        WIN.blit(self.image, (self.rect.x, self.rect.y))

    def extract_sprite(self, sheet, row, col, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(sheet, (0, 0), (col * width, row * height, width, height))
        sprite.set_colorkey((0, 0, 0))  # Assuming black (0, 0, 0) is the transparent color
        return sprite


chess_board = GUI(0, 0, chess_board, 6)

# Pieces count for a standard chess game
PIECE_COUNTS = {
    'rook': 2,
    'knight': 2,
    'bishop': 2,
    'queen': 1,
    'king': 1,
    'pawn': 8
}

WHITE_PIECES = {}
BLACK_PIECES = {}

PIECE_ORDER = ['rook', 'knight', 'bishop', 'queen', 'king', 'pawn']
for i, piece in enumerate(PIECE_ORDER):
    WHITE_PIECES[piece] = []
    BLACK_PIECES[piece] = []
    for j in range(PIECE_COUNTS[piece]):
        white_piece = GUI(0, 0, chess_board.extract_sprite(SPRITE_SHEET_WHITE, 0, i, PIECE_WIDTH, PIECE_HEIGHT), 6)
        black_piece = GUI(0, 0, chess_board.extract_sprite(SPRITE_SHEET_BLACK, 0, i, PIECE_WIDTH, PIECE_HEIGHT), 6)
        WHITE_PIECES[piece].append(white_piece)
        BLACK_PIECES[piece].append(black_piece)

UI_PIECES ={}
UI_PIECE_ORDER = ['cancel_button','help_button', 'some_button', 'redo_button',
                  'play_button', 'pause_button', 'sound_button', 'mute_button',
                  'minus_button', 'plus_button']

for i, piece in enumerate(UI_PIECE_ORDER):
    UI_PIECES[piece] = []
    for j in range(10):
        UI_piece = GUI(0, 0, chess_board.extract_sprite(SPRITE_SHEET_MENU, i, j, BUTTON_WIDTH, BUTTON_HEIGHT), 4)
        UI_PIECES[piece].append(UI_piece)


black_rooks = BLACK_PIECES['rook']
black_knights = BLACK_PIECES['knight']
black_bishops = BLACK_PIECES['bishop']
black_queen = BLACK_PIECES['queen']
black_king = BLACK_PIECES['king']
black_pawns = BLACK_PIECES['pawn']

OFFSET = (SQUARE_SIZE - PIECE_WIDTH*6) // 2  # Centering offset

black_rooks[0].rect.topleft = (FILES['A'] + OFFSET, RANKS['1'] + OFFSET)
black_knights[0].rect.topleft = (FILES['B'] + OFFSET, RANKS['1'] + OFFSET)
black_bishops[0].rect.topleft = (FILES['C'] + OFFSET, RANKS['1'] + OFFSET)
black_queen[0].rect.topleft = (FILES['D'] + OFFSET, RANKS['1'] + OFFSET)
black_king[0].rect.topleft = (FILES['E'] + OFFSET, RANKS['1'] + OFFSET)
black_bishops[1].rect.topleft = (FILES['F'] + OFFSET, RANKS['1'] + OFFSET)
black_knights[1].rect.topleft = (FILES['G'] + OFFSET, RANKS['1'] + OFFSET)
black_rooks[1].rect.topleft = (FILES['H'] + OFFSET, RANKS['1'] + OFFSET)

for i, file in enumerate(FILES):
    black_pawns[i].rect.topleft = (FILES[file] + OFFSET, RANKS['2'] + OFFSET)

white_rooks = WHITE_PIECES['rook']
white_knights = WHITE_PIECES['knight']
white_bishops = WHITE_PIECES['bishop']
white_queen = WHITE_PIECES['queen']
white_king = WHITE_PIECES['king']
white_pawns = WHITE_PIECES['pawn']

white_rooks[0].rect.topleft = (FILES['A'] + OFFSET, RANKS['8'] + OFFSET)
white_knights[0].rect.topleft = (FILES['B'] + OFFSET, RANKS['8'] + OFFSET)
white_bishops[0].rect.topleft = (FILES['C'] + OFFSET, RANKS['8'] + OFFSET)
white_queen[0].rect.topleft = (FILES['D'] + OFFSET, RANKS['8'] + OFFSET)
white_king[0].rect.topleft = (FILES['E'] + OFFSET, RANKS['8'] + OFFSET)
white_bishops[1].rect.topleft = (FILES['F'] + OFFSET, RANKS['8'] + OFFSET)
white_knights[1].rect.topleft = (FILES['G'] + OFFSET, RANKS['8'] + OFFSET)
white_rooks[1].rect.topleft = (FILES['H'] + OFFSET, RANKS['8'] + OFFSET)

cancel_button = UI_PIECES['cancel_button']
help_button = UI_PIECES['help_button']
some_button = UI_PIECES['some_button']
redo_button = UI_PIECES['redo_button']
play_button = UI_PIECES['play_button']
pause_button = UI_PIECES['pause_button']
sound_button = UI_PIECES['sound_button']
mute_button = UI_PIECES['mute_button']
minus_button = UI_PIECES['minus_button']
plus_button = UI_PIECES['plus_button']

cancel_button[0].rect.topleft = (800,330)
help_button[0].rect.topleft = (900,330)
some_button[0].rect.topleft = (1000,330)
redo_button[0].rect.topleft = (1100,330)

play_button[0].rect.topleft = (800,370)
pause_button[0].rect.topleft = (900,370)
sound_button[0].rect.topleft = (1000,370)
mute_button[0].rect.topleft = (1100,370)

minus_button[0].rect.topleft = (800,410)
plus_button[0].rect.topleft = (900,410)


for i, file in enumerate(FILES):
    white_pawns[i].rect.topleft = (FILES[file] + OFFSET, RANKS['7'] + OFFSET)


def display():

    WIN.fill(CHESS_GREY)  # Fill the background

    chess_board.draw()

    def draw_black():
        black_rooks[0].draw()
        black_knights[0].draw()
        black_bishops[0].draw()
        black_queen[0].draw()
        black_king[0].draw()
        black_bishops[1].draw()
        black_knights[1].draw()
        black_rooks[1].draw()

        black_pawns[0].draw()
        black_pawns[1].draw()
        black_pawns[2].draw()
        black_pawns[3].draw()
        black_pawns[4].draw()
        black_pawns[5].draw()
        black_pawns[6].draw()
        black_pawns[7].draw()

    def draw_white():
        white_rooks[0].draw()
        white_knights[0].draw()
        white_bishops[0].draw()
        white_queen[0].draw()
        white_king[0].draw()
        white_bishops[1].draw()
        white_knights[1].draw()
        white_rooks[1].draw()

        white_pawns[0].draw()
        white_pawns[1].draw()
        white_pawns[2].draw()
        white_pawns[3].draw()
        white_pawns[4].draw()
        white_pawns[5].draw()
        white_pawns[6].draw()
        white_pawns[7].draw()

    def draw_ui():
        cancel_button[0].draw()
        help_button[0].draw()
        some_button[0].draw()
        redo_button[0].draw()
        play_button[0].draw()
        pause_button[0].draw()
        sound_button[0].draw()
        mute_button[0].draw()
        minus_button[0].draw()
        plus_button[0].draw()

    draw_white()
    draw_black()
    draw_ui()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        display()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
