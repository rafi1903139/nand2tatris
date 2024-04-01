import constant as ct
from helper import Helper 

class CodeWriter:
    def __init__(self, source, isDir=False):
        try:
            
            source = source.split('.vm')[0]
            outputFile = source.split('/')[-1] if not isDir else source.split('/')[-2]
            source += '.asm' if not isDir else f'{outputFile}.asm'
            self.fileName = ""
            self.hp = Helper()
            self.file = open(source, 'w')

            print("File opened successfully for writing")
            print(source)
            self.file.write(self.hp.getBootstrap())

        except:
            print("Couldn't open file")
    
    def writeArithmetic(self, command):
        cmd = ''
        if command in ['add', 'sub', 'neg']:
            cmd = self.hp.arithmatic(command)
        elif command in ['gt', 'lt', 'eq']:
            cmd = self.hp.compare(command)
        elif command in ['and', 'or', 'not']:
            cmd = self.hp.logical(command)

        self.file.write(cmd)
            
    
    def writePushPop(self, cmdType, segment, index):
        if cmdType == ct.C_PUSH:
            cmd = self.hp.push(segment, index, self.fileName)
            self.file.write(cmd)
        
        elif cmdType == ct.C_POP:
            cmd = self.hp.pop(segment, index, self.fileName)
            self.file.write(cmd)

        else:
            print("invalid argument for push or pop")

    def writeLabel(self, label):
        # label would be different for function call
        label = self.fileName + "." + label 
        cmd = self.hp.getLabel(label) 
        self.file.write(cmd) 

    def writeGoto(self, label):
        label = self.fileName + "." + label 
        cmd = self.hp.getGoto(label) 
        self.file.write(cmd)
    
    def writeIf(self, label):
        label = self.fileName + "." + label 
        cmd = self.hp.getIfGoto(label) 
        self.file.write(cmd)
    
    def writeFunction(self, functionName, nVars):
        # used for testing purpose
        # functionLabel = self.fileName + "." + functionName 
        cmd = self.hp.getFunction(functionName, nVars) 
        self.file.write(cmd)

    def writeCall(self, functionName, nArgs):
        # testing purpose
        #functionLabel = self.fileName + "." + functionName 
        cmd = self.hp.getFunctionCall(functionName, nArgs) 

        self.file.write(cmd)
   
    def writeReturn(self):
        cmd = self.hp.getReturn()

        self.file.write(cmd)

    def close(self):
        self.file.close()

