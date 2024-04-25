# Define keyword as constant

KEYWORD = 0
SYMBOL = 1
IDENTIFIER = 2
INT_CONST = 3
STRING_CONST = 4

# defines virtual machine segements 
VM_CONSTANT = 9
VM_STATIC = 5
VM_ARGUMENT = 7
VM_VAR = 8
VM_LOCAL = 10 
VM_THIS = 11
VM_THAT = 12 
VM_POINTER = 13
VM_TEMP = 14

# defines the variable kind 
VAR_STATIC = 15
VAR_FIELD = 16
VAR_ARG = 17
VAR_VAR = 18




# defines the segment 
segments = {
    "CONSTANT": 0,
    "ARGUMENT": 1,
    "LOCAL": 2,
    "STATIC": 3,
    "THIS": 4,
    "THAT": 5,
    "POINTER": 6, 
    "TEMP": 7,
}




# keywords
keywordList = [
    "class", "constructor", "function", "method", "field", "static", "var", "int", "char", "boolean", "void", "true", "false", "null",
    "this", "let", "do", "if", "else", "while", "return",
]

symbolList = [
    '(',')', '{','}', '[',']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '>', '<', '=', '~',
]