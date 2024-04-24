# importy
import random
import pygame

# Inicializace
pygame.init()

# Screen
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chytáme mozkomora")

# Hodnoty hry
mozkomor_start_speed = 2
mozkomor_speed_acceleration = 0.5
score = 0
player_start_lives = 5

player_lives = player_start_lives
mozkomor_speed = mozkomor_start_speed
mozkomor_speed_2 = mozkomor_start_speed

# Obrázky
back_qround_image = pygame.image.load("img/hogwarts-castle.jpg")
back_qround_image_rect = back_qround_image.get_rect()
back_qround_image_rect.topleft = (0, 0)
back_qround_image_rect.bottomright = (width, height)

mozkomor_image = pygame.image.load("img/mozkomor.png")
mozkomor_image_rect = mozkomor_image.get_rect()
mozkomor_image_rect.center = (width//3, height//2)

mozkomor_image_2 = pygame.image.load("img/mozkomor.png")
mozkomor_image_rect_2 = mozkomor_image_2.get_rect()
mozkomor_image_rect_2.center = (width//1.5, height//2)

# Barvy
dark_yellow = pygame.Color("#938f0c")

# Fonty
game_font_big = pygame.font.Font("fonts/Harry.ttf", 50)
game_font_small = pygame.font.Font("fonts/Harry.ttf", 35)

# Texty
score_text = game_font_small.render(f"Score: {score}", True, dark_yellow)
score_text_rect = score_text.get_rect()
score_text_rect.top = 15
score_text_rect.right = width - 20

lives_text = game_font_small.render(f"Lives: {player_lives}", True, dark_yellow)
lives_text_center = lives_text.get_rect()
lives_text_center.top = 50
lives_text_center.right = width - 20

game_over_text = game_font_big.render("Game over!", True, dark_yellow, "black")
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (width//2, height//2)

continue_text = game_font_small.render("Click anywhere on the screen for continue.", True, dark_yellow, "black")
continue_text_rect = continue_text.get_rect()
continue_text_rect.top = height//2 + 30
continue_text_rect.centerx = width//2

mozkomor_x = random.choice([-1, 1])
mozkomor_y = random.choice([-1, 1])

mozkomor_2_x = random.choice([-1, 1])
mozkomor_2_y = random.choice([-1, 1])

# fps a clock
fps = 60
clock = pygame.time.Clock()

# music and sounds
pygame.mixer.music.load("media/bg-music-hp.wav")
pygame.mixer.music.play()

miss_sound = pygame.mixer.Sound("media/miss_click.wav")
miss_sound.set_volume(0.1)

success_click = pygame.mixer.Sound("media/success_click.wav")
success_click.set_volume(0.1)

# cyklus while pro hru
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]
            if mozkomor_image_rect.collidepoint(click_x, click_y):
                score += 1
                mozkomor_speed += mozkomor_speed_acceleration
                success_click.play()

                previous_x = mozkomor_x
                previous_y = mozkomor_y
                while previous_x == mozkomor_x and previous_y == mozkomor_y:
                    mozkomor_x = random.choice([-1, 1])
                    mozkomor_y = random.choice([-1, 1])

            elif mozkomor_image_rect_2.collidepoint(click_x, click_y):
                score += 1
                mozkomor_speed_2 += mozkomor_speed_acceleration
                success_click.play()

                previous_x = mozkomor_2_x
                previous_y = mozkomor_2_y
                while previous_x == mozkomor_2_x and previous_y == mozkomor_2_y:
                    mozkomor_2_x = random.choice([-1, 1])
                    mozkomor_2_y = random.choice([-1, 1])

            else:
                player_lives -= 1
                miss_sound.play()

    # Směr mozkomora
    mozkomor_image_rect.x += mozkomor_x * mozkomor_speed
    mozkomor_image_rect.y += mozkomor_y * mozkomor_speed

    if mozkomor_image_rect.left < 0 or mozkomor_image_rect.right > width:
        mozkomor_x = -1 * mozkomor_x
    if mozkomor_image_rect.top < 0 or mozkomor_image_rect.bottom > height:
        mozkomor_y = -1 * mozkomor_y

    # Směr mozkomora 2
    mozkomor_image_rect_2.x += mozkomor_2_x * mozkomor_speed_2
    mozkomor_image_rect_2.y += mozkomor_2_y * mozkomor_speed_2

    if mozkomor_image_rect_2.left < 0 or mozkomor_image_rect_2.right > width:
        mozkomor_2_x = -1 * mozkomor_2_x
    if mozkomor_image_rect_2.top < 0 or mozkomor_image_rect_2.bottom > height:
        mozkomor_2_y = -1 * mozkomor_2_y

    # Update lives & score
    score_text = game_font_small.render(f"Score: {score}", True, dark_yellow)
    lives_text = game_font_small.render(f"Lives: {player_lives}", True, dark_yellow)

    # Blit obrázků
    screen.blit(back_qround_image, back_qround_image_rect)
    screen.blit(mozkomor_image, mozkomor_image_rect)
    screen.blit(mozkomor_image_2, mozkomor_image_rect_2)

    # Text blit
    screen.blit(score_text, score_text_rect)
    screen.blit(lives_text, lives_text_center)

    # Update obrazovky
    pygame.display.update()

    # fps
    clock.tick(fps)

    if player_lives == 0:
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(continue_text, continue_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        cykle = True
        while cykle:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player_lives = player_start_lives
                    score = 0
                    mozkomor_speed = mozkomor_start_speed
                    mozkomor_speed_2 = mozkomor_start_speed
                    mozkomor_image_rect.center = (width//3, height//2)
                    mozkomor_x = random.choice([-1, 1])
                    mozkomor_y = random.choice([-1, 1])
                    mozkomor_image_rect_2.center = (width//1.5, height//2)
                    mozkomor_2_x = random.choice([-1, 1])
                    mozkomor_2_y = random.choice([-1, 1])
                    pygame.mixer.music.play()
                    cykle = False
                elif event.type == pygame.QUIT:
                    lets_continue = False
                    cykle = False

# Konec hry
pygame.quit()
