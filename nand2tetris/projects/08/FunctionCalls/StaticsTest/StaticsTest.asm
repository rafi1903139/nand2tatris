
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
            

        
        
            (Class1.set)

            // initialize local variable 
            // repeat 0 times and push 0 to the stack
            @0
            D=A
            @R13
            M=D

            (Class1.set$LOOP)
    
            @R13
            D=M
            @Class1.set$ENDLOOP
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
            @Class1.set$LOOP
            0;JMP

            (Class1.set$ENDLOOP)

            // function Class1.set execution starts
            
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
                    
            // pop the top value from the statck and store it in Class1.0
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @Class1.0
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
                    
            // pop the top value from the statck and store it in Class1.1
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @Class1.1
                    M=D
            
                    // pushes the constant 0 to the stack
                    @0
                    D=A
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
        
            (Class1.get)

            // initialize local variable 
            // repeat 0 times and push 0 to the stack
            @0
            D=A
            @R13
            M=D

            (Class1.get$LOOP)
    
            @R13
            D=M
            @Class1.get$ENDLOOP
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
            @Class1.get$LOOP
            0;JMP

            (Class1.get$ENDLOOP)

            // function Class1.get execution starts
            
                    // pushes the constant 0 to the stack
                    @Class1.0
                    D=M
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 1 to the stack
                    @Class1.1
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
            
                    // pushes the constant 6 to the stack
                    @6
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 8 to the stack
                    @8
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
        // function Class1.set called
        // push return address
                @Class1.set$ret.1
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

                @7
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
        
        // goto Class1.set
            
            // goto the specified location Class1.set
                @Class1.set
                0;JMP
            

        // return address 
            
            // specifying a label Class1.set$ret.1
                (Class1.set$ret.1)
            

        
                    // pop and store in the temp[0] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @R5
                    D=A 
                    @0
                    D=D+A
                    @R14
                    M=D
                    @R13 
                    D=M 
                    @R14
                    A=M
                    M=D 
                    
                    // pushes the constant 23 to the stack
                    @23
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 15 to the stack
                    @15
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
        // function Class2.set called
        // push return address
                @Class2.set$ret.2
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

                @7
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
        
        // goto Class2.set
            
            // goto the specified location Class2.set
                @Class2.set
                0;JMP
            

        // return address 
            
            // specifying a label Class2.set$ret.2
                (Class2.set$ret.2)
            

        
                    // pop and store in the temp[0] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @R5
                    D=A 
                    @0
                    D=D+A
                    @R14
                    M=D
                    @R13 
                    D=M 
                    @R14
                    A=M
                    M=D 
                    
        // function Class1.get called
        // push return address
                @Class1.get$ret.3
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
        
        // goto Class1.get
            
            // goto the specified location Class1.get
                @Class1.get
                0;JMP
            

        // return address 
            
            // specifying a label Class1.get$ret.3
                (Class1.get$ret.3)
            

        
        // function Class2.get called
        // push return address
                @Class2.get$ret.4
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
        
        // goto Class2.get
            
            // goto the specified location Class2.get
                @Class2.get
                0;JMP
            

        // return address 
            
            // specifying a label Class2.get$ret.4
                (Class2.get$ret.4)
            

        
            // specifying a label Sys.END
                (Sys.END)
            
            // goto the specified location Sys.END
                @Sys.END
                0;JMP
            
            (Class2.set)

            // initialize local variable 
            // repeat 0 times and push 0 to the stack
            @0
            D=A
            @R13
            M=D

            (Class2.set$LOOP)
    
            @R13
            D=M
            @Class2.set$ENDLOOP
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
            @Class2.set$LOOP
            0;JMP

            (Class2.set$ENDLOOP)

            // function Class2.set execution starts
            
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
                    
            // pop the top value from the statck and store it in Class2.0
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @Class2.0
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
                    
            // pop the top value from the statck and store it in Class2.1
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @Class2.1
                    M=D
            
                    // pushes the constant 0 to the stack
                    @0
                    D=A
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
        
            (Class2.get)

            // initialize local variable 
            // repeat 0 times and push 0 to the stack
            @0
            D=A
            @R13
            M=D

            (Class2.get$LOOP)
    
            @R13
            D=M
            @Class2.get$ENDLOOP
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
            @Class2.get$LOOP
            0;JMP

            (Class2.get$ENDLOOP)

            // function Class2.get execution starts
            
                    // pushes the constant 0 to the stack
                    @Class2.0
                    D=M
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    
                    // pushes the constant 1 to the stack
                    @Class2.1
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
        