
import mysql.connector                                      # Importamos el conector Python -> mysql.
import pandas as pd                                         # Importamos pandas para trabajar con dataFrame. 
from datetime import datetime                               # Importamos para filtrar fechas.


cnn = mysql.connector.connect(host="localhost", user="root", passwd="Cosmos99#", database="prueba_tecnica") # Iniciamos la coneccion.
                                                            # Sintaxis: host: <direccion>, user: <name_user>, passwd: <user_password>, database: <data_name>.

cursor = cnn.cursor()                                       # Obtenemos un cursor, objeto que me permite realizar consultas.
sql = "select id, name, company_id, amount, status, created_at, paid_at from data_prueba_tecnica "   # selct <serch_1>,<serch_2> from <name_table> 
cursor.execute(sql)                                         # Recorremos la base de datos.

datos = cursor.fetchall()                                   # Obtenemos todas las coincidencias y almacenamos en datos.

all_id = []
all_name = []                                               # Creamos dos listas auxiliares, donde almacenaremos los datos.
all_company_id = []
all_amount = []
all_status =[]
all_created_at = []
all_paid_at =[]

for id, name, company_id, amount, status, created_at, paid_at in datos:     # Obtenemos para cada id sus datos de la compañia.
    all_id.append(id[:24])                                                  # Agregamos y filtramos id_varchar(24)    
    all_name.append(name[:130])                                             # Agregamos y filtramos company_name(130)     
    all_company_id.append(company_id[:24])                                  # Agregamos y filtramos company_id(24)
    all_amount.append("{:.2f}".format(amount))                              # Agregamos y filtramos decimal(16,2)
    all_status.append(status[:30])                                          #  Agregamos y filtramos status_marchar(30)
    all_created_at.append(datetime.strptime(created_at, '%Y-%m-%d').date()) #  Agregamos y filtramos timestamp "year-month-day"
    all_paid_at.append(paid_at)                                              #  Agregamos y filtramos timestamp "year-month-day" problemas espacios

                                                                     # Usamos un diccionario para almacenar {'key': <value_1> }    
dic = {'Id': all_id, 'Name': all_name, 'Company_id': all_company_id, 'Amount' : all_amount, 'Status': all_status, 'Created_at':all_created_at, 'Paid_at':all_paid_at }    
df = pd.DataFrame(dic)                                                   # Estructura de datos con dos dimensiones
df_csv = df.to_csv('C:/Users/david/Desktop/archivos_prueba/prueba_tecnica.csv') # Se convierte el df a .csv <especificar ruta con 'Ruta/<nombre_Archivo.csv>'> 
