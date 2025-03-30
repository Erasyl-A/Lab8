import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROAD_COLOR = (50, 50, 50)
COIN_COLOR = (255, 223, 0)

font = pygame.font.SysFont(None, 36)

player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 100, 50, 80) 
player_speed = 5

coins = []
coin_spawn_delay = 60 
frame_count = 0
coin_radius = 10
collected_coins = 0

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60) 
    screen.fill(ROAD_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 200:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH - 200:
        player.x += player_speed

    frame_count += 1
    if frame_count >= coin_spawn_delay:
        coin_x = random.randint(220, WIDTH - 220)
        coin_y = -20
        coins.append(pygame.Rect(coin_x, coin_y, coin_radius * 2, coin_radius * 2))
        frame_count = 0

    for coin in coins[:]:
        coin.y += 5  
        if coin.colliderect(player):
            coins.remove(coin)
            collected_coins += 1
        elif coin.y > HEIGHT:
            coins.remove(coin)

    pygame.draw.rect(screen, WHITE, player)

    for coin in coins:
        pygame.draw.circle(screen, COIN_COLOR, coin.center, coin_radius)

    text = font.render(f"Coins: {collected_coins}", True, WHITE)
    screen.blit(text, (WIDTH - 150, 20))

    pygame.display.flip()

pygame.quit()
