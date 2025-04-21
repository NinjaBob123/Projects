import pygame
from pygame.locals import *
import time

class Game():
    def __init__(self):
        self.size = 640, 240
        self.width, self.height = self.size
        self.colors = {"RED": (255,0,0),
                       "GREEN": (0,255,0),
                       "BLUE": (0,0,255),
                       "LBLUE": (175,175,255)}
        pygame.init()
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Brick Breaker")
        ball = pygame.image.load("assets/ball.png")
        ballRect = ball.get_rect()
        self.speed = [2,2]
        self.ball = [ball, ballRect]
        paddle = pygame.image.load("assets/paddle.png")
        paddleRect = paddle.get_rect()
        self.paddle = [paddle, paddleRect, 0]

    def mainloop(self):
        running = True
        ballRect = self.ball[1]
        paddleRect = self.paddle[1]
        while running:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == 37:
                        self.paddle[2] = -2
                    elif event.key == 39:
                        self.paddle[2] = 2


            # Ball Movement
            ballRect = ballRect.move(self.speed)
            if ballRect.left < 0 or ballRect.right > self.width:
                self.speed[0] = -self.speed[0]
            if ballRect.top < 0 or ballRect.bottom > self.height:
                self.speed[1] = -self.speed[1]
            self.window.fill(self.colors["LBLUE"])
            self.ball[1] = ballRect
            self.window.blit(self.ball[0], self.ball[1])

                # Paddle Movement
#                paddleRect = paddleRect.move([self.paddle[2], 0])
#                if paddleRect.left < 0 or paddleRect.right > self.width:
#                    self.paddle[2] = -self.paddle[2]
#                self.paddle[1] = paddleRect
#                self.window.blit(self.paddle[0], self.paddle[1])
#
            self.window.fill(self.colors["LBLUE"])
            time.sleep(0.01)
            pygame.display.update()
            
            

g = Game()
g.mainloop()