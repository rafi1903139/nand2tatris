
        // initializing bootstrap code
            @256
            D=A
            @SP
            M=D
            
        // function Sys.init called
        // push return address
                @Sys.init$ret.0
                D=A
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        
        
        // push LCL
                @LCL
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push ARG
                @ARG
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push THIS
                @THIS
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push THAT
                @THAT
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // ARG = SP - 5 - nArgs
                @SP
                D=M
                @R13
                M=D

                @5
                D=A
                @R13
                M=M-D
                D=M
                
                @ARG
                M=D
        
        // LCL=SP
                @SP
                D=M
                @LCL
                M=D
        
        // goto Sys.init
            
            // goto the specified location Sys.init
                @Sys.init
                0;JMP
            

        // return address 
            
            // specifying a label Sys.init$ret.0
                (Sys.init$ret.0)
            

        
        
            (Sys.init)

            // initialize local variable 
            // repeat 0 times and push 0 to the stack
            @0
            D=A
            @R13
            M=D

            (Sys.init$LOOP)
    
            @R13
            D=M
            @Sys.init$ENDLOOP
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
            @Sys.init$LOOP
            0;JMP

            (Sys.init$ENDLOOP)

            // function Sys.init execution starts
            
                    // pushes the constant 4 to the stack
                    @4
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
        // function Main.fibonacci called
        // push return address
                @Main.fibonacci$ret.1
                D=A
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        
        
        // push LCL
                @LCL
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push ARG
                @ARG
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push THIS
                @THIS
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push THAT
                @THAT
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // ARG = SP - 5 - nArgs
                @SP
                D=M
                @R13
                M=D

                @6
                D=A
                @R13
                M=M-D
                D=M
                
                @ARG
                M=D
        
        // LCL=SP
                @SP
                D=M
                @LCL
                M=D
        
        // goto Main.fibonacci
            
            // goto the specified location Main.fibonacci
                @Main.fibonacci
                0;JMP
            

        // return address 
            
            // specifying a label Main.fibonacci$ret.1
                (Main.fibonacci$ret.1)
            

        
            // specifying a label Sys.END
                (Sys.END)
            
            // goto the specified location Sys.END
                @Sys.END
                0;JMP
            
            (Main.fibonacci)

            // initialize local variable 
            // repeat 0 times and push 0 to the stack
            @0
            D=A
            @R13
            M=D

            (Main.fibonacci$LOOP)
    
            @R13
            D=M
            @Main.fibonacci$ENDLOOP
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
            @Main.fibonacci$LOOP
            0;JMP

            (Main.fibonacci$ENDLOOP)

            // function Main.fibonacci execution starts
            
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
                    D;JLT
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
                     
        // goto the Main.N_LT_2 if stack top value is not zero

                // pop value from stack
                @SP
                M=M-1
                A=M
                D=M

                // check the condion if true then jump
                @Main.N_LT_2
                D;JNE
            
            // goto the specified location Main.N_GE_2
                @Main.N_GE_2
                0;JMP
            
            // specifying a label Main.N_LT_2
                (Main.N_LT_2)
            
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
        
            // specifying a label Main.N_GE_2
                (Main.N_GE_2)
            
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
                
        // function Main.fibonacci called
        // push return address
                @Main.fibonacci$ret.3
                D=A
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        
        
        // push LCL
                @LCL
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push ARG
                @ARG
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push THIS
                @THIS
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push THAT
                @THAT
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // ARG = SP - 5 - nArgs
                @SP
                D=M
                @R13
                M=D

                @6
                D=A
                @R13
                M=M-D
                D=M
                
                @ARG
                M=D
        
        // LCL=SP
                @SP
                D=M
                @LCL
                M=D
        
        // goto Main.fibonacci
            
            // goto the specified location Main.fibonacci
                @Main.fibonacci
                0;JMP
            

        // return address 
            
            // specifying a label Main.fibonacci$ret.3
                (Main.fibonacci$ret.3)
            

        
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
                
        // function Main.fibonacci called
        // push return address
                @Main.fibonacci$ret.4
                D=A
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        
        
        // push LCL
                @LCL
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push ARG
                @ARG
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push THIS
                @THIS
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // push THAT
                @THAT
                D=M
                
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        

        // ARG = SP - 5 - nArgs
                @SP
                D=M
                @R13
                M=D

                @6
                D=A
                @R13
                M=M-D
                D=M
                
                @ARG
                M=D
        
        // LCL=SP
                @SP
                D=M
                @LCL
                M=D
        
        // goto Main.fibonacci
            
            // goto the specified location Main.fibonacci
                @Main.fibonacci
                0;JMP
            

        // return address 
            
            // specifying a label Main.fibonacci$ret.4
                (Main.fibonacci$ret.4)
            

        
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
        