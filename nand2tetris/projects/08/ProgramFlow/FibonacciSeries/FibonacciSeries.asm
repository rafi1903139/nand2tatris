
        // initializing bootstrap code
            @256
            D=A
            @SP
            M=D
        
                    // push argument[1] to the stack
                    @ARG
                    D=M 
                    @1
                    D=D+A 
                    A=D 
                    D=M 
                    @SP 
                    A=M 
                    M=D 
                    @SP 
                    M=M+1
                    
                    // pop and store in the pointer[1] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @R3
                    D=A 
                    @1
                    D=D+A
                    @R14
                    M=D
                    @R13 
                    D=M 
                    @R14
                    A=M
                    M=D 
                    
                    // pushes the constant 0 to the stack
                    @0
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pop and store in the that[0] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @THAT
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
                    
                    // pushes the constant 1 to the stack
                    @1
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pop and store in the that[1] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @THAT
                    D=M 
                    @1
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
                    
                    // pushes the constant 2 to the stack
                    @2
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
                    
            // specifying a label FibonacciSeries.LOOP
                (FibonacciSeries.LOOP)
            
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
                     
        // goto the FibonacciSeries.COMPUTE_ELEMENT if stack top value is not zero

                // pop value from stack
                @SP
                M=M-1
                A=M
                D=M

                // check the condion if true then jump
                @FibonacciSeries.COMPUTE_ELEMENT
                D;JNE
            
            // goto the specified location FibonacciSeries.END
                @FibonacciSeries.END
                0;JMP
            
            // specifying a label FibonacciSeries.COMPUTE_ELEMENT
                (FibonacciSeries.COMPUTE_ELEMENT)
            
                    // push that[0] to the stack
                    @THAT
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
                    
                    // push that[1] to the stack
                    @THAT
                    D=M 
                    @1
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
                
                    // pop and store in the that[2] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @THAT
                    D=M 
                    @2
                    D=D+A
                    @R14
                    M=D
                    @R13 
                    D=M 
                    @R14
                    A=M
                    M=D 
                    
                    // push pointer[1] to the stack
                    @R3
                    D=A 
                    @1
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
                
                    // pop and store in the pointer[1] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @R3
                    D=A 
                    @1
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
                    
            // goto the specified location FibonacciSeries.LOOP
                @FibonacciSeries.LOOP
                0;JMP
            
            // specifying a label FibonacciSeries.END
                (FibonacciSeries.END)
            