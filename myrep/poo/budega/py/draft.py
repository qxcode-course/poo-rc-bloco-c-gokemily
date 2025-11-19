class Cliente:
    def __init__(self, nome: str):
        self.__nome = nome
    def getNome(self) -> str:
        return self.__nome
    def __str__(self) -> str:
        return f"{self.getNome()}"

class Mercantil:
    def __init__(self, qtdCaixas: int):
        self.__caixas: list[Cliente] | list[None] = [None for i in range(qtdCaixas)]
        self.__fila: list[Cliente] = []

    def getFila(self) -> list[Cliente]:
        return self.__fila

    def getCaixas(self) -> list[Cliente] | list[None]:
        return self.__caixas

    def __str__(self) -> str:
        string = 'Caixas: ['
        for i in self.getCaixas():
            string += '-----' if i == None else str(i)
            string += ', '
        string = string[0:-2]
        string += ']\nEspera: ['
        for i in self.getFila():
            string += str(i)
            string += ', '
        string = string[0:-2] if string[-1] == ' ' else string
        string += ']'
        return string
    
    def Chegar(self, cliente: Cliente) -> None:
        self.getFila().append(cliente)

    def Chamar(self, indice: int) -> None:
        if len(self.getFila()) == 0:
            print('fail: sem clientes')
        elif self.getCaixas()[indice] != None:
            print('fail: caixa ocupado')
        else:
            self.getCaixas()[indice] = self.getFila()[0]
            self.getFila().pop(0)

    def Finalizar(self, indice: int) -> Cliente | None:
        if len(self.getCaixas()) < indice + 1 or indice < 0:
            print('fail: caixa inexistente')
        elif self.getCaixas()[indice] == None:
            print('fail: caixa vazio')
        else:
            atendido = self.getCaixas()[indice]
            self.getCaixas()[indice] = None
            return atendido

def main():
    mercantil = Mercantil(3)
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)

        if arg[0] == "end":
            break
        elif arg[0] == "arrive":
            mercantil.Chegar(Cliente(arg[1]))
        elif arg[0] == "call":
            mercantil.Chamar(int(arg[1]))
        elif arg[0] == "finish":
            mercantil.Finalizar(int(arg[1]))
        elif arg[0] == "show":
            print(mercantil)
        elif arg[0] == "init":
            mercantil: Mercantil = Mercantil(int(arg[1]))
        else:
            print("fail: comando nao existe")

main()