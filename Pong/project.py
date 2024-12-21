# Proses Import
import pygame
from ball import Ball
from paddle import Paddle

pygame.init()

# Warna Game
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Tampilan Game
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")
 
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1.rect.y = 200
 
paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 670
paddle2.rect.y = 200
 
ball = Ball(WHITE, 10,10)
ball.rect.x = 345
ball.rect.y = 195
 

all_sprites_list = pygame.sprite.Group()
 
# Menambahkan paddle dan bola ke daftar objek
all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)
all_sprites_list.add(ball)

carryOn = True
clock = pygame.time.Clock()
 
# Score
scoreA = 0
scoreB = 0
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     carryOn=False
 
    # Kontrol Player A (w/s) dan Player B (up/down) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.moveUp(6)
    if keys[pygame.K_s]:
        paddle1.moveDown(6)
    if keys[pygame.K_UP]:
        paddle2.moveUp(6)
    if keys[pygame.K_DOWN]:
        paddle2.moveDown(6)    
 
    # Logika Game
    all_sprites_list.update()
    
    # Penambahan skor jika bola mantul ke salah satu dinding
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]    

    # Deteksi tabrakan antara paddle dan bola
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
      ball.bounce()
    

    # Warna Layar 
    screen.fill(BLACK)
    # Garis tengah
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen) 
 
    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
