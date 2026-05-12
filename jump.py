import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
tile_size = 64
level = [
    "........................",
    "........................",
    ".............###........",
    "......###...............",
    ".....................#.........................#",
    "################################################",
]

player_x, player_y = 100, 250
camera_x = 0

velocity_y = 0
gravity = 0.5
jump_power = -10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

        if keys[pygame.K_UP] and player_y >= 250:
            velocity_y = jump_power

        velocity_y += gravity
        player_y += velocity_y

        if player_y >= 250:
            player_y = 250
            velocity_y = 0
            is_jump = False

    camera_x = player_x - 300
    camera_x = max(0, camera_x)


    screen.fill((200, 230, 255))

    for row_index, row in enumerate(level):
        for col_index, cell in enumerate(row):
            if cell == "#":
                world_x = col_index * tile_size
                world_y = row_index * tile_size
                screen_x = world_x - camera_x
                pygame.draw.rect(
                    screen,
                    (80, 80, 80),
                    (screen_x, world_y, tile_size, tile_size),
                )

    pygame.draw.rect(screen, (0, 120, 255), (player_x - camera_x, player_y, 50, 60))

    pygame.display.update()
    clock.tick(60)

pygame.quit()