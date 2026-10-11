from pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, nome, idade, dias_estadia, quarto=None):
        super().__init__(nome, idade)
        self.dias_estadia = dias_estadia
        self._quarto = None

        if quarto is not None:
            self.atribuir_quarto(quarto)

    @property
    def quarto(self):
        return self._quarto

    @quarto.setter
    def quarto(self, quarto):
        if quarto is not None:
            if not quarto.ocupado:
                self._quarto = quarto
                quarto.ocupado = True
            else:
                print("Aviso: O quarto selecionado já se encontra ocupado!")

    def atribuir_quarto(self, quarto):
        self.quarto = quarto

    def calcular_conta(self):
        if self.quarto:
            return self.dias_estadia * self.quarto.preco_diaria
        return 0

    def mostrar_informacoes(self):
        num_quarto = self.quarto.numero if self.quarto else "Nenhum"
        print(f"Hóspede: {self.nome} | Idade: {self.idade} | Dias de Estadia: {self.dias_estadia} | Quarto: {num_quarto}")

    def checkout(self):
        if self.quarto:
            self.quarto.ocupado = False
            self._quarto = None
            print("Checkout realizado com sucesso e quarto libertado!")