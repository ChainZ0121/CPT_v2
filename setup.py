import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("Music & SF/SFX.wav")
pygame.mixer.music.load("Music & SF/gas gas gas final.wav")

scale = 1

display_width = 1000*scale
display_height = 600*scale

black = (0,0,0)
white = (225,225,225)
red = (150,0,0)
green = (0,150,0)
blue = (100,100,225)
bright_red = (225,0,0)
bright_green = (0,225,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('D')
clock = pygame.time.Clock()



carImg1 = pygame.transform.scale(pygame. image.load('car/car1.png'),(96*3*scale,31*3*scale))
carImg2 = pygame.transform.scale(pygame. image.load('car/car2.png'),(96*3*scale,31*3*scale))
carImg3 = pygame.transform.scale(pygame. image.load('car/car3.png'),(96*3*scale,31*3*scale))
carImg = [carImg1,carImg2,carImg3]

pause = False
game_over = False

def score(count1,count2):
    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render ("Score: " + str(count1) + "  Level: " + str(count2), True, white)
    gameDisplay.blit(text,(0,0))

def blocks(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y,z):
    gameDisplay.blit(carImg[z],(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text,score,level):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)

    game_over(score,level)

def crash(score,level):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('You Crashed',score,level)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
#            if action == "play":
#               game_loop()
#            elif action == "quit":
#                pygame.quit()
#                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + w/2), (y + h/2))
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()

def paused():

    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2 - 150))
        gameDisplay.blit(TextSurf, TextRect)

        button('Resume', display_width/ 2 - 50, 250, 100, 50, green, bright_green,unpause)
        button('Restart', display_width / 2 - 50, 350, 100, 50, green, bright_green, game_loop)
        button('Quit', display_width/ 2 - 50, 450, 100, 50, red, bright_red,quit)

        pygame.display.update()
        clock.tick(15)

def game_over(score,level):

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("GAME OVER", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2 - 150))
        gameDisplay.blit(TextSurf, TextRect)

        button('Score: ' + str(score) + '  Level: ' + str(level), display_width / 2 - 50, 200, 100, 50, black, black, None)
        button('Restart', display_width / 2 - 50, 350, 100, 50, green, bright_green, game_loop)
        button('Quit', display_width/ 2 - 50, 450, 100, 50, red, bright_red,quit)

        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("D", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button('Go!', 200, 450, 100, 50, green, bright_green,game_loop)
        button('Quit', 700, 450, 100, 50, red, bright_red,quit)

        pygame.display.update()
        clock.tick(15)

def game_loop():

    global pause

    pygame.mixer.music.play(-1)
    x = (display_width * 0.34)
    y = (display_height * 0.75)
    x_change = 0
    z = 0

    thing_startx = display_width * 0.5
    thing_starty = display_height * 0.0
    thing_speed = 5
    thing_speedx = random.randrange(-5 * thing_speed - 2 * thing_speed - 30, 5 * thing_speed + 10) * 0.1
    thing_speedy = 1 * thing_speed
    thing_width = 0
    thing_height = 0
    thing_size = 0.2 * thing_speed

    dodged = 0
    level = 1

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -7
                    z = 2
                elif event.key == pygame.K_d:
                    x_change = 7
                    z = 1
                elif event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                    z = 0


        x += x_change

        gameDisplay.fill(black)
        car(x, y, z)

        blocks(thing_startx,thing_starty,thing_width,thing_height,blue)
        thing_startx += thing_speedx
        thing_starty += thing_speedy
        thing_width += thing_size
        thing_height += thing_size


        score(dodged,level)

        if x < 0 - 28 * 3 or x > display_width -28 * 3 - 39 * 3:
            crash(dodged,level)

        if thing_starty > display_height:
            thing_startx = display_width * 0.5
            thing_starty = display_height * 0.0
            thing_speedx = random.randrange(-5 * thing_speed - 2 * thing_speed - 30, 5 * thing_speed + 10) * 0.1
            thing_speedy = 1 * thing_speed
            thing_width = 0
            thing_height = 0
            thing_size = 0.2 * thing_speed
            dodged += 1
            if dodged > 10:
                thing_speed = 10
                level = 2
                if dodged > 20:
                    thing_speed = 15
                    level = 3
                    if dodged > 30:
                        thing_speed = 20
                        level = 4
                        if dodged > 40:
                            thing_speed = 20
                            level = 4
                            if dodged > 50:
                                thing_speed = 25
                                level = 5

        if y < thing_starty + thing_height and y + 25*3 > thing_starty:
            if x+28*3 > thing_startx and x+28*3 < thing_startx + thing_width or x+28*3 + 39*3> thing_startx and x+28*3 + 39*3< thing_startx+thing_width:
                crash(dodged, level)


        pygame.display.update()
        clock.tick(60)

game_intro()

pygame.quit()
quit()