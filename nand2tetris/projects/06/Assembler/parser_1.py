class Parser:
    def __init__(self, file_name):
        try:
            self.file = open(file_name, 'r') 
            print("File opened Successfully")

        except:
            print("Couldn't open file") 
            
            
    def hasMoreCommnads(self):
        # Check if there more commands in the input 
    
        current_position = self.file.tell() 
        self.file.seek(0, 2) # end of file 
        end_posiiton = self.file.tell() 
        self.file.seek(current_position) 

        return current_position != end_posiiton 

    def advance(self):
        self.command = self.file.readline()

        self.command = self.command.strip().replace(' ', '')
        while self.hasMoreCommnads() and (self.command[0:2] == '//' or self.command == '\n' or self.command =='' or not self.command):
            self.command = self.file.readline() 
            self.command = self.command.strip().replace(' ', '')


        if '//' in self.command:
            self.command = self.command[0:self.command.find("//")]

        

    def commandType(self):
        flag = self.command
        if not flag:
            print("Empty line")
            return
        
        if flag[0] == '@':
            return 'A_COMMAND' 
        elif flag[0] == '(' and flag[-1] == ')':
            return 'L_COMMAND' 
        elif flag[0] == 'A' or flag[0] == 'M' or flag[0] == 'D' or flag[0] == '0':
            return 'C_COMMAND' 
        else:
            return "Invalid command" 


    def symbol(self):
        
        if self.commandType() == "A_COMMAND":
            return self.command[1:].strip()
        elif self.commandType() == "L_COMMAND":
            return self.command[1:-1].strip()
        else:
            return None 

    def dest(self): 
        cmd = self.command 
        if self.commandType() == "C_COMMAND":
            if '=' in cmd:
                return cmd.split('=')[0].strip()
            else:
                return 'null' 

    def comp(self):
        cmd = self.command 
        
        if self.commandType() == "C_COMMAND":
            start_index = cmd.find('=') 
            end_index = cmd.find(';') 

            if start_index == -1:
                start_index = 0 
            else: 
                start_index += 1

            if end_index == -1:
                return cmd[start_index: ].strip()
            else:
                return cmd[start_index:end_index].strip()

    def jump(self):
        
        cmd = self.command
        if self.commandType() == "C_COMMAND": 
            if ';' in cmd:
                return cmd[cmd.find(';')+1: ].strip()
