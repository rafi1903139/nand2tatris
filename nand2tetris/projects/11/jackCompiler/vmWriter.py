from constant import *


class VmWriter:
    
    def __init__(self, outputFileName):
        try:
            self.file = open(outputFileName, "w")
            print(f"Successfully opened {outputFileName} for writing")
        except:
            print("could'nt write to the file")
    

    def writePush(self, segment, index):
        if segment == VM_CONSTANT:
            segment = "constant"
        elif segment == VM_STATIC:
            segment = "static"
        elif segment == VM_THIS:
            segment = "this"
        elif segment == VM_ARGUMENT:
            segment = "argument"
        elif segment == VM_LOCAL:
            segment = "local" 
        elif segment == VM_THAT:
            segment = "that"
        elif segment == VM_POINTER:
            segment = "pointer"
        elif segment == VM_TEMP:
            segment = "temp"
        else:
            print("Invalid segement")
            return 

        output = f"push {segment} {index}"
        self.file.write(output + "\n") 

    def writePop(self, segment, index):
        if segment == VM_STATIC:
            segment = "static"
        elif segment == VM_THIS:
            segment = "this"
        elif segment == VM_ARGUMENT:
            segment = "argument"
        elif segment == VM_LOCAL:
            segment = "local" 
        elif segment == VM_THAT:
            segment = "that"
        elif segment == VM_POINTER:
            segment = "pointer"
        elif segment == VM_TEMP:
            segment = "temp"
        else:
            print("Invalid segement")
            return 


        output = f"pop {segment} {index}"
        self.file.write(output + "\n")

    def writeArithmetic(self, cmd, isUnary = False):
        if cmd == '+':
            command  = 'add'
        elif cmd == '-':
            if isUnary:
                command = 'neg'
            else:
                command = 'sub'
        elif cmd == '~':
            command = 'not'
        elif cmd == '>':
            command = 'gt'
        elif cmd == '<':
            command = 'lt'
        elif cmd == '=':
            command = 'eq'
        elif cmd == '&':
            command = 'and'
        elif cmd == '|':
            command = 'or' 
        elif cmd == '*':
            self.writeCall('Math.multiply', 2) 
            return
        elif cmd == '/':
            self.writeCall('Math.divide', 2)
            return
        else:
            print(cmd)
            print("Invalid operator in VMwriter")
            return

        output = f"{command}"
        self.file.write(output + "\n")

    def writeLabel(self, label):
        output = f"label {label}"
        self.file.write(output + "\n")

    def writeGoto(self, label):
        output = f"goto {label}"
        self.file.write(output + "\n")

    def writeIf(self, label):
        output = f"if-goto {label}"
        self.file.write(output + "\n")

    def writeCall(self, name, nArgs):
        output = f"call {name} {nArgs}"
        self.file.write(output + "\n")

    def writeFunction(self, name, nVars):
        output = f"function {name} {nVars}"
        self.file.write(output + "\n")

    def writeReturn(self):
        output = f"return"
        self.file.write(output + "\n")

    def close(self):
        self.file.close()
