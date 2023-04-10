#Programming Languages Project 4 Elena Lucci
import sys

class fsaParser:
    #global variables
    fsaFile = ""
    #list for each token in the fsa
    tokens = []
    #holds total number of states in the fsa
    totalStates = 0
    #holds legal move set rules
    legalMoves = []
    #start state
    startState = 0
    #keeps track of current state
    currState = 0
    #holds the legal end states
    legalEndStates = []
    #holds each part of the lisp program
    lispProg = []
    
    #default, retrieves fsa.txt as argument from bat file
    def __init__(self,fsaFile):
        self.fsaFile = fsaFile

    #opens and reads fsa file, parses into tokens
    def readFiles(self):
        f = open(self.fsaFile)
        content = f.readline()
        self.tokens = content.split(";")
        f.close()
        self.setVars()

    #splits up the tokens and holds them in separate variables
    def setVars(self):
        self.totalStates = self.tokens[0]
        self.legalMoves = self.tokens[2].split(',')
        self.startState = self.tokens[3]
        self.legalEndStates = self.tokens[4].split(',')
        self.currState = self.startState

    #writes the demo function for the lisp program, returns as a variable
    def writeDemoFunc(self):
        demoFunc = "(defun demo()\n\t(setq fp(open \"theString.txt\" :direction :input))\n\t(setq fsaChar (read  fp \"done\"))\n\t(princ \"processing\")\n\t(princ fsaChar)\n\t(fresh-line )\n\t(fsa fsaChar)\n)"
        return demoFunc

    #writes the start fsa function for the lisp program, returns as a variable
    def writeStartFunc(self):
        startFunc = "(defun fsa(fsaChar)\n\t(cond\n\t\t((NULL fsaChar) (pprint \"illegal empty fsa string\"))\n\t\t(t(state" + self.startState + " fsaChar))\n\t)\n)"
        return startFunc;
    
    #creates each individual state function, returns as a variable
    def createStateFunc(self,stateNum,funcRuleList): 
        #list of rules accumulated for each state function
        lispRuleList = []
        #keeps track of if the current state is a legal end state
        isLegalEndState = False
        
        #determines if current stateNum is a legal end state
        for x in self.legalEndStates:
            if (int(x) == int(stateNum)):
                isLegalEndState = True

        #loops through the rule sets for the current state, collects equality statements, adds to lispRuleList
        for x in funcRuleList:
           lispRuleList.append(self.writeEQ(x[2],x[1]))
        
        #adds the Null character rule to lispRuleList
        lispRuleList.append(self.writeNull(stateNum,isLegalEndState))
        #adds the else statement to the lispRuleList
        lispRuleList.append(self.writeElse(stateNum))

        #start of the state function
        stateFunction = "(defun state" + str(stateNum) + "(fsaChar)\n\t(cond\n"
        #loops through the rules we accumulated and adds them to the state function
        for x in lispRuleList:
            stateFunction += x
        #ending of state function
        stateFunction += "\t)\n)"

        return stateFunction

    #creates the equality rule statement
    def writeEQ(self,rule,nextState):
        EQ = "\t\t((EQ '" + rule + "(car fsaChar))(state" + nextState + "(cdr fsaChar)))\n"
        return EQ
    
    #creates the Null statement that is based on whether or not we are in a legal end state
    def writeNull(self,stateNum,isLegalEndState):
        nullStatement = ""
        if(isLegalEndState == False):
            nullStatement = "\t\t((NULL fsaChar) (pprint \"illegal fsa string: state " + str(stateNum) +" is not an accept state\"))\n"
        if(isLegalEndState == True):
            nullStatement = "\t\t((NULL fsaChar)(pprint \"legal fsa string\"))\n"
        return nullStatement

    #else (t) statement that is in every state function for illegal characters
    def writeElse(self,stateNum):
        tStatement = "\t\t(t (pprint \"illegal character in state " + str(stateNum) + "\"))\n"
        return tStatement
    
    #creates the lisp program
    def writeLisp(self):
        self.lispProg.append(self.writeDemoFunc())
        self.lispProg.append(self.writeStartFunc())
        
        #Holds the rule set for the current state
        funcRuleList = []
        #for each state, create a function
        for x in range(int(self.totalStates)):
            #parse the tokens
            for y in self.legalMoves:
                temp = y.replace(")","")
                temp = temp.replace("(","")
                tempSplit = temp.split(':')
                #finds the list of rules for the current state,adds those to the current funcRuleList
                if(int(tempSplit[0]) == x):
                    funcRuleList.append(tempSplit)
            
            #adds entire stateFunction to the lisp Program
            self.lispProg.append(self.createStateFunc(x,funcRuleList))
            #clears list for next state
            funcRuleList.clear()

        #creates and opens part2.lsp, returns an error if file name already exists
        f = open("part2.lsp", "x")
        #writes lispProgram into file
        for x in self.lispProg:
            f.write(x)
        f.close()
    
    #starts the program
    def start(self):
        self.readFiles()
        self.writeLisp()

#takes file argument from .bat file
fsa = fsaParser(sys.argv[1])
fsa.start()
