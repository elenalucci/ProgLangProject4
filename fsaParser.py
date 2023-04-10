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

    def __init__(self,fsaFile):
        self.fsaFile = fsaFile

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
        self.currState = self.startState
        #print(self.totalStates)
        #print(self.legalVars)
        #print(self.legalMoves)
        #print(self.startState)
        #print(self.legalEndStates)

    def writeDemoFunc(self):
        demoFunc = "(defun demo()\n\t(setq fp(open \"theString.txt\" :direction :input))\n\t(setq fsaChar (read  fp \"done\"))\n\t(princ \"processing\")\n\t(princ fsaChar)\n\t(fresh-line )\n\t(fsa fsaChar)\n)"
        return demoFunc

    def writeStartFunc(self):
        startFunc = "(defun fsa(fsaChar)\n\t(cond\n\t\t((NULL fsaChar) (pprint \"illegal empty fsa string\"))\n\t\t(t(state" + self.startState + " fsaChar))\n\t)\n)"
        return startFunc;
    
    def createStateFunc(self,stateNum,funcRuleList): 
        #print(stateNum)
        lispRuleList = []
        isLegalEndState = False

        for x in self.legalEndStates:
            if (int(x) == int(stateNum)):
                isLegalEndState = True

        for x in funcRuleList:
           lispRuleList.append(self.writeEQ(x[2],x[1]))
        
        lispRuleList.append(self.writeNull(stateNum,isLegalEndState))
        lispRuleList.append(self.writeElse(stateNum))

        stateFunction = "(defun state" + str(stateNum) + "(fsaChar)\n\t(cond\n"
        for x in lispRuleList:
            stateFunction += x
        stateFunction += "\t)\n)"

        return stateFunction


    def writeEQ(self,rule,nextState):
        EQ = "\t\t((EQ '" + rule + "(car fsaChar))(state" + nextState + "(cdr fsaChar)))\n"
        return EQ
    
    def writeNull(self,stateNum,isLegalEndState):
        nullStatement = ""
        if(isLegalEndState == False):
            nullStatement = "\t\t((NULL fsaChar) (pprint \"illegal fsa string: state " + str(stateNum) +" is not an accept state\"))\n"
        if(isLegalEndState == True):
            nullStatement = "\t\t((NULL fsaChar)(pprint \"legal fsa string\"))\n"
        return nullStatement

    def writeElse(self,stateNum):
        tStatement = "\t\t(t (pprint \"illegal character in state " + str(stateNum) + "\"))\n"
        return tStatement

    def writeLisp(self):
        self.lispProg.append(self.writeDemoFunc())
        self.lispProg.append(self.writeStartFunc())

        funcRuleList = []
        for x in range(int(self.totalStates)):
            #print(x)
            for y in self.legalMoves:
                temp = y.replace(")","")
                temp = temp.replace("(","")
                tempSplit = temp.split(':')
                if(int(tempSplit[0]) == x):
                    funcRuleList.append(tempSplit)
            #print(funcRuleList)

            self.lispProg.append(self.createStateFunc(x,funcRuleList))
            
            funcRuleList.clear()

        f = open("part2.lsp", "x")
        for x in self.lispProg:
            f.write(x)
        f.close()
    
    def start(self):
        self.readFiles()
        self.writeLisp()

fsa = fsaParser(sys.argv[1])
fsa.start()
