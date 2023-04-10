import sys

class fsaParser:

    fsaFile = ""
    tokens = []
    totalStates = 0
    legalVars = []
    legalMoves = []
    startState = 0
    currState = 0
    legalEndStates = []
    lispProg = []

    def __init__(self):
        self.fsaFile = "fsa.txt"

    def readFiles(self):
        f = open(self.fsaFile)
        content = f.readline()
        self.tokens = content.split(";")
        f.close()
        self.setVars()

    def setVars(self):
        self.totalStates = self.tokens[0]
        self.legalVars = self.tokens[1].split(',')
        self.legalMoves = self.tokens[2].split(',')
        self.startState = self.tokens[3]
        self.legalEndStates = self.tokens[4].split(',')
        print(self.totalStates)
        print(self.legalVars)
        print(self.legalMoves)
        print(self.startState)
        print(self.legalEndStates)

    def writeDemoFunc(self):
        demoFunc = "(defun demo()\n\t(setq fp(open \"theString.txt\" :direction :input))\n\t(setq fsaChar (read  fp \"done\"))\n\t(princ \"processing\")\n\t(princ fsaChar)\n\t(fsa fsaChar)\n)"
        return demoFunc

    def writeLisp(self):
        self.lispProg.append(self.writeDemoFunc())
        #print(self.lispProg[0])

    def start(self):
        self.readFiles()
        self.writeLisp()

fsa = fsaParser()
fsa.start()
