import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW= (255, 255, 0)

screen.fill(WHITE)
clock = pygame.time.Clock()
LMBpressed = False
tool = "brush"  
color = BLACK
thickness = 5
start_pos = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            start_pos = event.pos
            if tool in ["rect", "circle"]:
                temp_surface = screen.copy()  

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            end_pos = event.pos

            if tool == "rect":
                x1, y1 = start_pos
                x2, y2 = end_pos
                width = x2 - x1
                height = y2 - y1
                pygame.draw.rect(screen, color, (x1, y1, width, height), thickness)

            elif tool == "circle":
                center = start_pos
                radius = int(((end_pos[0] - center[0]) ** 2 + (end_pos[1] - center[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, color, center, radius, thickness)

        if event.type == pygame.MOUSEMOTION and LMBpressed:
            if tool == "brush":
                pygame.draw.circle(screen, color, event.pos, thickness)
            elif tool == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, thickness)
            elif tool in ["rect", "circle"]:
                screen.blit(temp_surface, (0, 0))
                curr_pos = event.pos
                if tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = curr_pos
                    pygame.draw.rect(screen, color, (x1, y1, x2 - x1, y2 - y1), thickness)
                elif tool == "circle":
                    radius = int(((curr_pos[0] - start_pos[0]) ** 2 + (curr_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, radius, thickness)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_e:
                tool = "eraser"
            if event.key == pygame.K_d:
                tool = "brush"

            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                thickness += 1
            if event.key == pygame.K_MINUS:
                thickness = max(1, thickness - 1)

            if event.key == pygame.K_1:
                color = RED
            if event.key == pygame.K_2:
                color = BLUE
            if event.key == pygame.K_3:
                color = GREEN
            if event.key == pygame.K_4:
                color = BLACK
            if event.key == pygame.K_5:
                color = YELLOW

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
