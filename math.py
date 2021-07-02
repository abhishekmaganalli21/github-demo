#Add implementation using pull command
def add(x,y):
    return x+y
#Subtract inplementation
def subtract(x,y):
    return x-y          #on bug456 branch
#Multiply inplementation
def multiply(x,y):
    return x*y      #on master branch
#Divide inplementation
def divide(x,y):
    if y==0:        #on bug789 branch
        return error
       else:
        return x/y
