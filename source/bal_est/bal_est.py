
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from bal_est.config import Config
from bal_est.datos import Datos


class WebScrap:
    """Extraemos mediante selenium los datos de la web con las estadísticas de baloncesto.
     Las ligas de las que extremos los datos son la LF Endesa, LEB Oro y LEB PLata """
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(1)
        user_agent = self.driver.execute_script("return navigator.userAgent") 
        self.driver.get(Config.url)
        time.sleep(3)


    def empezar(self):  
        """ Extraemos los datos para la cabecera del DataFrame y después extraemos los datos
        de cada una de las tres ligas. Una vez extraidos los datos generamos y guardamos en
         dicos el archivo csv"""
        
        Datos.crear_df(WebScrap.obtener_cabecera(self))
        WebScrap.lf_endesa(self)
        principal = self.driver.find_element(By.XPATH, '/html/body/form/div[2]/a/img').click()
        WebScrap.leb_oro(self)
        principal = self.driver.find_element(By.XPATH, '/html/body/form/div[2]/a/img').click()
        WebScrap.leb_plata(self)
        Datos.generar_csv()
        self.driver.close()


    def lf_endesa(self):

        #A esta liga ya hemos accedido para extrar la cabecera
        WebScrap.liga = "LF Endesa"
        time.sleep(3)
        i = 0
        while i< Config.anyos_extraer:
            WebScrap.anno, WebScrap.competicion = WebScrap.obtener_selec_endesa(i)
            WebScrap.recolectar(self)
            i +=1
            time.sleep(3)
            # Hacemos un seguimiento de por donde vamos extrayendo
            print(f"{i} extrayendo datos liga {WebScrap.liga}")
        
    def leb_oro(self):

        self.leb_oro_est = self.driver.find_element(By.XPATH, "/html/body/form/div[4]/div/div[3]/div/div[3]/div[2]/a[1]").click()
        WebScrap.liga = "LEB Oro"
        time.sleep(3)
        i = 0
        while i< Config.anyos_extraer:
            WebScrap.anno, WebScrap.competicion = WebScrap.obtener_selec_leboro(i)
            if WebScrap.competicion == 'Liga Regular "A"':
                WebScrap.recolectar(self)
                WebScrap.competicion = 'Liga Regular "B"'
                WebScrap.recolectar(self)
                i +=1
                time.sleep(3)
                # Hacemos un seguimiento de por donde vamos extrayendo
                print(f"{i} extrayendo datos liga {WebScrap.liga}")
            else:
                WebScrap.recolectar(self)
                i +=1
                time.sleep(3)
                # Hacemos un seguimiento de por donde vamos extrayendo
                print(f"{i} extrayendo datos liga {WebScrap.liga}")
        
    
    def leb_plata(self):

        self.lf_challenge_est = self.driver.find_element(By.XPATH, "/html/body/form/div[4]/div/div[3]/div/div[5]/div[2]/a[1]").click()
        WebScrap.liga = "LEB Plata"
        time.sleep(3)
        i = 0
        while i< Config.anyos_extraer:
            WebScrap.anno, WebScrap.competicion = WebScrap.obtener_selec_lebplata(i)
            if WebScrap.competicion == 'Liga Regular "Este"':
                WebScrap.recolectar(self)
                WebScrap.competicion = 'Liga Regular "Oeste"'
                WebScrap.recolectar(self)
                i +=1
                time.sleep(3)
                # Hacemos un seguimiento de por donde vamos extrayendo
                print(f"{i} extrayendo datos liga {WebScrap.liga}")
            else:
                WebScrap.recolectar(self)
                i +=1
                time.sleep(3)
                # Hacemos un seguimiento de por donde vamos extrayendo
                print(f"{i} extrayendo datos liga {WebScrap.liga}")
    
    def obtener_cabecera(self):
        self.lf_endesa_est = self.driver.find_element(By.XPATH, "/html/body/form/div[4]/div/div[3]/div/div[2]/div[2]/a[1]").click()
        time.sleep(5)
        self.cabecera = self.driver.find_elements(By.TAG_NAME, "th")
        list_cabeceras = WebScrap.datos_cabeceras(self.cabecera)
        return list_cabeceras 


    def recolectar(self):

        selec_año = Select(self.driver.find_element(By.XPATH, '//*[@id="_ctl0_MainContentPlaceHolderMaster_temporadasDropDownList"]'))
        selec_año.select_by_visible_text(WebScrap.anno)
        time.sleep(5)

        selec_comp= Select(self.driver.find_element(By.XPATH, '//*[@id="_ctl0_MainContentPlaceHolderMaster_fasesGruposDropDownList"]'))
        selec_comp.select_by_visible_text(WebScrap.competicion)
        time.sleep(5)
    
        
        if Config.obtener_medias:
            medias = self.driver.find_element(By.XPATH, "/html/body/form/div[4]/div[2]/div[2]/label/span").click()
            time.sleep(5)

        self.estadisticas = self. driver.find_elements(By.TAG_NAME, 'td')
        list_estadisticas = WebScrap.datos_estadisticas(self.estadisticas)


        Datos.generar_df(list_estadisticas, WebScrap.anno, WebScrap.liga) 

    
    def obtener_selec_endesa(i):
    
        return Config.lista_anyos[i], Config.lista_competicion_endesa[i]
    
    def obtener_selec_leboro(i):
   
        return Config.lista_anyos[i], Config.lista_competicion_leboro[i]

    def obtener_selec_lebplata(i):
   
        return Config.lista_anyos[i], Config.lista_competicion_lebplata[i]
    
    
    def datos_cabeceras(cabecera):

        list_cabeceras = []
        for elemento in cabecera:
            list_cabeceras.append(elemento.text)
        list_cabeceras = list_cabeceras[7:]
        return list_cabeceras
        

    def datos_estadisticas(estadisticas):

        list_estadisticas = []
        for valor in estadisticas:
            list_estadisticas.append(valor.text)
        return list_estadisticas
    





