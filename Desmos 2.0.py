import math
graphedEquations = []
count = 5

def graphFunction(count):
    
    print("What is the function you want to graph?")
    print("Give in terms of y = x")
    print("Example of squaring numbers: ^6, ^2")
    print("Example of rooting numbers: '1/6, '1/2")
    equation = input("Input Here: ")
    splitEquation = list(equation)
    splitEquation2 = []
    
    for rep in range(len(equation)):
        
        if (splitEquation[rep] == " "):
            
            pass
        
        else:
            
            splitEquation2.append(splitEquation[rep])
            
    graphedEquations.append(splitEquation2)
    
    del splitEquation2[0]
    del splitEquation2[0]
    
    eq = ''.join(splitEquation2)
    
    eq2 = ''.join(splitEquation2)
    
    values = {}

    count2 = -1*count

    for repeat in range(count*2):
    
        eq2 = eq2.replace("x",str(count2))
        
        eq2 = eq2.replace("^","**")
        
        eq2 = eq2.replace("'","**")
        
        print(eq2)
        
        ans = eval(eq2)
        
        print(ans)
        
        count2 += 1
        
        eq2 = eq

def doWhat():
    
    print("What would you like to?")
    print("Enter 1 to quit")
    print("Enter 2 to graph an Function")
    print("Enter 3 to delete an Function")
    print("Enter 4 to solve an equation")
    
    ans = 0
    
    try:
        
        ans = int(input("What will you choose? "))
        
    except:
        
        print("\n:(\n\n")
        return False
        
    print("\n\n\n\n")
    
    if (ans == 1):
        
        return True
        
    elif (ans < 0 or ans > 4):
        
        print("\n:(\n\n")
        return False
        
    elif (ans == 2):
        
        graphFunction(count)
        
    print("\n\n\n")
        
    return False

def drawReg():
    screen = turtle.Screen()
    screen.setup(400, 400)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(-1)
    pen.penup()
    pen.goto(-200,200)
    pen.pendown()
    pen.fillcolor("white")
    pen.begin_fill()
    
    for repeat in range(4):
        pen.forward(400)
        pen.right(90)
        
    pen.end_fill()
    
    pen.penup()
    
    pen.pensize(2.5)
    pen.goto(-200,0)
    pen.pendown()
    pen.goto(200,0)
    
    pen.penup()
    pen.goto(0,-200)
    pen.pendown()
    pen.goto(0,200)
    pen.penup()
    
    pen.pensize(0.5)
    
    pen.pencolor("grey")
    
    xCoord = -160
    
    for rep in range(9):
        pen.goto(xCoord,-200)
        pen.pendown()
        pen.goto(xCoord,200)
        pen.penup()
        xCoord += 40
        
    yCoord = -160
        
    for rep in range(9):
        pen.goto(-200,yCoord)
        pen.pendown()
        pen.goto(200,yCoord)
        pen.penup()
        yCoord += 40
        
    xCoord = -192
    count = -5
    pen.pencolor("black")
    pen.color("black")
    
    for rep in range(10):
        pen.penup()
        pen.goto(xCoord, -14)
        pen.pendown()
        pen.write(str(count), align="center", font=("Times", 11, "normal"))
        pen.penup()
        xCoord += 40
        count += 1
        
    pen.penup()
    yCoord = -192
    count2 = -5
    pen.pencolor("black")
    pen.color("black")
    
    for rep in range(10):
        pen.penup()
        pen.goto(-9,yCoord)
        pen.pendown()
        if (count2 < 0):
            pen.write(str(count2), align="center", font=("Times", 11, "normal"))
        else:
            pen.write(" " + str(count2), align="center", font=("Times", 11, "normal"))
        pen.penup()
        yCoord += 40
        count2 += 1
        
    pen.pencolor("black")
    pen.pensize(2)
    
    pen.goto(-196,5)
    pen.pendown()
    pen.goto(-196,-5)
    pen.goto(-200,0)
    pen.goto(-196,5)
    
    pen.penup()
    pen.goto(196,5)
    pen.pendown()
    pen.goto(196,-5)
    pen.goto(200,0)
    pen.goto(196,5)
    
    pen.penup()
    pen.goto(5,196)
    pen.pendown()
    pen.goto(-5,196)
    pen.goto(0,200)
    pen.goto(5,196)
    
    pen.penup()
    pen.goto(5,-196)
    pen.pendown()
    pen.goto(-5,-196)
    pen.goto(0,-200)
    pen.goto(5,-196)
    
    pen.update()
    turtle.done()

def main():
    
    drawReg()
    
    quit = False
    
    while (quit == False):
        
        quit = doWhat()
        
    print("Thank you!")

main()