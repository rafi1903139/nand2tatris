from tokenizer import *
from constant import *

class CompilationEngine:
    
    def __init__(self, fileName):
       self.tokenizer = Tokenizer(fileName) 
       self.file = open(f"{fileName.split('.')[0]}.xml", "w")

       token = self.getToken()
       if token == 'class':
           self.compileClass()
       else:
           print("No class to compile")
           
    
    def compileClass(self):
        xmlOutput = "<class>\n"
        xmlOutput += f"\t{self.writeKeyword('class')}"


        className = self.getToken()

        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += self.writeIdentifier(className)

        else:
            print("Invalid className")
            return 
        
        curlyBrace = self.getToken()

        if curlyBrace == '{':
            xmlOutput += self.writeSymbol(curlyBrace)
        else:
            print("Missing curly braces")
            return 
        
        self.file.write(xmlOutput)

        while self.tokenizer.hasMoreToken and self.tokenizer.currentToken != "}":
            currentToken = self.getToken()
            if currentToken == 'staic' or currentToken == 'field':
                self.compileClassVarDec()
            elif currentToken == 'constructor' or currentToken == 'function' or currentToken == 'method':
                self.compileSubroutine()
            else:
                print("Invalid format in class declaration")
                return 
        
        if self.tokenizer.currentToken == '}':
            self.file.write(self.writeSymbol('}'))
        else:
            print("Missing ending curly braces for class")
        
        self.file.write("</class>\n")


    def compileClassVarDec(self):
        pass 

    def compileSubroutine(self):
        xmlOutput = "<subroutineDec>\n"

        xmlOutput += self.writeKeyword(self.tokenizer.currentToken)

        # get the subroutine type
        token = self.getToken()

        if self.isType():
            if self.tokenizer.tokenType() == IDENTIFIER:
                xmlOutput += self.writeIdentifier(token)
            else: 
                xmlOutput += self.writeKeyword(token)
        elif token == 'void':
            xmlOutput += self.writeKeyword(token)
        else:
            print("invalid type")
            return 
        
        # get the subroutine name 
        token = self.getToken()

        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += self.writeIdentifier(token)
        else:
            print("Invalid subroutine name")
            return 
        
        # get opening brace
        token = self.getToken()

        if token == '(':
            xmlOutput += self.writeKeyword(token)
        else:
            print("Missing opening brace")
            return 
        
        self.file.write(xmlOutput)

        self.compileParameterList()        

        # get closing brace 
        if self.tokenizer.currentToken == ')':
            self.file.write(self.writeSymbol(')'))
        else:
            print("Missing closing braces in parameter list")
            return 
        
        self.compileSubroutineBody() 

        self.file.write("</subroutineDec>\n")
    

    def compileParameterList(self):
        # ((type varName) (',' varName)*)?
        xmlOutput = ""
        
        # get type 
        token = self.getToken()
        
        if self.isType():
            xmlOutput += f"\t{self.generateType()}"
        else:
            # no parameter found
            return 
        
        # get varName 
        token = self.getToken() 

        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += f"\t{self.writeIdentifier(token)}"
        else:
            print("invalid identifier in parameterlist")
            return 
        

        # get next token and decide 
        token = self.getToken() 

        while self.tokenizer.hasMoreToken() and token != ')' and token == ',':
            xmlOutput += f"\t{self.writeSymbol(token)}"

            # get type
            token = self.getToken()
            
            if self.isType():
                xmlOutput += f"\t{self.generateType()}"
            else:
                print("Invalid type in parameterlist")
                return

            # get varName 
            token = self.getToken() 

            if self.tokenizer.tokenType() == IDENTIFIER:
                xmlOutput += f"\t{self.writeIdentifier(token)}"
            else:
                print("invalid varName in parameterlist")
                return  

            # get next token and decide 
            token = self.getToken()
        

        self.file.write(xmlOutput)


    def compileSubroutineBody(self):

        # '{' varDec* statements '}' 

        # get opening curly brace
        token = self.getToken()
        xmlOutput = "\t<subroutineBody>\n"

        if token == '{':
            xmlOutput += self.writeSymbol(token)
        else:
            print('Missing opening curly brace in subrouting body')
            return 
        
        self.file.write(xmlOutput)

        xmlOutput = ""
        
        # get varDec*
        # 'var' type varName(',' varName)* ';' 

        # get token and decide
        token = self.getToken()
        while self.tokenizer.hasMoreToken() and self.tokenizer.currentToken == 'var':
            self.compileVarDec()
        
        # process statements
        self.compileStatements()

        # process closing curly braces
        if self.tokenizer.currentToken == '}':
            self.file.write(self.writeSymbol('}'))
        else:
            print("Missing closing curly braces for subroutine body")
            return 
        
        self.file.write("\t</subroutineBody>\n")

    def compileVarDec(self):
        # 'var' type varName(',' varName)*';'
        xmlOutput = "\t<varDec>\n"
        xmlOutput += f"\t{self.writeKeyword('var')}"

        # get type
        token = self.getToken() 

        if self.isType():
            xmlOutput += f"\t{self.generateType()}" 
        else:
            print("Missing type")
            return  

        # get varName 
        token = self.getToken() 
        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += f"\t{self.writeIdentifier(token)}" 
        else:
            print("Missing variable name in varDec")
            return 

        # get token and decide 
        token = self.getToken() 
        while self.tokenizer.hasMoreToken() and token != ';' and token == ',':
            xmlOutput += f"\t{self.writeSymbol(token)}" 
            # get identifier 
            token = self.getToken() 
            if self.tokenizer.tokenType() == IDENTIFIER:
                xmlOutput += f"\t{self.writeIdentifier(token)}"
            else:
                print("Invalid identifier in varDec")
                return

            # get the next token
            token = self.getToken()
        
        if token != ';':
            print("Missing ; after varDec")
            return 
        else:
            xmlOutput += f'\t{self.writeSymbol(token)}'
        
        xmlOutput += '\t</varDec>\n'
    
        self.getToken()
        self.file.write(xmlOutput)

    def compileStatements(self):

        if not self.isStatement():
            return 
        
        xmlOutput = "\t<statements\n>"

        self.file.write(xmlOutput)

        while self.tokenizer.hasMoreToken() and self.isStatement():
            token = self.tokenizer.currentToken 
            
            if token == 'let':
                self.compileLet()  
            elif token == 'if':
                self.compileIf() 
            elif token == 'while':
                self.compileWhile() 
            elif token == 'do':
                self.compileDo() 
            elif token == 'return':
                self.compileReturn 

            # get the next token and decide 
            self.getToken() 

        xmlOutput = "\t</statements>\n"
        self.file.write(xmlOutput)

    def compileLet(self):
        # 'let' varName ('[' expression ']')? '=' expression';'

        xmlOutput = "\t\t<letStatement>\n"
        xmlOutput += f"\t\t\t{self.writeKeyword(self.tokenizer.currentToken)}"

        # get varName 
        token = self.getToken()

        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += f"\t\t\t{self.writeIdentifier(token)}"
        else:
            print("Missing identifier in let statment")
        
        self.file.write(xmlOutput)

        # get expression 
        token = self.getToken()
        # process expression 
        #TODO

        # get '=' 
        
        if self.tokenizer.currentToken == '=':
            xmlOutput = f"\t\t\t{self.writeSymbol(token)}"
            self.file.write(xmlOutput)
        else:
            print("Missing = in letStatemtn")
            return 
        
        # get expression 
        token = self.getToken() 
        # process expression 
        # TODO 
        self.compileExpression()

        # get ';' 
        if self.tokenizer.currentToken == ';':
            xmlOutput = f"\t\t\t{self.writeSymbol(self.tokenizer.currentToken)}"
        else:
            print("Missing ; in let statement")
            return

        xmlOutput += "\t</letStatement>\n"

        self.file.write(xmlOutput) 

    def compileIf(self):
        pass 

    def compileWhile(self):
        pass

    def compileDo(self):
        pass 

    def compileReturn(self):
        pass 

    def compileExpression(self):
       
        xmlOutput = "\t<expression>\n"

        self.file.write(xmlOutput)

        self.compileTerm() 

        token = self.getToken()
        while self.isOperator():
            self.compileTerm() 
        

        xmlOutput ="\t</expression>\n"
        self.file.write(xmlOutput)       

        pass 

    def compileTerm(self):
        
        xmlOutput = "\t\t<term>\n"
        token = self.tokenizer.currentToken 
        tokenType = self.tokenizer.tokenType() 

        if tokenType == INT_CONST:
            xmlOutput += f"\t\t{self.writeIntegerConstant(token)}"
        elif tokenType == STRING_CONST:
            xmlOutput += f"\t\t{self.writeStringConstant(token)}"
        elif self.isKeywordConst():
            xmlOutput += f"\t\t{self.writeKeyword(token)}" 
        elif self.isUnaryOp():
            xmlOutput += f"\t\t\t{self.writeSymbol(token)}"
            self.file.write(xmlOutput)
            xmlOutput = ""
            self.compileTerm()
        elif token == '(':
            xmlOutput += f"\t\t\t{self.writeSymbol(token)}"
            self.file.write(xmlOutput)
            xmlOutput = ""
            self.compileExpression()
            
            token = self.tokenizer.currentToken 

            if token != ')':
                print("Missing closing paranthesis in term")
                return 
            
            xmlOutput += f"\t\t\t{self.writeSymbol(token)}"
        elif tokenType == IDENTIFIER:
            
            xmlOutput += f"\t\t\t{self.writeIdentifier(token)}"

            # get next token and decide
            token = self.getToken() 


            if token == '[':
                xmlOutput += f"\t\t\t{self.writeSymbol(token)}"
                self.compileExpression() 
                
                # get ']' 
                token = self.compileExpression() 

                if token != ']':
                    print("Missing closing bracket in  term varName[expression]")
                    return 
                

                xmlOutput = f"\t\t\t{self.writeSymbol(token)}"

            elif token == '(':
                xmlOutput += f"\t\t\t{self.writeSymbol(token)}"
                self.compileExpressionList() 
                
                # get ']' 
                token = self.compileExpression() 

                if token != ')':
                    print("Missing closing bracket in  term subroutine call varName(expression)")
                    return 
                

                xmlOutput = f"\t\t\t{self.writeSymbol(token)}"

            elif token == '.':
                            


        
        self.file.write(xmlOutput)
        self.file.write("\t\t</term>\n")
        

    def compileExpressionList(self):
        pass 


    def getToken(self):
        if self.tokenizer.hasMoreToken():
            self.tokenizer.advance()
            return self.tokenizer.currentToken 
        else:
            print("No more token left")
            return None

    def writeIdentifier(self, identifier):
        return f"\t<identifier> {identifier} </identifier>\n"
    
    def writeKeyword(self, keyword):
        return f"\t<keyword> {keyword} </keyword>\n"
    
    def writeSymbol(self, symbol):
        return f"\t<symbol> {symbol} </symbol>\n"
    
    def writeIntegerConstant(self, num):
        return f"\t<integerConstant> {num} </integerConstant>\n"
    
    def writeStringConstant(self, strConst):
        return f"\t<stringConstant> {strConst} </stringConstant>\n"
    
    def isType(self):
        token = self.tokenizer.currentToken
        if self.tokenizer.tokenType() == IDENTIFIER or token == 'int' or token == 'char' or token == 'boolean':
            return True
        else:
            return False
    
    def isStatement(self):
        token = self.tokenizer.currentToken

        if token == 'if' or token == 'let' or token == 'while' or token == 'do' or token == 'return':
            return True 
        else:
            return False 
    
    def generateType(self):
        token = self.tokenizer.currentToken 

        if self.tokenizer.tokenType() == IDENTIFIER:
            return self.writeIdentifier(token)
        else:
            return self.writeKeyword(token)
    
    def isOperator(self):

        token = self.tokenizer.currentToken 

        return token == '+' or token == '-'  or token == '*' or token == '/' or token == '&' or token == '|' or token == '<' or token == '>' or token == '=' 

    def isUnaryOp(self):

        token = self.tokenizer.currentToken 

        return token == '-' or token == '~' 
    
    def isKeywordConst(self):
        
        token = self.tokenizer.currentToken 

        return token == 'true' or token == 'false' or token == 'null' or token == 'this'


