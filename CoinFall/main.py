import pygame
import random
pygame.init() #Use Pygame
pygame.display.set_caption("CoinFall")
clock = pygame.time.Clock()

#Constants
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
SKY = (70, 150, 200)
SPEED = 15
BALL_SPEED = 7
FPS = 60


score = 0
fonts = pygame.font.SysFont("roboto", 50)
hp = 3

#Screen Settings
SCREEN_W = 1200
SCREEN_H = 675
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
screen_rect = screen.get_rect()


#Graphics Settings
player = pygame.image.load("Assets/Platform.png")
player = pygame.transform.scale(player, (200, 200))  
player_rect = player.get_rect()
player_rect.center = (SCREEN_W // 2, SCREEN_H // 2 + 250)
player_hitbox = pygame.Rect(0,0,195,60)


object1 = pygame.image.load("Assets/Gold_Coin.png")
object1 = pygame.transform.scale(object1, (150,150))
object1_rect = object1.get_rect()
object1_rect.y = 0
object1_rect.x = random.randint(object1_rect.width, SCREEN_W - object1_rect.width)
object1_hitbox = pygame.Rect(0,0,100,100)

full_heart = pygame.image.load("Assets/Full_Heart.png")
full_heart = pygame.transform.scale(full_heart, (150,150))
full_heart_rect = full_heart.get_rect()

empty_heart = pygame.image.load("Assets/Empty_Heart.png")
empty_heart = pygame.transform.scale(empty_heart, (150,150))
empty_heart_rect = empty_heart.get_rect()


#Screen Display
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Quit Detector
            running = False

    #Keyboard Controls       
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player_rect.left > 0:
        player_rect.centerx -= SPEED

    if keys[pygame.K_d] and player_rect.right < SCREEN_W:
        player_rect.centerx += SPEED

    #Collision Detector
    if player_hitbox.colliderect(object1_hitbox):
        object1_rect.x = random.randint(object1_rect.width, SCREEN_W - object1_rect.width)
        object1_rect.y = 0
        score +=1
    
    if object1_rect.top >= SCREEN_H:
        object1_rect.y = 0
        object1_rect.x = random.randint(object1_rect.width, SCREEN_W - object1_rect.width)
        hp -= 1

    #Ball Falling
    object1_rect.y += BALL_SPEED

    #Hitbox Position
    object1_hitbox.center = object1_rect.center
    player_hitbox.center = (player_rect.centerx, player_rect.centery - 5)

    #Score Update
    message = fonts.render(f"Score: {score}", True, BLACK)

    #Game Over
    if hp == 0:
        running = False

    #Graphics Render
    screen.fill(SKY)
    screen.blit(player, player_rect)
    screen.blit(object1, object1_rect)
    screen.blit(message, (0,0))

    for i in range(3):
        x = SCREEN_W - 120 * (i + 1)
        y = 0

        if i < hp:
            screen.blit(full_heart, (x, y))
        else:
            screen.blit(empty_heart, (x, y))
    
    #Debug Hitbox
    # pygame.draw.rect(screen, GREEN, player_hitbox, 4)
    # pygame.draw.rect(screen, GREEN, object1_hitbox, 4)

    #Display
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
