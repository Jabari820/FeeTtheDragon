import pygame

pygame.init()

window_width=10000
window_height=400
display_surface= pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Feed The Dragon")

''''''

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            running=flase

pygame.quit()