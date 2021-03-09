import pygame
import tkinter as tk
import socket
from pygame import time

#SERVER STUFF
HOST = ''
PORT = 12354

pixelX = 512
pixelY = 512

pygame.init()
screen = pygame.display.set_mode((512, 512))

done = False
sizeX = 8
sizeY = 8
width = pixelX/sizeX
height = pixelY/sizeY
grid = [[0 for x in range(sizeX)] for y in range (sizeY)]
redPieces = []
blackPieces = []

#images
gameBoard = pygame.image.load('CheckerBoard.png').convert()
gameBoardRect = gameBoard.get_rect()
redPiece = pygame.image.load('RedCheckerPiece.png').convert()
blackPiece = pygame.image.load('BlackCheckerPiece.png').convert()

class tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupied = False
        self.highlighted = False
    def getPiece(self):
        if self.occupied:
            for i in range(len(redPieces)):
                if redPieces[i].x == self.x:
                    if redPieces[i].y == self.y:
                        return redPieces[i]
            
            for i in range(len(blackPieces)):
                if blackPieces[i].x == self.x:
                    if blackPieces[i].y == self.y:
                        return blackPieces[i]
        else:
            return 0


class piece:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
    def draw(self):
        if self.team == 1:
            screen.blit(redPiece, (self.x * 64, self.y * 64))
        elif self.team == 2:
            screen.blit(blackPiece, (self.x * 64, self.y * 64))
    def validMoves(self):
        validMoves = []
        try:
            if not grid[self.x + 1][self.y + 1].occupied:
                validMoves.append(grid[self.x + 1][self.y + 1])
        except:
            self.x
        try:
            if not grid[self.x - 1][self.y + 1].occupied:
                validMoves.append(grid[self.x - 1][self.y + 1])
        except:
            self.x
        try:
            if not grid[self.x + 1][self.y - 1].occupied:
                validMoves.append(grid[self.x + 1][self.y - 1])
        except:
            self.x
        try:
            if not grid[self.x - 1][self.y - 1].occupied:
                validMoves.append(grid[self.x - 1][self.y - 1])
        except:
            self.x

        return validMoves

def initGame():

    for i in range(sizeX):
        for j in range(sizeY):
          grid[i][j] = tile(i, j)
    
    
    grid[0][0].occupied = True
    redPieces.append(piece(0, 0, 1))
    grid[2][0].occupied = True
    redPieces.append(piece(2, 0, 1))
    grid[4][0].occupied = True
    redPieces.append(piece(4, 0, 1))
    grid[6][0].occupied = True
    redPieces.append(piece(6, 0, 1))
    grid[1][1].occupied = True
    redPieces.append(piece(1, 1, 1))
    grid[3][1].occupied = True
    redPieces.append(piece(3, 1, 1))
    grid[5][1].occupied = True
    redPieces.append(piece(5, 1, 1))
    grid[7][1].occupied = True
    redPieces.append(piece(7, 1, 1))
    grid[0][2].occupied = True
    redPieces.append(piece(0, 2, 1))
    grid[2][2].occupied = True
    redPieces.append(piece(2, 2, 1))
    grid[4][2].occupied = True
    redPieces.append(piece(4, 2, 1))
    grid[6][2].occupied = True
    redPieces.append(piece(6, 2, 1))

    grid[1][7].occupied = True
    blackPieces.append(piece(1, 7, 2))
    grid[3][7].occupied = True
    blackPieces.append(piece(3, 7, 2))
    grid[5][7].occupied = True
    blackPieces.append(piece(5, 7, 2))
    grid[7][7].occupied = True
    blackPieces.append(piece(7, 7, 2))
    grid[0][6].occupied = True
    blackPieces.append(piece(0, 6, 2))
    grid[2][6].occupied = True
    blackPieces.append(piece(2, 6, 2))
    grid[4][6].occupied = True
    blackPieces.append(piece(4, 6, 2))
    grid[6][6].occupied = True
    blackPieces.append(piece(6, 6, 2))
    grid[1][5].occupied = True
    blackPieces.append(piece(1, 5, 2))
    grid[3][5].occupied = True
    blackPieces.append(piece(3, 5, 2))
    grid[5][5].occupied = True
    blackPieces.append(piece(5, 5, 2))
    grid[7][5].occupied = True
    blackPieces.append(piece(7, 5, 2))
    
def attemptConnection(ipEntry):
    print("allstar")
    HOST = str(ipEntry)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall('Connection attempted')

    prompt.quit()
    prompt.destroy()

def drawPieces():
    for i in range(len(redPieces)):
        redPieces[i].draw()
    for i in range(len(blackPieces)):
        blackPieces[i].draw()


def mouseClick(pos):
    global selectedPiece
    currentValidMoves = selectedPiece.validMoves()

    if grid[int((pos[0] / width))][int((pos[1] / height))].occupied:
        selectedPiece = grid[int((pos[0] / width))][int((pos[1] / height))].getPiece()
        currentValidMoves = selectedPiece.validMoves()
    elif (not grid[int((pos[0] / width))][int((pos[1] / height))].occupied) & (not selectedPiece == blankPiece):
        if grid[int((pos[0] / width))][int((pos[1] / height))] in currentValidMoves:
            grid[selectedPiece.x][selectedPiece.y].occupied = False
            selectedPiece.x = int((pos[0] / width))
            selectedPiece.y = int((pos[1] / height))
            grid[int((pos[0] / width))][int((pos[1] / height))].occupied = True
            selectedPiece = blankPiece 
        else:
            selectedPiece = blankPiece
    else:
        selectedPiece = blankPiece

blankPiece = piece(0, 0, 0)
selectedPiece = blankPiece

prompt = tk.Tk()
IPLabel = tk.Label(text = "Enter a IP to connect to:")
IPEntry = tk.Entry()
connectButton = tk.Button(text = "Connect", width = 10, height = 2, command = lambda: attemptConnection(IPEntry))

IPLabel.pack()
IPEntry.pack()
connectButton.pack()

prompt.mainloop()

initGame()

#Main loop
while not done:
    screen.blit(gameBoard, gameBoardRect)
    drawPieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if pygame.mouse.get_pressed()[0]:
            mouseClick(pygame.mouse.get_pos())

    time.delay(10)
    pygame.display.flip()