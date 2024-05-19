import pygame as py
import sys
import random as rand

py.init()
py.font.init()

screenSize = 800
clock = py.time.Clock()
canvas = py.display.set_mode((screenSize, screenSize))
gameOver = False
someText = py.font.SysFont('SourceCodeVF Semibold', 30)

score = 0

#CONTROLS THE WAY THAT THE PIPES BEHAVE

#RANDOM POSITION FOR THE PIPES
def randomPos():
    pipeTopPos = rand.randint(-screenSize + 100, -300)
    pipeBottomPos = pipeTopPos + screenSize + 200
    

    return [pipeTopPos, pipeBottomPos]

pipesPos = randomPos()

pipeTop = py.Rect(screenSize + 80, pipesPos[0], 80, screenSize)
pipeBottom = py.Rect(screenSize + 80, pipesPos[1], 80, screenSize)

#DRAW PIPES ON THE SCREEN
def drawPipes():
    py.draw.rect(canvas, (0, 255, 0), pipeTop)
    py.draw.rect(canvas, (0, 255, 0), pipeBottom)

    if pipeTop.x <= -pipeTop.width:
        pipeTop.x = screenSize + 80
        pipeBottom.x = screenSize + 80

        pipesPos = randomPos()
        pipeTop.y = pipesPos[0]
        pipeBottom.y = pipesPos[1]
    else:
        pipeTop.x -= 10
        pipeBottom.x -= 10




#CONTROLS THE WAY THE BIRDO BEHAVES

bird = py.Rect(100, (screenSize / 2) - 30, 60, 60)

gravidade = 1
def drawBird():
    global gravidade
    py.draw.rect(canvas, (255, 0, 0), bird)

    if bird.y < screenSize - 60:
        gravidade += 0.7
        bird.y += gravidade

    #if bird.y >= screenSize: gravidade = 0


#HERE IT CHECKS FOR COLLISIONS
def checkCollision():
    global score, gameOver
    if pipeTop.x == bird.x: score += 1 
    if not py.Rect.colliderect(pipeTop, bird) and not py.Rect.colliderect(pipeBottom, bird) and bird.y < screenSize - 60:
        canvas.blit(someText.render(str(score), False, (255, 255, 255)), (screenSize / 2, 100))
    else:
        gameOver = True

#MAIN GAME LOOP
while True:
    canvas.fill((30, 30, 30))

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                gravidade = 0
                gravidade -= 10
            if gameOver: 
                gameOver = False
                py.display.update()
                bird = py.Rect(100, (screenSize / 2) - 30, 60, 60)
                pipeTop = py.Rect(screenSize + 80, pipesPos[0], 80, screenSize)
                pipeBottom = py.Rect(screenSize + 80, pipesPos[1], 80, screenSize)
                score = 0
    
    if not gameOver:
        drawPipes()
        drawBird()
        checkCollision()
        py.display.update()
    else:
        text = someText.render("GAME OVER, PRESS ANY KEY TO RESTART", False, (255, 255, 255))
        canvas.blit(text, ((screenSize / 2) - text.get_width() / 2, (screenSize / 2) - text.get_height()))
        py.display.update()

    clock.tick(60)
