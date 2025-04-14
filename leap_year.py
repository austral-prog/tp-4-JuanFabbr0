def leap_year():
	año = int(input("Ingrese un año: "))
	if año%400 == 0:
		year = "es bisiesto"
	elif año%100 == 0:
		year = "no es bisiesto"
	elif año%4 == 0:
		year = "es bisiesto"
	else:
		year = "no es bisiesto"
	print(f"El año {año} {year}")
