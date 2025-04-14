import math
def line():
	CoeficienteA = float(input("Ingrese el Coeficiente A: "))
	CoeficienteB = float(input("Ingrese el Coeficiente B: "))
	CoeficienteX1 = float(input("Ingrese el Coeficiente X1: ")) 
	CoeficienteX2 = float(input("Ingrese el Coeficiente X2: "))
	print(f"El coeficiente A de su ecuación de la recta es: {CoeficienteA}")
	print(f"El coeficiente B de su ecuación de la recta es: {CoeficienteB}")
	print(f"El coeficiente X1 de su ecuación de la recta es: {CoeficienteX1}")
	print(f"El coeficiente X2 de su ecuación de la recta es: {CoeficienteX2}\n")

	print(f"Para la siguiente ecuación:\n\tY = {CoeficienteA}X + {CoeficienteB}\n")

	y1 = CoeficienteA * CoeficienteX1 + CoeficienteB
	y2 = CoeficienteA * CoeficienteX2 + CoeficienteB

	print(f"Dados los siguientes puntos:")
	print(f"\tP1 ({CoeficienteX1}, {y1})")
	print(f"\tP2 ({CoeficienteX2}, {y2})\n")

	Distancia = math.sqrt((CoeficienteX1 - CoeficienteX2)**2 + (y1 - y2)**2)
	print(f"La distancia entre ellos es: {Distancia}")
