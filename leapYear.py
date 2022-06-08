test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

def is_year_leap(yr):
	if yr % 4 != 0: #Si no es divisible en 4 es común
		return False
	elif yr % 100 !=0: #Si no es divisible en 100 es bisiesto
		return True
	elif yr % 400 != 0: # si no es divisible en 400 es común
		return False
	else:
		return True 

for i in range(len(test_data)): #iteramos los datos del test
	yr = test_data[i] #definimos el parametro de la funcion
	print(yr,"->",end="")
	result = is_year_leap(yr) #asignamos la funcion a la variable result
	if result == test_results[i]: #revisamos la variable result
		if result == True:
			print("True")
		elif result == False:
			print("False")
	else:
		print("Fallido")

#Se me quemó una neurona en este
