import pygame, sys
import random

# Iniciar
pygame.init()

# Pantalla
width, height = 700, 775
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego hecho por Juan José Echavarria")

# Cargar imagenes
player_image = pygame.image.load("jose.png")
player_image = pygame.transform.scale(player_image, (60, 60))

bullet_image = pygame.image.load("bala.png")
bullet_image = pygame.transform.scale(bullet_image, (50, 50))

enemy_image = pygame.image.load("cris.png")
enemy_image = pygame.transform.scale(enemy_image, (60, 60))

background_image = pygame.image.load("fondo.png")
background_image = pygame.transform.scale(background_image, 
                                            (width, height))

# Jugador
player_rect = player_image.get_rect()
player_rect.topleft = (width // 2 - player_rect.width // 2,
                        height - player_rect.height - 10)
player_speed = 15

# Bala
bullet_rect = bullet_image.get_rect()
bullet_speed = 10
bullets = []

# Enemigo
enemy_rect = enemy_image.get_rect()
enemy_speed = 5
enemies = []

# reloj
clock = pygame.time.Clock()

# Mantener registro
keys_pressed = {'left': False, 'right': False}

# Bucle juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Movimientos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys_pressed['left'] = True
            elif event.key == pygame.K_RIGHT:
                keys_pressed['right'] = True
            elif event.key == pygame.K_SPACE:
                bullet_rect = bullet_image.get_rect()  # Fixed: Should be assignment, not comparison
                bullet = {
                    'rect' : pygame.Rect(
                        player_rect.x +
                        player_rect.width // 2 -
                        bullet_rect.width // 2,
                        player_rect.y,
                        bullet_rect.width,
                        bullet_rect.height
                    ),
                    'image' : bullet_image
                }
                bullets.append(bullet)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys_pressed['left'] = False
            elif event.key == pygame.K_RIGHT:
                keys_pressed['right'] = False  # Fixed typo: Changed event.kry to event.key

    # Actualizar posición
    if keys_pressed['left'] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys_pressed['right'] and player_rect.right < width:  # Fixed: Should be player_rect.right < width
        player_rect.x += player_speed

    # Actualizar balas
    for bullet in bullets:
        bullet['rect'].y -= bullet_speed

    # Generar enemigos
    if random.randint(0, 100) < 5:
        enemy_rect = enemy_image.get_rect()
        enemy_rect.x = random.randint(0, width - enemy_rect.width)
        enemies.append(enemy_rect.copy())

    # Actualizar enemigos
    for enemy in enemies:
        enemy.y += enemy_speed  # Fixed: Should be enemy_rect.y

    # Colisiones
    for bullet in bullets:
        for enemy in enemies:
            if enemy.colliderect(bullet['rect']):  # Fixed: Changed colliderec to colliderect
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Coli jugador enemigo
    for enemy in enemies:
        if player_rect.colliderect(enemy):  # Fixed: Changed colliderec to colliderect
            pygame.quit()
            sys.exit()

    # Limpiar pantalla
    screen.blit(background_image, (0, 0))

    # Dibujo jugador
    screen.blit(player_image, player_rect)

    # Dibujar balas
    for bullet in bullets:
        screen.blit(bullet['image'], bullet['rect'].topleft)

    # Dibujar enemigos
    for enemy in enemies:
        screen.blit(enemy_image, enemy)  # Fixed: Changed enemy_rect to enemy

    # Actualizar pantalla
    pygame.display.flip()

    # FPS
    clock.tick(30)  # Fixed: Changed clock,tick(30) to clock.tick(30)