# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen Dimensions
# WIDTH = 800
# HEIGHT = 600

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)

# # Car settings
# CAR_WIDTH = 50
# CAR_HEIGHT = 80

# # Create the screen object
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Car Game")

# # Car class
# class Car:
#     def _init_(self):
#         self.x = WIDTH // 2 - CAR_WIDTH // 2
#         self.y = HEIGHT - CAR_HEIGHT - 10
#         self.speed = 5

#     def move(self, keys):
#         if keys[pygame.K_LEFT] and self.x > 0:
#             self.x -= self.speed
#         if keys[pygame.K_RIGHT] and self.x < WIDTH - CAR_WIDTH:
#             self.x += self.speed

#     def draw(self):
#         pygame.draw.rect(screen, BLUE, (self.x, self.y, CAR_WIDTH, CAR_HEIGHT))

# # Obstacle class
# class Obstacle:
#     def _init_(self):
#         self.x = random.randint(0, WIDTH - CAR_WIDTH)
#         self.y = -CAR_HEIGHT
#         self.speed = random.randint(5, 10)

#     def move(self):
#         self.y += self.speed

#     def draw(self):
#         pygame.draw.rect(screen, RED, (self.x, self.y, CAR_WIDTH, CAR_HEIGHT))

# # Game Loop
# def game_loop():
#     car = Car()
#     obstacles = []
#     score = 0
#     clock = pygame.time.Clock()

#     run_game = True
#     while run_game:
#         screen.fill(WHITE)
#         pygame.display.update()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run_game = False

#         keys = pygame.key.get_pressed()
#         car.move(keys)
#         car.draw()

#         # Generate obstacles
#         if random.randint(1, 30) == 1:  # Adjust frequency of obstacles
#             obstacles.append(Obstacle())

#         # Move and draw obstacles
#         for obstacle in obstacles:
#             obstacle.move()
#             obstacle.draw()
#             if obstacle.y > HEIGHT:
#                 obstacles.remove(obstacle)
#                 score += 1  # Increase score when obstacle passes

#             # Check collision
#             if car.x < obstacle.x + CAR_WIDTH and car.x + CAR_WIDTH > obstacle.x and \
#                car.y < obstacle.y + CAR_HEIGHT and car.y + CAR_HEIGHT > obstacle.y:
#                 print(f"Game Over! Final Score: {score}")
#                 run_game = False

#         # Display score
#         font = pygame.font.SysFont(None, 30)
#         score_text = font.render(f"Score: {score}", True, BLACK)
#         screen.blit(score_text, (10, 10))

#         pygame.display.update()

#         # Set FPS
#         clock.tick(60)

#     pygame.quit()

# # Start the game loop
# if __name__ == "_main_":
#     game_loop()

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Car settings
CAR_WIDTH = 50
CAR_HEIGHT = 80

# Create the screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Car class
class Car:
    def __init__(self):  # Corrected the constructor method
        self.x = WIDTH // 2 - CAR_WIDTH // 2
        self.y = HEIGHT - CAR_HEIGHT - 10
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - CAR_WIDTH:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, CAR_WIDTH, CAR_HEIGHT))

# Obstacle class
class Obstacle:
    def __init__(self):  # Corrected the constructor method
        self.x = random.randint(0, WIDTH - CAR_WIDTH)
        self.y = -CAR_HEIGHT
        self.speed = random.randint(5, 10)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, CAR_WIDTH, CAR_HEIGHT))

# Game Loop
def game_loop():
    car = Car()
    obstacles = []
    score = 0
    clock = pygame.time.Clock()

    run_game = True
    while run_game:
        screen.fill(WHITE)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        keys = pygame.key.get_pressed()
        car.move(keys)
        car.draw()

        # Generate obstacles
        if random.randint(1, 30) == 1:  # Adjust frequency of obstacles
            obstacles.append(Obstacle())

        # Move and draw obstacles
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw()
            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)
                score += 1  # Increase score when obstacle passes

            # Check collision
            if car.x < obstacle.x + CAR_WIDTH and car.x + CAR_WIDTH > obstacle.x and \
               car.y < obstacle.y + CAR_HEIGHT and car.y + CAR_HEIGHT > obstacle.y:
                print(f"Game Over! Final Score: {score}")
                run_game = False

        # Display score
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        # Set FPS
        clock.tick(60)

    pygame.quit()

# Start the game loop
if __name__ == "__main__":  # Corrected the if condition
    game_loop()
