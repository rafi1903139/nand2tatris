
        // initializing bootstrap code
            @256
            D=A
            @SP
            M=D
        
                    // pushes the constant 0 to the stack
                    @0
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pop and store in the local[0] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @LCL
                    D=M 
                    @0
                    D=D+A
                    @R14
                    M=D
                    @R13 
                    D=M 
                    @R14
                    A=M
                    M=D 
                    
            // specifying a label BasicLoop.LOOP
                (BasicLoop.LOOP)
            
                    // push argument[0] to the stack
                    @ARG
                    D=M 
                    @0
                    D=D+A 
                    A=D 
                    D=M 
                    @SP 
                    A=M 
                    M=D 
                    @SP 
                    M=M+1
                    
                    // push local[0] to the stack
                    @LCL
                    D=M 
                    @0
                    D=D+A 
                    A=D 
                    D=M 
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
                
                    // pop and store in the local[0] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @LCL
                    D=M 
                    @0
                    D=D+A
                    @R14
                    M=D
                    @R13 
                    D=M 
                    @R14
                    A=M
                    M=D 
                    
                    // push argument[0] to the stack
                    @ARG
                    D=M 
                    @0
                    D=D+A 
                    A=D 
                    D=M 
                    @SP 
                    A=M 
                    M=D 
                    @SP 
                    M=M+1
                    
                    // pushes the constant 1 to the stack
                    @1
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
                
                    // pop and store in the argument[0] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @ARG
                    D=M 
                    @0
                    D=D+A
                    @R14
                    M=D
                    @R13 
                    D=M 
                    @R14
                    A=M
                    M=D 
                    
                    // push argument[0] to the stack
                    @ARG
                    D=M 
                    @0
                    D=D+A 
                    A=D 
                    D=M 
                    @SP 
                    A=M 
                    M=D 
                    @SP 
                    M=M+1
                     
        // goto the BasicLoop.LOOP if stack top value is not zero

                // pop value from stack
                @SP
                M=M-1
                A=M
                D=M

                // check the condion if true then jump
                @BasicLoop.LOOP
                D;JNE
            
                    // push local[0] to the stack
                    @LCL
                    D=M 
                    @0
                    D=D+A 
                    A=D 
                    D=M 
                    @SP 
                    A=M 
                    M=D 
                    @SP 
                    M=M+1
                    