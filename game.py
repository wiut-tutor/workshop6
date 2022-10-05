import pygame
from sys import exit  # closes any kind of code

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()  # to control the how fast frames get change per second


test_font = pygame.font.Font('font/Pixeltype.ttf', 70)
bg_surface = pygame.image.load("graphics/bg.jpg")
ground_surface = pygame.image.load('graphics/ground.jpg')
text_surface = test_font.render('My Game', False, 'Blue')

man_surface = pygame.image.load('graphics/man1.png')
man_x_pos= 600

man2_surface = pygame.image.load('graphics/man2.png')
man2_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # opposite of init()
            exit()
    # display the screen, update the screen

    screen.blit(bg_surface, (0, 0))
    screen.blit(ground_surface,(0, 500)) #700-200 (the height of the image)
    screen.blit(text_surface, (300, 10))
    # screen.blit(man_surface,(man_x_pos, 250))
    man_x_pos-=4 #same as man_x_pos = man_x_pos-4
    man2_x_pos += 4  # same as man_x_pos = man_x_pos-4

    #create an if statement if goes too far too left
    if man_x_pos < -100:
        man_x_pos = 800

    if man2_x_pos > 800:
        man2_x_pos = -800

    screen.blit(man_surface, (man_x_pos, 230))
    screen.blit(man2_surface, (man2_x_pos, 0))
    pygame.display.update()
    clock.tick(60)
