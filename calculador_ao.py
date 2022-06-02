year = int(input("Introduce un año:"))

if  year < 1585:
    print("No está dentro del periodo del calendario Gregoriano")
elif year % 4 != 0 and year % 400 != 0: #si el año no es divisible en 4
    print("Año común")
else: 
    year % 100 != 0 and year >= 1585 #Si el año no es divisible en 100
    print ("Año bisiesto")
 
   
