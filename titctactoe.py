import pygame
import sys
GAME_WIDTH = 600
GAME_HEIGHT = 800
LINE_WIDTH = 5
c11 = None
c12 = None
c13 = None
c21 = None
c22 = None
c23 = None
c31 = None
c32 = None
c33 = None
turn = "X"

class imagine():
    def __init__(self,image, size = None):
        image = pygame.image.load(image)
        if size:
            image = pygame.transform.scale(image,size)
        self.image = image

imagineax = imagine("W:/vscode/proiecte personale/x.jpg", (60,60))
imaginea0 = imagine("W:/vscode/proiecte personale/red-number-zero.jpg",(60,60))

color = (137, 199, 194)
line_color = (0, 0, 0)
pygame.display.set_caption("TICTACTOE")
pygame.init()

screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

def castigat():
    if c11 == c12 == c13 and c11 is not None:
        print(f"{c11} a castigat")
        pygame.quit()
        sys.exit()
    if c11 == c21 == c31 and c11 is not None:
        print(f"{c11} a castigat")
        pygame.quit()
        sys.exit()
    if c31 == c32 == c33 and c31 is not None:
        print(f"{c31} a castigat")
        pygame.quit()
        sys.exit()
    if c13 == c23 == c33 and c13 is not None:
        print(f"{c13} a castigat")
        pygame.quit()
        sys.exit()
    if c12 == c22 == c32 and c12 is not None:
        print(f"{c12} a castigat")
        pygame.quit()
        sys.exit()
    if c11 == c22 == c33 and c11 is not None:
        print(f"{c11} a castigat")
        pygame.quit()
        sys.exit()
    if c31 == c22 == c13 and c31 is not None:
        print(f"{c31} a castigat")
        pygame.quit()
        sys.exit()
    if c21 == c22 == c23 and c21 is not None:
        print(f"{c21} a castigat")
        pygame.quit()
        sys.exit()
    if not None in [c11, c12, c13, c21, c22, c23, c31, c32, c33]:
        print("Remiza")
        pygame.quit()
        sys.exit()
    
def linii():
    # linii verticale
    pygame.draw.rect(screen, line_color, (GAME_WIDTH/3, 0, LINE_WIDTH, GAME_HEIGHT))
    pygame.draw.rect(screen, line_color, ((GAME_WIDTH/3) * 2, 0,LINE_WIDTH, GAME_HEIGHT))

    #linii orizontale
    pygame.draw.rect(screen,line_color, (0, GAME_HEIGHT/3, GAME_WIDTH, LINE_WIDTH))
    pygame.draw.rect(screen,line_color, (0, 2*(GAME_HEIGHT/3), GAME_WIDTH, LINE_WIDTH))

def draw():
    screen.fill(color)
    linii()
    pygame.display.flip()
draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

            #c1 l1
            if x > 0 and x < GAME_WIDTH / 3 and y > 0 and y < GAME_HEIGHT//3:
                x_width, y_width = imagineax.image.get_size()
                if turn == "X":
                    if c11 == None:
                        c11 = screen.blit(imagineax.image, (((GAME_WIDTH // 3 - x_width) / 2), ((GAME_HEIGHT // 3) - y_width ) // 2))
                        c11 = "X"
                        turn = "0"
                else:
                    if c11 == None:
                        c11 = screen.blit(imaginea0.image, (((GAME_WIDTH // 3 - x_width) / 2), ((GAME_HEIGHT // 3) - y_width ) // 2))
                        c11 = "0"
                        turn = "X"
                castigat()
                pygame.display.flip()
            #c1 l2
            if x > 0 and x < GAME_WIDTH / 3 and y > GAME_HEIGHT // 3 and y < (2 * GAME_HEIGHT) //3:
                x_width, y_width = imagineax.image.get_size()
                if turn == "X":
                    if c12 == None:
                        c12 = screen.blit(imagineax.image, (((GAME_WIDTH // 3 - x_width) / 2), (GAME_HEIGHT - y_width) // 2))
                        c12 = "X"
                        turn = "0"
                else:
                    if c12 == None:
                        c12 = screen.blit(imaginea0.image, (((GAME_WIDTH // 3 - x_width) / 2), (GAME_HEIGHT - y_width) // 2))
                        c12 = "0"
                        turn = "X"
                castigat()
                pygame.display.flip()
            #c1 l3
            if x > 0 and x < GAME_WIDTH / 3 and y > (2 * GAME_HEIGHT) //3 and y < GAME_HEIGHT:
                x_width, y_width = imagineax.image.get_size()
                if turn == "X":
                    if c13 == None:
                        c13 = screen.blit(imagineax.image, (((GAME_WIDTH // 3 - x_width) / 2), ((2 * GAME_HEIGHT // 3) + ((GAME_HEIGHT // 3) - y_width ) // 2)))
                        c13 = "X"
                        turn = "0"
                else:
                    if c13 == None:
                        c13 = screen.blit(imaginea0.image, (((GAME_WIDTH // 3 - x_width) / 2), ((2 * GAME_HEIGHT // 3) + ((GAME_HEIGHT // 3) - y_width ) // 2)))
                        c13 = "0"
                        turn = "X"
                castigat()
                pygame.display.flip()
            #c2 l1
            if x > GAME_WIDTH // 3 and x < GAME_WIDTH // 3 + GAME_WIDTH // 3 and y > 0 and y < GAME_HEIGHT//3:
                x_width, y_width = imagineax.image.get_size()
                if turn == "X":
                    if c21 == None:
                        c21 = screen.blit(imagineax.image, (((GAME_WIDTH - x_width) // 2), ((GAME_HEIGHT // 3) - y_width ) // 2))
                        c21 = "X"
                        turn = "0"
                else:
                    if c21 == None:
                        c21 = screen.blit(imaginea0.image, (((GAME_WIDTH - x_width) // 2), ((GAME_HEIGHT // 3) - y_width ) // 2))
                        c21 = "0"
                        turn = "X"
                castigat()
                pygame.display.flip()
            #c2 l2
            if x > GAME_WIDTH // 3 and x < GAME_WIDTH // 3 + GAME_WIDTH // 3 and y > GAME_HEIGHT // 3 and y < 2 * GAME_HEIGHT //3:
                x_width, y_width = imagineax.image.get_size()
                if turn == "X":
                    if c22 == None:
                        c22 = screen.blit(imagineax.image, ((GAME_WIDTH - x_width) // 2, (GAME_HEIGHT - y_width) // 2))
                        c22 = "X"
                        turn = "0"
                else:
                    if c22 == None:
                        c22 = screen.blit(imaginea0.image, ((GAME_WIDTH - x_width) // 2, (GAME_HEIGHT - y_width) // 2))
                        c22 = "0"
                        turn = "X"
                castigat()
                pygame.display.flip()
            #c2 l3
            if x > GAME_WIDTH // 3 and x < 2 * GAME_WIDTH // 3 and y > 2 * GAME_HEIGHT // 3 and y < GAME_HEIGHT:
                x_width, y_width = imagineax.image.get_size()
                if turn == "X":
                    if c23 == None:
                        c23 = screen.blit(imagineax.image, ((GAME_WIDTH - x_width) // 2,  ((GAME_HEIGHT - y_width) // 2) + GAME_HEIGHT // 3))
                        c23 = "X"
                        turn = "0"
                else:
                    if c23 == None:
                        c23 = screen.blit(imaginea0.image, ((GAME_WIDTH - x_width) // 2,  ((GAME_HEIGHT - y_width) // 2) + GAME_HEIGHT // 3))
                        c23 = "0"
                        turn = "X"
                castigat()
                pygame.display.flip()
            #c3 l1
            if x > GAME_WIDTH // 3 * 2 and x < GAME_WIDTH and y > 0 and y < GAME_HEIGHT//3:
                x_width, y_width = imagineax.image.get_size()
                if turn == "X":
                    if c31 == None:
                        c31 = screen.blit(imagineax.image, (((GAME_WIDTH // 3 + (GAME_WIDTH - x_width) // 2), ((GAME_HEIGHT // 3) - y_width) / 2)))
                        c31 = "X"
                        turn = "0"
                else:
                    if c31 == None:
                        c31 = screen.blit(imaginea0.image, (((GAME_WIDTH // 3 + (GAME_WIDTH - x_width) // 2), ((GAME_HEIGHT // 3) - y_width) / 2)))
                        c31 = "0"
                        turn = "X"
                castigat()
                pygame.display.flip()
            #c3 l2
            if x > GAME_WIDTH // 3 * 2 and x < GAME_WIDTH and y > GAME_HEIGHT // 3 and y < 2 * GAME_HEIGHT//3:
                x_width, y_width = imagineax.image.get_size()
                if turn == "X":
                    if c32 == None:
                        c32 = screen.blit(imagineax.image, (((GAME_WIDTH // 3 + (GAME_WIDTH - x_width) // 2), (GAME_HEIGHT - y_width) // 2)))
                        c32 = "X"
                        turn = "0"
                else:
                    if c32 == None:
                        c32 = screen.blit(imaginea0.image, (((GAME_WIDTH // 3 + (GAME_WIDTH - x_width) // 2), (GAME_HEIGHT - y_width) // 2)))
                        c32 = "0"
                        turn = "X"
                castigat()
                pygame.display.flip()
            #c3 l3
            if x > 2 * GAME_WIDTH // 3 and x < GAME_WIDTH and y > 2 * GAME_HEIGHT // 3 and y < GAME_HEIGHT:
                x_width, y_width = imagineax.image.get_size()
                if turn == "X":
                    if c33 == None:
                        c33 = screen.blit(imagineax.image, (2 * GAME_WIDTH // 3 + ((GAME_WIDTH // 3) - x_width) // 2,  2 * GAME_HEIGHT // 3 + ((GAME_HEIGHT // 3) - y_width) // 2))
                        c33 = "X"
                        turn = "0"
                else:
                    if c33 == None:
                        c33 = screen.blit(imaginea0.image, (2 * GAME_WIDTH // 3 + ((GAME_WIDTH // 3) - x_width) // 2,  2 * GAME_HEIGHT // 3 + ((GAME_HEIGHT // 3) - y_width) // 2))
                        c33 = "0"
                        turn = "X"
                castigat()
                pygame.display.flip()
        if event.type == pygame.QUIT:
            raise SystemExit