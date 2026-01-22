import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("3 ta stakan o‘yini")

# RASMALAR
cup_img = pygame.image.load("cup.png")
ball_img = pygame.image.load("ball.png")

cup_img = pygame.transform.scale(cup_img, (120, 140))
ball_img = pygame.transform.scale(ball_img, (50, 50))

# STAKAN POZITSIYALARI
positions = [150, 340, 530]
cups = [0, 1, 2]

# To‘p qaysi stakan ostida turadi
ball_pos = random.choice(cups)

font = pygame.font.SysFont("Arial", 40)

def draw_game(hidden=True):
    screen.fill((30, 30, 30))

    for i, pos in zip(cups, positions):
        screen.blit(cup_img, (pos, 180))

    if not hidden:
        screen.blit(ball_img, (positions[ball_pos] + 35, 250))

    pygame.display.update()


def shuffle_cups():
    global cups, ball_pos

    for _ in range(10):  # 10 marta almashtirish
        a, b = random.sample(range(3), 2)  # 2 ta stakanni tanlash
        cups[a], cups[b] = cups[b], cups[a]

        if ball_pos == a:
            ball_pos = b
        elif ball_pos == b:
            ball_pos = a

        draw_game()
        pygame.time.delay(300)


# O‘yin boshlanishi
running = True
game_over = False
show_ball = False

draw_game()
pygame.time.delay(500)
shuffle_cups()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not show_ball:
            x, y = event.pos

            for i, pos in enumerate(positions):
                if pos < x < pos + 120 and 180 < y < 320:
                    show_ball = True

                    if i == ball_pos:
                        message = "YUTDINGIZ!"
                        color = (0, 255, 0)
                    else:
                        message = "YUTQAZDINGIZ!"
                        color = (255, 0, 0)

                    text = font.render(message, True, color)
                    screen.blit(text, (300, 50))

                    draw_game(hidden=False)
                    pygame.display.update()

    draw_game(hidden=not show_ball)

pygame.quit()
