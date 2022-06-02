blocks = int(input("Ingresa el número de bloques: "))
height = 0
inline = 1
while inline <= blocks:
    blocks -= inline
    inline += 1
    height +=1
print("La altura de la pirámide:", height)