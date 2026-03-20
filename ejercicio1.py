longitud1 = float(input("Dame la longitud de un lado del triangulo: "))
longitud2 = float(input("Dame la longitud del otro lado del triangulo: "))
longitud3 = float(input("Dame la longitud del ultimo lado del triangulo: "))

if longitud1 == longitud2 and longitud1 == longitud3:
    print("equilatero")
    
elif longitud1 == longitud2 or longitud1 == longitud3 or longitud2 == longitud3:
    print("isosceles")
    
else:
    print("escaleno")
    
    
    