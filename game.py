import pygame
from settings import *
import random

pygame.init()
class Game:
    def __init__(self):
        self.sequence = []
        self.makeSequence()
        self.sequenceCount = 0
        self.sequenceCoolDown = 0
        self.speed = FPS // 1.5

        self.surface = pygame.Surface((WIDTH//2,HEIGHT//2))
        self.surface.fill("blacK")
        self.surface.set_alpha(100)
        self.pressed = ""
        self.pressedButton = False
        self.makingSequence = True
        self.pressCooldown = 0
        self.resetCooldown = 0
        self.memoryCount = 0
        self.failed = False

        self.font = pygame.font.Font("font/LEMONMILK-Regular.otf",WIDTH // 4)
        self.text = self.font.render(str(len(self.sequence)),True,WHITE)

        self.volume = 0.1
        self.failSound = pygame.mixer.Sound("audio/fail.wav")
        self.greenSound = pygame.mixer.Sound("audio/green.wav")
        self.redSound = pygame.mixer.Sound("audio/red.wav")
        self.yellowSound = pygame.mixer.Sound("audio/yellow.wav")
        self.blueSound = pygame.mixer.Sound("audio/blue.wav")
        self.failSound.set_volume(self.volume)
        self.greenSound.set_volume(self.volume)
        self.redSound.set_volume(self.volume)
        self.yellowSound.set_volume(self.volume)
        self.blueSound.set_volume(self.volume)


    def press(self,button):
        self.pressed = button
        self.pressedButton = True
        match self.pressed:
            case "green":
                self.greenSound.play()
            case "red":
                self.redSound.play()
            case "yellow":
                self.yellowSound.play()
            case "blue":
                self.blueSound.play()


    def makeSequence(self):
        self.sequence.append(random.choice(["green","red","yellow","blue"]))

    def showSequence(self):
        if self.sequenceCount >= len(self.sequence):
            self.sequenceCount = 0
            self.makingSequence = False
            self.sequenceCoolDown = 0
        if self.makingSequence:
            if self.sequenceCoolDown % self.speed == 0:
                print(self.speed)
                self.press(self.sequence[self.sequenceCount])
                self.sequenceCount += 1

            self.sequenceCoolDown += 1

    def playAgain(self):
        if self.failed:
            self.resetCooldown += 1
            if self.resetCooldown > self.speed:
                self.sequenceCount = 0
                self.memoryCount = 0
                self.makingSequence = True
                self.resetCooldown = 0
                self.failed = False

    def update(self):
        self.playAgain()
        if self.memoryCount == len(self.sequence):
            self.resetCooldown += 1
            if self.resetCooldown > self.speed:
                if self.speed > 10:
                    self.speed -= 1
                self.memoryCount = 0
                self.resetCooldown = 0
                self.makeSequence()
                self.text = self.font.render(str(len(self.sequence)), True, WHITE)
                self.makingSequence = True


        self.showSequence()
        if self.pressCooldown >= FPS // 4:
            self.pressed = ""
            self.pressedButton = False
            self.pressCooldown = 0
        if self.pressedButton == True:
            self.pressCooldown += 1

    def reset(self):
        self.speed = FPS // 1.5
        self.sequence = []
        self.makeSequence()
        self.sequenceCount = 0
        self.sequenceCoolDown = 0
        self.pressCooldown = 0
        self.resetCooldown = 0
        self.memoryCount = 0
        self.failed = False
        self.pressed = ""
        self.pressedButton = False
        self.makingSequence = True
        pygame.time.wait(500)

        self.text = self.font.render(str(len(self.sequence)), True, WHITE)


    def display(self,screen):
        self.update()
        pygame.draw.rect(screen,GREEN,(0,0,WIDTH // 2,HEIGHT//2))
        pygame.draw.rect(screen, RED, (WIDTH//2, 0, WIDTH // 2, HEIGHT // 2))
        pygame.draw.rect(screen, YELLOW, (0, HEIGHT//2, WIDTH // 2, HEIGHT // 2))
        pygame.draw.rect(screen, BLUE, (WIDTH//2, HEIGHT//2, WIDTH // 2, HEIGHT // 2))

        if self.pressed != "":
            match self.pressed:
                case "green":
                    screen.blit(self.surface,(0,0))
                case "red":
                    screen.blit(self.surface,(WIDTH//2, 0))
                case "yellow":
                    screen.blit(self.surface,(0, HEIGHT//2))
                case "blue":
                    screen.blit(self.surface, (WIDTH//2, HEIGHT//2))
        screen.blit(self.text,(WIDTH // 2 - self.text.get_width() // 2,HEIGHT//2 - self.text.get_height() // 2))

game = Game()