
while True :
    gauge = input("Fraction: ")
    try:
        f= numerator, denominator = gauge.split("/")
        X = int(numerator)
        Y = int(denominator)
        f = X/Y
        if f<=1:
            break
    except (ValueError, ZeroDivisionError):
        pass 
p = int ( f * 100)

if p <=1:
    print("E")
elif p >=99:
    print("F")
else:
    print("f{p}%")    
