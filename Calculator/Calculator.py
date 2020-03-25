
#import necessary library 
import re

print("This is a simple calculator")
print("Type 'quit' to exit\n")

#define variables
previous = 0
run = True

#define function
def Math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit' :
        print ("Bye")
        run = False
    else: 
        equation=re.sub('[a-zA-Z,.:""()]', '' , equation)

        if previous == 0:
            previuos = eval(equation)
        else:
            previous = eval(str(previous)+ equation)
while run:
    Math()





