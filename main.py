import pygame
from settings import *
from game import game

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def display(screen):
    screen.fill(GRAY)
    game.display(screen)
    pygame.display.update()
    clock.tick(FPS)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mos = pygame.mouse.get_pos()
                if 0 <= mos[0] < WIDTH // 2 and 0 <= mos[1] < HEIGHT // 2:
                    pressed = "green"
                elif WIDTH // 2 <= mos[0] < WIDTH and 0 <= mos[1] < HEIGHT // 2:
                    pressed = "red"
                elif 0 <= mos[0] < WIDTH // 2 < WIDTH and HEIGHT // 2 <= mos[1] < HEIGHT:
                    pressed = "yellow"
                elif WIDTH // 2 <= mos[0] < WIDTH and HEIGHT // 2 <= mos[1] < HEIGHT:
                    pressed = "blue"
                if game.pressedButton == False and game.makingSequence == False:
                    if pressed == game.sequence[game.memoryCount]:
                        game.memoryCount += 1
                    else:
                        game.failed = True
                        game.failSound.play()
                    game.press(pressed)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()

        display(screen)


main()