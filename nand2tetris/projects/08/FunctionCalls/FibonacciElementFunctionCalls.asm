
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
            

        
        