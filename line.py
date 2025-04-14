def line():
    print("TO DO")
    CoeficienteA = float(input("Ingrese el Coeficiente A: "))
    CoeficienteB = float(input("Ingrese el Coeficiente B: "))
    CoeficienteX1 = float(input("Ingrese el Coeficiente X1: ")) 
    CoeficienteX2 = float(input("Ingrese el Coeficiente X2: "))
    print(f"El Coeficiente A de su ecuación de la recta es: {CoeficienteA}")
    print(f"El Coeficiente B de su ecuación de la recta es: {CoeficienteB}")
    print(f"El Coeficiente X1 de su ecuación de la recta es: {CoeficienteX1}")
    print(f"El Coeficiente X2 de su ecuación de la recta  es: {CoeficienteX2}\n")
    print(f"Para la siguiente ecuación:\n\t Y= {CoeficienteA}X + {CoeficienteB}\n")
    y1 = CoeficienteA * CoeficienteX1 + CoeficienteB
    y2 = CoeficienteA * CoeficienteX2 + CoeficienteB
    print(f"Dados los siguientes puntos:\t")
    print(f"P1 ({CoeficienteX1}, {y1})\t")
    print(f"P2 ({CoeficienteX2}, {y2})\n")
    Distancia = math.sqrt((CoeficienteX1 - CoeficienteX2)**2 + (y1 - y2)**2)
    print(f"La distancia entre ellos es: {Distancia}")
