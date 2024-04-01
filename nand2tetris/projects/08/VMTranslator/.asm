
            // get the top two value of the stack
            @SP
            A=M
            D=M
            @R13 
            M=D
            @SP 
            M=M-1 
            A=M 
            D=M 
            @R13 
            M=D 
            @SP 

            // perform the arithmetic operation
            @R13 
            D=M 
            @R14
            D=D+M 

            // store the result on the stack
            @SP
            A=M 
            M=D 
            @SP 
            M=M+1 
            
            // get the top two value of the stack
            @SP
            A=M
            D=M
            @R13 
            M=D
            @SP 
            M=M-1 
            A=M 
            D=M 
            @R13 
            M=D 
            @SP 

            // perform the arithmetic operation
            @R13 
            D=M 
            @R14
            D=D-M 

            // store the result on the stack
            @SP
            A=M 
            M=D 
            @SP 
            M=M+1 
            
            // get the top two value of the stack
            @SP
            A=M
            D=M
            @R13 
            M=D
            @SP 
            M=M-1 
            A=M 
            D=M 
            @R13 
            M=D 
            @SP 

            // perform the arithmetic operation
            @R13 
            D=M 
            @R14
            D=D+M 

            // store the result on the stack
            @SP
            A=M 
            M=D 
            @SP 
            M=M+1 
            
            // get the top two value of the stack
            @SP
            A=M
            D=M
            @R13 
            M=D
            @SP 
            M=M-1 
            A=M 
            D=M 
            @R13 
            M=D 
            @SP 

            // perform the arithmetic operation
            @R13 
            D=M 
            @R14
            D=D-M 

            // store the result on the stack
            @SP
            A=M 
            M=D 
            @SP 
            M=M+1 
            
            // get the top two value of the stack
            @SP
            A=M
            D=M
            @R13 
            M=D
            @SP 
            M=M-1 
            A=M 
            D=M 
            @R13 
            M=D 
            @SP 

            // perform the arithmetic operation
            @R13 
            D=M 
            @R14
            D=D+M 

            // store the result on the stack
            @SP
            A=M 
            M=D 
            @SP 
            M=M+1 
            