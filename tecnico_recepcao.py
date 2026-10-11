from funcionario import Funcionario, Recepcionista, TecnicoManutencao

class TecnicoRecepcao(Recepcionista, TecnicoManutencao):
    def __init__(self, nome, id_func, idade, salario, setor, especialidade):
        Funcionario.__init__(self, nome, idade, salario)
        self.id_func = id_func
        self.turno = "manhã"
        self.especialidade = especialidade
        self.setor = setor

    def registar_reparo(self, descricao):
        print(f"Reparo registado na Receção (Setor {self.setor}) por {self.nome}: {descricao}")

    def mostrar_informacoes(self):
        print(f"Técnico de Receção: {self.nome} (ID: {self.id_func}) | Setor: {self.setor} | Especialidade: {self.especialidade} | Salário: {self.salario}€")