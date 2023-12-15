import pygame
import random

pygame.init()

red = (255, 0, 0)
W, H = 800, 700
Fenetre = pygame.display.set_mode((W, H))
pygame.display.set_caption('Snake')

pause = False
game_over = False


def play():
    global game_over
    game_over = False
    x = 500
    y = 500

    x_change = 0
    y_change = 0

    pomme_x = random.randrange(20, W - 20)
    pomme_y = random.randrange(100, H - 20)
    snake_liste = []
    snake_taille = 1
    point = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -6
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 6
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -6
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = 6
                    x_change = 0
                elif event.key == pygame.K_SPACE:
                    paused()

        Fenetre.fill((82, 190, 128))

        pomme_img = pygame.image.load('img/pomme.png')
        Fenetre.blit(pomme_img, (pomme_x, pomme_y))
        pygame.draw.rect(Fenetre, (0, 0, 0), [x, y, 20, 20])

        if x > W -20 or x < 0 or y > H - 20 or y < 80:
            game_over = True
            game_over_screen()
        x += x_change
        y += y_change

        snake_corps = []
        snake_corps.append(x)
        snake_corps.append(y)
        snake_liste.append(snake_corps)

        if len(snake_liste) > snake_taille:
            del snake_liste[0]

        for i in snake_liste[:-1]:
            if i == snake_corps:
                game_over = True
                game_over_screen()

        pygame.draw.rect(Fenetre, (22, 22, 62), (0, 0, 800, 80))
        ShowScore = pygame.font.SysFont(None, 40, italic=True, bold=True).render(f"{point}", True, (128, 139, 150))
        ShowScore_rect = ShowScore.get_rect(center=(W // 4, 40))
        pomme_img = pygame.image.load('img/pomme.png')
        Fenetre.blit(ShowScore, ShowScore_rect)
        Fenetre.blit(pomme_img, (W//4-40, 80//2 - pomme_img.get_width() //2))

        snake(snake_liste)
        pygame.display.update()

        if x <= pomme_x + 25 and x >= pomme_x - 25 and y <= pomme_y + 25 and y >= pomme_y - 25:
            print("pomme")
            pomme_x = random.randrange(25, W - 25)
            pomme_y = random.randrange(105, H - 25)
            snake_taille += 1
            point += 1

        pygame.time.Clock().tick(30)


def snake(snake_liste):
    for i in snake_liste:
        pygame.draw.rect(Fenetre, (0, 0, 0), [i[0], i[1], 20, 20])


def paused():
    pause = True

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
        Fenetre.fill((39, 55, 70))

        TextPause = pygame.font.SysFont(None, 60, italic=True, bold=True).render("Pause", True, (128, 139, 150))
        Pause_rect = TextPause.get_rect(center=(W // 2, H // 2 - 30))
        Fenetre.blit(TextPause, Pause_rect)

        TextContinue = pygame.font.SysFont(None, 50, italic=True, bold=True).render(
            "Appuyer sur 'Espace' pour continuer", True, (128, 139, 150))
        Continue_rect = TextContinue.get_rect(center=(W // 2, H // 2 + 100))
        Fenetre.blit(TextContinue, Continue_rect)
        pygame.display.update()


def game_over_screen():
    global game_over
    lost = True

    while lost:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_over = False
                    play()

        Fenetre.fill((39, 55, 70))

        TextPause = pygame.font.SysFont(None, 60, italic=True, bold=True).render("Game Over", True, (192, 57, 43))
        Pause_rect = TextPause.get_rect(center=(W // 2, H // 2 - 30))
        Fenetre.blit(TextPause, Pause_rect)

        TextContinue = pygame.font.SysFont(None, 50, italic=True, bold=True).render(
            "Appuyer sur 'Espace' pour continuer", True, (128, 139, 150))
        Continue_rect = TextContinue.get_rect(center=(W // 2, H // 2 + 100))
        Fenetre.blit(TextContinue, Continue_rect)

        pygame.display.update()


play()
