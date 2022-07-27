var1 = int(input("enter the first number : "))
var2 = int(input("enter the second number : "))
var3 = input('select one operetor (+,-,/,*) :')

if var3=='+':
    print(f"{var1+var2}")
elif var3=='-':
    print(f"{var1-var2}")
elif var3=='/':
    print(f"{var1/var2}")
elif var3=='*':
    print(f"{var1*var2}")
else:
    print("thank you")
