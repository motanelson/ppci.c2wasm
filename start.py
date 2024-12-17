import pygame
import math
import random
# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boneco Anatômico 3D Simulado")

# Cores
BLACK = (0, 0, 0)
WHITE =(255,255,255)
nstars=120
xxx=[]
yyy=[]
for nn in range(nstars):
    xxx=xxx+[random.randint(0, screen_width-1)]
    yyy=yyy+[random.randint(0, screen_height-1)]
    
# Carregar a imagem do boneco anatômico
boneco_image = pygame.image.load("boneco.png").convert_alpha()  # Substitua pelo caminho da sua imagem
boneco_original_width = boneco_image.get_width()
boneco_original_height = boneco_image.get_height()

# Posição inicial do boneco
x = 0
z = 10  # Controle da "profundidade"
z_min = 5
z_max = 50
scale_factor = 10

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar entrada do teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        z = max(z_min, z - 1)
    if keys[pygame.K_DOWN]:
        z = min(z_max, z + 1)

    # Calcular parâmetros com base em z
    scale = 1 / z * scale_factor
    scaled_width = int(boneco_original_width * scale)
    scaled_height = int(boneco_original_height * scale)
    center_x = screen_width // 2 + int(x * scale * 20)
    center_y = screen_height // 2 + int(z * scale * 10)

    # Redimensionar a imagem do boneco
    boneco_scaled = pygame.transform.scale(boneco_image, (scaled_width, scaled_height))

    # Limpar tela
    screen.fill(BLACK)
    for nn in range(nstars):
        pygame.draw.line(screen,WHITE,(xxx[nn],yyy[nn]),(xxx[nn]+1,yyy[nn]),1)
    # Desenhar o boneco
    boneco_rect = boneco_scaled.get_rect(center=(center_x, center_y))
    screen.blit(boneco_scaled, boneco_rect)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    clock.tick(60)

# Sair do Pygame
pygame.quit()
