from abc import ABC, abstractmethod

class Quarto(ABC):
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self._ocupado = False

    @property
    def ocupado(self):
        return self._ocupado

    @ocupado.setter
    def ocupado(self, valor):
        self._ocupado = valor

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, valor):
        if valor < 0:
            raise ValueError("Preço da diária não pode ser negativo!")
        self._preco_diaria = valor

    @abstractmethod
    def mostrar_informacoes(self):
        pass


class QuartoSimples(Quarto):
    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "Simples", preco_diaria)

    def mostrar_informacoes(self):
        status = "Sim" if self.ocupado else "Não"
        print(f"Quarto: {self.numero} | Tipo: {self.tipo} | Preço/Dia: {self.preco_diaria}€ | Ocupado: {status}")


class QuartoLuxo(Quarto):
    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "Luxo", preco_diaria)

    def mostrar_informacoes(self):
        status = "Sim" if self.ocupado else "Não"
        print(f"Quarto: {self.numero} | Tipo: {self.tipo} | Preço/Dia: {self.preco_diaria}€ | Ocupado: {status}")