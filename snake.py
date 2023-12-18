import pygame
import random

pygame.init()

red = (255, 0, 0)
W, H = 800, 700
Fenetre = pygame.display.set_mode((W, H))
pygame.display.set_caption('Snake by Lucas Martinie')

pause = False
game_over = False
color = ''
user_input = ''

def play():
    global game_over
    game_over = False
    x = random.randrange(200, W - 200)
    y = random.randrange(150, H - 150)

    x_change = 0
    y_change = 0
    
    angle = 0
    angle_a = 0
    

    pomme_x = random.randrange(20, W - 20)
    pomme_y = random.randrange(100, H - 20)

    snake_liste = []
    snake_direction = []
    turning_positions = []
    snake_taille = 1
    point = 0

    bonus = random.randint(1,100)

    color = choose_snake()
    
    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if y_change < 0:
                        angle_a = -90
                    elif y_change > 0:
                        angle_a = 180
                    if x_change != -20:
                        x_change = -20
                        y_change = 0
                        angle = 0
                        add_turning_position(x, y, angle_a, turning_positions)
                elif event.key == pygame.K_RIGHT:
                    if y_change < 0:
                        angle_a = 0
                    elif y_change > 0:
                        angle_a = 90
                    if x_change != 20:
                        x_change = 20
                        y_change = 0
                        angle = 180
                        add_turning_position(x, y, angle_a, turning_positions)
                elif event.key == pygame.K_UP:
                    if x_change < 0:
                        angle_a = 90
                    elif x_change > 0:
                        angle_a = 180
                    if y_change != -20:
                        y_change = -20
                        x_change = 0
                        angle = 270
                        add_turning_position(x, y, angle_a, turning_positions)
                elif event.key == pygame.K_DOWN:
                    if x_change < 0:
                        angle_a = 0
                    elif x_change > 0:
                        angle_a = 270
                    if y_change != 20:
                        y_change = 20
                        x_change = 0
                        angle = 90
                        add_turning_position(x, y, angle_a, turning_positions)

                elif event.key == pygame.K_SPACE:
                    paused()                    

        Fenetre.fill((82, 190, 128))

        

        if bonus <= 2:
            pomme_img = pygame.image.load('img/pomme_g.png')
            Fenetre.blit(pomme_img, (pomme_x, pomme_y))
        else:
            pomme_img = pygame.image.load('img/pomme.png')
            Fenetre.blit(pomme_img, (pomme_x, pomme_y))

        if x > W - 20 or x < 0 or y > H - 20 or y < 80:
            game_over = True
            game_over_screen()

        x += x_change
        y += y_change

        snake_corps = []
        snake_corps.append(x)
        snake_corps.append(y)
        snake_liste.append(snake_corps)
        snake_direction.append(angle)

        for turning_position, angle_a in list(turning_positions):
            if tuple(snake_liste[-1]) == turning_position:
                turning_positions.remove((turning_position, angle_a))

        if len(snake_liste) > snake_taille:
            del snake_liste[0]
            del snake_direction[0]

        for i, (segment, direction) in enumerate(zip(snake_liste, snake_direction)):
            if i == len(snake_liste) - 1:
                head = pygame.image.load(f"img/{color}/head.png")
                head_a = pygame.transform.rotate(head, angle)
                Fenetre.blit(head_a, segment)
            elif i == 0:
                position_actu = (segment[0], segment[1])
                
                for pos, angle_a in turning_positions:
                    if position_actu == pos:
                        turning_body = pygame.image.load(f"img/{color}/body_turn.png")
                        turning_body_a = pygame.transform.rotate(turning_body, angle_a)
                        Fenetre.blit(turning_body_a, segment)
                        break
                else:
                    tail = pygame.image.load(f"img/{color}/tail.png")
                    tail_a = pygame.transform.rotate(tail, direction)
                    Fenetre.blit(tail_a, segment)

            else:
                position_actu = (segment[0], segment[1])
                for pos, angle_a in turning_positions:
                    if position_actu == pos:
                        turning_body = pygame.image.load(f"img/{color}/body_turn.png")
                        turning_body_a = pygame.transform.rotate(turning_body, angle_a)
                        Fenetre.blit(turning_body_a, segment)
                        break
                else:
                    body = pygame.image.load(f"img/{color}/body.png")
                    body_a = pygame.transform.rotate(body, direction)
                    Fenetre.blit(body_a, segment)

        pygame.draw.rect(Fenetre, (22, 22, 62), (0, 0, 800, 80))
        ShowScore = pygame.font.SysFont(None, 40, italic=True, bold=True).render(f"{point}", True, (128, 139, 150))
        ShowScore_rect = ShowScore.get_rect(center=(W // 4, 40))
        pomme_img = pygame.image.load('img/pomme.png')
        Fenetre.blit(ShowScore, ShowScore_rect)
        Fenetre.blit(pomme_img, (W // 4 - 40, 80 // 2 - pomme_img.get_width() // 2))

        pygame.display.update()

        if x <= pomme_x + 25 and x >= pomme_x - 25 and y <= pomme_y + 25 and y >= pomme_y - 25:
            pomme_x = random.randrange(25, W - 25)
            pomme_y = random.randrange(105, H - 25)
            if bonus <= 2:
                point += 3
            else:
                point += 1
            bonus = random.randint(1,100)
            snake_taille += 1
        pygame.time.Clock().tick(25)

def add_turning_position(x, y, angle_a, turning_positions):
    if (x, y) not in [pos for pos, _ in turning_positions]:
        turning_positions.append(((x, y), angle_a))

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

        TextOver = pygame.font.SysFont(None, 150, italic=True, bold=True).render("Game Over", (W // 2, H // 2 - 100), (192, 57, 43))
        TextOver_rect = TextOver.get_rect(center=(W // 2, H // 2 - 100))
        TextOverS = pygame.font.SysFont(None, 150, italic=True, bold=True).render("Game Over", True, (100, 30, 22))
        TextOverS.set_alpha(120)
        TextOverS_rect = TextOverS.get_rect(center=(W // 2 - 10, H // 2 - 90))

        Fenetre.blit(TextOverS, TextOverS_rect)
        Fenetre.blit(TextOver, TextOver_rect)

        TextContinue = pygame.font.SysFont(None, 50, italic=True, bold=True).render("Appuyer sur 'Espace' pour relancer la partie", True, (128, 139, 150))
        Continue_rect = TextContinue.get_rect(center=(W // 2, H // 2 + 100))
        Fenetre.blit(TextContinue, Continue_rect)

        pygame.display.update()

def username():
    font = pygame.font.Font(None, 60)
    user_input = ""
    supr = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    supr = True
                elif event.key == pygame.K_RETURN:
                    return user_input , play()
                else:
                    user_input += event.unicode
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    supr = False

        if supr:
            user_input2 = user_input[:-1]
            if len(user_input2) < len(user_input):
                pygame.time.delay(100)
                user_input = user_input2


        Fenetre.fill((39, 55, 70))

        text = pygame.font.SysFont(None, 80, italic=True).render("Entrer votre nom", True, (0, 0, 0))
        text_rect = text.get_rect(center=(W // 2, H // 3))
        Fenetre.blit(text, text_rect)
        
        input_rect = pygame.Rect(W // 2 - 200, H // 2, 400, 80)
        pygame.draw.rect(Fenetre, (0, 0, 0), input_rect, 2)
        input_surface = font.render(user_input, True, (0, 0, 0))
        input_surface_rect = input_surface.get_rect(center=input_rect.center)
        Fenetre.blit(input_surface, (input_surface_rect.x + 5, input_surface_rect.y))

        TextContinue = pygame.font.SysFont(None, 50, italic=True, bold=True).render("Appuyer sur 'Entrer' pour lancer la partie", True, (128, 139, 150))
        Continue_rect = TextContinue.get_rect(center=(W // 2, H // 2 + 200))
        Fenetre.blit(TextContinue, Continue_rect)
        pygame.display.update()

def choose_snake():
    c = 1
    right = False
    left = False 
    down = False
    up = False
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if c == 1:
                        color = 'green'
                    elif c == 2:
                        color = 'blue'
                    elif c == 3:
                        color = 'pink'
                    elif c == 4:
                        color = 'yellow'
                    elif c == 5:
                        color = 'sandwich'
                        # rand_color = ['green','blue','pink','yellow']
                        # color = random.choice(rand_color)
                    return color
                elif event.key == pygame.K_RIGHT:
                    right = True
                    if c == 1:
                        c = 2
                    elif c == 3:
                        c = 4
                elif event.key == pygame.K_LEFT:
                    left = True
                    if c == 2:
                        c = 1
                    elif c == 4:
                        c = 3
                elif event.key == pygame.K_DOWN:
                    down = True
                    if c == 1:
                        c = 3
                    elif c == 2:
                        c = 4
                    elif c == 3 or c == 4:
                        c = 5
                elif event.key == pygame.K_UP:
                    up = True
                    if c == 5:
                        c = 3
                    elif c == 3:
                        c = 1
                    elif c == 4:
                        c = 2
            elif event.type == pygame.KEYUP:
                    right = False
                    left = False 
                    down = False
                    up = False


        Fenetre.fill((39, 55, 70))


        ColorTitle = pygame.font.SysFont(None, 70, italic=True, bold=True).render("Choisir la couleur du Snake", True, (60, 73, 171))
        ColorTitle_rect = ColorTitle.get_rect(center=(W // 2, 40))
        ColorTitleS = pygame.font.SysFont(None, 70, italic=True, bold=True).render("Choisir la couleur du Snake", True, (60, 73, 131))
        ColorTitleS.set_alpha(180)
        ColorTitleS_rect = ColorTitleS.get_rect(center=(W // 2 - 5, 45))
        ColorTitleS2 = pygame.font.SysFont(None, 70, italic=True, bold=True).render("Choisir la couleur du Snake", True, (60, 73, 91))
        ColorTitleS2.set_alpha(140)
        ColorTitleS2_rect = ColorTitleS2.get_rect(center=(W // 2 - 10, 50))

        Fenetre.blit(ColorTitleS2, ColorTitleS2_rect)
        Fenetre.blit(ColorTitleS, ColorTitleS_rect)
        Fenetre.blit(ColorTitle, ColorTitle_rect)

        c1_button_rect = pygame.Rect(100, 110, 250, 200)
        pygame.draw.rect(Fenetre, (69, 90, 100), c1_button_rect)
        c2_button_rect = pygame.Rect(450, 110, 250, 200)
        pygame.draw.rect(Fenetre, (69, 90, 100), c2_button_rect)
        c3_button_rect = pygame.Rect(100, 360, 250, 200)
        pygame.draw.rect(Fenetre, (69, 90, 100), c3_button_rect)
        c4_button_rect = pygame.Rect(450, 360, 250, 200)
        pygame.draw.rect(Fenetre, (69, 90, 100), c4_button_rect)
        
        c5_text = pygame.font.Font(None, 30).render("Aléatoire", True, (210, 180, 222))
        c5_button_rect = pygame.Rect(W // 2  - 150, 605, 300, 50)
        c5_text_rect = c5_text.get_rect(center=c5_button_rect.center)
        pygame.draw.rect(Fenetre, (69, 90, 100), c5_button_rect)
        Fenetre.blit(c5_text, c5_text_rect)
        if c == 1:
            pygame.draw.rect(Fenetre, (140, 140, 140), c1_button_rect)
        elif c == 2:
            pygame.draw.rect(Fenetre, (140, 140, 140), c2_button_rect)
        elif c == 3:
            pygame.draw.rect(Fenetre, (140, 140, 140), c3_button_rect)
        elif c == 4:
            pygame.draw.rect(Fenetre, (140, 140, 140), c4_button_rect)
        elif c == 5:
            pygame.draw.rect(Fenetre, (140, 140, 140), c5_button_rect)
            Fenetre.blit(c5_text, c5_text_rect)

        snake_g = pygame.image.load(f"img/choose/snake_green.png")
        Fenetre.blit(snake_g, (100, 110))

        snake_b = pygame.image.load(f"img/choose/snake_blue.png")
        Fenetre.blit(snake_b, (450, 110))

        snake_p = pygame.image.load(f"img/choose/snake_pink.png")
        Fenetre.blit(snake_p, (100, 360))

        snake_y = pygame.image.load(f"img/choose/snake_yellow.png")
        Fenetre.blit(snake_y, (450, 360))

        key_ret = pygame.image.load("img/touche/key_return.png")
        Fenetre.blit(key_ret, (625, 580))        

        if right :
            key_r = pygame.image.load("img/touche/key_right_pressed.png")
            key_r = pygame.transform.scale(key_r, (60, 60))
            Fenetre.blit(key_r, (150, 635))
        else: 
            key_r = pygame.image.load("img/touche/key_right.png")
            Fenetre.blit(key_r, (150, 640))
        if left:
            key_l = pygame.image.load("img/touche/key_left_pressed.png")
            key_l = pygame.transform.scale(key_l, (60, 60))
            Fenetre.blit(key_l, (40, 635))
        else:
            key_l = pygame.image.load("img/touche/key_left.png")
            Fenetre.blit(key_l, (50, 640))
        if down:
            key_d = pygame.image.load("img/touche/key_down_pressed.png")
            key_d = pygame.transform.scale(key_d, (60, 60))
            Fenetre.blit(key_d, (95, 640))
        else:
            key_d = pygame.image.load("img/touche/key_down.png")
            Fenetre.blit(key_d, (100, 640))
        if up:
            key_u = pygame.image.load("img/touche/key_up_pressed.png")
            key_u = pygame.transform.scale(key_u, (60, 60))
            Fenetre.blit(key_u, (95, 580))
        else:
            key_u = pygame.image.load("img/touche/key_up.png")
            Fenetre.blit(key_u, (100, 590))
        pygame.display.update()

def main():
    menu = True
    titre_charge = True
    titre_index = 0
    right = False
    left = False 
    down = False
    up = False    
    w_k = 40
    h_k = 580
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    username()
                    menu = False
                elif event.key == pygame.K_RIGHT:
                    right = True
                elif event.key == pygame.K_LEFT:
                    left = True
                elif event.key == pygame.K_DOWN:
                    down = True
                elif event.key == pygame.K_UP:
                    up = True
            elif event.type == pygame.KEYUP:
                    right = False
                    left = False 
                    down = False
                    up = False

        Fenetre.fill((39, 55, 70))
        titre = "Snake"

        if titre_charge:
            pygame.time.delay(200)
            texte_titre = pygame.font.SysFont('Calibri', 90, bold=True).render(titre[:titre_index], True, (0, 0, 0))
            texte_titre_rect = texte_titre.get_rect(center=(W//2, 100))
            Fenetre.blit(texte_titre, texte_titre_rect)
            pygame.display.flip()
            titre_index += 1

            if titre_index > len(titre):
                titre_charge = False
        else:
            texte_titre = pygame.font.SysFont('Calibri', 90, bold=True).render(titre, True, (0, 0, 0))
            texte_titre_rect = texte_titre.get_rect(center=(W//2, 100))
            Fenetre.blit(texte_titre, texte_titre_rect)

        TextContinue = pygame.font.SysFont(None, 50, italic=True, bold=True).render(
            "Appuyer sur 'Enter' pour continuer", True, (128, 139, 150))
        Continue_rect = TextContinue.get_rect(center=(W // 2, H // 2 + 100))
        Fenetre.blit(TextContinue, Continue_rect)

        key_ret = pygame.image.load("img/touche/key_return.png")
        Fenetre.blit(key_ret, (625, 580))        
        banane(right, left, down, up, w_k, h_k)
       
        pygame.display.update()

def banane(right, left, down, up, w_k, h_k):
    if right:
        key_r = pygame.image.load("img/touche/key_right_pressed.png")
        key_r = pygame.transform.scale(key_r, (60, 60))
        Fenetre.blit(key_r, (w_k + 110, h_k + 65))
    else:
        key_r = pygame.image.load("img/touche/key_right.png")
        Fenetre.blit(key_r, (w_k + 110, h_k + 60))

    if left:
        key_l = pygame.image.load("img/touche/key_left_pressed.png")
        key_l = pygame.transform.scale(key_l, (60, 60))
        Fenetre.blit(key_l, (w_k, h_k + 65))
    else:
        key_l = pygame.image.load("img/touche/key_left.png")
        Fenetre.blit(key_l, (w_k + 10, h_k + 60))

    if down:
        key_d = pygame.image.load("img/touche/key_down_pressed.png")
        key_d = pygame.transform.scale(key_d, (60, 60))
        Fenetre.blit(key_d, (w_k + 55, h_k + 60))
    else:
        key_d = pygame.image.load("img/touche/key_down.png")
        Fenetre.blit(key_d, (w_k + 60, h_k + 60))

    if up:
        key_u = pygame.image.load("img/touche/key_up_pressed.png")
        key_u = pygame.transform.scale(key_u, (60, 60))
        Fenetre.blit(key_u, (w_k + 55, h_k))
    else:
        key_u = pygame.image.load("img/touche/key_up.png")
        Fenetre.blit(key_u, (w_k + 60, h_k + 10))

    return key_r, key_l, key_d, key_u

main()


