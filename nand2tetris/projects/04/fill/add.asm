// This program will two digit from the user and
// add them store the result in R0

// Pseudocode 

// take input from the user and store it into R0 and R1 
// R2 = R0 + R1 

// cnt = 2 
// if kbd = 0
//  go back 
// R0 = input value

// if kbd = 0
//  go back 
// R1 = input value 

// R2 = R0 + R1 

// end 

@48 
D=A 
@normal
M=D 

(INPUT1)
    @KBD 
    D=M 
    @INPUT1 
    D;JEQ 

    @R0 
    M=D // store the input in R0 


    // normalize the value from keyboard input
    @normal 
    D=M 
    @R0 
    M=M-D    

(INPUT2)
    @KBD 
    D=M 
    @INPUT2 
    D;JEQ

    @R1
    M=D // store the value in R1 

    // normalize the value from keyboard input
    @normal
    D=M
    @R1 
    M=M-D     

    @R1 
    D=M
    @R2 
    M=D 
    @R0 
    D=M 
    @R2 
    M=D+M


(END)
    @END 
    0;JMP