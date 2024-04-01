
                // pushes the constant 20 to the stack
                @20
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1 
                
                // pushes the constant 20 to the stack
                @20
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1 
                
                // get the top two value of the stack
                @SP
                A=M-1
                D=M
                @R14 
                M=D
                @SP 
                M=M-1 
                A=M-1
                D=M 
                @R13 
                M=D 

                // perform the comparision operation
                @R13 
                D=M 
                @R14
                D=D-M 
              
                @IF 
                D;JEQ
                D=0
                @RES
                0;JMP

                (IF)
                D=-1
               
                // store the result on the stack
            (RES)
                @SP
                A=M-1 
                M=D 
                