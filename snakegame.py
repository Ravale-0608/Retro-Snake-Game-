import pygame
import random

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
snake_x_axis = 400
snake_y_axis = 400
right_key = False
x_velocity = 1
y_velocity = 0
food_width = 10
food_x = random.randint(0, screen_width - food_width)
food_y = random.randint(0, screen_height - food_width)
food = pygame.image.load('mushroom2.png')
snake = pygame.draw.rect(screen, (255, 0, 0), (snake_x_axis, snake_y_axis, 10, 10))

clock = pygame.time.Clock()

def draw_food(food_x, food_y):
    screen.blit(food, (food_x, food_y))

def movement(snake_x_axis, snake_y_axis, food_x, food_y):
    screen.fill((0, 0, 0))
    draw_food(food_x, food_y)
    snake = pygame.draw.rect(screen, (255, 0, 0), (snake_x_axis, snake_y_axis, 10, 10))
    pygame.display.update()

def get_move(event, x_velocity,y_velocity):
    if event.key == pygame.K_LEFT:
        #To make sure the snake does not move left if moving right 
        if y_velocity != 0 and x_velocity != 1:
            y_velocity = 0
            x_velocity = -1
    elif event.key == pygame.K_DOWN:
        #To make sure the snake does not move up if moving down 
        if y_velocity != -1 and x_velocity != 0:
            y_velocity = 1
            x_velocity = 0
    elif event.key == pygame.K_RIGHT:
        #To make sure the snake does not move left if moving right 
        if y_velocity != 0 and x_velocity != -1:
            y_velocity = 0
            x_velocity = 1
    elif event.key == pygame.K_UP:
        #To make sure the snake does not move down if moving up 
        if y_velocity != 1 and x_velocity != 0:
            y_velocity = -1
            x_velocity = 0
            
    return (x_velocity,y_velocity)
    
    
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            x_velocity, y_velocity = get_move(event, x_velocity, y_velocity)

    snake_x_axis = snake_x_axis + x_velocity
    snake_y_axis = snake_y_axis + y_velocity

    # Check for collision with screen boundaries
    if (snake_x_axis < 0 or snake_x_axis >= screen_width or
        snake_y_axis < 0 or snake_y_axis >= screen_height):
        run = False  # End the game

    # Check for collision between snake and food
    if (snake_x_axis < food_x + food_width and
        snake_x_axis + 10 > food_x and
        snake_y_axis < food_y + food_width and
        snake_y_axis + 10 > food_y):
        food_x = random.randint(0, screen_width - food_width)
        food_y = random.randint(0, screen_height - food_width)
        snake = pygame.draw.rect(screen, (255, 0, 0), (snake_x_axis, snake_y_axis, 10+10, 10))


    movement(snake_x_axis, snake_y_axis, food_x, food_y)
    clock.tick(150)

# Display "Game Over" when the game ends
font = pygame.font.Font(None, 36)
text = font.render("Game Over", True, (255, 0, 0))
screen.blit(text, (screen_width // 2 - 80, screen_height // 2 - 18))
pygame.display.update()

# Wait for a moment and then quit the game
pygame.time.delay(2000)
pygame.quit()