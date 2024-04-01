// the program compare two number stored in R0 and R1
// and write max of them in R2 

// if R1 > R0 
//      R2 = R1 
// else 
//       R2 = R0 


    @R0
    D=M 
    @R1 
    D=D-M 
    @ELSE
    D;JGT // R0 > R1 goto else part 
(IF)
    // R1 > R0
    @R1 
    D=M
    @R2
    M=D 
    @END 
    0;JMP

(ELSE)
    // R2 <= R0
    @R0 
    D=M 
    @R2 
    M=D

(END)
    @END 
    0;JMP