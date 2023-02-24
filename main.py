import pygame
import random
import sys

pygame.init() #initialise pygame

# définir les couleurs
white = (255, 255, 255) 
yellow = (255, 255, 102) 
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# définir la taille de la fenêtre
dis_width = 600
dis_height = 400


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')


clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# définir les police d'écriture
font_message = pygame.font.SysFont("bahnschrift", 20) 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# définir la fonction pour afficher le score
def Score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# définir la fonction pour afficher le serpent
def Bloc_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# définir la fonction pour afficher le message a la fin de la partie
def Message(msg, color):
    mesg = font_message.render(msg, True, color)
    dis.blit(mesg, [dis_width / 8, dis_height / 3])

# définir la fonction pour afficher le 2eme message a la fin de la partie
def Message2(msg, color):
    mesg = font_message.render(msg, True, color)
    dis.blit(mesg, [dis_width / 8, dis_height / 2])

# définir la fonction pour créer un menu au début du jeu 
def start_game():
    dis.fill(black)
    font_start_1 = score_font.render("Bienvenue !", True, green)
    font_start_2 = font_style.render("Nouvelle partie", True, red, blue)
    font_start_3 = font_style.render("Quitter", True, red, blue)
    font_start_4 = font_style.render("Tableau des scores", True, red, blue)

    font_start_1_rect = font_start_1.get_rect()
    font_start_2_rect = font_start_2.get_rect()
    font_start_3_rect = font_start_3.get_rect()
    font_start_4_rect = font_start_4.get_rect()

    font_start_1_rect.center = (dis_width/2, dis_height/2 - 100)
    font_start_2_rect.center = (dis_width/2 + 100, dis_height/2 + 50)
    font_start_3_rect.center = (dis_width/2 + 100, dis_height/2 + 150)
    font_start_4_rect.center = (dis_width / 2 + 100, dis_height / 2 + 100)

    dis.blit(font_start_1, font_start_1_rect) 
    dis.blit(font_start_2, font_start_2_rect)
    dis.blit(font_start_3, font_start_3_rect)
    dis.blit(font_start_4, font_start_4_rect)
    pygame.display.update()

    #boucle qui permet de cliquer sur les boutons du menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameLoop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > font_start_2_rect.left and x < font_start_2_rect.right:
                    if y > font_start_2_rect.top and y < font_start_2_rect.bottom:
                        gameLoop()
                if x > font_start_4_rect.left and x < font_start_4_rect.right:
                    if y > font_start_4_rect.top and y < font_start_4_rect.bottom:
                        score()
                if x > font_start_3_rect.left and x < font_start_3_rect.right:
                    if y > font_start_3_rect.top and y < font_start_3_rect.bottom:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()

# définir la fonction pour ajouter le nom du joueur et son score dans un fichier texte
def add_name_score():
    dis.fill(black)

    font_gameover2 = font_style.render("Tapez votre nom puis sur ENTER : ", True, red, blue)
    font_gameover2_rect = font_gameover2.get_rect()
    font_gameover2_rect.center = (dis_width / 2, dis_height / 2)
    dis.blit(font_gameover2, font_gameover2_rect)

    font = pygame.font.Font(None, 32)

    nom = ""

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    nom += event.unicode
                elif event.key == pygame.K_RETURN:
                    with open("score.txt", "a") as f:
                        f.write(f"{nom} : {Length_of_snake - 1}\n")
                    start_game()

        text = font.render(nom, True, (255, 255, 255))
        dis.blit(text, (dis_width/2 - 100, dis_height/2 + 100))

        pygame.display.update()

# définir la fonction pour afficher le tableau des scores
def score():
    dis.fill(black)

    with open("score.txt", "r") as file:
        lines = file.readlines()

        y = 50

        for line in lines:
            score_text = font_style.render(line.strip(), True, (255, 255, 255))
            score_rect = score_text.get_rect()
            score_rect.center = (dis_width / 2, y)
            dis.blit(score_text, score_rect)

            y += 50

    start_inst5 = font_style.render("<<Retour", True, red, blue)
    start_inst5_rect = start_inst5.get_rect()
    start_inst5_rect.center = (dis_width - start_inst5_rect.width / 2, dis_height - start_inst5_rect.height / 2)
    dis.blit(start_inst5, start_inst5_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
        pygame.display.update()

# définir la fonction pour le jeu
def gameLoop():
    global Length_of_snake
    game_over = False
    game_close = False
    # définir les coordonnées de départ du serpent
    x1 = dis_width / 2
    y1 = dis_height / 2
    # définir les mouvements du serpent sur l'axe des x et des y
    x1_change = 0
    y1_change = 0
    # la liste qui contient les coordonnées du serpent
    snake_List = []
    Length_of_snake = 1
    # la bouffe du serpent
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        #Ecran de game over 
        while game_close == True:
            dis.fill(black)
            Message("Perdu !   R=Rejouer   M=Retour au menu     Q=Quitter ", blue)
            Message2("S=Enregistrer le Score", blue)
            Score(Length_of_snake - 1)
            pygame.display.update()
            #touches pour rejouer, retourner au menu ou quitter
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()
                    if event.key == pygame.K_m:
                        start_game()
                    if event.key == pygame.K_s:
                        add_name_score()
        #Touches pour se déplacer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change == snake_block:
                        pass #pour ne pas pouvoir aller à gauche si on va déjà à droite
                    else:
                        x1_change = -snake_block
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change == -snake_block:
                        pass #pour ne pas pouvoir aller à droite si on va déjà à gauche
                    else:
                        x1_change = snake_block
                        y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change == snake_block:
                        pass #pour ne pas pouvoir aller en haut si on va déjà en bas
                    else:
                        y1_change = -snake_block
                        x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change == -snake_block:
                        pass # pour ne pas pouvoir aller en bas si on va déjà en haut
                    else:
                        y1_change = snake_block 
                        x1_change = 0
        #conditions de défaite
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        Bloc_snake(snake_block, snake_List)
        Score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

start_game()