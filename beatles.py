Beatles = []
print("Paso 1:", Beatles)

Beatles.append ("John Lennon")
Beatles.append ("Paul McCartney")
Beatles.append ("George Harrison")
print("Paso 2:", Beatles)


for i in range(2):
    Beatles.append (input("Ingresa los nombres: "))
print("Paso 3:", Beatles)

for i in range(2):
    del Beatles [-1]
print("Paso 4:", Beatles)

Beatles.insert (0, "Ringo Starr")
print("Paso 5:", Beatles)

# probando la longitud de la lista
print("Los Fav", len(Beatles))
