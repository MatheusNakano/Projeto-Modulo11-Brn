from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_informacoes(self):
        print(f"Funcionário: {self.nome} | Idade: {self.idade} | Salário: {self.salario}€")


class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, bonus):
        super().__init__(nome, idade, salario)
        self.bonus = bonus

    def mostrar_informacoes(self):
        total = self.salario + self.bonus
        print(f"Gerente: {self.nome} | Idade: {self.idade} | Salário Base: {self.salario}€ | Bónus: {self.bonus}€ | Total: {total}€")

    def gerar_relatorio(self, funcionarios):
        print("\n--- RELATÓRIO DE FUNCIONÁRIOS (GERADO PELO GERENTE) ---")
        for f in funcionarios:
            f.mostrar_informacoes()


class Recepcionista(Funcionario):
    def __init__(self, nome, id_func, idade, salario, turno):
        super().__init__(nome, idade, salario)
        self.id_func = id_func
        self.turno = turno

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, turno):
        if turno.lower() in ["manhã", "tarde", "noite"]:
            self._turno = turno.lower()
        else:
            print("Turno inválido! Mantenha: manhã, tarde ou noite.")
            self._turno = "manhã"

    def mostrar_informacoes(self):
        print(f"Recepcionista: {self.nome} (ID: {self.id_func}) | Idade: {self.idade} | Turno: {self.turno} | Salário: {self.salario}€")

    def registar_hospede(self, hospede, lista_hospedes):
        lista_hospedes.append(hospede)
        print(f"Hóspede {hospede.nome} registado com sucesso!")

    def listar_hospedes(self, lista_hospedes):
        print("\n--- LISTA DE HÓSPEDES ---")
        for hospede in lista_hospedes:
            hospede.mostrar_informacoes()


class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, salario, especialidade):
        super().__init__(nome, idade, salario)
        self.especialidade = especialidade

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self._especialidade = especialidade

    def mostrar_informacoes(self):
        print(f"Técnico de Manutenção: {self.nome} | Idade: {self.idade} | Especialidade: {self.especialidade} | Salário: {self.salario}€")

    def registar_reparo(self, descricao):
        print(f"Reparo registado por {self.nome}: {descricao}")