// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.


    @SCREEN 
    D=A  
    @R0 
    M=D // POINTS TO THE NEXT PIXEL ADDRESS WHICH WILL BE BLACKEN NEXT 
(LOOP)
    // CHECK KEYBOARD 
    @24576 
    D=M 
    // IF NO KEY IS PRESSED GOTO LOOP ELSE BLACK SCREEN 
    @LOOP 
    D;JEQ
    @R0 
    A=M 
    M=1 // BLACK THE SCREEN  
    A=A+1 //POINT TO THE NEXT ADDRESS
    D=A 
    @R0
    M=D // LOAD IN R0 

    @LOOP
    0;JMP 
