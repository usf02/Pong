import pygame
from Pong import game
import neat
import os


class PongGame:
    def __init__(self, window, width, height):
        self.game = game.Game(window, width, height)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def test_ai(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                game.move_paddle(True, True)
            if keys[pygame.K_s]:
                game.move_paddle(True, False)

            game_info = game.loop()
            print(game_info.left_score, game_info.right_score)
            game.draw()
            pygame.display.update()

        pygame.quit()


def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint()
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
