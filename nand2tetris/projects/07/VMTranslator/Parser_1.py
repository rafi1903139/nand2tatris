import constant as ct



class Parser:
    def __init__(self, file_name):
        try:
            self.file = open(file_name, 'r') 
            print("File opened Successfully")

        except:
            print("Couldn't open file") 
            
            
    def hasMoreLines(self):
        # Check if there more commands in the input 
    
        current_position = self.file.tell() 
        self.file.seek(0, 2) # end of file 
        end_posiiton = self.file.tell() 
        self.file.seek(current_position) 

        return current_position != end_posiiton 

    def advance(self):
        self.command = self.file.readline()

        self.command = self.command.strip()
        while self.hasMoreLines() and (self.command[0:2] == '//' or self.command == '\n' or self.command =='' or not self.command):
            self.command = self.file.readline() 
            self.command = self.command.strip()


        if '//' in self.command:
            self.command = self.command[0:self.command.find("//")]
            self.command = self.command.strip()

        self.command = self.command.split(' ')
        self.command = [str for str in self.command if str != '']
        

        self.command = ' '.join(self.command)

    def commandType(self):
        # Return a constant representing the type of the current command 
        
        command = self.command 

        # find the commandtype 

        # check if arithmetic command
        list_arithmetic_commands = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]

        c_a = [cmd for cmd in list_arithmetic_commands if cmd in command] 

        cmdType = command.split()[0]

        if cmdType in c_a:
            return ct.C_ARITHMETIC 
        elif cmdType == 'push':
            return ct.C_PUSH 
        elif cmdType == 'pop':
            return ct.C_POP 
        else:
            print("Invalid command")
            return -1

    def arg1(self):
        # Returns the first agument of the current command
        command = self.command.split(' ')

        if self.commandType() == ct.C_ARITHMETIC:
            if len(command) > 1: 
                print("Invalid arguement for arithmatic command")
                return None 
            return command[0]
        elif self.commandType() == ct.C_RETURN:
            print("for return stateement this should not be called")
            return None 
        
        if len(command) != 3:
            print("Invalid arguments")
            return None 
        
        return command[1]

    def arg2(self):
        # returns the seconds argument of the current command
        cType = self.commandType()
        

        if (cType == ct.C_POP) or (cType == ct.C_PUSH) or (cType == ct.C_FUNCTION) or (cType == ct.C_CALL):
            return int(self.command.split(' ')[2])
        else:
            print("Invalid second argument call")
            return None 


