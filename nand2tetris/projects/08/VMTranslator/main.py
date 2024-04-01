from Parser_1 import Parser 
import sys 
from codewriter import CodeWriter 
import constant 
from glob import glob


source = sys.argv[1]
sourceFiles = []
isDirectory = True if ".vm" not in source else False 

# Check if the input is a directory
if isDirectory:
    sourceFiles = glob(source + "*.vm")
else:
    sourceFiles.append(source)

# initialize codewriter
cw = CodeWriter(source, isDirectory)

# iterate all the files and generate a single assembly file
for f in sourceFiles:
    p = Parser(f)
    cw.fileName = f.split(".vm")[0].split("/")[-1]
    while p.hasMoreLines():
        p.advance()
        print(p.command)
        if p.commandType() == constant.C_ARITHMETIC:
            cw.writeArithmetic(p.command)
        elif p.commandType() == constant.C_PUSH or p.commandType() == constant.C_POP:
            cw.writePushPop(p.commandType(), p.arg1(), p.arg2())
        elif p.commandType() == constant.C_LABEL:
            cw.writeLabel(p.arg1())
        elif p.commandType() == constant.C_GOTO:
            cw.writeGoto(p.arg1())
        elif p.commandType() == constant.C_IF:
            cw.writeIf(p.arg1())
        elif p.commandType() == constant.C_FUNCTION:
            cw.writeFunction(p.arg1(), p.arg2())
        elif p.commandType() == constant.C_CALL:
            cw.writeCall(p.arg1(), p.arg2())
        elif p.commandType() == constant.C_RETURN:
            cw.writeReturn()

cw.close()




