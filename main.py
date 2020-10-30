import pygame
from time import sleep

# Initializing the PyGame library
pygame.init()

# Generating a window display for our application
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# Initializing, loading, and playing our first mp3 file (Our spooky music)
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()

# "sleep" works like wait in JavaScript (or was it Java??), this will cause a pause in our events
sleep(5)

# Now for our scary sound
pygame.mixer.init()
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()
sleep(1)

# Getting our image to display in screen
# This loads it in
image = pygame.image.load('scr.jpg')

# This line does like a block image transfer to the screen
screen.blit(image, (0,0))

# Updating the screen with our above image
pygame.display.update()
sleep(3)

