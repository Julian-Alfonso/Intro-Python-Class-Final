#Final - Long Program
#Global Variable for the offset
offset = 0
#Defining the main
def main():    
    x = 0
#Inputs for the Height, Width, Number of steps
    stepHeight = int(input('Enter Height of step: '))
    stepWidth = int(input('Enter Width of step: '))
    numSteps = int(input('Enter number of steps: '))
#For loop for the number of steps    
    for x in range(numSteps):
#Calling the drawSteps function        
        drawSteps(stepHeight,stepWidth,numSteps)
#Defining drawSteps function
def drawSteps(stepHeight,stepWidth,numSteps):
#Using the global variable    
    global offset
#calling the drawRectangle function    
    drawRectangle(stepHeight,stepWidth,offset)
#Creating the offset for each step    
    offset += stepWidth // 2
#Creating the drawRectangle function
def drawRectangle(height,width,offset):
#Variable for numChars    
    numChars = width
    y = 0
#For loop for the height    
    for y in range(height):
        drawRow(offset,numChars)
        y += 1
#Defining the drawRow function 
def drawRow(numSpaces,numChars):
#For loop to determine the offset    
    for offset in range(numSpaces):
        print(' ',end='')
#For loop for '*' in each rectangle        
    for col in range(numChars):
        print('*',end='')
    print()
#Calling Main    
main()
#End of Program
