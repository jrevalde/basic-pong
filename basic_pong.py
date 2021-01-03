import pygame, sys

#section for creating classes for necessary instances
class Ball(pygame.sprite.Sprite): 
     def __init__(self, image_file, speed, location): 
         pygame.sprite.Sprite.__init__(self) 
         self.image = pygame.image.load(image_file) 
         self.rect = self.image.get_rect() 
         self.rect.left, self.rect.top = location 
         self.speed = speed 
     def move(self): 
         global score, score_surf, score_font 
         self.rect = self.rect.move(self.speed) 
         if self.rect.left < 0 or self.rect.right > screen.get_width(): 
             self.speed[0] = -self.speed[0]
             #sound when ball hits side of wall
             if self.rect.top < screen.get_height():
                 hit_wall.play()
 
         if self.rect.top <= 0 : 
             self.speed[1] = -self.speed[1] 
             score = score + 1 
             score_surf = score_font.render(str(score), 1, (0, 0, 0))
             #sound when player gets a point)
             get_point.play()
 #paddle class definition            
class Paddle(pygame.sprite.Sprite): 
     def __init__(self, location = [0,0]): 
        pygame.sprite.Sprite.__init__(self) 
        image_surface = pygame.surface.Surface([100, 20]) 
        image_surface.fill([0,0,0])
        self.image = image_surface.convert() 
        self.rect = self.image.get_rect() 
        self.rect.left, self.rect.top = location
        
pygame.init()
#initialise the sound module
pygame.mixer.init()


pygame.mixer.music.load("bg_music.mp3")
#sets the volume of the music
pygame.mixer.music.set_volume(0.3)
#starts playing the music and repeats forever
pygame.mixer.music.play(-1)

#soundss for other stuff
hit = pygame.mixer.Sound("hit_paddle.wav") 
hit.set_volume(0.4) 
new_life = pygame.mixer.Sound("new_life.wav") 
new_life.set_volume(0.5) 
splat = pygame.mixer.Sound("splat.wav") 
splat.set_volume(0.6) 
hit_wall = pygame.mixer.Sound("hit_wall.wav") 
hit_wall.set_volume(0.4) 
 
get_point = pygame.mixer.Sound("get_point.wav") 
get_point.set_volume(0.2) 
bye = pygame.mixer.Sound("game_over.wav") 
bye.set_volume(0.6)

screen = pygame.display.set_mode([640,480]) 
clock = pygame.time.Clock()

#makes an instance of the ball
myBall = Ball('wackyball.bmp', [10,5], [50, 50]) 
ballGroup = pygame.sprite.Group(myBall) 
paddle = Paddle([270, 400]) 
lives = 3 
score = 0
#creates the font object
score_font = pygame.font.Font(None, 50)
#renders text onto surface
score_surf = score_font.render(str(score), 1, (0, 0, 0)) 
score_pos = [10, 10] 
done = False
running = True

while running: 
    clock.tick(30)
    screen.fill([255, 255, 255])

    #checking for something to happen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #detects mouse movement and moves the ball  
        elif event.type == pygame.MOUSEMOTION: 
            paddle.rect.centerx = event.pos[0]

    #checks if ball hits paddle        
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        #play sound when the ball hits the paddle
        hit.play()
        myBall.speed[1] = -myBall.speed[1]

        
    myBall.move() #moves the ball
    if not done:
        #redraws everything
        screen.blit(myBall.image, myBall.rect) 
        screen.blit(paddle.image, paddle.rect)
        #blit the surface containing score text at that location
        screen.blit(score_surf, score_pos) 
        for i in range (lives): 
            width = screen.get_width() 
            screen.blit(myBall.image, [width - 40 * i, 20]) 
        pygame.display.flip() 
    if myBall.rect.top >= screen.get_rect().bottom: 
        lives = lives - 1 
        if lives == 0: 
            final_text1 = "Game Over" 
            final_text2 = "Your final score is: " + str(score) 
            ft1_font = pygame.font.Font(None, 70) 
            ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0)) 
            ft2_font = pygame.font.Font(None, 50) 
            ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0)) 
            screen.blit(ft1_surf, [screen.get_width()//2 - ft1_surf.get_width()//2, 100]) 
            screen.blit(ft2_surf, [screen.get_width()//2 - ft2_surf.get_width()//2, 200]) 
            pygame.display.flip() 
            done = True 
        else: 
            pygame.time.delay(2000) 
            myBall.rect.topleft = [50, 50] 
pygame.quit()
