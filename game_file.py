import pygame
import character
import maze
import resource

pygame.init()

game_maze = maze.Maze(25,25,15,1)
display_width = game_maze.get_display_width()
display_height = game_maze.get_display_length()
tile_size = game_maze.get_tile_size()
map_grid = game_maze.gridit()
map_obstacles = game_maze.map_obstacles()

GRASS = pygame.image.load(r'./assets/grass.png')
GRASS = pygame.transform.scale(GRASS, (tile_size, tile_size))
GLASS = pygame.image.load(r'./assets/glass.png')
GLASS = pygame.transform.scale(GLASS, (tile_size, tile_size))
FIRE = pygame.image.load(r'./assets/fire.png')
FIRE = pygame.transform.scale(FIRE, (tile_size, tile_size))
BLACK = (0,0,0)
WHITE = (255,255,255)

resource_maze = resource.Resource("Glass",GLASS,10,True);
resource_location = resource_maze.random_resource_spread(game_maze)

agent = character.Character()
agent.transform_avatar(tile_size)
car = agent.get_avatar()
car_length,car_width = agent.get_avatar_dim()
crashed = agent.get_state()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('reinforeced game')


clock = pygame.time.Clock()

def draw_rectangles(point, texture):
    x,y = point
    gameDisplay.blit(texture, (x,y))

def show_car(x,y):
    gameDisplay.blit(car, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.58)
x_change = 0
y_change = 0
car_speed = 0


while not agent.get_state():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            agent.set_state(True)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -1
            elif event.key == pygame.K_RIGHT:
                x_change = 1
            elif event.key == pygame.K_UP:
                y_change = -1
            elif event.key == pygame.K_DOWN:
                y_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 0

    x += x_change
    y += y_change

    gameDisplay.fill(WHITE)

    for grid_point in map_grid:
        draw_rectangles(grid_point,GRASS)

    for obstacle in map_obstacles:
        draw_rectangles(obstacle,FIRE)

    for resource in resource_location:
        draw_rectangles(resource,GLASS)

    show_car(x,y)

    currentPosition = (x,y)
    car_dim = agent.get_avatar_dim()

    # Adding points to the object if it gets the resource
    if resource_maze.overlaps(game_maze,currentPosition,(car_length,car_width)):
        agent.reward()
        resource_location = resource_maze.random_resource_spread(game_maze)

    # Closing the game for now but in the future this would be used to penalize the agent instead
    if game_maze.overlaps(map_obstacles,currentPosition,(car_length,car_width)):
        agent.set_state(True)
    elif x > display_width - car_width or x < 0 or y < 0 or y > display_height - car_length:
        agent.set_state(True)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
