import numpy as np
import pygame
import time

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life")

bg = (25, 25, 25)

nxC, nyC = 25, 25
dimCW = width / nxC
dimCH = height / nyC

gameState = np.zeros((nxC, nyC))
pauseExect = False

clock = pygame.time.Clock()

while True:

    newGameState = np.copy(gameState)
    screen.fill(bg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pauseExect = not pauseExect

    mouseClick = pygame.mouse.get_pressed()
    if sum(mouseClick) > 0:
        posX, posY = pygame.mouse.get_pos()
        celX, celY = int(posX // dimCW), int(posY // dimCH)
        if mouseClick[0]: 
            newGameState[celX, celY] = 1
        elif mouseClick[2]:  
            newGameState[celX, celY] = 0


    for y in range(nyC):
        for x in range(nxC):

            if not pauseExect:
                n_neigh = (
                    gameState[(x-1) % nxC, (y-1) % nyC] +
                    gameState[(x)   % nxC, (y-1) % nyC] +
                    gameState[(x+1) % nxC, (y-1) % nyC] +
                    gameState[(x-1) % nxC, (y)   % nyC] +
                    gameState[(x+1) % nxC, (y)   % nyC] +
                    gameState[(x-1) % nxC, (y+1) % nyC] +
                    gameState[(x)   % nxC, (y+1) % nyC] +
                    gameState[(x+1) % nxC, (y+1) % nyC]
                )

                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0


            poly = [
                (x * dimCW, y * dimCH),
                ((x + 1) * dimCW, y * dimCH),
                ((x + 1) * dimCW, (y + 1) * dimCH),
                (x * dimCW, (y + 1) * dimCH)
            ]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 0)

    gameState = np.copy(newGameState)
    pygame.display.flip()
    clock.tick(10)
