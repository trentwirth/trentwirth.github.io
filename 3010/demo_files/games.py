# coding_assignment_05.md – Problem 3 starter

import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Bouncing Ball")
    clock = pygame.time.Clock()

    # Ball setup
    ball_radius = 15
    ball_x      = random.randint(ball_radius, 640 - ball_radius)
    ball_y      = random.randint(ball_radius, 480 - ball_radius)
    vel_x       = 3
    vel_y       = 3

    running = True
    while running:
        clock.tick(60)  # 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # TODO: Update ball_x and ball_y
        ball_x += vel_x
        ball_y += vel_y

        # TODO: Bounce off edges
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= 640:
            vel_x = -vel_x
        if ball_y - ball_radius <= 0 or ball_y + ball_radius >= 480:
            vel_y = -vel_y

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (0, 255, 0),
                           (ball_x, ball_y), ball_radius)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
