
from random import randint,random,uniform #Libreria

#a=randint(1,100) #Genera aleatorio de un rango a-b proporcionado
#b=uniform(0,10)#Numero decimal
#c=random()
lista = []
natural = 1
encontrado = 0
for i in range(100): #crea la lista para los 100 números naturales
    lista.append(natural)
    natural = natural + 1

print(lista)
#print("Lista creada")
num_Encontar = int(input("Ingrese el número que quiere encontrar  en la lista:  ")) 

for j in range(len(lista)-1,-1,-1): #Busca en el tamaño de la lista (Parte del ultimo elemento, hasta -1 para pasar por cero, de atras hacia adelante)
    if num_Encontar == lista[j]:
        #print("El numero {} se ha encontrado en la posicion {}".format(num_Encontar,j ))
        extraer = lista.pop(j)#Metodo pop, extrae
        print(extraer)
        print(lista)
        break


encontrado = 5050 - sum(lista)
print("El numero extraido fue:  {} ".format(encontrado))