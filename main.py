import pygame, os, math

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 1065, 760
# Draws the window of the game.
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

BOARD_WIDTH, BOARD_HEIGHT = (128 * 6 - 2 * PADDING, 128 * 6 - 2 * PADDING)
# A dictionary in Key : Value pairs
FILES = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
RANKS = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}

""" This code initializes a variable file and pos and assigns the key of the 
dictionary of FILE to file and the value of FILE to pos. It then adjusts
the value of file and pos so it is in the top-left corner.
"""
FILES = {file: pos * SQUARE_SIZE + PADDING for file, pos in FILES.items()}
RANKS = {rank: pos * SQUARE_SIZE + PADDING for rank, pos in RANKS.items()}
# This loads the images. "os.path.join" is used so it works in any operating system.
chess_board = pygame.image.load(os.path.join('Assets', 'set_regular', 'board_empty.png'))

SPRITE_SHEET_WHITE = pygame.image.load(
    os.path.join('Assets', 'set_regular', 'pieces_white_1.png'))

SPRITE_SHEET_BLACK = pygame.image.load(
    os.path.join('Assets', 'set_regular', 'pieces_black_1.png'))

SPRITE_SHEET_MENU = pygame.image.load(os.path.join('Assets', 'GUI', 'buttons.png'))

clicked_piece = None


# GUI Class


class GUI:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        # This makes all GUI's rectangles allowing for manipulation in the future.
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
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
for i, piece in enumerate(PIECE_ORDER):  # enumerate adds a counter to an iterable and returns it
    WHITE_PIECES[piece] = []
    BLACK_PIECES[piece] = []
    for j in range(PIECE_COUNTS[piece]):
        white_piece = GUI(0, 0,
                          chess_board.extract_sprite(SPRITE_SHEET_WHITE, 0, i, PIECE_WIDTH, PIECE_HEIGHT), 6)
        black_piece = GUI(0, 0,
                          chess_board.extract_sprite(SPRITE_SHEET_BLACK, 0, i, PIECE_WIDTH, PIECE_HEIGHT), 6)
        WHITE_PIECES[piece].append(white_piece)
        BLACK_PIECES[piece].append(black_piece)

UI_PIECES = {}
UI_PIECE_ORDER = ['cancel_button', 'help_button', 'some_button', 'redo_button',
                  'play_button', 'pause_button', 'sound_button', 'mute_button',
                  'minus_button', 'plus_button']

for i, piece in enumerate(UI_PIECE_ORDER):
    UI_PIECES[piece] = []
    for j in range(10):
        UI_piece = GUI(0, 0, chess_board.extract_sprite(SPRITE_SHEET_MENU, i, j,
                                                        BUTTON_WIDTH, BUTTON_HEIGHT), 4)
        UI_PIECES[piece].append(UI_piece)


black_rooks = BLACK_PIECES['rook']
black_knights = BLACK_PIECES['knight']
black_bishops = BLACK_PIECES['bishop']
black_queen = BLACK_PIECES['queen']
black_king = BLACK_PIECES['king']
black_pawns = BLACK_PIECES['pawn']

OFFSET = (SQUARE_SIZE - PIECE_WIDTH * 6) // 2  # Centering offset


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

cancel_button[0].rect.topleft = (800, 330)
help_button[0].rect.topleft = (900, 330)
some_button[0].rect.topleft = (1000, 330)
redo_button[0].rect.topleft = (1100, 330)

play_button[0].rect.topleft = (800, 370)
pause_button[0].rect.topleft = (900, 370)
sound_button[0].rect.topleft = (1000, 370)
mute_button[0].rect.topleft = (1100, 370)

minus_button[0].rect.topleft = (800, 410)
plus_button[0].rect.topleft = (900, 410)


for i, file in enumerate(FILES):
    white_pawns[i].rect.topleft = (FILES[file] + OFFSET, RANKS['7'] + OFFSET)


def display():

    global clicked_piece

    WIN.fill(CHESS_GREY)  # Fill the background

    chess_board.draw()

    def draw_black():
        for piece_name, pieces in BLACK_PIECES.items():
            for piece in pieces:
                if piece != clicked_piece:
                    piece.draw()

    def draw_white():
        for piece_name, pieces in WHITE_PIECES.items():
            for piece in pieces:
                if piece != clicked_piece:
                    piece.draw()

    def draw_ui():
        for piece_name, pieces in UI_PIECES.items():
            for piece in pieces:
                piece.draw()

    draw_black()
    draw_white()
    draw_ui()

    if clicked_piece is not None:
        clicked_piece.draw()
        print("yes")

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    dragged_piece = None
    global clicked_piece

    while run:
        clicked_piece = None
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button pressed
                    pos = pygame.mouse.get_pos()
                    for piece_name, pieces in BLACK_PIECES.items():
                        for piece in pieces:
                            if piece.rect.collidepoint(pos):
                                piece.dragging = True
                                piece.offset_x = pos[0] - piece.rect.x
                                piece.offset_y = pos[1] - piece.rect.y
                                dragged_piece = piece
                                clicked_piece = piece
                    for piece_name, pieces in WHITE_PIECES.items():
                        for piece in pieces:
                            if piece.rect.collidepoint(pos):
                                piece.dragging = True
                                piece.offset_x = pos[0] - piece.rect.x
                                piece.offset_y = pos[1] - piece.rect.y
                                dragged_piece = piece
                                clicked_piece = piece

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button released
                    if dragged_piece is not None:
                        # Calculate the closest square's index
                        piece_center_x = dragged_piece.rect.x + dragged_piece.rect.w // 2
                        piece_center_y = dragged_piece.rect.y + dragged_piece.rect.h // 2
                        # Calculate the square index in both directions
                        square_index_x = (piece_center_x - PADDING) // SQUARE_SIZE
                        square_index_y = (piece_center_y - PADDING) // SQUARE_SIZE
                        # Calculate the closest square's index
                        closest_square_x = round(square_index_x)
                        closest_square_y = round(square_index_y)
                        # Convert the index back to pixels and offset by the padding and the piece's offset
                        new_x = closest_square_x * SQUARE_SIZE + PADDING
                        new_y = closest_square_y * SQUARE_SIZE + PADDING
                        # Snap the piece to the center of the closest square
                        dragged_piece.rect.x = new_x + OFFSET
                        dragged_piece.rect.y = new_y + OFFSET

                        for piece_name, pieces in list(WHITE_PIECES.items()):  # We create a copy of the items
                            for piece in pieces:
                                if piece is not dragged_piece and piece.rect.colliderect(dragged_piece.rect):
                                    print(f"Piece at {piece.rect.x}, {piece.rect.y} was squashed!")
                                    pieces.remove(piece)  # Remove the piece from the board
                                    break  # Stop checking after finding one collision, to prevent modifying the list during iteration
                        for piece_name, pieces in list(BLACK_PIECES.items()):  # We create a copy of the items
                            for piece in pieces:
                                if piece is not dragged_piece and piece.rect.colliderect(dragged_piece.rect):
                                    print(f"Piece at {piece.rect.x}, {piece.rect.y} was squashed!")
                                    pieces.remove(piece)  # Remove the piece from the board
                                    break  # Stop checking after finding one collision, to prevent modifying the list during iteration

                        dragged_piece.dragging = False
                        dragged_piece = None
                        clicked_piece = None

            elif event.type == pygame.MOUSEMOTION:
                if dragged_piece is not None and dragged_piece.dragging:
                    mouse_x, mouse_y = event.pos
                    dragged_piece.rect.x = mouse_x - dragged_piece.offset_x
                    dragged_piece.rect.y = mouse_y - dragged_piece.offset_y

        display()
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

    pygame.quit()


if __name__ == "__main__":
    main()
