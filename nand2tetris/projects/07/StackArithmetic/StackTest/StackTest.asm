
                    // pushes the constant 17 to the stack
                    @17
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 17 to the stack
                    @17
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
                
                    @IF0 
                    D;JEQ
                    D=0
                    @RES0
                    0;JMP

                    (IF0)
                    D=-1
                
                    // store the result on the stack
                (RES0)
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 17 to the stack
                    @17
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 16 to the stack
                    @16
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
                
                    @IF1 
                    D;JEQ
                    D=0
                    @RES1
                    0;JMP

                    (IF1)
                    D=-1
                
                    // store the result on the stack
                (RES1)
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 16 to the stack
                    @16
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 17 to the stack
                    @17
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
                
                    @IF2 
                    D;JEQ
                    D=0
                    @RES2
                    0;JMP

                    (IF2)
                    D=-1
                
                    // store the result on the stack
                (RES2)
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 892 to the stack
                    @892
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 891 to the stack
                    @891
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
                
                    @IF3 
                    D;JLT
                    D=0
                    @RES3
                    0;JMP

                    (IF3)
                    D=-1
                
                    // store the result on the stack
                (RES3)
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 891 to the stack
                    @891
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 892 to the stack
                    @892
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
                
                    @IF4 
                    D;JLT
                    D=0
                    @RES4
                    0;JMP

                    (IF4)
                    D=-1
                
                    // store the result on the stack
                (RES4)
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 891 to the stack
                    @891
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 891 to the stack
                    @891
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
                
                    @IF5 
                    D;JLT
                    D=0
                    @RES5
                    0;JMP

                    (IF5)
                    D=-1
                
                    // store the result on the stack
                (RES5)
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 32767 to the stack
                    @32767
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 32766 to the stack
                    @32766
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
                
                    @IF6 
                    D;JGT
                    D=0
                    @RES6
                    0;JMP

                    (IF6)
                    D=-1
                
                    // store the result on the stack
                (RES6)
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 32766 to the stack
                    @32766
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 32767 to the stack
                    @32767
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
                
                    @IF7 
                    D;JGT
                    D=0
                    @RES7
                    0;JMP

                    (IF7)
                    D=-1
                
                    // store the result on the stack
                (RES7)
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 32766 to the stack
                    @32766
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 32766 to the stack
                    @32766
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
                
                    @IF8 
                    D;JGT
                    D=0
                    @RES8
                    0;JMP

                    (IF8)
                    D=-1
                
                    // store the result on the stack
                (RES8)
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 57 to the stack
                    @57
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 31 to the stack
                    @31
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 53 to the stack
                    @53
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                // get the top two value of the stack and perform add
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

                // perform the arithmetic operation
                @R13 
                D=M 
                @R14
                D=D+M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                
                    // pushes the constant 112 to the stack
                    @112
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                // get the top two value of the stack and perform sub
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

                // perform the arithmetic operation
                @R13 
                D=M 
                @R14
                D=D-M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                
                // get the top value of the stack and perform neg
                @SP
                A=M-1
                D=M
                @R14 
                M=D
                // perform the arithmetic operation
                
                D=-M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                
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

                    // perform the arithmetic operation
                    @R13 
                    D=M 
                    @R14
                    D=D&M 

                    // store the result on the stack
                    @SP
                    A=M-1 
                    M=D 
                    
                    // pushes the constant 82 to the stack
                    @82
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

                    // perform the arithmetic operation
                    @R13 
                    D=M 
                    @R14
                    D=D|M 

                    // store the result on the stack
                    @SP
                    A=M-1 
                    M=D 
                    
                // get the top value of the stack
                @SP
                A=M-1
                D=M
                @R14 
                M=D
                // perform the arithmetic operation
                
                D=!M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                