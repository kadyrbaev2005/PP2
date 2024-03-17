import pygame
from datetime import datetime
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Mickey mouse')
clock = pygame.image.load('images/Mickey mouse.png')
hands = pygame.image.load('images/both hand.png')
left_hand = pygame.image.load('images/left.png')
right_hand = pygame.image.load('images/right.png')
center = (800/2, 600/2)

running = True
while running:

    time = datetime.now()
    minute, second = time.minute, time.second

    angle_minute = minute*360/60
    angle_second = second*360/60

    minute_rotated_image = pygame.transform.rotate(right_hand, -angle_minute)
    second_rotated_image = pygame.transform.rotate(left_hand, -angle_second)

    minute_rotated_rec = minute_rotated_image.get_rect(center=center)
    second_rotated_rec = second_rotated_image.get_rect(center=center)

    screen.blit(clock, (center[0] - clock.get_width()/2, center[1] - clock.get_height()/2))

    screen.blit(minute_rotated_image, minute_rotated_rec.topleft)
    screen.blit(second_rotated_image, second_rotated_rec.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.time.Clock().tick(30)