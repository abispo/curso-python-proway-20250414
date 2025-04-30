"""
Programação Orientada a Objetos

Polimorfismo
-----------

Polimorfismo significa "muitas formas", ou seja, um método pode ser chamado de diferentes formas, tendo diferentes comportamentos
"""

class Funcionario:

    def __init__(self, nome: str):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    def calcular_salario(self):
        # Abaixo estamos lançando a exceção NotImplementedError. Essa exceção geralmente é utilizada quando queremos forçar a implementação de algum método nas classes filhas.
        # Outra maneira é definir a classe Funcionario como uma classe abstrata
        raise NotImplementedError
    
# O funcionário CLT, possui um salário fixo. Por isso, vamos passar esse valor no momento em que a classe for instanciada
class FuncionarioCLT(Funcionario):

    def __init__(self, nome: str, salario: float):
        super().__init__(nome)

        self._salario = salario

    def calcular_salario(self):
        return self._salario


# O funcionário terceirizado tem seu salário definido como resultado da multiplicação entre a quantidade de horas trabalhadas e o valor da hora cobrada. Vamos passar essas informações no momento em que a classe estiver sendo instanciada
class FuncionarioTerceirizado(Funcionario):

    def __init__(self, nome: str, qtd_horas_trabalhadas: int, valor_hora: float):
        super().__init__(nome)

        self._qtd_horas_trabalhadas = qtd_horas_trabalhadas
        self._valor_hora = valor_hora

    def calcular_salario(self):
        return self._qtd_horas_trabalhadas * self._valor_hora
    

# O funcionário comissionado tem o seu salário definido a partir de comissão calculada de acordo com a quantidade de vendas que realizou no mês. Portanto, precisamos de 2 informações: Quantidade de vendas realizadas no mês e a comissão recebida
