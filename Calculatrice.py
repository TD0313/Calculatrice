A = float(input("La valeur de A :"))
B = float(input("La valeur de A :"))
Op = input("Choissisez un opérateur :")
if Op == "+":
    print ("A+B =",A+B)
elif Op == "-":
    print ("A-B =",A-B)
elif Op == "/":
    if B != 0:
        print ("A/B =",A/B)
    else :
        print ("Incorrect")
elif Op == "*":
    print ("A*B =",A*B)
else :
    print ("Incorrect")

