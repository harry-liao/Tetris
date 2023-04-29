import pygame
import random

class Tetris:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()

        # Define the shapes of the Tetrominos
        self.shapes = [
            [[1, 1, 1],
             [0, 1, 0]],

            [[0, 2, 2],
             [2, 2, 0]],

            [[3, 3, 0],
             [0, 3, 3]],

            [[4, 0, 0],
             [4, 4, 4]],

            [[0, 0, 5],
             [5, 5, 5]],

            [[6, 6, 6, 6]],

            [[7, 7],
             [7, 7]]
        ]

        self.colors = [
            (0, 0, 0),
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255),
            (192, 192, 192)
        ]

        self.block_size = 30
        self.grid_width = 10
        self.grid_height = 20
        self.grid = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.score = 0
        self.active_tetromino = self.get_random_tetromino()
        self.next_tetromino = self.get_random_tetromino()
        self.tetromino_x = 3
        self.tetromino_y = 0

    def get_random_tetromino(self):
        return random.choice(self.shapes)

    def draw_block(self, x, y, color):
        pygame.draw.rect(self.screen, self.colors[color], pygame.Rect(x, y, self.block_size, self.block_size))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, self.block_size, self.block_size), 1)

    def draw_tetromino(self, x, y, tetromino):
        for i in range(len(tetromino)):
            for j in range(len(tetromino[i])):
                if tetromino[i][j] != 0:
                    self.draw_block((j + x) * self.block_size, (i + y) * self.block_size, tetromino[i][j])

    def draw_grid(self):
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                if self.grid[i][j] != 0:
                    self.draw_block(j * self.block_size, i * self.block_size, self.grid[i][j])

    def move_tetromino(self, dx, dy):
        if not self.check_collision(dx, dy, self.active_tetromino):
            self.tetromino_x += dx
            self.tetromino_y += dy
            return True
        else:
            return False

    def rotate_tetromino(self):
        new_tetromino = []
        for i in range(len(self.active_tetromino[0])):
            new_row = []            
            for row in self.active_tetromino[::-1]:
                new_row.append(row[i])
            new_tetromino.append(new_row)
        if not self.check_collision(0, 0, new_tetromino):
            self.active_tetromino = new_tetromino

    def check_collision(self, dx, dy, tetromino):
        for i in range(len(tetromino)):
            for j in range(len(tetromino[i])):
                if tetromino[i][j] != 0:
                    x = self.tetromino_x + j + dx
                    y = self.tetromino_y + i + dy
                    if x < 0 or x >= self.grid_width or y >= self.grid_height or self.grid[y][x] != 0:
                        return True
        return False

    def fix_tetromino(self):
        for i in range(len(self.active_tetromino)):
            for j in range(len(self.active_tetromino[i])):
                if self.active_tetromino[i][j] != 0:
                    x = self.tetromino_x + j
                    y = self.tetromino_y + i
                    self.grid[y][x] = self.active_tetromino[i][j]
        self.clear_rows()
        self.active_tetromino = self.next_tetromino
        self.next_tetromino = self.get_random_tetromino()
        self.tetromino_x = 3
        self.tetromino_y = 0
        if self.check_collision(0, 0, self.active_tetromino):
            self.game_over()

    def clear_rows(self):
        num_rows_cleared = 0
        for i in range(len(self.grid)):
            if all(self.grid[i]):
                self.grid.pop(i)
                self.grid.insert(0, [0 for _ in range(self.grid_width)])
                num_rows_cleared += 1
        if num_rows_cleared > 0:
            self.score += 10 * (2 ** (num_rows_cleared - 1))

    def game_over(self):
        font = pygame.font.SysFont(None, 100)
        text = font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
    
    def display_score(self):
        font = pygame.font.SysFont(None, 24)
        text = font.render("Score: {}".format(self.score), True, (255,255,255))
        self.screen.blit(text, (10,10))
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_tetromino(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move_tetromino(1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.move_tetromino(0, 1)
                    elif event.key == pygame.K_UP:
                        self.rotate_tetromino()

            self.screen.fill((255,255,255))
            self.draw_grid()
            self.draw_tetromino(self.tetromino_x, self.tetromino_y, self.active_tetromino)
            pygame.display.flip()

            if not self.move_tetromino(0, 1):
                self.fix_tetromino()

            self.clock.tick(5)

if __name__ == '__main__':
    game = Tetris()
    game.run()
    pygame.quit()

