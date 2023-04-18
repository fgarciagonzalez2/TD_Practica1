
import sys
from bal_est.enlace_app import Enlace
from bal_est.bal_est import WebScrap



def main(args= None):
    """ Aplicación para extraer mediante web scraping los datos estadísticos de varias
    ligas de baloncestos de las últimas 10 temporadas completas. En el módulo config.py
    se encuentra configurada la url a la que accedemos"""

    if args is None:
        args= sys.argv[1:]


    if (Enlace.internet_ok() & Enlace.response_ok()):
        print("La conexión es correcta, podemos seguir.")
        iniciar = WebScrap()
        iniciar.empezar()



if __name__ == "__main__":
    sys.exit(main())