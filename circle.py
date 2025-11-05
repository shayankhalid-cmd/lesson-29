import pygame
pygame.init()
window = pygame.display.set_mode((400, 400))
window.fill((0, 0, 0))
green = (79, 12, 34)
pygame.draw.circle(window, green, (200, 100), 75)
pygame.draw.circle(window,green, (200, 300), 50,3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()