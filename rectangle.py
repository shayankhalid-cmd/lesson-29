import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (int(input("enter a number")), int(input("enter a number")), int(input("enter a number"))), pygame.Rect(50, 50, 100, 50))
    pygame.display.flip()