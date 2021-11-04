import pygame, sys
from random import choice

ball_x, ball_y = 25, 25

pygame.init()

f1 = pygame.font.Font(None, 150)

# scenes

player_scene = f1.render("YOU", True, (255, 255, 255))
player_scene_rect = player_scene.get_rect(center=(540, 1300))

a_i_scene = f1.render("A.I.", True, "white")
a_i_rect = a_i_scene.get_rect(center=(540, 700))


screen = pygame.display.set_mode((1080, 2031))
clock = pygame.time.Clock()

player = pygame.Rect(400, 2000, 200, 14)
ball = pygame.Rect(540, 1015, 30, 30)
movex = 0
print(screen.get_height())

opponent = pygame.Rect(400, 13, 200, 14)
game_active = False
playercol = "white"
enemycol = "white"

your_score = 0
ai_score = 0

main_sc = f1.render("CLICK TO START", True, "white")

main2 = f1.render("TENNIS: A.I.", True, "white")

bg_music=pygame.mixer.Sound('Kfluff.mp3')

bg_music.play(loops=-1)

bounce_m=pygame.mixer.Sound('bbepp.wav')
run=True
while run:

    mx, my = pygame.mouse.get_pos()

    my_score = f1.render(f"Score: {your_score}", True, "white")
    my_score_rect = my_score.get_rect(center=(540, 1700))

    ene_score = f1.render(f"Score: {ai_score}", True, "white")
    ene_score_rect = ene_score.get_rect(center=(540, 300))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()
        if game_active:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                pass
                # player.x=mx

            if ev.type == pygame.MOUSEBUTTONUP:
                movex = 0

        else:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                ball.center = 540, 1000

    screen.fill((70, 0, 0))
    if game_active:
        ball.x += ball_x
        ball.y += ball_y
        if ball.colliderect(player):
            print("coll")
            ball_y *= -1
            ball_x *= choice([1, -1])
            playercol = "green"

        if ball.colliderect(opponent):
            print("coll2")
            ball_y *= -1
            ball_x *= choice([1, -1])
            enemycol = "green"

        if ball.left <= 0 or ball.right >= 1080:
            ball_x *= -1
            ball_y *= choice([1, -1, 1, 1, 1])
        if ball.top <= 0 or ball.bottom >= 2031:
            ball_y *= -1
            # ball_x*=choice([1,1,-1])
            if ball.bottom >= 2031:
                playercol = "red"
                ai_score += 1
                bounce_m.play()
            if ball.top <= 0:
                enemycol = "red"
                your_score += 1
                bounce_m.play()

        if player.left <= 0:
            player.left = 0
        if player.right >= 1080:
            player.right = 1080

        if ball.y <= 200:
            opponent.centerx = ball.centerx
        # if ball.y<=600 or (ball.y<1200 and ball.y>300):
        #    playercol="white"

        if playercol == "red":
            if ball.y <= 300:
                playercol = "white"
        if playercol == "green":
            if ball.y <= 1500:
                playercol = "white"
        if ball.y >= 500:
            enemycol = "white"

        if opponent.right >= 1080:
            opponent.right = 1070
        if opponent.left <= 10:
            opponent.left = 10

        player.x = mx - 100

        if your_score <= 0:
            your_score = 0
        if ai_score <= 0:
            ai_score = 0

        if ball.bottom > 2031:
            ball.center = (540, 1015)
        if ball.top <= 0:
            ball.center = (540, 1015)
        if ball.centerx < 0:
            ball.x = 1
        if ball.centerx > 2031:
            ball.right = 2030

        pygame.draw.rect(screen, playercol, player)
        pygame.draw.ellipse(screen, "white", ball)
        pygame.draw.rect(screen, enemycol, opponent)
        pygame.draw.rect(screen, "white", (0, 1010, 1700, 10))
        screen.blit(player_scene, player_scene_rect)
        screen.blit(a_i_scene, a_i_rect)
        screen.blit(my_score, my_score_rect)
        screen.blit(ene_score, ene_score_rect)
    else:
        screen.fill((70, 0, 0))
        screen.blit(main_sc, (150, 1000))
        screen.blit(main2, (300, 500))

    clock.tick(60)
    pygame.display.update()
