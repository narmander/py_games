import os
import sys
import pygame
import time

from utilities import load_image, past_time, BASE_WIDTH, BASE_HEIGHT, BLACK, WHITE
from shape import Shape


def main(BASE_WIDTH, BASE_HEIGHT):
    pygame.init()
    screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT))
    pygame.display.set_caption('Q-Tetris')

    background = pygame.Surface(screen.get_size())
    background = background.convert()

    image = load_image('big-galaxy', (BASE_WIDTH, BASE_HEIGHT))
    image_rect = image.get_rect()

    background.blit(image, (0, 0))
    screen.blit(background, image_rect)

    grid_size = BASE_WIDTH, BASE_HEIGHT = BASE_WIDTH - BASE_WIDTH/3, BASE_HEIGHT + 10
    grid = pygame.Rect((4, -15), grid_size)

    i_shape = Shape('I')
    key_pressing = False
    while 1:
        time_now = time.time()

        for event in pygame.event.get():
            print(time_now)
            key_hold = past_time(time_now)
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key_pressing = True
            if event.type == pygame.KEYUP:
                key_pressing = False

        if key_pressing:
            i_shape.update(event.key)
            screen.blit(background, i_shape.last_location)

        pygame.draw.rect(screen, WHITE, grid, 10)
        screen.blit(i_shape.letter_surface, (i_shape.x_pos, i_shape.y_pos))
        pygame.display.flip()


if __name__ == "__main__":
    main(BASE_WIDTH, BASE_HEIGHT)
