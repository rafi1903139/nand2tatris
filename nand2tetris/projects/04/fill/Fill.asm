// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.


// check keyboad input 
(listen)
    @KBD 
    D=M 
    @R1 
    M=D
    

// initialize the variable for loop
    @SCREEN 
    D=A 
    @offset 
    M=D 
    @i 
    M=0 
    @8192 
    D=A 
    @n 
    M=D 

(outerLoop) 
// if i > n exit the loop 
    @i 
    D=M
    @n 
    D=D-M 
    @listen
    D;JGE 
    
    // initialize the inner loop
    @j 
    M=0 
    @32 
    D=A 
    @m 
    M=D 

(innerLoop)
// if j > m exit the loop 
    @j 
    D=M
    @m 
    D=D-M 
    @endLoop 
    D;JGE 

// calculate the offset address and change value according to key pressed 
   @i 
   D=M 
   @R0 
   M=D 
   @offset 
   D=M 
   @R0 
   M=D+M 
   @j 
   D=M 
   @R0 
   M=D+M
   
   // check if the key pressed 
   @R1 
   D=M 
   @clear 
   D;JEQ 

(black) 
    @R0 
    A=M 
    M=-1 
    @endIF
    0;JMP 
(clear) 
    @R0 
    A=M 
    M=0 

(endIF) 

// increase the value of j 
   @j 
   M=M+1 
   @innerLoop 
   0;JMP 

(endLoop)
// increase the value of i 
   @32 
   D=A
   @i 
   M=D+M
   @outerLoop 
   0;JMP 
