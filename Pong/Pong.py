# Importing main library
import pygame

# Initialization of library
pygame.init()

# Setting the dimensions of window
WIDTH, HEIGHT = 1200, 600

# Running the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting the caption of Pong game
pygame.display.set_caption("Pong game")

# Setting font that is used to render text
font20 = pygame.font.Font('freesansbold.ttf', 20)

# Setting RGB values for standard colors which are responsible for: color of background, color of ball and color of player/Striker
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# These 2 lines of code are used to adjust the frame rate
clock = pygame.time.Clock()
FPS = 30

# Setting player class
class Striker:
    # Method used by me for initialization variables of class such as initial position, dimensions, speed and color of object
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        # Using rectangle that is used to control the position and collision of the object
        self.geekRect = pygame.Rect(posx, posy, width, height)
        # Using object that is blit on the screen
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)
    # Method used to display object on the screen 
    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)
    # Method used to change state of the object
    def update(self, yFac):
        self.posy = self.posy + self.speed*yFac
        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height
        self.geekRect = (self.posx, self.posy, self.width, self.height)
    # Method used to render score of player on the screen in text format
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        
        screen.blit(text, textRect)
    # It is used to download the object    
    def getRect(self):
        return self.geekRect
# Setting ball class    
class Ball:
    # Method used for initialization variables of class such as initial position, radius, speed and color of object
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color 
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
    # Method used for rendering object on the screen    
    def display(self):
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        
    # Method used for change state of the object    
    def update(self):
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac
        
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1
        
        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
    # Method used to reset position of the ball
    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1
    # Method used to reflect the ball along the x-axis    
    def hit(self):
        self.xFac *= -1
    # Method used to download the object
    def getRect(self):
        return self.ball  
# Game manager    
def main():
    running = True
    # Defining the objects
    geek1 = Striker(20, 0, 10, 100, 10, GREEN)
    geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
    listOfGeeks = [geek1, geek2]
    # Initial parameters of the players
    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0
    
    while running:
        screen.fill(BLACK)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                if event.key == pygame.K_DOWN:
                    geek2YFac = 1
                if event.key == pygame.K_w:
                    geek1YFac = -1
                if event.key == pygame.K_s:
                    geek1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0
        # Collision detection
        for geek in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                ball.hit()
        # Updating the objects
        geek1.update(geek1YFac)
        geek2.update(geek2YFac) 
        point = ball.update()  
        
        if point == -1:
            geek1Score += 1 
        elif point == 1:
            geek2Score += 1
        # Someone has scored the point and the ball is out of bounds. So, we reset it's position.    
        if point:
            ball.reset()
        
        # Displaying the objects on the screen
        geek1.display()
        geek2.display()
        ball.display()   
        
        # Displaying the scores of the players
        geek1.displayScore("Geek_1 : ", geek1Score, 100, 20, WHITE)
        geek2.displayScore("Geek_2 : ", geek2Score, WIDTH-100, 20, WHITE)
        
        pygame.display.update()
        
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()
    pygame.quit()
