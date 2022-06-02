
palabra= input ("Ingresa una palabra: ")
while palabra != "chupacabra":
    if palabra == "chupacabra":
        break
    else:
        palabra = input("Ingresa una palabra: ")

if palabra == "chupacabra":
    print ("¡Has dejado el bucle con éxito!")
else:
    pass