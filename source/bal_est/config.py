
class Config:
    """Configuramos las variables iniciales"""

    url = "https://competiciones.feb.es/estadisticas/"

    anyos_extraer = 10   
    variables = 20
    obtener_medias = False
    j = 0

    lista_completa = []
    cabecera = []

    lista_anyos = ['2021/2022','2020/2021','2019/2020','2018/2019','2017/2018',
                   '2016/2017','2015/2016','2014/2015','2013/2014','2012/2013']

    lru = 'Liga Regular Único'
    lrf = 'Liga Regular 2ª Fase "A1"'

    lista_competicion_endesa = [lru,lru,lru,'Liga Regular',lru,lru,lru,lru,
                                    'Liga Regular Grupo Unico',lru]  
    
    lista_competicion_leboro = [lru,'Liga Regular "A"',lru,'Liga Regular',
                                    lru,lru,lru,lru,lru,lru]

    lista_competicion_lebplata = ['Liga Regular "Este"','Liga Regular "Este"', lrf,
                                  lrf,lru,lru,lru,lru,'Liga Regular Unico',lru]

    def __init__(self):
        pass