import pygame
import random

pygame.init()

W, H = 800, 700
Back = pygame.display.set_mode((W, H))
Fenetre = pygame.display.set_mode((W, H))
pygame.display.set_caption('Snake by Lucas Martinie')

pause = False
game_over = False
user_input = ''
right = False
left = False 
down = False
up = False
color = 'green'

def main():
    global right, left, up, down, color
    c = 1
    menu = True
    w_k = 40
    h_k = 580
    color_menu = 'green'
    x_change = -20
    y_change = 0
    angle = 0
    angle_a = 90
    snake_liste = []
    snake_direction = []
    turning_positions = []
    snake_taille = 35
    decalage = 0
    dir = 'left'
    starting = True
    x = 400
    y = 230
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                    if c == 1:
                        username()
                    elif c == 2:
                        color = choose_snake()
                    elif c == 3:
                        score()
                elif event.key == pygame.K_RIGHT:
                    right = True
                elif event.key == pygame.K_LEFT:
                    left = True
                elif event.key == pygame.K_DOWN:
                    down = True
                    if c== 1:
                        c=2
                        starting = True
                    elif c==2:
                        c=3
                        starting = True
                elif event.key == pygame.K_UP:
                    up = True
                    if c== 2:
                        c=1
                        starting = True
                    elif c==3:
                        c=2
                        starting = True
            elif event.type == pygame.KEYUP:
                right = False
                left = False 
                down = False
                up = False

        Fenetre.fill((39, 55, 70))
        if color == 'sandwich':
            snake_title("Snack")
        else: 
            snake_title("Snake")

        c1_text = pygame.font.SysFont('Calibri', 60, bold=True).render("Jouer", True, (210, 180, 222))
        c1_button_rect = pygame.Rect(W // 2  - 300, 150, 600, 100)
        c1_text_rect = c1_text.get_rect(center=c1_button_rect.center)
        pygame.draw.rect(Fenetre, (69, 90, 100), c1_button_rect)
        Fenetre.blit(c1_text, c1_text_rect)
        c2_text = pygame.font.SysFont('Calibri', 60, bold=True).render("Options", True, (210, 180, 222))
        c2_button_rect = pygame.Rect(W // 2  - 300, 300, 600, 100)
        c2_text_rect = c2_text.get_rect(center=c2_button_rect.center)
        pygame.draw.rect(Fenetre, (69, 90, 100), c2_button_rect)
        Fenetre.blit(c2_text, c2_text_rect)
        
        c3_text = pygame.font.SysFont('Calibri', 60, bold=True).render("Score", True, (210, 180, 222))
        c3_button_rect = pygame.Rect(W // 2  - 300, 450, 600, 100)
        c3_text_rect = c3_text.get_rect(center=c3_button_rect.center)
        pygame.draw.rect(Fenetre, (69, 90, 100), c3_button_rect)
        Fenetre.blit(c3_text, c3_text_rect)

        if c == 1:
            pygame.draw.rect(Fenetre, (140, 140, 140), c1_button_rect)
            Fenetre.blit(c1_text, c1_text_rect)
            if starting:
                snake_liste = []
                snake_direction = []
                decalage = 0
                x = 400
                y = 230
                dir = 'left'
                color_menu = 'green'
                starting = False
        elif c == 2:
            pygame.draw.rect(Fenetre, (140, 140, 140), c2_button_rect)
            Fenetre.blit(c2_text, c2_text_rect)
            if starting:
                snake_liste = []
                snake_direction = []
                decalage = 150
                x = 400
                y = 380
                dir = 'left'
                color_menu = 'blue'
                starting = False
        elif c == 3:
            pygame.draw.rect(Fenetre, (140, 140, 140), c3_button_rect)
            Fenetre.blit(c3_text, c3_text_rect)
            if starting:
                snake_liste = []
                snake_direction = []
                decalage = 300
                x = 400
                y = 530
                dir = 'left'
                color_menu = 'pink'
                starting = False

        key_ret = pygame.image.load("img/touche/key_return.png")
        Fenetre.blit(key_ret, (625, 580))        
        touche_anim(right, left, down, up, w_k, h_k)

        credit = pygame.font.SysFont('Calibri', 18).render("Snake par Lucas Martinie", True, (189, 189, 189))
        credit_rect = credit.get_rect(center=(W - 140, H - 15))
        Fenetre.blit(credit, credit_rect)

        if dir == 'left':
            if y_change < 0:
                angle_a = -90
            elif y_change > 0:
                angle_a = 180
            if x_change != -20:
                x_change = -20
                y_change = 0
                angle = 0
                add_turning_position(x, y, angle_a, turning_positions)

        elif dir == 'right':
            if y_change < 0:
                angle_a = 0
            elif y_change > 0:
                angle_a = 90
            if x_change != 20:
                x_change = 20
                y_change = 0
                angle = 180
                add_turning_position(x, y, angle_a, turning_positions)

        elif dir == 'up':
            if x_change < 0:
                angle_a = 90
            elif x_change > 0:
                angle_a = 180
            if y_change != -20:
                y_change = -20
                x_change = 0
                angle = 270
                add_turning_position(x, y, angle_a, turning_positions)

        elif dir == 'down':
            if x_change < 0:
                angle_a = 0
            elif x_change > 0:
                angle_a = 270
            if y_change != 20:
                y_change = 20
                x_change = 0
                angle = 90
                add_turning_position(x, y, angle_a, turning_positions)

        x += x_change
        y += y_change


        if x == 100 and y == 230 + decalage:
            dir = 'up'
        elif x == 100 and y == 150 + decalage:
            dir = 'right'
        elif x == 680 and y == 150 + decalage:
            dir = 'down'
        elif x == 680 and y == 230 + decalage:
            dir = 'left'

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
                head = pygame.image.load(f"img/{color_menu}/head.png")
                head_a = pygame.transform.rotate(head, angle)
                Back.blit(head_a, segment)
            elif i == 0:
                position_actu = (segment[0], segment[1])

                for pos, angle_a in turning_positions:
                    if position_actu == pos:
                        turning_body = pygame.image.load(f"img/{color_menu}/body_turn.png")
                        turning_body_a = pygame.transform.rotate(turning_body, angle_a)
                        Back.blit(turning_body_a, segment)
                        break
                else:
                    tail = pygame.image.load(f"img/{color_menu}/tail.png")
                    tail_a = pygame.transform.rotate(tail, direction)
                    Back.blit(tail_a, segment)

            else:
                position_actu = (segment[0], segment[1])
                for pos, angle_a in turning_positions:
                    if position_actu == pos:
                        turning_body = pygame.image.load(f"img/{color_menu}/body_turn.png")
                        turning_body_a = pygame.transform.rotate(turning_body, angle_a)
                        Back.blit(turning_body_a, segment)
                        break
                else:
                    body = pygame.image.load(f"img/{color_menu}/body.png")
                    body_a = pygame.transform.rotate(body, direction)
                    Back.blit(body_a, segment)

        pygame.time.Clock().tick(30)
       
        pygame.display.update()

def play(color,user_input):
    global point
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

    with open("scores.txt", "r") as scores_file:
        scores = [tuple(map(str, line.strip().split())) for line in scores_file if len(line.strip().split()) == 2]
        if scores:
            sorted_scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
            high_score = max(sorted_scores, key=lambda x: int(x[1]))
        else:
            high_score = "0"

    bonus = random.randint(1,100)

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
                
        if color == 'water':
            Fenetre.fill((36, 113, 163))
        elif color == 'desert':
            Fenetre.fill((183, 149, 11))
        elif color == 'neige':
            Fenetre.fill((214, 234, 248))
        else:
            Fenetre.fill((82, 190, 128))

        if color == 'sandwich':
            object_eat = 'sandwich'
        elif color == "water":
            object_eat = 'poisson'
        elif color == "desert":
            object_eat = 'papyrus'
        elif color == 'neige':
            object_eat = 'boulle'
        else:
            object_eat = 'pomme'

        if bonus <= 2:
            pomme_img = pygame.image.load(f'img/manger/{object_eat}_b.png')
            Fenetre.blit(pomme_img, (pomme_x, pomme_y))
        else:
            pomme_img = pygame.image.load(f'img/manger/{object_eat}_n.png')
            Fenetre.blit(pomme_img, (pomme_x, pomme_y))

        if x > W - 20 or x < 0 or y > H - 20 or y < 80:
            update_scores(user_input, point)
            game_over = True
            game_over_screen()
        for i in snake_liste[:-1]:
            if i == snake_corps:
                update_scores(user_input, point)
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
        ShowScore_rect = ShowScore.get_rect(center=(150, 40))
        pomme_img = pygame.image.load(f'img/manger/{object_eat}_n.png')
        pomme_img = pygame.transform.scale(pomme_img, (40, 40))
        Fenetre.blit(ShowScore, ShowScore_rect)
        Fenetre.blit(pomme_img, (90, 80 // 2 - pomme_img.get_width() // 2))

        HighestScore = pygame.font.SysFont(None, 40, italic=True, bold=True).render(f"{high_score[1]}", True, (128, 139, 150))
        HighestScore_rect = HighestScore.get_rect(center=(260, 40))
        Fenetre.blit(HighestScore, HighestScore_rect)
        trophee_img = pygame.image.load(f'img/manger/trophee.png')
        trophee_img = pygame.transform.scale(trophee_img, (40, 40))
        Fenetre.blit(trophee_img, (200, 80 // 2 - trophee_img.get_width() // 2))

        if color == "sandwich":
            title = "Snack"
        else:
            title = "Snake"
        Text_titre = pygame.font.SysFont(None, 60, italic=True, bold=True).render(title, True, (128, 139, 150))
        Text_rect = Text_titre.get_rect(center=(W // 2, 40))
        Fenetre.blit(Text_titre, Text_rect)
        pygame.display.update()

        if x <= pomme_x + 25 and x >= pomme_x - 25 and y <= pomme_y + 25 and y >= pomme_y - 25:
            pomme_x = random.randrange(25, W - 25)
            pomme_y = random.randrange(105, H - 25)
            bonus = random.randint(1, 100)
            snake_taille += 1
            if bonus <= 2:
                point += 3
            else:
                point += 1
        while any((pomme_x, pomme_y) == segment for segment in snake_liste):
            pomme_x = random.randrange(25, W - 25)
            pomme_y = random.randrange(105, H - 25)

        pygame.time.Clock().tick(30)

def add_turning_position(x, y, angle_a, turning_positions):
    if (x, y) not in [pos for pos, _ in turning_positions]:
        turning_positions.append(((x, y), angle_a))

def snake_title(titre):
        ColorTitle = pygame.font.SysFont(None, 150, italic=True, bold=True).render(titre, True, (39, 174, 96))
        ColorTitle_rect = ColorTitle.get_rect(center=(W // 2, 65))
        ColorTitleS = pygame.font.SysFont(None, 150, italic=True, bold=True).render(titre, True, (34, 153, 84))
        ColorTitleS.set_alpha(140)
        ColorTitleS_rect = ColorTitleS.get_rect(center=(W // 2 - 10, 75))
        ColorTitleS2 = pygame.font.SysFont(None, 150, italic=True, bold=True).render(titre, True, (20, 90, 50))
        ColorTitleS2.set_alpha(120)
        ColorTitleS2_rect = ColorTitleS2.get_rect(center=(W // 2 - 15, 85))
        Fenetre.blit(ColorTitleS2, ColorTitleS2_rect)
        Fenetre.blit(ColorTitleS, ColorTitleS_rect)
        Fenetre.blit(ColorTitle, ColorTitle_rect)

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

        snake_title("Snake")

        pause_img = pygame.image.load(f"img/touche/pause.png")
        pause_img_a = pygame.transform.scale(pause_img, (300,300))
        Fenetre.blit(pause_img_a,(W//2 - pause_img_a.get_width()//2, 180))

        TextPause = pygame.font.SysFont('Calibri', 150, italic=True, bold=True).render("Pause", True, (128, 139, 150))
        TextPause.set_alpha(180)
        Pause_rect = TextPause.get_rect(center=(W // 2, 330))
        Fenetre.blit(TextPause, Pause_rect)

        TextContinue = pygame.font.SysFont(None, 50, italic=True, bold=True).render(
            "Appuyer sur 'Espace' pour continuer", True, (128, 139, 150))
        Continue_rect = TextContinue.get_rect(center=(W // 2, H -100))
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
                if event.key == pygame.K_RETURN:
                    game_over = False
                    main()

        Fenetre.fill((39, 55, 70))

        TextOver = pygame.font.SysFont(None, 150, italic=True, bold=True).render("Game Over", (W // 2, H // 2 - 100), (192, 57, 43))
        TextOver_rect = TextOver.get_rect(center=(W // 2, H // 2 - 100))
        TextOverS = pygame.font.SysFont(None, 150, italic=True, bold=True).render("Game Over", True, (100, 30, 22))
        TextOverS.set_alpha(120)
        TextOverS_rect = TextOverS.get_rect(center=(W // 2 - 10, H // 2 - 90))

        Fenetre.blit(TextOverS, TextOverS_rect)
        Fenetre.blit(TextOver, TextOver_rect)

        TextContinue = pygame.font.SysFont(None, 50, italic=True, bold=True).render("'Entrer' pour revenir au menu", True, (128, 139, 150))
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
                    if user_input != '':
                        formatted_input = user_input.capitalize()
                        return formatted_input, play(color, formatted_input)
                else:
                    if len(user_input) < 12:
                        if event.unicode.isalpha():
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
        snake_title("Snake")

        text = pygame.font.SysFont('Calibri', 80, italic=True, bold=True).render("Entrer votre nom", True, (0, 0, 0))
        text_rect = text.get_rect(center=(W // 2, H // 3))
        Fenetre.blit(text, text_rect)
        
        input_rect = pygame.Rect(W // 2 - 200, H // 2, 400, 80)
        pygame.draw.rect(Fenetre, (0, 0, 0), input_rect, 3)
        input_surface = font.render(user_input.capitalize(), True, (212, 239, 223))
        input_surface_rect = input_surface.get_rect(center=input_rect.center)
        Fenetre.blit(input_surface, (input_surface_rect.x + 5, input_surface_rect.y))

        TextContinue = pygame.font.SysFont(None, 50, italic=True, bold=True).render("Appuyer sur 'Entrer' pour lancer la partie", True, (128, 139, 150))
        Continue_rect = TextContinue.get_rect(center=(W // 2, H // 2 + 200))
        Fenetre.blit(TextContinue, Continue_rect)
        pygame.display.update()

def choose_snake():
    global up, down, right, left
    etage = 1
    w_k = 40
    h_k = 580
    scroll = 0
    scroll2 = 0
    c = 1
    global color
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
                        color = 'water'
                    elif c == 6:
                        color = 'sandwich'
                    elif c == 7:
                        color = 'desert'
                    elif c == 8:
                        color = 'neige'
                    elif c == 9:
                        rand_color = ['green','blue','pink','yellow', 'water', 'sandwich', 'desert', 'neige']
                        color = random.choice(rand_color)
                    main()
                    return color
                elif event.key == pygame.K_RIGHT:
                    right = True
                    if c < 9:
                        c+= 1
                elif event.key == pygame.K_LEFT:
                    left = True
                    if c > 1:
                        c-= 1
                elif event.key == pygame.K_DOWN:
                    down = True
                    if c < 8:
                        c+= 2
                    elif c == 8:
                        c+=1
                elif event.key == pygame.K_UP:
                    up = True
                    if c > 2:
                        c-= 2
            elif event.type == pygame.KEYUP:
                right = False
                left = False 
                down = False
                up = False

        Fenetre.fill((39, 55, 70))

        pygame.time.Clock().tick(40)

        c1_button_rect = pygame.Rect(100, 110 + scroll, 250, 200)
        pygame.draw.rect(Fenetre, (69, 90, 100), c1_button_rect)
        c2_button_rect = pygame.Rect(450, 110 + scroll, 250, 200)
        pygame.draw.rect(Fenetre, (69, 90, 100), c2_button_rect)
        c3_button_rect = pygame.Rect(100, 360 + scroll, 250, 200)
        pygame.draw.rect(Fenetre, (69, 90, 100), c3_button_rect)
        c4_button_rect = pygame.Rect(450, 360 + scroll, 250, 200)
        pygame.draw.rect(Fenetre, (69, 90, 100), c4_button_rect)
        
        c5_button_rect = pygame.Rect(100, 360+scroll2, 250, 200)
        c6_button_rect = pygame.Rect(450, 360+scroll2, 250, 200)
        c7_button_rect = pygame.Rect(100, 360, 250, 200)
        c8_button_rect = pygame.Rect(450, 360, 250, 200)

        snake_g = pygame.image.load("img/choose/snake_green.png")
        Fenetre.blit(snake_g, (100, 110 + scroll))

        snake_b = pygame.image.load("img/choose/snake_blue.png")
        Fenetre.blit(snake_b, (450, 110 + scroll))

        snake_p = pygame.image.load("img/choose/snake_pink.png")
        Fenetre.blit(snake_p, (100, 360 + scroll))

        snake_y = pygame.image.load("img/choose/snake_yellow.png")
        Fenetre.blit(snake_y, (450, 360 + scroll))

        snake_water = pygame.image.load("img/choose/snake_water.png")

        snake_sandwich = pygame.image.load("img/choose/snake_sandwich.png")
        snake_desert = pygame.image.load("img/choose/snake_desert.png")
        snake_neige = pygame.image.load("img/choose/snake_neige.png")

        if c == 1:
            pygame.draw.rect(Fenetre, (140, 140, 140), c1_button_rect)
            Fenetre.blit(snake_g, (100, 110 + scroll))

        elif c == 2:
            pygame.draw.rect(Fenetre, (140, 140, 140), c2_button_rect)
            Fenetre.blit(snake_b, (450, 110 + scroll))

        elif c == 3:
            pygame.draw.rect(Fenetre, (140, 140, 140), c3_button_rect)
            Fenetre.blit(snake_p, (100, 360 + scroll))
        elif c == 4:
            pygame.draw.rect(Fenetre, (140, 140, 140), c4_button_rect)
            Fenetre.blit(snake_y, (450, 360 + scroll))
        if etage == 1 and c > 4:
            scroll = -250
            etage = 2
        elif etage == 2 and c > 6:
            scroll = -500
            scroll2 = -250
            etage = 3
        elif etage == 3 and c < 5:
            etage = 2
            scroll = -250
            scroll2 = 0
        elif etage == 2 and c < 3:
            scroll = 0
            etage = 1


        if c <= 4 and scroll == 0: 
            ColorTitle = pygame.font.SysFont(None, 70, italic=True, bold=True).render("Choisir la couleur du Snake", True, (84, 153, 199))
            ColorTitle_rect = ColorTitle.get_rect(center=(W // 2, 40))
            ColorTitleS = pygame.font.SysFont(None, 70, italic=True, bold=True).render("Choisir la couleur du Snake", True, (41, 128, 185))
            ColorTitleS.set_alpha(140)
            ColorTitleS_rect = ColorTitleS.get_rect(center=(W // 2 - 5, 45))
            ColorTitleS2 = pygame.font.SysFont(None, 70, italic=True, bold=True).render("Choisir la couleur du Snake", True, (31, 97, 141))
            ColorTitleS2.set_alpha(100)
            ColorTitleS2_rect = ColorTitleS2.get_rect(center=(W // 2 - 10, 50))

            Fenetre.blit(ColorTitleS2, ColorTitleS2_rect)
            Fenetre.blit(ColorTitleS, ColorTitleS_rect)
            Fenetre.blit(ColorTitle, ColorTitle_rect)

        elif c >= 2 and scroll < 0:
            pygame.draw.rect(Fenetre, (69, 90, 100), c5_button_rect)
            Fenetre.blit(snake_water, (100, 360 + scroll2))

            pygame.draw.rect(Fenetre, (69, 90, 100), c6_button_rect)
            Fenetre.blit(snake_sandwich, (450, 360 + scroll2))

        if c > 4 and scroll == -500:
            pygame.draw.rect(Fenetre, (69, 90, 100), c7_button_rect)
            Fenetre.blit(snake_desert, (100, 360))

            pygame.draw.rect(Fenetre, (69, 90, 100), c8_button_rect)
            Fenetre.blit(snake_neige, (450, 360))

        menu_button_rect = pygame.Rect(W // 2  - 150, 605, 300, 50)
        if etage == 3:

            menu_text = pygame.font.Font(None, 30).render("Aléatoire", True, (210, 180, 222))
            menu_text_rect = menu_text.get_rect(center=menu_button_rect.center)
            if c == 9:
                pygame.draw.rect(Fenetre, (140, 140, 140), menu_button_rect)
                Fenetre.blit(menu_text, menu_text_rect)
            else : 
                pygame.draw.rect(Fenetre, (69, 90, 100), menu_button_rect)
                Fenetre.blit(menu_text, menu_text_rect)
        else:
            menu_text = pygame.font.Font(None, 30).render("Voir plus", True, (210, 180, 222))
            menu_text_rect = menu_text.get_rect(center=menu_button_rect.center)
            pygame.draw.rect(Fenetre, (69, 90, 100), menu_button_rect)
            Fenetre.blit(menu_text, menu_text_rect)

        if c == 5:
            pygame.draw.rect(Fenetre, (140, 140, 140), c5_button_rect)
            Fenetre.blit(snake_water, (100, 360+ scroll2))
        elif c== 6:
            pygame.draw.rect(Fenetre, (140, 140, 140), c6_button_rect)
            Fenetre.blit(snake_sandwich, (450, 360+ scroll2))
        elif c == 7:
            pygame.draw.rect(Fenetre, (140, 140, 140), c7_button_rect)
            Fenetre.blit(snake_desert, (100, 360))            
        elif c == 8:
            pygame.draw.rect(Fenetre, (140, 140, 140), c8_button_rect)
            Fenetre.blit(snake_neige, (450, 360))
        
        key_ret = pygame.image.load("img/touche/key_return.png")
        Fenetre.blit(key_ret, (625, 580))   
        touche_anim(right, left, down, up, w_k, h_k)

        pygame.draw.rect(Fenetre, (69, 90, 100), (W - 45, 100, 30, H - 200))
        if etage == 1:
            pygame.draw.rect(Fenetre, (39, 55, 70), (W - 42, 130, 24, 180))
        elif etage == 2:
            pygame.draw.rect(Fenetre, (39, 55, 70), (W - 42, 270, 24, 180))
        elif etage == 3:
            pygame.draw.rect(Fenetre, (39, 55, 70), (W - 42, 390, 24, 180))    
        if etage == 1 or etage == 2:
            scrolling_arrow = pygame.image.load("img/touche/fleche_down.png")
            Fenetre.blit(scrolling_arrow, (W-42, 560))
        if etage == 2 or etage == 3:
            scrolling_arrow = pygame.image.load("img/touche/fleche.png")
            Fenetre.blit(scrolling_arrow, (W-42, 120))
        pygame.display.update()

def touche_anim(right, left, down, up, w_k, h_k):
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

def load_scores():
    scores = []
    try:
        with open("scores.txt", "r") as scores_file:
            for line in scores_file:
                data = line.strip().split()
                if len(data) == 2:
                    name, score = data
                    scores.append((name, int(score)))
    except FileNotFoundError:
        pass
    return scores

def score():
    scores = load_scores()
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_RETURN:
                    main()

        Fenetre.fill((39, 55, 70))

        TextContinue = pygame.font.SysFont('Calibri', 50, italic=True, bold=True).render("'Entrer' pour revenir au menu", True, (128, 139, 150))
        Continue_rect = TextContinue.get_rect(center=(W // 2, H - 50))
        Fenetre.blit(TextContinue, Continue_rect)

        text = pygame.font.SysFont('Calibri', 80, bold=True).render("Top scores", True, (244, 208, 63))
        text_rect = text.get_rect(center=(W // 2, 55))
        Fenetre.blit(text, text_rect)
        trophee_img = pygame.image.load(f'img/manger/trophee.png')
        trophee_img = pygame.transform.scale(trophee_img, (80, 80))
        Fenetre.blit(trophee_img, (100, 55- trophee_img.get_width() // 2))
        Fenetre.blit(trophee_img, (W - 180, 55- trophee_img.get_width() // 2))

        if len(scores) > 14:
            half_length = len(scores) // 2
            left_scores = scores[:half_length]
            right_scores = scores[half_length:]
            left_position = 130
            for name, score in left_scores:
                score_text = pygame.font.Font(None, 40).render(f"{name}: {score}", True, (212, 239, 223))
                score_rect = score_text.get_rect(topleft=(W // 4, left_position))
                Fenetre.blit(score_text, score_rect)
                left_position += 40

            right_position = 130
            for name, score in right_scores:
                score_text = pygame.font.Font(None, 40).render(f"{name}: {score}", True, (212, 239, 223))
                score_rect = score_text.get_rect(topright=(3 * W // 4, right_position))
                Fenetre.blit(score_text, score_rect)
                right_position += 40
        else:
            y_position = 130
            for name, score in scores:
                score_text = pygame.font.Font(None, 40).render(f"{name}: {score}", True, (212, 239, 223))
                score_rect = score_text.get_rect(center=(W//2, y_position))
                Fenetre.blit(score_text, score_rect)
                y_position += 40

        pygame.display.flip()

def update_scores(user_input, point):
    scores = load_scores()
    user_exists = False

    for i, (name, score) in enumerate(scores):
        if name == user_input:
            user_exists = True
            if point > score:
                scores[i] = (user_input, point)
            break

    if not user_exists:
        scores.append((user_input, point))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    with open("scores.txt", "w") as scores_file:
        for name, score in scores:
            scores_file.write(f"{name} {score}\n")

main()