'''
Cop and Robber Game - (Graphical Version)
Done by: Rafael De La Cruz
Min Resolution of (1050 x 510)
**not scalable**
'''
from CopRobConsole import *
from tkinter import *
from random import randint
from PIL import Image, ImageTk
from platform import system


class CopRobGraphics:

    def __init__(self):
        self.copRob = CopRobGame(None)
        self.os = system()
        # self.windowSize = self.getWindowSize()

        root = Tk()  # start event loop
        root.title("Cop and Robber")
        root.geometry(self.getWindowSize())
        # root.resizable(False, False)
        self.screen = root

        self.welcomeFrame = Frame(root)
        self.welcomeFrame.place(x=340, y=20)

        welcomeMSG = self.copRob.UI.introMSG()
        welcomeLabel = Label(
            self.welcomeFrame,
            text=welcomeMSG,
            justify=CENTER,
            font=("Helvetica", 16))

        welcomeLabel.pack()

        continueButton = Button(self.welcomeFrame, text="Continue")
        continueButton.pack()
        continueButton.bind("<Button-1>", self.startGame)

        root.mainloop()

    def getWindowSize(self):
        if self.os == "Darwin":  # mac/linux
            return "1050x510"
        else:
            return "1190x510"

    def startGame(self, event):
        self.welcomeFrame.place_forget()
        self.gameWindow(self.screen)

    def gameWindow(self, root):

        self.msgCanv = msgCanvas(root, self.copRob)
        self.msgCanv.place()

        self.imageCanvas = imageCanvas(root)
        self.imageCanvas.place()

        self.mainFrame = Frame(root)
        self.mainFrame.place(x=650, y=367)

        self.moveSection = movePlayerSection(
            self.mainFrame, self.copRob,
            self.imageCanvas, self.msgCanv)

        self.playersSection = playerPositionSection(
            self.mainFrame, self.copRob,
            self.moveSection, self.msgCanv)

        self.edgesSection = createEdgeSection(
            self.mainFrame, self.copRob,
            self.playersSection, self.msgCanv)

        self.vertexSection = createVertexSection(
            self.mainFrame, self.copRob,
            self.edgesSection, self.msgCanv)

        self.move = movesAllowedSection(
            self.mainFrame, self.copRob,
            self.vertexSection, self.msgCanv)

        root.mainloop()  # ends event loop


class msgCanvas(Frame):

    def __init__(self, root, copRob):
        Frame.__init__(self, root)
        self.copRob = copRob
        self.root = root
        self.height = self.textBoxHeight()
        self.resultBox()
        self.msgBox()

    def resultBox(self):
        self.resultString = StringVar()
        self.resultsBox = Label(self.root, textvariable=self.resultString)
        self.resultsBox.place(x=650, y=5)
        self.resultsBox['font'] = ("Helvetica", 14)
        self.resultsBox['anchor'] = CENTER
        self.resultsBox['wraplength'] = 258
        self.resultsBox['relief'] = SUNKEN
        self.resultsBox['width'] = 48
        self.resultsBox['height'] = self.height

    def msgBox(self):
        self.messageString = StringVar()
        self.messageBox = Label(self.root, textvariable=self.messageString)
        self.messageBox.place(x=650, y=183)
        self.messageBox['anchor'] = CENTER
        self.messageBox['font'] = ("Helvetica", 14)
        self.messageBox['relief'] = SUNKEN
        self.messageBox['width'] = 48
        self.messageBox['height'] = self.height

    def textBoxHeight(self):
        if system() == 'Darwin':
            return 11
        else:
            return 8

    def introMSG(self, messageDisplay):

        if messageDisplay == "welcome":
            welcomeMSG = (
                "                                        "
                + "\nEnter the amount of moves the cop   "
                + "\n          is allowed!               "
                + "\n                                    "
                + "\n                                    "
                + "\n   Press 'Enter' to contine!        "
            )
            self.messageString.set(welcomeMSG)

        if messageDisplay == "vertex":
            vertexMSG = self.copRob.UI.questionExplained("vertex")
            self.messageString.set(vertexMSG)

        if messageDisplay == "edges":
            edgeMSG = self.copRob.UI.questionExplained("edges")
            self.messageString.set(edgeMSG)

        if messageDisplay == "place":
            placeMSG = self.copRob.UI.questionExplained("place")
            self.messageString.set(placeMSG)

        if messageDisplay == "move":
            moveMSG = self.copRob.UI.questionExplained("move")
            self.messageString.set(moveMSG)

        if messageDisplay == "end":
            self.messageString.set(f"{self.copRob.UI.displayThanks()}")

        if messageDisplay == "GameOver":
            self.messageBox['fg'] = 'red'
            gameOverMSG = ("Game Over!\n")
            self.messageString.set(gameOverMSG*13)

    def updateResults(self):
        self.resultString.set(self.copRob.display())


class imageCanvas(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        img = ImageTk.PhotoImage(self.displayPlayer("start_image"))
        self.panel = Label(root, image=img)
        self.panel.image = img
        self.panel.place(x=1, y=2)

    def displayPlayer(self, player):
        displayPhoto = {"start_image": "./assets/start_image.jpg",
                        "Cop": "./assets/cop.jpg",
                        "Cop_2": "./assets/cop_2.jpg",
                        "Robber": "./assets/robber.jpg",
                        "Robber_2": "./assets/robber_2.jpg",
                        "CopWon": "./assets/robber_won_2.jpg",
                        "RobberWon": "./assets/robber_won.jpg"}

        assert (player in displayPhoto)
        return Image.open(displayPhoto[player])

    def changeImage(self, player):

        if player == "Cop":
            copIMG = ImageTk.PhotoImage(self.displayPlayer("Cop"))
            self.panel.configure(image=copIMG)
            self.panel.image = copIMG

        if player == "Cop_2":
            copIMG2 = ImageTk.PhotoImage(self.displayPlayer("Cop_2"))
            self.panel.configure(image=copIMG2)
            self.panel.image = copIMG2

        if player == "Robber":
            robberIMG = ImageTk.PhotoImage(self.displayPlayer("Robber"))
            self.panel.configure(image=robberIMG)
            self.panel.image = robberIMG

        if player == "Robber_2":
            robberIMG_2 = ImageTk.PhotoImage(self.displayPlayer("Robber_2"))
            self.panel.configure(image=robberIMG_2)
            self.panel.image = robberIMG_2

        if player == "CopWon":
            copWon = ImageTk.PhotoImage(self.displayPlayer("CopWon"))
            self.panel.configure(image=copWon)
            self.panel.image = copWon

        if player == "RobberWon":
            robberWon = ImageTk.PhotoImage(self.displayPlayer("RobberWon"))
            self.panel.configure(image=robberWon)
            self.panel.image = robberWon

        if player == "start_image":
            copVSrobber = ImageTk.PhotoImage(self.displayPlayer("start_image"))
            self.panel.configure(image=copVSrobber)
            self.panel.image = copVSrobber


class movesAllowedSection:

    def __init__(self, root, mainGame, vertex, msgCan):
        self.copRob = mainGame
        self.vertex = vertex
        self.msgCan = msgCan
        self.makeMovesAllowedLabel(root)
        self.makeMovesAllowedEntry(root)
        self.placeMovesWidgets()
        self.msgCan.introMSG("welcome")
        self.msgCan.updateResults()

    def makeMovesAllowedLabel(self, root):
        self.movesAllowedLabel = Label(
            root, text="Moves Allowed:")

    def makeMovesAllowedEntry(self, root):
        self.movesAllowedEntry = Entry(root)
        self.movesAllowedEntry.bind("<Button-1>", self.clearBoxClick)
        self.movesAllowedEntry.bind("<Return>", self.changeMoves)

    def placeMovesWidgets(self):
        self.movesAllowedLabel.grid(row=0, column=0, sticky="w")
        self.movesAllowedEntry.grid(row=0, column=1, sticky="e")

    def changeMoves(self, event):
        self.copRob.movesAllowed = int(self.movesAllowedEntry.get())
        self.movesAllowedEntry["state"] = DISABLED
        self.vertex.activateEntry()
        self.vertex.acticateButton()
        self.msgCan.introMSG("vertex")
        self.msgCan.updateResults()

    def clearBoxClick(self, event):
        self.movesAllowedEntry.delete(0, END)


class createVertexSection:

    def __init__(self, root, mainGame, edges, msgCan):
        self.copRob = mainGame
        self.edges = edges
        self.msgCan = msgCan
        self.makeVertexLabel(root)
        self.makeVertexEntryBox(root)
        self.makeVertextButton(root)
        self.placeVertexWidgets()
        self.vertex = None

    def makeVertexLabel(self, root):
        self.vertexLabel = Label(root, text="Create Vertices:")

    def makeVertexEntryBox(self, root):
        self.vertexEntryBox = Entry(root)
        self.vertexEntryBox.insert(0, 'Example: a')
        self.vertexEntryBox["state"] = DISABLED
        self.vertexEntryBox.bind("<Key>", self.clearBox)
        self.vertexEntryBox.bind("<Button-1>", self.clearBoxClick)
        self.vertexEntryBox.bind("<Return>", self.createVertex)

    def makeVertextButton(self, root):
        self.vertexDoneButton = Button(root, text="Done")
        self.vertexDoneButton.bind("<Button-1>", self.disableButton)
        self.vertexDoneButton["state"] = DISABLED

    def placeVertexWidgets(self):
        self.vertexLabel.grid(row=2, column=0, sticky="e")
        self.vertexEntryBox.grid(row=2, column=1, sticky="w")
        self.vertexDoneButton.grid(row=2, column=2, sticky="w")

    def createVertex(self, event):  # working on

        vertex = self.vertexEntryBox.get()

        checkList = ['', "Vertex Created", "Vertex already exist",
                     'hit "RETURN" to create vertex', 'Disabled']

        if vertex in checkList:
            pass

        elif vertex not in self.copRob.vertex:
            self.copRob.createVertex(vertex)
            self.vertexEntryBox.delete(0, END)
            self.vertexEntryBox.insert(0, "Vertex Created")
            self.msgCan.updateResults()

        elif self.vertex in self.copRob.vertex:
            self.vertexEntryBox.delete(0, END)
            self.vertexEntryBox.insert(0, "Vertex already exist")

    def disableButton(self, event):
        if self.vertexDoneButton["state"] == NORMAL:
            self.vertexEntryBox.delete(0, END)
            self.vertexEntryBox["state"] = DISABLED
            self.vertexDoneButton["state"] = DISABLED
            self.msgCan.introMSG("edges")
            self.edges.activateEntry()
            self.msgCan.updateResults()
            self.edges.activateButton()

    def clearBox(self, event):
        self.vertexEntryBox.delete(0, END)

    def clearBoxClick(self, event):
        self.vertexEntryBox.delete(0, END)
        self.vertexEntryBox.insert(0, '"RETURN" to create vertex')

    def getVetex(self):
        self.vertex = self.copRob.getVertices()

    def activateEntry(self):
        self.vertexEntryBox['state'] = NORMAL

    def acticateButton(self):
        self.vertexDoneButton["state"] = NORMAL


class createEdgeSection:

    def __init__(self, root, mainGame, players, msgCan):
        self.copRob = mainGame
        self.players = players
        self.msgCan = msgCan
        self.makeEdgeLabel(root)
        self.makeEdgeEntryBox(root)
        self.makeEdgeButton(root)
        self.placeEdgeWidgets()

    def makeEdgeLabel(self, root):
        self.edgeLabel = Label(root, text="Create Edges:")

    def makeEdgeEntryBox(self, root):
        self.edgeEntryBox = Entry(root)
        self.edgeEntryBox.insert(0, 'Example: a,b')
        self.edgeEntryBox.bind("<Key>", self.clearBox)
        self.edgeEntryBox.bind("<Button-1>", self.clearBoxClick)
        self.edgeEntryBox.bind("<Return>", self.createEdge)
        self.edgeEntryBox["state"] = DISABLED

    def makeEdgeButton(self, root):
        self.edgeDoneButton = Button(root, text="Done")
        self.edgeDoneButton.bind("<Button-1>", self.disableButton)
        self.edgeDoneButton["state"] = DISABLED

    def placeEdgeWidgets(self):
        self.edgeLabel.grid(row=4, column=0, sticky="w")
        self.edgeEntryBox.grid(row=4, column=1, sticky="w")
        self.edgeDoneButton.grid(row=4, column=2, sticky="w")

    def createEdge(self, event):
        self.edge = self.edgeEntryBox.get()
        try:
            edge = (self.edge[0], self.edge[2])
            flippedEdge = (edge[1], edge[0])

            checkList = ['', "Edge Created", "Edge already exist",
                         '"RETURN" to create Edge', 'Disabled']
            if self.edge in checkList:
                pass

            create = self.copRob.createEdge(edge[0], edge[1])

            if create == False:
                if edge in self.copRob.edges or flippedEdge in self.copRob.edges:
                    self.edgeEntryBox.delete(0, END)
                    self.edgeEntryBox.insert(0, "Edge already exist")
                else:
                    self.edgeEntryBox.delete(0, END)
                    self.edgeEntryBox.insert(0, "Edge not created")

            if create == True:
                self.edgeEntryBox.delete(0, END)
                self.edgeEntryBox.insert(0, "Edge Created")
                self.msgCan.updateResults()
        except:
            self.edgeEntryBox.insert(0, "Invalid Entry")

    def clearBox(self, event):
        if len(self.edgeEntryBox.get()) >= 3:
            self.edgeEntryBox.delete(0, END)

    def clearBoxClick(self, event):
        self.edgeEntryBox.delete(0, END)
        self.edgeEntryBox.insert(0, '"RETURN" to create Edge')

    def disableButton(self, event):
        if self.edgeDoneButton["state"] == NORMAL:
            self.edgeEntryBox.delete(0, END)
            self.edgeEntryBox["state"] = DISABLED
            self.players.activateEntry()
            self.msgCan.introMSG("place")
            self.edgeDoneButton["state"] = DISABLED

    def activateEntry(self):
        self.edgeEntryBox["state"] = NORMAL

    def activateButton(self):
        self.edgeDoneButton["state"] = NORMAL


class playerPositionSection:
    def __init__(self, root, mainGame, move, msgCan):
        self.copRob = mainGame
        self.msgCan = msgCan
        self.move = move
        self.firstMove = self.copRob.firstMove
        self.playersPlaced = False
        self.winner = None
        self.makePositionLabel(root)
        self.makePositionEntryBox(root)
        self.placePositionWidgets()

    def makePositionLabel(self, root):
        self.positionLabel = Label(root, text="Place Player's:")

    def makePositionEntryBox(self, root):
        self.positionEntryBox = Entry(root)
        self.positionEntryBox.insert(0, 'Example: C,a')
        self.positionEntryBox.bind("<Key>", self.clearBox)
        self.positionEntryBox.bind("<Button-1>", self.clearBoxClick)
        self.positionEntryBox.bind("<Return>", self.placePlayer)
        self.positionEntryBox["state"] = DISABLED

    def placePositionWidgets(self):
        self.positionLabel.grid(row=6, column=0, sticky="w")
        self.positionEntryBox.grid(row=6, column=1, sticky="w")

    def placePlayer(self, event):
        self.playerPosition = self.positionEntryBox.get()
        player = self.playerPosition[0]
        vertex = self.playerPosition[2]

        checkList = ['', 'Cop Placed', 'Robber Placed', 'Not Your Turn',
                     'Player Not Placed', 'hit "RETURN" to place player']

        if self.playerPosition in checkList:
            pass

        elif self.firstMove == True and player == 'C':
            self.copRob.placePlayer(player, vertex)
            self.positionEntryBox.delete(0, END)
            self.positionEntryBox.insert(0, 'Cop Placed')
            self.firstMove = False

        elif self.firstMove == False and player == 'R':
            self.copRob.placePlayer(player, vertex)
            self.positionEntryBox.delete(0, END)
            self.positionEntryBox.insert(0, 'Robber Placed')
            self.playersPlaced = True

        else:
            if player == 'C' or player == 'R':
                self.positionEntryBox.delete(0, END)
                self.positionEntryBox.insert(0, 'Not Your Turn')
            else:
                self.positionEntryBox.delete(0, END)
                self.positionEntryBox.insert(0, 'Player Not Placed')

        self.msgCan.updateResults()
        self.showWinner()
        self.deactivateEntry()

    def clearBox(self, event):
        if len(self.positionEntryBox.get()) >= 3:
            self.positionEntryBox.delete(0, END)

    def clearBoxClick(self, event):
        self.positionEntryBox.delete(0, END)
        self.positionEntryBox.insert(0, '"RETURN" to place player')

    def deactivateEntry(self):
        if self.playersPlaced == True:
            self.positionEntryBox.delete(0, END)
            self.positionEntryBox["state"] = DISABLED
            self.move.activateEntry()
            self.msgCan.introMSG("move")
            self.move.activateButton()

    def activateEntry(self):
        self.positionEntryBox['state'] = NORMAL

    def showWinner(self):
        if len(self.copRob.playersPosition) == 2:
            check = self.copRob.winCheck()

            if check == 'C':
                self.winner = 'Cop Wins'
            elif check == 'R':
                self.winner = 'Robber Wins'
            elif check == 'X':
                self.winner = "No Winner Yet"


class movePlayerSection:
    def __init__(self, root, mainGame, imageCanvas, msgCanvas):
        self.msgCan = msgCanvas
        self.copRob = mainGame
        self.imageCan = imageCanvas
        self.firstMove = True
        self.playersTurn = 'C'
        self.copQuit = False
        self.winner = None
        self.makeMovePlayerLabel(root)
        self.makeMovePlayerEntry(root)
        self.makeMovePlayerButton(root)
        self.placeMovePlayerWidgets()

    def makeMovePlayerLabel(self, root):
        self.movePlayerLabel = Label(root, text="Move Player's:")

    def makeMovePlayerEntry(self, root):
        self.movePlayerEntry = Entry(root)
        self.movePlayerEntry.insert(0, 'Example: C,c')
        self.movePlayerEntry["state"] = DISABLED
        self.movePlayerEntry.bind("<Key>", self.clearBox)
        self.movePlayerEntry.bind("<Button-1>", self.clearBoxClick)
        self.movePlayerEntry.bind("<Return>", self.movePlayer)

    def makeMovePlayerButton(self, root):
        self.movePlayerButton = Button(root, text="Cop Quit")
        self.movePlayerButton.bind("<Button-1>", self.disableButton)
        self.movePlayerButton["state"] = DISABLED

    def placeMovePlayerWidgets(self):
        self.movePlayerLabel.grid(row=8, column=0, sticky="w")
        self.movePlayerEntry.grid(row=8, column=1, sticky="w")
        self.movePlayerButton.grid(row=8, column=2, sticky="w")

    def movePlayer(self, event):
        try:
            movePlayer = self.movePlayerEntry.get()
            player = movePlayer[0]
            vertex = movePlayer[2]

            checkList = ['', 'Cop moved', 'Robber moved',
                         'Not your turn', '"RETURN" to move player']

            if self.playersTurn == 'C':
                if self.copRob.movesAllowed > self.copRob.copMoves:
                    self.copRob.copMoves += 1

            if movePlayer in checkList:
                pass

            elif player == 'C' and self.firstMove == True:
                self.copRob.movePlayer(player, vertex)
                self.movePlayerEntry.delete(0, END)
                self.movePlayerEntry.insert(0, "Cop moved")
                self.msgCan.updateResults()
                self.imageCan.changeImage("Robber_2")
                self.firstMove = False

            elif player == self.playersTurn and self.firstMove == False:
                if self.playersTurn == 'C':
                    self.copRob.movePlayer(player, vertex)
                    self.movePlayerEntry.delete(0, END)
                    self.movePlayerEntry.insert(0, "Cop moved")
                    self.msgCan.updateResults()
                    self.imageCan.changeImage("Robber_2")

                if self.playersTurn == 'R':
                    self.copRob.movePlayer(player, vertex)
                    self.movePlayerEntry.delete(0, END)
                    self.movePlayerEntry.insert(0, "Robber moved")
                    self.msgCan.updateResults()
                    self.imageCan.changeImage("Cop_2")

            if player != self.playersTurn:
                self.movePlayerEntry.delete(0, END)
                self.movePlayerEntry.insert(0, "Not your turn")

            self.movePlayerEntry.delete(0, END)

            self.changeTurns(player)
            self.checkWinner()
            self.endGame()
        except:
            self.movePlayerEntry.insert(0, "Invalid")

    def disableButton(self, event):
        if self.playersTurn == 'C' and self.firstMove == False:
            self.movePlayerEntry.delete(0, END)
            self.movePlayerEntry.insert(0, "Robber has won, Cop Quit!")
            self.movePlayerEntry["state"] = DISABLED
            self.winner = 'Cop Wins'
            self.imageCan.changeImage("RobberWon")

    def activateEntry(self):
        self.movePlayerEntry["state"] = NORMAL

    def activateButton(self):
        self.movePlayerButton["state"] = NORMAL

    def clearBox(self, event):
        if len(self.movePlayerEntry.get()) > 3:
            self.movePlayerEntry.delete(0, END)

    def clearBoxClick(self, event):
        if self.movePlayerEntry["state"] == NORMAL:
            self.imageCan.changeImage("Cop_2")
            self.movePlayerEntry.delete(0, END)
            self.movePlayerEntry.insert(0, '"RETURN" to move player')

    def changeTurns(self, player):
        if player == self.playersTurn:
            if self.playersTurn == 'C':
                self.playersTurn = 'R'
            elif self.playersTurn == 'R':
                self.playersTurn = 'C'

    def checkWinner(self):
        try:
            check = self.copRob.winCheck()

            if check == 'C':
                self.winner = 'Cop Wins'
            elif check == 'R':
                self.winner = 'Robber Wins'
            elif check == 'X':
                self.winner = "No Winner Yet"
        except:
            pass

    def endGame(self):
        if self.winner == 'Cop Wins':
            self.movePlayerEntry.delete(0, END)
            self.movePlayerEntry.insert(0, "Cop has won")
            self.movePlayerEntry["state"] = DISABLED
            self.imageCan.changeImage("CopWon")
            self.movePlayerButton["state"] = DISABLED
            self.msgCan.introMSG("GameOver")

        elif self.winner == 'Robber Wins':
            self.movePlayerEntry.delete(0, END)
            self.movePlayerEntry.insert(0, "Robber has won")
            self.movePlayerEntry["state"] = DISABLED
            self.imageCan.changeImage("RobberWon")


if __name__ == '__main__':
    CopRobGraphics()
