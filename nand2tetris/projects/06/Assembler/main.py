from parser_1 import Parser 
import code_1 
import sys 
from symbol_1 import Symbol  


if len(sys.argv) != 2:
    print("Invalid argument")
    exit() 

p = Parser(sys.argv[1])
hackFile = open("test.hack", 'w')
ins = -1 
sm = Symbol()

# Add the symbols in the table

while p.hasMoreCommnads():
    p.advance()
    if p.commandType() == 'L_COMMAND':
        if not sm.contains(p.symbol()):
            sm.addEntry(p.symbol(), str(ins+1))

    else:
        ins += 1 


p = Parser(sys.argv[1])
cnt = 16 
while p.hasMoreCommnads(): 
    p.advance() 

    if p.commandType() == 'A_COMMAND':
        if p.symbol().isdigit():
            bin_loc = format(int(p.symbol()), f'0{16}b')
        else:
            if not sm.contains(p.symbol()):
                sm.addEntry(p.symbol(), str(cnt))
                cnt += 1 
            bin_loc = format(int(sm.GetAddress(p.symbol())), f'0{16}b')
        hackFile.write(bin_loc + "\n")

    elif p.commandType() == 'C_COMMAND':
        # dest=comp;jump 
        # 1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3 

        c_hack = '111' 
        cmp = code_1.comp(p.comp())
        if cmp == None:
            c_hack += '0000000'
        else:
            c_hack += cmp 

        dest = code_1.dest(p.dest())
        if dest == None:
            c_hack += '000'
        else: 
            c_hack += dest 

        jump = code_1.jump(p.jump())
        if jump == None:
            c_hack += '000' 
        else: 
            c_hack += jump 

        hackFile.write(c_hack + '\n') 


hackFile.close() 

