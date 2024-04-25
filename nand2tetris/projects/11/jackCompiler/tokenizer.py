from constant import *


class Tokenizer:
    def __init__(self, file_name):
        try:
            self.file = open(file_name, 'r') 
            self.command = ''
            self._tokens = []
            self.currentToken = None 

            self.buildToken()
            
            print("File opened Successfully")

        except:
            print("Couldn't open file") 
    
    def buildToken(self):
        while self.hasMoreLines():
            self.nextLine()
            for temp in self.command:
                self._tokens.append(temp)
            
            
    def hasMoreLines(self):
        # Check if there more tokens in the input 
    
        current_position = self.file.tell() 
        self.file.seek(0, 2) # end of file 
        end_posiiton = self.file.tell() 
        self.file.seek(current_position) 

        return current_position != end_posiiton 

    def nextLine(self):
        self.command = self.file.readline()

        self.command = self.command.strip()
        while self.hasMoreLines() and (self.command[0:2] == '//' or self.command == '\n' or self.command =='' or not self.command):
            self.command = self.file.readline() 
            self.command = self.command.strip()


        if '//' in self.command:
            self.command = self.command[0:self.command.find("//")]
            self.command = self.command.strip()
        
        # testing purpose
        if '/*' in self.command:
            temp = self.command[self.command.find('/*') + 2: ]
            self.command = self.command[0:self.command.find('/*')]
            self.command.strip()

            while self.hasMoreLines() and '*/' not in temp:
                temp = self.file.readline()
            self.command = temp[temp.find('*/') + 2:]
            self.command.strip()

        self.command = self.command.split(' ')
        self.command = [str.strip() for str in self.command if str.strip() != '']
        

    def hasMoreToken(self):
        return len(self._tokens) > 0
    
    def advance(self):
        # gets next token and makes it the current token
        if not self.hasMoreToken():
            print("No more token left")
            return 
        
        
        
        isTokenSet = False
        tempToken = self._tokens[0]
        
        if tempToken == '' or tempToken == '\n':
            self._tokens = self._tokens[1:]
            tempToken = self._tokens[0]

        tempStr = ""
        if tempToken[0] == '\"':
            self.isStrConst = True
            self._tokens[0] = self._tokens[0][1:]
            ptr = 0
            suff = ""
            for i in range(len(self._tokens)):
                ptr = i
                if '\"' in  self._tokens[i]:
                    tempStr += " "
                    tempStr += self._tokens[i][0: self._tokens[i].find('\"')]
                    suff = self._tokens[i][self._tokens[i].find('\"') + 1: ] 
                    break 
                else:
                    tempStr += f" {self._tokens[i]}"

            self._tokens = self._tokens[ptr + 1: ] 
            if suff:
                self._tokens.insert(0, suff)
            self.currentToken = tempStr.strip()

            return
        else:
            self.isStrConst = False


        for i in range(len(tempToken)):
            if tempToken[i] in symbolList:
                pre = tempToken[0:i]
                tok = tempToken[i]
                suff = tempToken[i+1:]
                
                if pre:
                    self.currentToken = pre 
                    self._tokens[0] = tok
                    self._tokens.insert(1, suff)
                else:
                    self.currentToken = tok
                    if suff and suff != '\n':
                        self._tokens[0] = suff
                    else:
                        self._tokens = self._tokens[1:]

                isTokenSet = True
                break

        if not isTokenSet:
            self.currentToken = self._tokens[0]
            self._tokens = self._tokens[1:]


    def tokenType(self):
        # returns the current tokentype as constant
        if self.currentToken == None:
            return None 
        else:
            if self.currentToken in symbolList:
                return SYMBOL 
            elif self.currentToken in keywordList:
                return KEYWORD 
            elif self.currentToken.isdigit():
                val = int(self.currentToken)
                if val >= 0 and val <= 32767:
                    return INT_CONST 
                else:
                    print("value not in range")
                    return None 
            elif self.isStrConst:
                return STRING_CONST 
            elif not self.currentToken[0].isdigit():
                return IDENTIFIER
            else:
                print("Not matched to any token type")
                return None




