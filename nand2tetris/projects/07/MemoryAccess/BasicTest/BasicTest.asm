
                // pushes the constant 10 to the stack
                @10
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
            
                // pushes the constant 21 to the stack
                @21
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1 
                
                // pushes the constant 22 to the stack
                @22
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1 
                
            // pop and store in the argument[2] from stack 
            @SP 
            A=M-1
            D=M 
            @R13
            M=D
            @SP 
            M=M-1
            @ARG
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
            
            // pop and store in the argument[1] from stack 
            @SP 
            A=M-1
            D=M 
            @R13
            M=D
            @SP 
            M=M-1
            @ARG
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
            
                // pushes the constant 36 to the stack
                @36
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1 
                
            // pop and store in the this[6] from stack 
            @SP 
            A=M-1
            D=M 
            @R13
            M=D
            @SP 
            M=M-1
            @THIS
            D=M 
            @6
            D=D+A
            @R14
            M=D
            @R13 
            D=M 
            @R14
            A=M
            M=D 
            
                // pushes the constant 42 to the stack
                @42
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1 
                
                // pushes the constant 45 to the stack
                @45
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1 
                
            // pop and store in the that[5] from stack 
            @SP 
            A=M-1
            D=M 
            @R13
            M=D
            @SP 
            M=M-1
            @THAT
            D=M 
            @5
            D=D+A
            @R14
            M=D
            @R13 
            D=M 
            @R14
            A=M
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
            
                // pushes the constant 510 to the stack
                @510
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1 
                
            // pop and store in the temp[6] from stack 
            @SP 
            A=M-1
            D=M 
            @R13
            M=D
            @SP 
            M=M-1
            @R5
            D=A 
            @6
            D=D+A
            @R14
            M=D
            @R13 
            D=M 
            @R14
            A=M
            M=D 
            
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
                
                // push that[5] to the stack
                @THAT
                D=M 
                @5
                D=D+A 
                A=D 
                D=M 
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
                D=D-M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                
                // push this[6] to the stack
                @THIS
                D=M 
                @6
                D=D+A 
                A=D 
                D=M 
                @SP 
                A=M 
                M=D 
                @SP 
                M=M+1
                
                // push this[6] to the stack
                @THIS
                D=M 
                @6
                D=D+A 
                A=D 
                D=M 
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
                D=D+M 

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
                D=D-M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                
                // push temp[6] to the stack
                @R5
                D=A 
                @6
                D=D+A 
                A=D 
                D=M 
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
                D=D+M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                