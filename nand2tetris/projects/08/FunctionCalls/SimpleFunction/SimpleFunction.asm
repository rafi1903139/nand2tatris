
        // initializing bootstrap code
            @256
            D=A
            @SP
            M=D
        
            (SimpleFunction.SimpleFunction.test)

            // initialize local variable 
            // repeat 2 times and push 0 to the stack
            @2
            D=A
            @R13
            M=D

            (SimpleFunction.SimpleFunction.test$LOOP)
    
            @R13
            D=M
            @SimpleFunction.SimpleFunction.test$ENDLOOP
            D;JEQ

            
                    // pushes the constant 0 to the stack
                    @0
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
            
            @R13
            M=M-1
            @SimpleFunction.SimpleFunction.test$LOOP
            0;JMP

            (SimpleFunction.SimpleFunction.test$ENDLOOP)

            // function SimpleFunction.SimpleFunction.test execution starts
            
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
                    
                    // push local[1] to the stack
                    @LCL
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
                
            // initiate return 

            // endFrame = LCL
            @LCL
            D=A
            @R13
            M=D

            // R14 = return address
            @R13 // pointing to LCL
            A=M // poiting to the value LCL contains
            D=M
            @5
            D=D-A
            A=D
            D=M
            @R14
            M=D

            // *ARG = POP()
            @SP
            A=M-1
            D=M
            @ARG
            A=M
            M=D

            // SP = ARG + 1
            D=A
            @SP
            M=D+1

            // THAT = *(endFrame -1)
           
        // THAT = *(endFrame - 1)
            @R13
            A=M
            D=M
            @1
            A=D-A
            D=M
            @THAT
            M=D
             

            // THIS  = *(endFrame - 2)
            
        // THIS = *(endFrame - 2)
            @R13
            A=M
            D=M
            @2
            A=D-A
            D=M
            @THIS
            M=D
             

            // ARG = *(endFrame - 3)
            
        // ARG = *(endFrame - 3)
            @R13
            A=M
            D=M
            @3
            A=D-A
            D=M
            @ARG
            M=D
             

            // LCL = *(endFrame - 4)
            
        // LCL = *(endFrame - 4)
            @R13
            A=M
            D=M
            @4
            A=D-A
            D=M
            @LCL
            M=D
             

            // goto return address
            @R14
            A=M
            0;JMP
        