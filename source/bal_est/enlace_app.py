import requests
from requests.exceptions import HTTPError
from bal_est.config import Config


class Enlace:
        """ Comprobamos que el equipo tiene conexión a internet y que la web
        es accesible"""
        def __init__(self):
                pass

        def internet_ok():
                try:
                        request = requests.get("https://www.google.com", timeout=5)
                except (requests.ConnectionError, requests.Timeout):
                        print("No hay conexion a internet")
                        return False
                else:
                        return True
                
        def response_ok():
                try:
                        response = requests.get(Config.url ) 
                        response.raise_for_status()
                except HTTPError as http_err:
                        print(f'HTTP Error: {http_err}, no hay conexión con la WEB indicada')
                        return False
                except Exception as err:
                        print(f'Other Error: {err} no hay conexión con la WEB indicada')
                        return False
                else:
                        return True
