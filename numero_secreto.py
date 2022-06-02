secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number = (int(input("Ingresa el número secreto: ")))
while number != 777:
    if number == 777:
        print ()
    else:
        number = (int(input("Ingresa el número secreto: ")))
 
print ("Lo adivinaste")