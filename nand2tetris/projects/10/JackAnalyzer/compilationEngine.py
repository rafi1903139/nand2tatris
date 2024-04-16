from tokenizer import *
from constant import *

class CompilationEngine:
    
    def __init__(self, fileName):
        try:
            self.tokenizer = Tokenizer(fileName) 
            self.file = open(f"{fileName.split('.jack')[0]}_custom.xml", "w")
            self.tabspace = ""

            token = self.getToken()
            if token == 'class':
                self.compileClass()
            else:
                print("No class to compile")
        except:
            print("Error occured")    
    
    def compileClass(self):

        xmlOutput = "<class>\n"
        self.tabspace += " "
        tabspace = self.tabspace

        xmlOutput += f"{self.writeKeyword('class')}"


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

        token = self.getToken()

        while self.tokenizer.hasMoreToken() and token != "}":
            
            if token == 'static' or token == 'field':
                self.compileClassVarDec()

            elif token == 'constructor' or token == 'function' or token == 'method':
                self.compileSubroutine()

            else:
                print(token)
                print("Invalid format in class declaration")
                return 
            
            token = self.getToken()
        
        if self.tokenizer.currentToken == '}':
            self.file.write(self.writeSymbol('}'))
        else:
            print("Missing ending curly braces for class")
        
        self.file.write("</class>\n")
        self.tabspace = self.tabspace.removesuffix(" ")


    def compileClassVarDec(self):
    # ('static' | 'field') type varName(',' varName)*';'

        tabspace = self.tabspace 

        xmlOutput = tabspace + "<classVarDec>\n"

        self.tabspace += " "

        token = self.tokenizer.currentToken 

        xmlOutput += self.writeKeyword(token)
        
        # get type 
        token = self.getToken()

        if not self.isType():
            print("Invalid type in classVarDec")
            return 
        
        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += self.writeIdentifier(token)
        else:
            xmlOutput += self.writeKeyword(token)

        # get varName 
        token = self.getToken() 

        if self.tokenizer.tokenType() != IDENTIFIER:
            print("Invalid varName in classVarDec")
            return 
        
        xmlOutput += self.writeIdentifier(token)

        # get token and decide 
        token = self.getToken()

        while self.tokenizer.hasMoreToken() and token == ',':
            xmlOutput += self.writeSymbol(token)

            # get varName
            token = self.getToken() 

            if self.tokenizer.tokenType() != IDENTIFIER:
                print("Invalid varName in classVarDec mul")
                return 
            
            xmlOutput += self.writeIdentifier(token)

            # get token and decide 
            token = self.getToken() 
        
        if token != ';':
            print("Missing ; in classVarDec")
            return
    
        xmlOutput += self.writeSymbol(token)

        xmlOutput += tabspace + "</classVarDec>\n"

        self.file.write(xmlOutput)
            
        self.tabspace = self.tabspace.removesuffix(" ")




    def compileSubroutine(self):
        tabspace = self.tabspace
        xmlOutput = tabspace + "<subroutineDec>\n"
        self.tabspace += " "
        tabspace = self.tabspace

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
            xmlOutput += self.writeSymbol(token)
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

        self.file.write(tabspace + "</subroutineDec>\n")
        self.tabspace = self.tabspace.removesuffix(" ")


    

    def compileParameterList(self):
        # ((type varName) (',' varName)*)?
        tabspace = self.tabspace
        xmlOutput = tabspace + "<parameterList>\n"

        self.tabspace += " "
        
        # get type 
        token = self.getToken()
        
        if self.isType():
            xmlOutput += f"{self.generateType()}"
        else:
            xmlOutput += tabspace + "</parameterList>\n"
            self.file.write(xmlOutput) 
            return 
        
        # get varName 
        token = self.getToken() 

        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += f"{self.writeIdentifier(token)}"
        else:
            print("invalid identifier in parameterlist")
            return 
        

        # get next token and decide 
        token = self.getToken() 

        while self.tokenizer.hasMoreToken() and token != ')' and token == ',':
            xmlOutput += f"{self.writeSymbol(token)}"

            # get type
            token = self.getToken()
            
            if self.isType():
                xmlOutput += f"{self.generateType()}"
            else:
                print("Invalid type in parameterlist")
                return

            # get varName 
            token = self.getToken() 

            if self.tokenizer.tokenType() == IDENTIFIER:
                xmlOutput += f"{self.writeIdentifier(token)}"
            else:
                print("invalid varName in parameterlist")
                return  

            # get next token and decide 
            token = self.getToken()
        
        xmlOutput += tabspace + "</parameterList>\n"
        self.file.write(xmlOutput)

        self.tabspace = self.tabspace.removesuffix(" ")


    def compileSubroutineBody(self):

        # '{' varDec* statements '}' 

        # get opening curly brace
        token = self.getToken()
        tabspace = self.tabspace
        xmlOutput = tabspace + "<subroutineBody>\n"


        self.tabspace += " "

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
        token = self.tokenizer.currentToken

        if token == '}':
            self.file.write(self.writeSymbol('}'))
        else:
            print(token)
            print("Missing closing curly braces for subroutine body")
            return 
        
        self.file.write(tabspace + "</subroutineBody>\n")
        self.tabspace = self.tabspace.removesuffix(" ")

    def compileVarDec(self):
        # 'var' type varName(',' varName)*';'

        tabspace = self.tabspace
        xmlOutput = tabspace + "<varDec>\n"
        
        self.tabspace += ' '

        xmlOutput += f"{self.writeKeyword('var')}"

        # get type
        token = self.getToken() 

        if self.isType():
            xmlOutput += f"{self.generateType()}" 
        else:
            print("Missing type")
            return  

        # get varName 
        token = self.getToken() 
        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += f"{self.writeIdentifier(token)}" 
        else:
            print("Missing variable name in varDec")
            return 

        # get token and decide 
        token = self.getToken() 
        while self.tokenizer.hasMoreToken() and token != ';' and token == ',':
            xmlOutput += f"{self.writeSymbol(token)}" 
            # get identifier 
            token = self.getToken() 
            if self.tokenizer.tokenType() == IDENTIFIER:
                xmlOutput += f"{self.writeIdentifier(token)}"
            else:
                print("Invalid identifier in varDec")
                return

            # get the next token
            token = self.getToken()
        
        if token != ';':
            print("Missing ; after varDec")
            return 
        else:
            xmlOutput += f'{self.writeSymbol(token)}'
        
        xmlOutput += tabspace + '</varDec>\n'
    
        self.getToken()
        self.file.write(xmlOutput)

        self.tabspace = self.tabspace.removesuffix(" ")


    def compileStatements(self):


        if not self.isStatement():
            return 

        tabspace = self.tabspace
        
        xmlOutput = tabspace + "<statements>\n"

        self.tabspace += " "
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
                self.compileReturn() 

            # get the next token and decide 
            self.getToken() 

        xmlOutput = tabspace + "</statements>\n"
        self.file.write(xmlOutput)


        self.tabspace = self.tabspace.removesuffix(" ")

    def compileLet(self):
        # 'let' varName ('[' expression ']')? '=' expression';'
        tabspace = self.tabspace 
        xmlOutput = tabspace + "<letStatement>\n"
        
        self.tabspace += " "

        xmlOutput += f"{self.writeKeyword(self.tokenizer.currentToken)}"

        # get varName 
        token = self.getToken()

        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += f"{self.writeIdentifier(token)}"
        else:
            print("Missing identifier in let statment")
        
        self.file.write(xmlOutput)

        # get expression 
        token = self.getToken()
        # process expression 
        if token == '[':
            xmlOutput = self.writeSymbol(token)
            self.file.write(xmlOutput)

            # process expression 
            self.getToken()
            self.compileExpression() 

            # get ']'
            token = self.tokenizer.currentToken 
            
            if token != ']':
                print("Missing ] in let statement")
                return 
            
            xmlOutput = self.writeSymbol(token)
            self.file.write(xmlOutput)

            # get next token and decide
            self.getToken()


        # get '=' 
        token = self.tokenizer.currentToken 
        if token == '=':
            xmlOutput = f"{self.writeSymbol(token)}"
            self.file.write(xmlOutput)
        else:
            print("Missing = in letStatemtn")
            return 
        
        # process expression 
        self.getToken() 
        self.compileExpression()

        # get ';' 
        token = self.tokenizer.currentToken
        if token == ';':
            xmlOutput = f"{self.writeSymbol(self.tokenizer.currentToken)}"
        else:
            print("Missing ; in let statement")
            return

        xmlOutput += tabspace + "</letStatement>\n"

        self.file.write(xmlOutput) 
        self.tabspace = self.tabspace.removesuffix(" ")

    def compileIf(self):
        # 'if' '(' expression ')' '{' statements '}' ('else''{' statements '}')?
        tabspace = self.tabspace 
        token = self.tokenizer.currentToken

        self.tabspace += " "

        xmlOutput = f"{tabspace}<ifStatement>\n"
        xmlOutput += f"{self.writeKeyword(token)}"

        # get '(' 
        token = self.getToken() 

        if token != '(':
            print("Missing opening breaces in if statement")
            return 
        
        xmlOutput += f"{self.writeSymbol(token)}"
        self.file.write(xmlOutput)

        token = self.getToken()
        self.compileExpression() 

        # get ')' 
        token = self.tokenizer.currentToken 

        if token != ')':
            print("Missing closing braces in if statement")
            return 
        
        xmlOutput = f"{self.writeSymbol(token)}"

        # get '{' 
        token = self.getToken() 

        if token != '{':
            print("Missing { in if")
            return  
        
        xmlOutput += f"{self.writeSymbol(token)}"

        self.file.write(xmlOutput)

        token = self.getToken()
        
        self.compileStatements() 

        # get '}' 
        token = self.tokenizer.currentToken 
        if token != '}':
            print("Missing } in if")
            return 
        
        xmlOutput = f"{self.writeSymbol(token)}" 
        self.file.write(xmlOutput)

        # get token and decide 
        token = self.getToken() 

        if token != 'else':
            xmlOutput = tabspace + "</ifStatement>\n"
            self.file.write(xmlOutput)
            self.tabspace = self.tabspace.removesuffix(" ")


            if self.isStatement():
                if token == 'let':
                    self.compileLet()  
                elif token == 'if':
                    self.compileIf() 
                elif token == 'while':
                    self.compileWhile() 
                elif token == 'do':
                    self.compileDo() 
                elif token == 'return':
                    self.compileReturn() 


            return 
        
        xmlOutput = f"{self.writeKeyword(token)}"


        # get '{' 
        token = self.getToken() 

        if token != '{':
            print("Missing { in if")
            return  
        
        xmlOutput += f"{self.writeSymbol(token)}"

        self.file.write(xmlOutput)

        token = self.getToken()
        
        self.compileStatements() 

        # get '}' 
        token = self.tokenizer.currentToken 

        if token != '}':
            print("Missing } in else")
            return 
        
        xmlOutput = f"{self.writeSymbol(token)}" 
        xmlOutput += tabspace + "</ifStatement>\n"
        self.file.write(xmlOutput)

        self.tabspace = self.tabspace.removesuffix(" ")

            
    def compileWhile(self):
    # 'while' '(' expression ')' '{' statements '}'
       tabspace = self.tabspace 

       xmlOutput = tabspace + "<whileStatement>\n"

       self.tabspace += " "
       
       # get while
       token = self.tokenizer.currentToken 

       xmlOutput += self.writeKeyword(token)

       # get '('
       token = self.getToken() 

       if token != "(":
           print("Missing ( in while")
           return 
       
       xmlOutput += self.writeSymbol(token)

       self.file.write(xmlOutput)
       
       self.getToken()
       self.compileExpression() 

       # get ')' 
       token = self.tokenizer.currentToken 
       print(token)

       if token != ')':
           print("Missing ) in while")
           return 
       
       xmlOutput = self.writeSymbol(token)

       # get '{'
       token = self.getToken() 

       if token != '{':
           print("Missing { in while")
           return 
       
       xmlOutput += self.writeSymbol(token)

       self.file.write(xmlOutput)

       token = self.getToken()
       self.compileStatements() 

       # get '}' 
       token = self.tokenizer.currentToken 

       if token != '}':
           print("Missing } in while")
           return 
       
       xmlOutput = self.writeSymbol(token)

       xmlOutput += tabspace + "</whileStatement>\n"

       self.file.write(xmlOutput)

       self.tabspace = self.tabspace.removesuffix(" ") 


    def compileDo(self):
        tabspace = self.tabspace 

        xmlOutput = tabspace + "<doStatement>\n"

        self.tabspace += " "

        # get do
        token = self.tokenizer.currentToken 

        xmlOutput += self.writeKeyword(token)

        # process subroutine call 
        token = self.getToken()

        if self.tokenizer.tokenType() != IDENTIFIER:
            print("Invalid subroutine name")
            return 
        
        xmlOutput += self.writeIdentifier(token)

        self.file.write(xmlOutput)

        # get token and decide
        token = self.getToken()

        if token == '(' or token == '.':
            self.generateSubroutineCall() 
            self.getToken()
        else:
            print("invalid subroutine call in do")
            return 
        
        # get ; 
        token = self.tokenizer.currentToken
        if token != ';':
            print("Missing ; in do")
            return 
        xmlOutput = self.writeSymbol(token)
        xmlOutput += tabspace + "</doStatement>\n"

        self.file.write(xmlOutput)

        self.tabspace = self.tabspace.removesuffix(" ")


        
    def compileReturn(self):
        tabspace = self.tabspace 

        xmlOutput = tabspace + "<returnStatement>\n"

        self.tabspace += " "

        token = self.tokenizer.currentToken

        xmlOutput += self.writeKeyword(token)

        # get next token and decide 
        token = self.getToken()

        self.file.write(xmlOutput)

        if token != ';':
            self.compileExpression() 
        

        # get ;

        token = self.tokenizer.currentToken 

        if token != ';':
            print("Missing ; in return statement")
            return 
        
        xmlOutput = self.writeSymbol(token)
        xmlOutput += tabspace + "</returnStatement>\n"

        self.file.write(xmlOutput)

        self.tabspace = self.tabspace.removesuffix(" ")


    def compileExpression(self):
        
        tabspace = self.tabspace
        xmlOutput = tabspace + "<expression>\n"

        self.tabspace += " "

        self.file.write(xmlOutput)
        self.compileTerm() 

        while self.isOperator():
            # process the operator
            token = self.tokenizer.currentToken
            xmlOutput = self.writeSymbol(token)
            self.file.write(xmlOutput)

            # get the term
            token = self.getToken()
            self.compileTerm() 
        

        xmlOutput = tabspace + "</expression>\n"
        self.file.write(xmlOutput)       
        self.tabspace = self.tabspace.removesuffix(" ")


    def compileTerm(self):

        tabspace = self.tabspace 
        xmlOutput = tabspace + "<term>\n"

        self.tabspace += " "

        token = self.tokenizer.currentToken 
        
        tokenType = self.tokenizer.tokenType() 

        if tokenType == INT_CONST:
            xmlOutput += f"{self.writeIntegerConstant(token)}"
            self.file.write(xmlOutput)

            self.getToken()

        elif tokenType == STRING_CONST:
            xmlOutput += f"{self.writeStringConstant(token)}"
            self.file.write(xmlOutput)

            self.getToken()

        elif self.isKeywordConst():
            xmlOutput += f"{self.writeKeyword(token)}" 
            self.file.write(xmlOutput)

            self.getToken()

        elif self.isUnaryOp():
            xmlOutput += f"{self.writeSymbol(token)}"
            self.file.write(xmlOutput)

            self.getToken()
            self.compileTerm()



        elif token == '(':
            xmlOutput += f"{self.writeSymbol(token)}"
            self.file.write(xmlOutput)

            self.getToken()
            self.compileExpression()
            
            token = self.tokenizer.currentToken 

            if token != ')':
                print(token)
                print("Missing closing paranthesis in term")
                return 
            
            xmlOutput = f"{self.writeSymbol(token)}"
            self.file.write(xmlOutput)

            # get the next token
            self.getToken()

        elif tokenType == IDENTIFIER:
            
            temp = token
            xmlOutput += f"{self.writeIdentifier(token)}"

            # get next token and decide
            token = self.getToken() 


            if token == '[':
                xmlOutput += f"{self.writeSymbol(token)}"
                self.file.write(xmlOutput)

                self.getToken()
                self.compileExpression() 
                
                # get ']' 
                token = self.tokenizer.currentToken 

                if token != ']':
                    print("Missing closing bracket in  term varName[expression]")
                    return 
                

                xmlOutput = f"{self.writeSymbol(token)}"
                self.file.write(xmlOutput)

                self.getToken()


            elif token == '(' or token == '.':
                self.file.write(xmlOutput)

                self.generateSubroutineCall()
                self.getToken()

            else:
                self.file.write(xmlOutput)            
            

        self.file.write(tabspace + "</term>\n")

        self.tabspace = self.tabspace.removesuffix(" ")

        
        

    def compileExpressionList(self):
    # (expression(',' expression)*)?

        tabspace = self.tabspace 

        xmlOutput = tabspace + "<expressionList>\n"
        self.file.write(xmlOutput)

        self.tabspace += " "


        self.compileExpression() 

        # get token and decide 
        token = self.tokenizer.currentToken
        while self.tokenizer.hasMoreToken() and token == ',':
            xmlOutput = self.writeSymbol(token)
            self.file.write(xmlOutput)
            # process expression
            self.getToken()
            self.compileExpression() 

            token = self.tokenizer.currentToken

            
        xmlOutput = tabspace + "</expressionList>\n"
        self.file.write(xmlOutput)
        self.tabspace = self.tabspace.removesuffix(" ")

    def getToken(self):
        if self.tokenizer.hasMoreToken():
            self.tokenizer.advance()
            return self.tokenizer.currentToken 
        else:
            print("No more token left")
            return None

    def writeIdentifier(self, identifier):
        return self.tabspace + f"<identifier> {identifier} </identifier>\n"
    
    def writeKeyword(self, keyword):
        return self.tabspace + f"<keyword> {keyword} </keyword>\n"
    
    def writeSymbol(self, symbol):
        if symbol == '<':
            return self.tabspace + f"<symbol> &lt; </symbol>\n"
        elif symbol == '>':
            return self.tabspace + f"<symbol> &gt; </symbol>\n"
        elif symbol == '&':
            return self.tabspace + f"<symbol> &amp; </symbol>\n"
        elif symbol == '\"':
            return self.tabspace + f"<symbol> &quot; </symbol>\n"
        else:        
            return self.tabspace + f"<symbol> {symbol} </symbol>\n"
    
    def writeIntegerConstant(self, num):
        return self.tabspace + f"<integerConstant> {num} </integerConstant>\n"
    
    def writeStringConstant(self, strConst):
        return self.tabspace + f"<stringConstant> {strConst} </stringConstant>\n"
    
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

    def generateSubroutineCall(self):
        token = self.tokenizer.currentToken
        if token == '(':
                xmlOutput = f"{self.writeSymbol(token)}"
                self.file.write(xmlOutput)

                # get token and decide
                token = self.getToken()

                if token != ')':
                    self.compileExpressionList() 
                    token = self.getToken()
                else:
                    xmlOutput = self.tabspace + "\t<expressionList>\n"
                    xmlOutput += self.tabspace + "\t</expressionList>\n"
                    self.file.write(xmlOutput)

                if token != ')':
                    print("Missing closing bracket in  term subroutine call varName(expression)")
                    return 
                

                xmlOutput = f"{self.writeSymbol(token)}"

                self.file.write(xmlOutput)

        elif token == '.':
                xmlOutput = f"{self.writeSymbol(token)}"

                # get subroutine name
                token = self.getToken()
                
                if self.tokenizer.tokenType() != IDENTIFIER:
                    print("Missing identifier in subroutine call")
                    return 
                
                xmlOutput += f"{self.writeIdentifier(token)}"

                # get '(' 
                token = self.getToken() 

                if token != '(':
                    print("Missing ( in subroutine call")
                    return 

                xmlOutput += f"{self.writeSymbol(token)}"

                self.file.write(xmlOutput)

                # get token and decide
                token = self.getToken()

                if token != ')':
                    self.compileExpressionList() 
                else:
                    xmlOutput = self.tabspace + "\t<expressionList>\n"
                    xmlOutput += self.tabspace + "\t</expressionList>\n"
                    self.file.write(xmlOutput)


                token = self.tokenizer.currentToken
                if token != ')':
                    print(token)
                    print("Missing ) in subroutine call")
                    return 
                
                xmlOutput = f"{self.writeSymbol(token)}"

                self.file.write(xmlOutput)


        

