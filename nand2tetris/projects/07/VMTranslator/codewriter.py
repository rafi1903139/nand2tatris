import constant as ct
from helper import Helper 

class CodeWriter:
    def __init__(self, fileName):
        try:
            fileName = fileName.split('.vm')[0]
            self.hp = Helper()
            self.file = open(f'{fileName}.asm', 'w')
            print("File opened successfully for writing")

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
            cmd = self.hp.push(segment, index)
            self.file.write(cmd)
        
        elif cmdType == ct.C_POP:
            cmd = self.hp.pop(segment, index)
            self.file.write(cmd)

        else:
            print("invalid argument for push or pop")
    
    def close(self):
        self.file.close()

