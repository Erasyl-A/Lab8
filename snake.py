import pygame
import random

pygame.init()

CELL_SIZE = 20
WIDTH, HEIGHT = 600, 400
COLUMNS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (100, 100, 100)

font = pygame.font.SysFont(None, 32)

snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0) 
new_direction = direction

walls = [(10, 10), (10, 11), (10, 12), (15, 15), (16, 15), (17, 15)]

def generate_food():
    while True:
        pos = (random.randint(0, COLUMNS - 1), random.randint(0, ROWS - 1))
        if pos not in snake and pos not in walls:
            return pos

food = generate_food()

score = 0
level = 1
speed = 10

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        new_direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        new_direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        new_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        new_direction = (1, 0)

    direction = new_direction

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if (head[0] < 0 or head[0] >= COLUMNS or
        head[1] < 0 or head[1] >= ROWS or
        head in snake or
        head in walls):
        print("Game Over")
        running = False

    snake.insert(0, head)

    if head == food:
        score += 1
        food = generate_food()
       
        if score % 4 == 0:
            level += 1
            speed += 2  
    else:
        snake.pop()  

    screen.fill(BLACK)

    for wall in walls:
        pygame.draw.rect(screen, GRAY, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0] * CELL_SIZE, part[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    score_text = font.render(f"Score: {score}   Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
