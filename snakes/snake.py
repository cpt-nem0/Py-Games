import pygame
import sys
import random
import config


class Snake(object):
    def __init__(self):
        self.length = 1
        self.position = [((config.HEIGHT/2), (config.WIDTH/2))]
        self.direction = random.choice(
            [config.UP, config.DOWN, config.LEFT, config.RIGHT])
        self.color = (75, 75, 75)
        self.score = 0

    def getHeadPosition(self):
        return self.position[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * (-1), point[1] * (-1)) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.getHeadPosition()
        x, y = self.direction
        new_location = (((cur[0] + (x*config.GRID_SIZE)) % config.WIDTH),
                        ((cur[1]+(y*config.GRID_SIZE)) % config.HEIGHT))

        if len(self.position) > 2 and new_location in self.position[2:]:
            self.reset()
        else:
            self.position.insert(0, new_location)
            if len(self.position) > self.length:
                self.position.pop()

    def reset(self):
        self.length = 1
        self.position = [((config.HEIGHT/2), (config.WIDTH/2))]
        self.direction = random.choice(
            [config.UP, config.DOWN, config.LEFT, config.RIGHT])
        self.score = 0

    def draw(self, surface):
        for i in self.position:
            r = pygame.Rect((i[0], i[1]), (config.GRID_SIZE, config.GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (154, 255, 0), r, 1)

    def keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.turn(config.UP)
                if event.key == pygame.K_DOWN:
                    self.turn(config.DOWN)
                if event.key == pygame.K_LEFT:
                    self.turn(config.LEFT)
                if event.key == pygame.K_RIGHT:
                    self.turn(config.RIGHT)


class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (75, 75, 75)
        self.rand_Position()

    def rand_Position(self):
        self.position = (random.randint(0, config.GRID_WIDTH-1) *
                         config.GRID_SIZE, random.randint(0, config.GRID_HEIGHT-1)*config.GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect(
            (self.position[0], self.position[1]), (config.GRID_SIZE, config.GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (154, 255, 0), r, 1)


def game_init():
    pygame.display.set_caption("SNAKE")
    icon = pygame.image.load('snake.png')
    pygame.display.set_icon(icon)


def main():
    state = True
    pygame.init()

    game_init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((config.HEIGHT, config.WIDTH), depth=16)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((154, 255, 0))

    snake = Snake()
    food = Food()

    font = pygame.font.SysFont("monospace", 16, bold=True)

    while state:
        clock.tick(10)
        snake.keys_pressed()
        surface.fill((154, 255, 0))
        snake.move()
        if snake.getHeadPosition() == food.position:
            snake.length += 1
            snake.score += 1
            food.rand_Position()

        snake.draw(surface)
        food.draw(surface)

        screen.blit(surface, (0, 0))
        score_text = font.render(
            "score: {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(score_text, (5, 10))
        pygame.display.update()


if __name__ == "__main__":
    main()
