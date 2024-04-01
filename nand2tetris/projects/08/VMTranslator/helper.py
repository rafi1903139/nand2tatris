
class Helper:
    def __init__(self):
        # initialize a counter 
        self.cnt = 0

        self.mem_segments = {
            'local': 'LCL',
            'argument': 'ARG',
            'this': 'THIS',
            'that': 'THAT',
            'temp': 'R5',
            'pointer': 'R3',
            'static': 'R16'
        }

        # arithmatich and logical operations
        self.alo_symbols = {
            'add': '+',
            'sub': '-',
            'neg': '-',
            'eq': 'JEQ',
            'and': '&',
            'or': '|',
            'gt': 'JGT',
            'lt': 'JLT',
            'not': '!',
        }

               

    def push(self, arg1, arg2, fileName):
        cmd = ''
        staticLabel = fileName + "." + str(arg2) 
        if arg1 == 'constant' or arg1 == 'static':
            cmd += f"""
                    // pushes the constant {arg2} to the stack
                    @{arg2 if arg1 == 'constant' else staticLabel}
                    D={'A' if arg1 == 'constant' else 'M'}
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1 
                    """

        else :
            if arg1 not in self.mem_segments:
                return None
            cmd += f"""
                    // push {arg1}[{arg2}] to the stack
                    @{self.mem_segments[arg1]}
                    D={'M' if arg1 != 'temp' and arg1 != 'pointer' else 'A'} 
                    @{arg2}
                    D=D+A 
                    A=D 
                    D=M 
                    @SP 
                    A=M 
                    M=D 
                    @SP 
                    M=M+1
                    """ 
        return cmd

    def pop(self, arg1, arg2, fileName):
        cmd = ''
        staticLabel = fileName + "." + str(arg2)

        if arg1 not in self.mem_segments:
            return None 
        elif arg1 == 'static':
            cmd += f"""
            // pop the top value from the statck and store it in {fileName}.{arg2}
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @{staticLabel}
                    M=D
            """
        else:
            cmd += f"""
                    // pop and store in the {arg1}[{arg2}] from stack 
                    @SP 
                    A=M-1
                    D=M 
                    @R13
                    M=D
                    @SP 
                    M=M-1
                    @{self.mem_segments[arg1]}
                    D={'M' if arg1 != 'temp' and arg1 != 'pointer' else 'A'} 
                    @{arg2}
                    D=D+A
                    @R14
                    M=D
                    @R13 
                    D=M 
                    @R14
                    A=M
                    M=D 
                    """

        return cmd

    def arithmatic(self, command):
        cmd = ''
        if command == 'add' or command == 'sub':
            cmd += f"""
                // get the top two value of the stack and perform {command}
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
                D=D{self.alo_symbols[command]}M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                """
        elif command == 'neg':
            cmd += f"""
                // get the top value of the stack and perform {command}
                @SP
                A=M-1
                D=M
                @R14 
                M=D
                // perform the arithmetic operation
                
                D={self.alo_symbols[command]}M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                """ 
        return cmd

    def logical(self, command):
        cmd = ''
        if command == 'or' or command == 'and':
                cmd += f"""
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
                    D=D{self.alo_symbols[command]}M 

                    // store the result on the stack
                    @SP
                    A=M-1 
                    M=D 
                    """
        elif command == 'not':
            cmd += f"""
                // get the top value of the stack
                @SP
                A=M-1
                D=M
                @R14 
                M=D
                // perform the arithmetic operation
                
                D={self.alo_symbols[command]}M 

                // store the result on the stack
                @SP
                A=M-1 
                M=D 
                """ 
        return cmd


    def compare(self, command):
            cmd = f"""
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
                
                    @IF{self.cnt} 
                    D;{self.alo_symbols[command]}
                    D=0
                    @RES{self.cnt}
                    0;JMP

                    (IF{self.cnt})
                    D=-1
                
                    // store the result on the stack
                (RES{self.cnt})
                    @SP
                    A=M-1 
                    M=D 
                    """
            self.cnt += 1 
            return cmd

    def getLabel(self, label):
        cmd = f"""
            // specifying a label {label}
                ({label})
            """
        return cmd     

    def getGoto(self, label):
        cmd = f"""
            // goto the specified location {label}
                @{label}
                0;JMP
            """
        return cmd
    
    def getIfGoto(self, label):
        cmd = f""" 
        // goto the {label} if stack top value is not zero

                // pop value from stack
                @SP
                M=M-1
                A=M
                D=M

                // check the condion if true then jump
                @{label}
                D;JNE
            """
        return cmd

    def getFunction(self, functionLabel, nVars):
        
        cmd = f"""
            ({functionLabel})

            // initialize local variable 
            // repeat {nVars} times and push 0 to the stack
            @{nVars}
            D=A
            @R13
            M=D

            ({functionLabel + "$LOOP"})
    
            @R13
            D=M
            @{functionLabel + "$ENDLOOP"}
            D;JEQ

            {self.push("constant", 0, "test101")}
            
            @R13
            M=M-1
            @{functionLabel + "$LOOP"}
            0;JMP

            ({functionLabel + "$ENDLOOP"})

            // function {functionLabel} execution starts
            """
        return cmd
    
    def getFunctionCall(self, functionLabel, nArgs):

        returnAddressLabel = functionLabel + "$ret." + str(self.cnt)
        self.cnt += 1 
        diff = int(nArgs) + 5

        cmd = f"""
        // function {functionLabel} called
        // push return address
                @{returnAddressLabel}
                D=A
                {self.pushSegment()}
        
        // push LCL
                @LCL
                D=M
                {self.pushSegment()}

        // push ARG
                @ARG
                D=M
                {self.pushSegment()}

        // push THIS
                @THIS
                D=M
                {self.pushSegment()}

        // push THAT
                @THAT
                D=M
                {self.pushSegment()}

        // ARG = SP - 5 - nArgs
                @SP
                D=M
                @R13
                M=D

                @{diff}
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
        
        // goto {functionLabel}
            {self.getGoto(functionLabel)}

        // return address 
            {self.getLabel(returnAddressLabel)}

        """ 
        return cmd

    def pushSegment(self):
        cmd = f"""
            // pushes the value stored in D register into the stack
            @SP
            A=M
            M=D

            @SP
            M=M+1

        """
        return cmd

    def getReturn(self):
        cmd = f"""
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
           {self.getSegment(1,'THAT')} 

            // THIS  = *(endFrame - 2)
            {self.getSegment(2, 'THIS')} 

            // ARG = *(endFrame - 3)
            {self.getSegment(3, 'ARG')} 

            // LCL = *(endFrame - 4)
            {self.getSegment(4, 'LCL')} 

            // goto return address
            @R14
            A=M
            0;JMP
        """
        return cmd
    
    def getSegment(self, index, segment):
        cmd = f"""
        // {segment} = *(endFrame - {index})
            @R13
            A=M
            D=M
            @{index}
            A=D-A
            D=M
            @{segment}
            M=D
            """
        return cmd

    def getBootstrap(self):
        cmd = f"""
        // initializing bootstrap code
            @256
            D=A
            @SP
            M=D
            {self.getFunctionCall('Sys.init', 0)}
        """
        return cmd