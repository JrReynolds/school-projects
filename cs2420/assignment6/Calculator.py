import graphics
import Stack

def inf_post(inf):
    stack = Stack.Stack()
    newStr = ""
    for i in inf:
        if i in "123456789x":
            newStr += i
        if i in "+-*/":
            pass

def main():
    equation = raw_input("Enter an equation to graph\n")
    equation = equation.split()
    print equation

main()