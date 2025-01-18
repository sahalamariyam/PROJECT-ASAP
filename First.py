#PROGRAM FOR SIMPLE CALCULATOR
op=input("1.ADDITION\n 2.SUBTRACTION\n 3.MULTIPLICATION\n 4.DIVISION\n 5.EXIT\n")
if op>=1 and op<=4:
    num1=float(input("ENTER YOUR FIRST NUMBER\n"))
    num2=float(input("ENTER YOUR FIRST NUMBER\n"))
    if op==1:
        print("SUM IS:",num1+num2)
    elif op==2:
        print("DIFFERENCE IS:",num1-num2)
    elif op==3:
        print("PRODUCT IS:",num1*num2)
    elif op==4:
        if num2==0:
            print("DIVISION BY ZERO NOT POSSIBLE:\n")
        else:
            print("QUOTIENT IS:",num1/num2)
    elif op==5:
        exit(0)
    else:
        print("INVALID CHOICE\n")

else:
    print("INVALID OPERATOR\n")            
        
            




