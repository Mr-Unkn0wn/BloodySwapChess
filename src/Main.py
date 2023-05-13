# Example file showing a basic pygame "game loop"
import pygame

from Board import Board
from pieces.TextureLoader import TextureLoader


def draw_board(size_in_pixels, screen):
    for x in range(8):
        for y in range(8):
            count = x * 7 + y

            color = (13, 27, 42)
            if count % 2 == 0:
                color = (224, 225, 221)

            pygame.draw.rect(screen, color, (size_in_pixels * x, size_in_pixels * y,
                                             size_in_pixels * (x + 1), size_in_pixels * (y + 1)))


def main_loop():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    running = True
    loader = TextureLoader()
    board = Board()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("gray")

        # RENDER YOUR GAME HERE
        draw_board(75, screen)
        board.draw_board(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


main_loop()
