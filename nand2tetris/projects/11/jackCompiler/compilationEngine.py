from constant import *
from symbolTable import SymbolTable

class CompilationEngine:
    
    def __init__(self, tokenizer, writer):
        self.tokenizer = tokenizer 
        self.codeWriter = writer
        self.file = open(f"test.xml", "w")
        self.tabspace = ""
        self.label = 0

        self.classLevelSymbolTable = SymbolTable()
        self.subroutineLevelSymbolTable = SymbolTable()

        token = self.getToken()
        if token == 'class':
            self.compileClass()
        else:
            print("No class to compile")
        
        print("Successfully compiled")


    def compileClass(self):

        xmlOutput = "<class>\n"
        self.tabspace += " "
        tabspace = self.tabspace

        xmlOutput += f"{self.writeKeyword('class')}"


        self.className = self.getToken()

        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += self.writeIdentifier(self.className)

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
        kind = token

        xmlOutput += self.writeKeyword(token)
        
        # get type 
        token = self.getToken()

        if not self.isType():
            print("Invalid type in classVarDec")
            return 
        
        varType = token
        
        if self.tokenizer.tokenType() == IDENTIFIER:
            xmlOutput += self.writeIdentifier(token)
        else:
            xmlOutput += self.writeKeyword(token)

        # get varName 
        token = self.getToken() 

        if self.tokenizer.tokenType() != IDENTIFIER:
            print("Invalid varName in classVarDec")
            return 
        
        varName = token
        # insert into table
        self.classLevelSymbolTable.define(varName, varType, VAR_STATIC if kind == 'static' else VAR_FIELD)
        xmlOutput += self.writeIdentifier(f"{varName}, {kind}, {self.classLevelSymbolTable.indexOf(varName)}, d")

        # get token and decide 
        token = self.getToken()

        while self.tokenizer.hasMoreToken() and token == ',':
            xmlOutput += self.writeSymbol(token)

            # get varName
            token = self.getToken() 

            if self.tokenizer.tokenType() != IDENTIFIER:
                print("Invalid varName in classVarDec mul")
                return 
            
            
            varName = token
            self.classLevelSymbolTable.define(varName, varType, VAR_STATIC if kind == 'static' else VAR_FIELD)
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
        
        self.subroutineLevelSymbolTable.reset()
        subroutineKind = self.tokenizer.currentToken 
        if subroutineKind == 'method':
            self.subroutineLevelSymbolTable.define('this', self.className, VAR_ARG)

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
        
        subRoutineType = token

        
        # get the subroutine name 
        token = self.getToken()
        subRoutineName = token

        if self.tokenizer.tokenType() != IDENTIFIER:
           print("Invalid subroutine name")
           return 

        
        xmlOutput += self.writeIdentifier(self.describeIdentifier(subRoutineName, "subroutine", None, "d"))


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
        
        
               
        self.compileSubroutineBody(subRoutineName, subroutineKind) 

        self.file.write(tabspace + "</subroutineDec>\n")
        self.tabspace = self.tabspace.removesuffix(" ")

    def compileParameterList(self):
        # ((type varName) (',' varName)*)?
        tabspace = self.tabspace
        xmlOutput = tabspace + "<parameterList>\n"

        self.tabspace += " "
        
        # get type 
        token = self.getToken()
        varType = token
        args = 0
        
        if self.isType():
            xmlOutput += f"{self.generateType()}"
            args += 1
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

        # store the parameter in the symbol table 
        self.subroutineLevelSymbolTable.define(token, varType, VAR_ARG)

        # get next token and decide 
        token = self.getToken() 

        while self.tokenizer.hasMoreToken() and token != ')' and token == ',':
            xmlOutput += f"{self.writeSymbol(token)}"
            args += 1
            # get type
            token = self.getToken()
            varType = token
            
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

            # store the parameter in the symbol table 
            self.subroutineLevelSymbolTable.define(token, varType, VAR_ARG)

            # get next token and decide 
            token = self.getToken()
        
        xmlOutput += tabspace + "</parameterList>\n"
        self.file.write(xmlOutput)

        self.tabspace = self.tabspace.removesuffix(" ")
        return args

    def compileSubroutineBody(self, subroutineName, subroutineKind):

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
        

        # write the subroutine declaration on vm code
        self.codeWriter.writeFunction(f"{self.className}.{subroutineName}", self.subroutineLevelSymbolTable.varCount(VAR_VAR))
        if subroutineKind == 'method':
            self.codeWriter.writePush(VM_ARGUMENT, 0)
            self.codeWriter.writePop(VM_POINTER, 0)
        elif subroutineKind == 'constructor':
            self.codeWriter.writePush(VM_CONSTANT, self.classLevelSymbolTable.varCount(VAR_FIELD))
            self.codeWriter.writeCall('Memory.alloc', 1)
            self.codeWriter.writePop(VM_POINTER, 0)


        
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
        
        varType = token

        # get varName 
        token = self.getToken() 
        if self.tokenizer.tokenType() != IDENTIFIER:
           print("Missing variable name in varDec") 
           return

        varName = token
        self.subroutineLevelSymbolTable.define(varName, varType, VAR_VAR) 

        xmlOutput += self.writeIdentifier(f"{varName}, var, {self.subroutineLevelSymbolTable.indexOf(varName)}, d")        


        # get token and decide 
        token = self.getToken() 
        while self.tokenizer.hasMoreToken() and token != ';' and token == ',':
            xmlOutput += f"{self.writeSymbol(token)}" 
            # get identifier 
            # get varName 
            token = self.getToken() 
            if self.tokenizer.tokenType() != IDENTIFIER:
                print("Missing variable name in varDec") 
                return

            varName = token
            self.subroutineLevelSymbolTable.define(varName, varType, VAR_VAR) 

            xmlOutput += self.writeIdentifier(self.describeIdentifier(varName, varType, self.subroutineLevelSymbolTable.indexOf(varName), "d" ))        


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
        varName = token

        if self.tokenizer.tokenType() != IDENTIFIER:
            print("Missing identifier in let statment")
            return 

        if self.subroutineLevelSymbolTable.kindOf(token) != None:
            varKind = self.subroutineLevelSymbolTable.kindOf(token)
            index = self.subroutineLevelSymbolTable.indexOf(token)

        elif self.classLevelSymbolTable.kindOf(token) != None:
            varKind = self.classLevelSymbolTable.kindOf(token)
            index = self.classLevelSymbolTable.indexOf(token)

        else:
            print("Invalid variable name")
            return 
        

        xmlOutput += self.writeIdentifier(self.describeIdentifier(token, varKind, index, "u" ))

        self.file.write(xmlOutput)
        isArray = False

        # get expression 
        token = self.getToken()
        # process expression 
        if token == '[':
            isArray = True
            xmlOutput = self.writeSymbol(token)
            self.file.write(xmlOutput)

            # set that to arr + i

            self.codeWriter.writePush(self.getSegement(varKind), index)
  

            # process expression 
            self.getToken()
            self.compileExpression() 

            self.codeWriter.writeArithmetic('+')

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

        if isArray:

            # store the result in temp 
            self.codeWriter.writePop(VM_TEMP, 0)

            # store the variable in that
            self.codeWriter.writePop(VM_POINTER, 1)

            # push the result
            self.codeWriter.writePush(VM_TEMP, 0)

            # store the result
            self.codeWriter.writePop(VM_THAT, 0)
        else:
            self.codeWriter.writePop(self.getSegement(varKind), index)

        # get ';' 
        token = self.tokenizer.currentToken
        if token == ';':
            xmlOutput = f"{self.writeSymbol(self.tokenizer.currentToken)}"
        else:
            print("Missing ; in let statement")
            return

        xmlOutput += tabspace + "</letStatement>\n"

        # self.codeWriter.writePop(self.getSegement(varKind), index)
        self.file.write(xmlOutput) 
        self.tabspace = self.tabspace.removesuffix(" ")

        # process next statement
        self.getToken()


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

        self.codeWriter.writeArithmetic('~') 
        label1 = self.getLabel()

        # get '{' 
        token = self.getToken() 

        if token != '{':
            print("Missing { in if")
            return  
        
        xmlOutput += f"{self.writeSymbol(token)}"

        self.file.write(xmlOutput)

        token = self.getToken()

        self.codeWriter.writeIf(label1)
        
        self.compileStatements() 

        label2 = self.getLabel()
        self.codeWriter.writeGoto(label2)
        self.codeWriter.writeLabel(label1)

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
            self.codeWriter.writeLabel(label2)
            xmlOutput = tabspace + "</ifStatement>\n"
            self.file.write(xmlOutput)
            self.tabspace = self.tabspace.removesuffix(" ")

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

        self.codeWriter.writeLabel(label2)

        self.file.write(xmlOutput)

        self.tabspace = self.tabspace.removesuffix(" ")
        
        # process next statement
        self.getToken()

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

       label1 = self.getLabel()
       self.codeWriter.writeLabel(label1)

       self.compileExpression() 
       
       self.codeWriter.writeArithmetic('~')

       label2 = self.getLabel()
       self.codeWriter.writeIf(label2)

       # get ')' 
       token = self.tokenizer.currentToken 

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
       
       self.codeWriter.writeGoto(label1)

       self.codeWriter.writeLabel(label2)

       # get '}' 
       token = self.tokenizer.currentToken 

       if token != '}':
           print("Missing } in while")
           return 
       
       xmlOutput = self.writeSymbol(token)

       xmlOutput += tabspace + "</whileStatement>\n"

       self.file.write(xmlOutput)

       self.tabspace = self.tabspace.removesuffix(" ") 

       # process next statement
       self.getToken()

    def compileDo(self):
        tabspace = self.tabspace 

        xmlOutput = tabspace + "<doStatement>\n"

        self.tabspace += " "

        # get do
        token = self.tokenizer.currentToken 

        xmlOutput += self.writeKeyword(token)

        # process subroutine call 
        token = self.getToken()
        subroutineName = token

        if self.tokenizer.tokenType() != IDENTIFIER:
            print("Invalid subroutine name")
            return 
        
        varName = subroutineName
        isMethod = True

        if self.subroutineLevelSymbolTable.kindOf(varName) != None:
            kind = self.subroutineLevelSymbolTable.kindOf(varName)
            segment = self.getSegement(kind)

            self.codeWriter.writePush(
                segment,
                self.subroutineLevelSymbolTable.indexOf(varName)
            )
        elif self.classLevelSymbolTable.kindOf(varName) != None:
                
            kind = self.classLevelSymbolTable.kindOf(varName)
            segment = self.getSegement(kind)

            self.codeWriter.writePush(
                segment,
                self.classLevelSymbolTable.indexOf(varName)
            )
        else:
            isMethod = False
    
        xmlOutput += self.writeIdentifier(token)

        self.file.write(xmlOutput)

        # get token and decide
        token = self.getToken()

        if token == '(' or token == '.':
            self.generateSubroutineCall(subroutineName, isMethod) 
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

        self.codeWriter.writePop(VM_TEMP, 0)

        # process next statement
        self.getToken()


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
        else:
            # nothing to return 0 is add 
            self.codeWriter.writePush(VM_CONSTANT, 0)
        

        # get ;

        token = self.tokenizer.currentToken 

        if token != ';':
            print("Missing ; in return statement")
            return 
        
        xmlOutput = self.writeSymbol(token)

        # write return to the vm code
        self.codeWriter.writeReturn()
        xmlOutput += tabspace + "</returnStatement>\n"

        self.file.write(xmlOutput)


        self.tabspace = self.tabspace.removesuffix(" ")

        # process next statement
        self.getToken()


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
            operator = token

            # get the term
            token = self.getToken()
            self.compileTerm() 

            self.codeWriter.writeArithmetic(operator)
        

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
            self.codeWriter.writePush(VM_CONSTANT, token)
            self.getToken()

        elif tokenType == STRING_CONST:
            xmlOutput += f"{self.writeStringConstant(token)}"
            strLen = len(token)

            # pushing the string length to the stack
            self.codeWriter.writePush(VM_CONSTANT, strLen)
            self.codeWriter.writeCall('String.new', 1)
            
            for i in range(strLen):
                self.codeWriter.writePush(VM_CONSTANT, ord(token[i]))
                self.codeWriter.writeCall('String.appendChar', 2)
            self.file.write(xmlOutput)

            self.getToken()

        elif self.isKeywordConst():
            xmlOutput += f"{self.writeKeyword(token)}" 
            keyword = token 

            if keyword == 'false' or keyword == 'null':
                self.codeWriter.writePush(VM_CONSTANT, 0)
            elif keyword == 'true':
                self.codeWriter.writePush(VM_CONSTANT, 1)
                self.codeWriter.writeArithmetic('-', True)
            elif keyword == 'this':
                self.codeWriter.writePush(VM_POINTER, 0)

            self.file.write(xmlOutput)

            self.getToken()

        elif self.isUnaryOp():
            xmlOutput += f"{self.writeSymbol(token)}"
            self.file.write(xmlOutput)
            operator = token

            self.getToken()
            self.compileTerm()
            self.codeWriter.writeArithmetic(operator, True)



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
            
            varName = token
            xmlOutput += f"{self.writeIdentifier(token)}"
            isMethod = True


            if self.subroutineLevelSymbolTable.kindOf(varName) != None:
                kind = self.subroutineLevelSymbolTable.kindOf(varName)
                segment = self.getSegement(kind)

                self.codeWriter.writePush(
                    segment,
                    self.subroutineLevelSymbolTable.indexOf(varName)
                )
            elif self.classLevelSymbolTable.kindOf(varName) != None:
                    
                kind = self.classLevelSymbolTable.kindOf(varName)
                segment = self.getSegement(kind)

                self.codeWriter.writePush(
                    segment,
                    self.classLevelSymbolTable.indexOf(varName)
                )
            else:
                isMethod = False

            # get next token and decide
            token = self.getToken() 


            if token == '[':
                xmlOutput += f"{self.writeSymbol(token)}"
                self.file.write(xmlOutput)

                self.getToken()
                self.compileExpression() 

                self.codeWriter.writeArithmetic('+')
                self.codeWriter.writePop(VM_POINTER, 1)
                self.codeWriter.writePush(VM_THAT, 0)

                token = self.tokenizer.currentToken
                              

                if token != ']':
                    print(token)
                    print("Missing closing bracket in  term varName[expression]")
                    return 
                

                xmlOutput = f"{self.writeSymbol(token)}"
                self.file.write(xmlOutput)

                self.getToken()


            elif token == '(' or token == '.':
                self.file.write(xmlOutput)

                self.generateSubroutineCall(varName, isMethod)
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

        args = 1
        self.compileExpression() 

        # get token and decide 
        token = self.tokenizer.currentToken
        while self.tokenizer.hasMoreToken() and token == ',':
            xmlOutput = self.writeSymbol(token)
            args += 1
            self.file.write(xmlOutput)
            # process expression
            self.getToken()
            self.compileExpression() 

            token = self.tokenizer.currentToken

            
        xmlOutput = tabspace + "</expressionList>\n"
        self.file.write(xmlOutput)
        self.tabspace = self.tabspace.removesuffix(" ")

        return args

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

    def generateSubroutineCall(self, identifier, isMethod):
        token = self.tokenizer.currentToken
        if token == '(':
                self.codeWriter.writePush(VM_POINTER, 0)
                xmlOutput = f"{self.writeSymbol(token)}"
                self.file.write(xmlOutput)

                # get token and decide
                token = self.getToken()
                args = 0

                if token != ')':
                    args = self.compileExpressionList() 
                else:
                    xmlOutput = self.tabspace + "\t<expressionList>\n"
                    xmlOutput += self.tabspace + "\t</expressionList>\n"
                    self.file.write(xmlOutput)
                
                token = self.tokenizer.currentToken

                if token != ')':
                    print(token)
                    print("Missing closing bracket in  term subroutine call varName(expression)")
                    return 
                

                xmlOutput = f"{self.writeSymbol(token)}"

                self.file.write(xmlOutput)
                self.codeWriter.writeCall(f"{self.className}.{identifier}", args+1)

        elif token == '.':
                xmlOutput = f"{self.writeSymbol(token)}"

                # get subroutine name
                token = self.getToken()
                subroutine = token
                
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
                args = 0

                if token != ')':
                    args = self.compileExpressionList() 
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
                


                className = self.subroutineLevelSymbolTable.typeOf(identifier)

                if className == None:
                    className = self.classLevelSymbolTable.typeOf(identifier)
                
                if className == None:
                    className = identifier

                self.codeWriter.writeCall(f"{className}.{subroutine}", args + 1 if isMethod else args)

    def describeIdentifier(self, name, category, index, usage):
        return f"{name}, {category}, {index}, {usage}"

    def getSegement(self, kind):
        if kind == VAR_STATIC:
            return VM_STATIC 
        elif kind == VAR_ARG:
            return VM_ARGUMENT 
        elif kind == VAR_FIELD:
            return VM_THIS 
        elif kind == VAR_VAR:
            return VM_LOCAL 
        else:
            print("Invalid kind")
        
    def getLabel(self):
        label = f"label{self.label}" 
        self.label += 1 
        return label
