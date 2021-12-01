import pygame
import time
import random

def bubleSort(a):
    running = True

    while running:
        running = False
        for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                b = a[i]
                a[i] = a[i+1] 
                a[i+1] = b
                running = True
    return a

def bubleSortStep(a):
    for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                b = a[i]
                a[i] = a[i+1] 
                a[i+1] = b
    return a

def selectionSortStep(a, l):
    min = a[l]
    f = l
    for i in range(l, len(a)):
        if(a[i]<min):
            min = a[i]
            f =i
    b = a[l]
    a[l] = min
    a[f] = b
    return a


def fill(i):
    a = []
    for j in range(0,i):
        a.append( random.randint(0,49))
    return a
    


def setup():
    pygame.init()

    screen = pygame.display.set_mode([900,550])
    running = True
    clock = pygame.time.Clock()

    color = (255,0,0)
    offsetX = 20 
    rectWidth = 5

    start= time.time()
    k = 1
    b = fill(173)
    while running:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if (time.time() - start) >= (1/8)*k:
            print(k)
            #b = bubleSortStep(b)
            selectionSortStep(b,k-1)
            k = k+1
            print(b)
            for i in range(0,len(b)):
                offsetY = 498-10*b[i]
                pygame.draw.rect(screen,color,pygame.Rect((offsetX+i*rectWidth),2+offsetY,2,10*b[i]))
            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    setup()