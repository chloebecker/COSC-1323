#Lab 8
#Chloe ******

#imports random module for main function
import random

##Functions
#factorial function using a for loop
def factorial_for(n):
    if n == 0:
        return 1
    f = 1
    for i in range(n,0,-1):
        f *= i
    return f

#factorial function using a while loop
def factorial_while(n):
    if n == 0:
        return 1
    f = 1 
    while n > 0:
        f *= n
        n -= 1
    return(f)

#main function
def main():
    x1 = random.randint(1,50)
    print("x1 =",x1)
    for i in range(1,x1+1):
        x1 = i
        #prints the iteration number and calls factorial_for with x1
        print("Iteration",i,"=",factorial_for(x1))
    x2 = random.randint(1,50)
    print("\nx2 =",x2)
    for i in range(1,x2+1):
        x2 = i
        #prints the iteration number and calls factorial_while with x2
        print("Iteration",i,"=",factorial_while(x2))

##MAIN CODE
main() 
    
