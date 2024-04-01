import sys 

if len(sys.argv) != 3:
    print("Invalid argument") 
    exit()


try:
    testfile = open(sys.argv[1], 'r')
    cmpfile = open(sys.argv[2], 'r')
    
    cnt = 0
    for line in cmpfile:
        temp  = testfile.readline() 
        if line != temp:
            print(f'mismatch at line {cnt}') 
            exit() 
        cnt += 1

    print("Successfully completed")

except:
    print("Error occured")
