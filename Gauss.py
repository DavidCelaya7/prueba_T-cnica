
'''Esta es una clase para extraer y encontrar un número en los primeros 101 números naturales.'''

lista = []                              # Declaramos nuestra lista global en donde trabajaremos.

class Gauss:
    def __init__(self):                 # Constructor.
        natural = 0                     # Iniciamos la variable natural en 0.
        for i in range(101):            # Crea la lista para los 101 números naturales.
            lista.append(natural)       # Agregamos cada número a la lista.
            natural = natural + 1       # Aumentamos uno para la siguiente ronda.

    def extract(self,num_Econtrar):     # Método extraer, recibe el número por el usuario.
        num = num_Econtrar              # Declaramos una variable auxiliar llamada num.
        for j in range(len(lista)-1,-1,-1): # Busca en el tamaño de la lista (Parte del ultimo elemento, hasta -1 para pasar por cero, de atras hacia adelante)
            
            if num == lista[j]:         # Buscamos la posición del número del usuario en la lista.
                #print("El numero {} se ha encontrado en la posicion {}".format(num_Encontar,j ))
                extraer = lista.pop(j)  # Método pop, extraera el número de la posición encontrada.
                #print(extraer)
                print("--> Los números que quedaron fueron...\n") # Realiza feedback de la lista sin el del elemento como comprobación.
                print(lista)            # Imprime lista sin elemento.
                print("\n")
                aux = 1                 # Segunda variable auxiliar, regresa 1 en caso de haber realizado la acción de manera exitosa.
                break
            else:
                aux = 0                 # La acción no se pudoo completar,
        return aux                      # Retorno de varible.
        

    def encontrar(self):                # Método encontrar.

        num_Extract = 5050 - sum(lista) # Método de Gauss  y como resultado encontraremos el número extraido.
        #print("El número faltante es:  {} ".format(num_Extract))
        return num_Extract              # Regresamos el número faltante.

    def generar(self):                  # Método para formar de nuevo la lista original.
        lista.clear()                   # Borramos lista vieja.
        natural = 0                        
        for i in range(101):            # Crea la lista para los 101 números naturales dentro de una listclsa
            lista.append(natural)
            natural = natural + 1