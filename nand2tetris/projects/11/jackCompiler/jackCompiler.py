import sys
from glob import glob 
from tokenizer import Tokenizer
from vmWriter import VmWriter
from compilationEngine import CompilationEngine



# get the files for compilation

source = sys.argv[1]
sourceFiles = []
isDirectory = True if ".jack" not in source else False 

# Check if the input is a directory
if isDirectory:
    sourceFiles = glob(source + "*.jack")
else:
    sourceFiles.append(source)

# compile all the source files

for jackFile in sourceFiles:
    tokennizer = Tokenizer(jackFile) 

    # create and open output vm file
    outputFileName = jackFile.removesuffix(".jack") + ".vm"

    # vmWriter for writing on the output file
    writer = VmWriter(outputFileName)

    # create compilation engine and process the token from tokenizer and 
    # write to the file
    compileEngine = CompilationEngine(tokennizer, writer)


