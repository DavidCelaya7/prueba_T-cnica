'''El prposito de este scrip es extraer un número dado por el usuario para despues quitarlo de una lista de los 100 primeros números
   naturales. Esto con el proposito de encontrarlo, sin almacenarlo en una cariable.
   Utilizaremos el método de Gauss para poder saber que número fue el que se extrajo.
   Recordemos que los primeros 100 numero naturales suman 5050, es decir, 100+1 = 101, 99+2=101, etc...'''

from Gauss import Gauss         # Nuestra clase de numero desconocidos

numero = Gauss()                # Objeto de nuestra clase


menu = '''                      # Menú de bienvenida.
*************************************
*****        Bienvenido         *****
*En este programa eligiras un numero*
*        del 1 - 100                *
*  Nos encargaremos de extraerlo    *
*          del conjunto             *
*    Gracias por confiar en NT      *
*************************************
'''

def main():         
    opcion= input(" -->  ¿Desea iniciar?  S/N ").upper()    # Mensaje de confirmación para el usuario, convertimos todo a mayuscula,
                                                            # para no tener inconveniente. 
    while opcion != 'N':                                    # Ciclo con finalidad de evitar el cierre o fin del programa.
        print(menu)                                         # Traemos a Ménu.
        num_Encontar = int(input(" --> Ingrese el número que quiere retirar: ")) # Usuario proporciona el número a extraer.
        #num_Encontar = ord(num_Encontar)
        if num_Encontar >= 0  and num_Encontar < 101:                            # Validación que se encuentre en el rango especifico.

            r = numero.extract(num_Encontar)                                     # Guardamos lo que regrese método extract()
            if r == 1:                                                           # r = 1 Extracción correcta.
                print("--> Procesando tu información...\n")                        # Mensaje de cortesia.
                print("--> El numero que se extrajo fue: {} \n".format(numero.encontrar())) # Utilizamos el método encontrar()
                                                                                 # con la finalidad de mostrarle al usuario el número faltante.
                numero.generar()                                                 # Generamos nuevamente la lista original.
                opcion= input(" -->  ¿Desea realizar otra operacion?  S/N \n").upper()   # Validamos si quiere realizar otra acción.
            else:
                print("No se retiro el número")                                        # r = 0 Accion NO completada.
                opcion= input(" -->  ¿Desea realizar otra operacion?  S/N \n").upper()   # Validamos si quiere realizar otra acción.
                numero.generar()                                                  # Generamos nuevamente la lista original.

        else:
            print("-->   Por favor ingrese un número en rango permitido: 1 - 100 \n ")   # Pedimos que ingrese valor valido.
            opcion= input("-->  ¿Desea intentarlo de nuevo?  S/N \n").upper()            # Validamos si quiere realizar otra acción.

    pass



if __name__ == "__main__": 
    main()