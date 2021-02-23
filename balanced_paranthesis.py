# -*- coding: utf-8 -*-

from MyStack import MyStack

FILENAME = './data/input.txt'
pattern = ['(', '[' , '{']
antipattern = [')', ']', '}']
negative = {')':'(', ']':'[' , '}':'{'}

with open(FILENAME) as f:
    content = f.readlines()
 
content = [x.strip() for x in content] 
   
for line in content:
    
    stack = MyStack()
    
    print('------------------------------------------------------------------------')
    print('Input  : ', line)
    
    isCorrect = True
    isString = False
    
    for c in  line:
            
        if(c == "'"):
            isString = not isString
            
        if(isString):
            continue
        
        else:    
            if(c in pattern):
                stack.push(c)
                print('Open     : Push ', c, 'Stack Contents: ', stack.print_stack())
                
            elif(c in antipattern):
                if(stack.top() == negative[c]):
                    stack.pop()
                    print('Closed    : Pop ', c,' Stack Contents: ', stack.print_stack())
                else:
                    isCorrect = False
            else:
                continue
    
    if(stack.get_size() != 0):
        isCorrect = False
        
    print('Final Stack : Stack Contents: ', stack.print_stack())
    print('Answer: Expression is ', 'correct' if isCorrect else 'incorrect')