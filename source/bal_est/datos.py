import pandas as pd
from bal_est.config import Config


class Datos:
    """Convertimos los datos extraidos de las web en una datafram de pandas para después
    pasarlos a una archivo csv"""
    def __init__(self):
        pass
    
    
    def crear_df(list_cabeceras):
        """Creamos la cabecera del DataFrame, con los 20 valores de las estadísticas, a los que 
        añadimos las columnas para la temporada y la liga"""
        Datos.datos = pd.DataFrame(columns = list_cabeceras)
        Datos.datos['Temporada'] = None
        Datos.datos['Liga'] = None
        
    
    def generar_df(list_estadisticas, temporada, liga):
        """Los datos extraidos de la web tienen 20 atributos, a los cuales les añadimos
        la temporada y la liga. Vamos añadiendo por filas, para saber el número de filas
         extraidas dividimos el total de datos entre los 20 atributos, necesitamos definir
          una variable auxilar j para compensar los desplazamientos """
        inicio = 0
        fin = 20
        Config.j += 1
        for i in range(int(len(list_estadisticas)/Config.variables)):

            fila = list_estadisticas[inicio:fin]
            fila.append(temporada)
            fila.append(liga)
            Datos.datos.loc[i+Datos.datos.shape[0]+Config.j] = fila
            inicio = fin
            fin = fin + 20


    def generar_csv():
        #Guardamos el archivo csv con los datos extraidos
        Datos.datos.to_csv("baloncesto_est.csv", index = 0)
