a = int(input(" enter first number :"))
b = int(input(" enter second number :"))
symbol = (input(" choose a symbol ( + , - , * , / ): "))
if symbol == "+" :
    print (a + b)
elif symbol == "-" :
    print  (a - b)
elif symbol == "*" :
    print (a * b)
elif symbol == "/" :
    print (a / b)
else : 
    print ("Invalid Symbol")

print ("Thanks for using my calculator")
