from fastapi import FastAPI    # Nos ayuda a crear la API
from pydantic import BaseModel # Ayuda a validar datos 
from typing import Optional    # Valida datos pero permite ciertas variables
from Gauss import Gauss        # Nuestra clase de extracción
numero = Gauss()
app = FastAPI()
#Ruta para appi
#http://127.0.0.1:8000
# '@' Es un decorador
#Un decorador modifica a la funcion 
#En este caso solo registra la funcion
#Cuando alguien llame a la ruta con get, quiero que se ejecute la funcion sig. 

'''class Libro(BaseModel): #La clase BaseModel garantizara el tipo de dato(Validación de datos)
    titulo: str
    autor: str
    paginas: str
    editorial: Optional[str]  #Atributo editorial, es opcional str'''

@app.get('/') # '/' ruta raíz.
def index():
    return {"message" : '''
*************************************
*****        Bienvenido         *****
*En este programa eligiras un numero*
*        del 1 - 100                *
*  Nos encargaremos de extraerlo    *
*          del conjunto             *
*    Gracias por confiar en NT      *
*************************************
'''}                        # Fastapi lo convertira a Json

@app.get("/numeros/{id}")
def mostrar_libro(id: int): # Especificamos que id sea entero 'id: int'
                            # En este caso el usuario quitara el número indicandolo en la barra de busqueda, de la siguiente manera:
                            # http://127.0.0.1:8000/numeros/<numero a retirar>
    num_Encontar = id       # Utilizamos una variable auxiliar para guardar lo proporcinado por el usuario.
    if num_Encontar > 0  and num_Encontar < 101: # Validamos rango.

            r = numero.extract(num_Encontar)     # Validamos acción realizada r = 1. 
            if r == 1:
                #print("--> Procesando tu información...")
                num_Encontar =numero.encontrar()                                    # Lo guardamos como auxiliar.
                numero.generar()                                                    # Generamos lista original
                return "--> El numero que se extrajo fue: {}".format(num_Encontar) # Muestra al usuario el número faltante.
                
                #opcion= input(" -->  ¿Desea realizar otra operacion?  S/N ").upper()
            else:           # Acción sin exito r = 0. 
                return "--> Acción sin exito"
                #print("No se retiro el número")
               # opcion= input(" -->  ¿Desea realizar otra operacion?  S/N ").upper()
                #numero.generar()

    else:
        
            return " -->   Por favor ingrese un número en rango permitido: 1 - 100 usando el formato : http://127.0.0.1:8000/numeros/<numero a retirar> "
            #opcion= input(" -->  ¿Desea intentarlo de nuevo?  S/N ").upper()

