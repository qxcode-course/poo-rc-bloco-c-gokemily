class Clientes:
    def __init__(self, nome: str):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f"{self.__nome}"


class Mercantil:
    def __init__(self, caixa: int):
        self.__caixas = [None]
        self.__fila = []













# def __str__(self):