lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list = []
copia = list(lista) #se copia la lista para que la tome en el bucle for

for i in copia: #otro metodo es con in range(len(lista)-1,-1,-1) para que empieze desde 9
    if i not in my_list:
        my_list.append(i)
    else:
        lista.remove(i)


print("La lista con elementos únicos:")
print(my_list)
