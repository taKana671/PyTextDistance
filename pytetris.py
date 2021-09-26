import logging

import pygame
import random
import sys
from collections import namedtuple
from pygame.locals import *

SCREEN = Rect(0, 0, 700, 600)
BLOCK_AREA_LEFT = 100
BLOCK_AREA_RIGHT = 300
BLOCK_AREA_BOTTOM = 475
BLOCK_AREA_TOP = 100

COLS = 10   # the number of columns
ROWS = 20  # the number of rows
BLOCK_SIZE = 20


Assembled = namedtuple('Assembled', 'filename coordinates')


class AssembledBlocks(Assembled):

    def update_coords(self):
        pass





BLUE = Shaped('images/blue25.png',
              [[[-1, 4], [0, 4], [1, 4], [2, 4]], [[0, 4], [0, 5], [0, 6], [0, 7]], [[-1, 4], [0, 4], [1, 4], [2, 4]], [[0, 4], [0, 5], [0, 6], [0, 7]]])
DARK = Shaped('images/dark25.png', [[-1, 4], [0, 4], [1, 4], [1, 5]])
GREEN = Shaped('images/green25.png', [[-1, 4], [-1, 5], [0, 3], [0, 4]])
ORANGE = Shaped('images/orange25.png', [[-1, 4], [-1, 5], [0, 5], [1, 5]])
PURPLE = Shaped('images/purple25.png', [[-1, 4], [0, 3], [0, 4], [0, 5]])
RED = Shaped('images/red25.png', [[-1, 3], [-1, 4], [0, 4], [0, 5]])
YELLOW = Shaped('images/yellow25.png', [[-1, 4], [-1, 5], [0, 4], [0, 5]])
# SHAPED_LIST = [BLUE, DARK, GREEN, ORANGE, PURPLE, RED, YELLOW]
SHAPED_LIST = [BLUE]

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='test.log')
logger.addHandler(handler)


class PyTetris:

    def __init__(self, matrix, screen):
        self.matrix = matrix
        self.screen = screen
        self.stop = False
        self.start()

    def start(self):
        index = random.randint(0, len(SHAPED_LIST) - 1)
        shaped = SHAPED_LIST[index]
        self.blocks = pygame.sprite.Group()
        for row, col in shaped.coordinates:
            block = Block(shaped.filename, row, col)
            self.blocks.add(block)

    def update(self):
        if not self.stop:
            self.move_down()
        if any(self.judge_right(block) for block in self.blocks.sprites()):
            self.move_left()
        if any(self.judge_left(block) for block in self.blocks.sprites()):
            self.move_right()
        if any(self.judge_down(block) for block in self.blocks.sprites()):
            self.move_up()
        if any(self.judge_ground(block) for block in self.blocks.sprites()):
            self.update_matrix()
            # Game over
            if any(block for block in self.matrix[0]):
                self.stop = True
                self.game_over()
            else:
                self.start()
        if not self.stop:
            for block in self.blocks.sprites():
                block.rect.centerx = BLOCK_AREA_LEFT + block.col * BLOCK_SIZE
                block.rect.centery = BLOCK_AREA_TOP + block.row * BLOCK_SIZE

    def judge_left(self, block):
        return block.col < 0 or self.matrix[block.row][block.col]

    def judge_right(self, block):
        logger.info(f'row: {block.row}, col:{block.col}')
        return block.col >= COLS or self.matrix[block.row][block.col]

    def judge_down(self, block):
        return block.row >= ROWS or self.matrix[block.row][block.col]

    def judge_ground(self, block):
        return block.row == ROWS - 1 or self.matrix[block.row + 1][block.col]

    def update_matrix(self):
        for block in self.blocks.sprites():
            self.matrix[block.row][block.col] = block

    def move_right(self):
        for block in self.blocks.sprites():
            block.col += 1

    def move_left(self):
        for block in self.blocks.sprites():
            block.col -= 1

    def move_down(self):
        for block in self.blocks.sprites():
            block.row += 1

    def move_up(self):
        for block in self.blocks.sprites():
            block.row -= 1

    def rotate(self):

        pass

    def game_over(self):
        self.sysfont = pygame.font.SysFont(None, 20)
        img = self.sysfont.render('Game over', True, (255, 255, 250))
        self.screen.blit(img, (400, 300))


class Block(pygame.sprite.Sprite):

    def __init__(self, filename, row, col):
        super().__init__(self.containers)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col
        self.stop = False


class Plate(pygame.sprite.Sprite):

    def __init__(self, filename):
        super().__init__(self.containers)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (250, 5))
        self.rect = self.image.get_rect()
        self.rect.left = BLOCK_AREA_LEFT
        self.rect.bottom = BLOCK_AREA_BOTTOM


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    group = pygame.sprite.RenderUpdates()

    matrix = [[None for _ in range(COLS)] for _ in range(ROWS)]
    Block.containers = group
    Plate.containers = group

    plate = Plate('images/plate.png')

    tetris = PyTetris(matrix, screen)

    clock = pygame.time.Clock()

    while True:
        clock.tick(5)
        # pygame.key.set_repeat(10)
        screen.fill((0, 100, 0))

        tetris.update()

        group.update()
        group.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    tetris.move_right()
                if event.key == K_LEFT:
                    tetris.move_left()
                if event.key == K_DOWN:
                    tetris.move_down()
                if event.key == K_UP:
                    # tetris.rorate()
                    pass


if __name__ == '__main__':
    main()
