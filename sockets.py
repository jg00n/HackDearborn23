import pygame
import sys

pygame.init()

# Set up the screen
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hydrogen Fuel Cell Simulator')

# Set up the colors
GREEN = (34, 139, 34)
GREY = (169, 169, 169)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the car object
car_width = 50
car_height = 80
car = pygame.Surface((car_width, car_height))
car.fill(RED)
car_rect = car.get_rect(center=(screen_width//2, screen_height//2))

# Set up the movement controls
car_speed = 3
move_left = False
move_right = False
move_up = False
move_down = False

# Set up the road path
road_path = []

# Set up the game state
game_state = "game"

# Set up the settings state
settings_state = "speed"
settings_speed = 3

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game_state == "game":
                if event.key == pygame.K_a:
                    move_left = True
                elif event.key == pygame.K_d:
                    move_right = True
                elif event.key == pygame.K_w:
                    move_up = True
                elif event.key == pygame.K_s:
                    move_down = True
                elif event.key == pygame.K_ESCAPE:
                    game_state = "settings"
            elif game_state == "settings":
                if settings_state == "speed":
                    if event.key == pygame.K_UP:
                        settings_speed += 1
                    elif event.key == pygame.K_DOWN:
                        settings_speed -= 1
                    elif event.key == pygame.K_RETURN:
                        car_speed = settings_speed
                        settings_state = "back"
                elif settings_state == "back":
                    if event.key == pygame.K_RETURN:
                        game_state = "game"

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_d:
                move_right = False
            elif event.key == pygame.K_w:
                move_up = False
            elif event.key == pygame.K_s:
                move_down = False

    # Move the car
    if move_left and car_rect.left > 0:
        car_rect.x -= car_speed
    elif move_right and car_rect.right < screen_width:
        car_rect.x += car_speed
    if move_up and car_rect.top > 0:
        car_rect.y -= car_speed
    elif move_down and car_rect.bottom < screen_height:
        car_rect.y += car_speed

    # Update the road path
    prev_position = (car_rect.x + car_width/2, car_rect.y + car_height/2)
    road_path.append(prev_position)
    current_position = (car_rect.x + car_width/2, car_rect.y + car_height/2)

    # Draw the screen
    screen.fill(GREEN)

    # Draw the road
    road_rect = pygame.Rect(screen_width/4, 0, screen_width/2, screen_height)
    pygame.draw.rect(screen, GREY, road_rect)
    line_rect = pygame.Rect(screen_width/2 - 2.5, 0, 5, 25)
    for i in range(0, screen_height, 50):
        line_rect.top = i
        pygame.draw.rect(screen, WHITE, line_rect)

    # Draw the car
    screen.blit(car, car_rect)

    # Draw the settings menu
    if game_state == "settings":
        # Draw the background rectangle
        settings_rect = pygame.Rect(screen_width/4, screen_height/4, screen_width/2, screen_height/2)
        pygame.draw.rect(screen, GREY, settings_rect)

        # Draw the settings text
        font = pygame.font.SysFont(None, 48)
        if settings_state == "speed":
            text = font.render("Car Speed: " + str(settings_speed), True, BLACK)
        elif settings_state == "back":
            text = font.render("Press Enter to Go Back", True, BLACK)
        screen.blit(text, ((screen_width/2 - text.get_width()/2), (screen_height/2 - text.get_height()/2)))

    pygame.display.update()

# Limit the frame rate
    clock = pygame.time.Clock()
    clock.tick(60)

