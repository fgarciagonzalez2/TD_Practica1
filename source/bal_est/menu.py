
from api_esios import Esios
from ent_datos import Fechas
from config import Config
from limpia_screen import Limpia
from ent_datos import Indicador

class Menu():
    """Clase con las funciones referentes al Menú. Tenemos 10 opciones incluyendo salir.
    Cada opción establece la configuración necesaria para conectarse a la API de ESIOS y
    después acceder a la función correspondiente de la clase ESIOS. La función menu es la 
    que se llama desde el punto de entrada en main."""

    def __init__(self):
        pass


    def elegir_opcion(self):
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("Introduce la opción elegida: "))
                correcto=True
            except ValueError:
                print('Error, por favor introduce una opción válida\n')
        return num
    

    def menu(self):
        salir = False
        opcion = 0
        Limpia.limpia_pantalla(self)
        while not salir:
            print("===========================================================================================")
            print("\nAPI ESIOS PARA DESCARGAR INFORMACIÓN DEL SISTEMA ELÉCTRICO DE ESPAÑA (C) 1992")
            print("Información y documentación se puede  consultar en https://api.esios.ree.es\n")
            print("1. Demanda eléctrica intervalo de tiempo Islas Canarias")
            print("2. Precios para el día de hoy por horas de energía del PVPC (Mercado Regulado) 2.0TD Canarias")
            print("3. Precios medios de la generación y la demanda subsistema Lanzarote-Fuerteventura")
            print("4. Descargar archivo con listado de indicadores")
            print("5. Descargar datos de otro Indicador")
            print("6. Descarga archivo con listado de códigos de archivos descargables")
            print("7. Descargar archivo")
            print("8. Generación Fotovoltáica SNP")
            print("9. Generación Eólica SNP")
            print("10. Salir")
            print ("\nElige una opcion\n")
    
            opcion = self.elegir_opcion()
    
            if opcion == 1:
                self.opcion_1()    
            elif opcion == 2:
                self.opcion_2()
            elif opcion == 3:
                self.opcion_3()
            elif opcion == 4:
                self.opcion_4()
            elif opcion == 5:
                self.opcion_5()
            elif opcion == 6:
                self.opcion_6()
            elif opcion == 7:
                self.opcion_7()
            elif opcion == 8:
                self.opcion_8()
            elif opcion == 9:
                self.opcion_9()
            elif opcion == 10:
                salir = True
            else:
                print ("Elige una opción válida\n")
        
        Limpia.limpia_pantalla(self)
        print ("Adios, gracias por usar")
        

    def opcion_1(self):
        Config.fecha_inicio_esios, Config.fecha_fin_esios = Fechas.obtener_intervalo_fechas(self)
        Config.question_esios = 'indicators/'
        Config.indicador_esios = Indicador.seleccion_indicador_demanda(self)
        Esios.acceso_esios(self)
        Esios.extraer_datos_esios(self)

    def opcion_2(self):
        Config.fecha_inicio_esios, Config.fecha_fin_esios, Config.fecha_esios = ("", "", "")
        Config.question_esios = 'indicators/'
        Config.indicador_esios= Config.indicador_precios
        Config.time_agg= 'sum'
        Config.time_trunc= 'hour'
        Config.geo_agg= 'sum'
        Config.geo_ids= ''
        Config.geo_trunc= ''
        Esios.acceso_esios(self)
        Esios.precios_diario_energia(self)

    def opcion_3(self):
        Config.fecha_inicio_esios, Config.fecha_fin_esios = Fechas.obtener_intervalo_fechas(self)
        Config.question_esios = 'indicators/'
        Config.geo_ids= 8796
        indicadores = Config.indicador_precios_dem_gen 
        Esios.precios_medios_gen_dem(self, indicadores)

    def opcion_4(self):
        Config.fecha_inicio_esios, Config.fecha_fin_esios, Config.fecha_esios = ("", "", "")
        Config.question_esios = 'indicators/'
        Config.indicador_esios= ""
        Esios.acceso_esios(self)
        Esios.lista_indicadores(self)

    def opcion_5(self):
        if not Config.lista_indicadores: 
            self.opcion_4() #Si no hemos descargado antes la lista de indicadores de lo hacemos ahora
        Config.fecha_inicio_esios, Config.fecha_fin_esios = Fechas.obtener_intervalo_fechas(self)
        Config.question_esios = 'indicators/'
        Config.indicador_esios= Indicador.obtener_indicador_esios(self, Config.lista_indicadores)
        Esios.acceso_esios(self)
        Esios.otro_indicador(self)

    def opcion_6(self):
        Config.fecha_inicio_esios, Config.fecha_fin_esios, Config.fecha_esios = ("", "", "")
        Config.question_esios = 'archives/'
        Config.indicador_esios = ""
        Esios.acceso_esios(self)
        Esios.lista_archivos(self)
        
    def opcion_7(self):
        if not Config.lista_indicadores_archivos:
            self.opcion_6() #Si no hemos descargado antes la lista de indicadores de archivos lo hacemos ahora
        Config.fecha_inicio_esios, Config.fecha_fin_esios, Config.fecha_esios = ("", "", "")
        Config.question_esios = 'archives/'
        Config.indicador_esios= Indicador.obtener_indicador_esios(self, Config.lista_indicadores_archivos)
        Esios.acceso_esios(self)
        Esios.esios_archivos(self)

    def opcion_8(self):
        Config.fecha_inicio_esios, Config.fecha_fin_esios= Fechas.obtener_intervalo_fechas(self)
        Config.question_esios = 'indicators/'
        Config.indicador_esios= '1748' # Indicador de Generació Real Fotovoltáica SNP
        Config.time_agg= 'sum'
        Config.time_trunc= 'day'
        Config.geo_agg= 'sum'
        Config.geo_ids= ''
        Config.geo_trunc= 'electric_subsystem'
        Esios.acceso_esios(self)
        identificador_geografico= Indicador.seleccion_identificador_geográfico(self)
        Esios.generacion_fv(self, identificador_geografico)

    def opcion_9(self):
        Config.fecha_inicio_esios, Config.fecha_fin_esios = Fechas.obtener_intervalo_fechas(self)
        Config.question_esios = 'indicators/'
        Config.indicador_esios= '1745' # Indicador de Generació Real Eólica SNP
        Config.time_agg= 'sum'
        Config.time_trunc= 'day'
        Config.geo_agg= 'sum'
        Config.geo_ids= ''
        Config.geo_trunc= 'electric_subsystem'
        Esios.acceso_esios(self)
        identificador_geografico= Indicador.seleccion_identificador_geográfico(self)
        Esios.generacion_eolica(self, identificador_geografico) 

        
