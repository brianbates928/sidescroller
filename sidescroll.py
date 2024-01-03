import pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60
SPEED = 5

# Define the Player object
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.vel = pygame.Vector2(0, 0)

    def update(self):
        self.vel.x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel.x = -5
        if keys[pygame.K_RIGHT]:
            self.vel.x = 5
        self.rect.move_ip(self.vel)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create a sprite group and add the Player
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Create a background
background = pygame.image.load('background.jpg')
background_rect = background.get_rect()

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Scroll the background
    if player.vel.x < 0:  # moving left
        background_rect.x += SPEED
    elif player.vel.x > 0:  # moving right
        background_rect.x -= SPEED

    # Wrap the background
    if background_rect.right < WIDTH:
        background_rect.x = 0
    elif background_rect.left > 0:
        background_rect.x = -background_rect.width + WIDTH

    # Draw
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
