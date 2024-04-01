
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

               

    def push(self, arg1, arg2):
        cmd = ''
        if arg1 == 'constant':
            cmd += f"""
                    // pushes the constant {arg2} to the stack
                    @{arg2}
                    D=A
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

    def pop(self, arg1, arg2):
        cmd = ''
        if arg1 not in self.mem_segments:
            return None 
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

        
