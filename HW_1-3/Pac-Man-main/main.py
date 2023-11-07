import pygame
import sys

# Game settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
PACMAN_SIZE = 50
DOT_SIZE = 20
DOT_COLOR = (255, 255, 255)  # White
PACMAN_COLOR = (255, 255, 0)  # Yellow
BG_COLOR = (0, 0, 0)  # Black
TILE_SIZE = 100
WIDTH = TILE_SIZE * 8
HEIGHT = TILE_SIZE * 8
TILE_COLOR = (0, 0, 255)



# Initialize the game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Player
pacman = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PACMAN_SIZE, PACMAN_SIZE)

# Dots
dots = [pygame.Rect(x, y, DOT_SIZE, DOT_SIZE) for x in range(50, SCREEN_WIDTH, 100) for y in range(50, SCREEN_HEIGHT, 100)]

#tile = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

# Maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

def playerMovement(key):
    if key[pygame.K_LEFT]:
        pacman.move_ip(-5, 0)
    if key[pygame.K_RIGHT]:
        pacman.move_ip(5, 0)
    if key[pygame.K_UP]:
        pacman.move_ip(0, -5)
    if key[pygame.K_DOWN]:
        pacman.move_ip(0, 5)

    # Keep the player inside the screen
    pacman.clamp_ip(screen.get_rect())

def eatDots():
    # Eat dots
    for dot in dots[:]:
        if pacman.colliderect(dot):
            dots.remove(dot)
def drawings():
    # Drawing
    screen.fill(BG_COLOR)
    for dot in dots:
        pygame.draw.ellipse(screen, DOT_COLOR, dot)
    pygame.draw.ellipse(screen, PACMAN_COLOR, pacman)

    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile_type = maze[row][column]

            if tile_type == 1:
                pygame.draw.rect(screen, TILE_COLOR, pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))

def startGame():
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        
        playerMovement(keys)

        eatDots()

        drawings()

        # Collision
        # pacman.colliderect(tile)

        # Refresh the display
        pygame.display.flip()

        # Cap at 60 FPS
        clock.tick(60)

startGame()