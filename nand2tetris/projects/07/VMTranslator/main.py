from Parser_1 import Parser 
import sys 
from codewriter import CodeWriter 
import constant 



p = Parser(sys.argv[1])
cw = CodeWriter(sys.argv[1])

while p.hasMoreLines():
    p.advance()
    if p.commandType() == constant.C_ARITHMETIC:
        cw.writeArithmetic(p.command)
    elif p.commandType() == constant.C_PUSH or p.commandType() == constant.C_POP:
        cw.writePushPop(p.commandType(), p.arg1(), p.arg2())

cw.close()




