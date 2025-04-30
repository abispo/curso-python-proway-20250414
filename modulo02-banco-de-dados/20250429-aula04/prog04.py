"""
Programação Orientada a Objetos

Polimorfismo
-----------

Polimorfismo significa "muitas formas", ou seja, um método pode ser chamado de diferentes formas, tendo diferentes comportamentos
"""

from typing import List


class Funcionario:

    def __init__(self, nome: str):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    def __str__(self):
        return self._nome
    
    def __repr__(self):
        return self._nome

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
    

# O funcionário comissionado tem o seu salário definido a partir de comissão calculada de acordo com a quantidade de vendas que realizou no mês. Portanto, precisamos de 2 informações: Valor total de vendas realizadas no mês e a comissão recebida
class FuncionarioComissionado(Funcionario):

    def __init__(self, nome: str, valor_total_vendas: float, comissao: float):
        super().__init__(nome)

        self._valor_total_vendas = valor_total_vendas
        self._comissao = comissao

    def calcular_salario(self):
        return self._valor_total_vendas * (self._comissao / 100)
    

# A classe FolhaDePagamento é a responsável por chamar o método calcular_salario() e mostrar o salário dos funcionários
class FolhaDePagamento:

    def __init__(self, funcionarios: List[Funcionario]):
        self._funcionarios = funcionarios

    def gerar(self):
        print("== FOLHA DE PAGAMENTO ==")

        for funcionario in self._funcionarios:
            nome = funcionario.nome
            # O atributo especial __class__ contém informações da classe a qual o objeto foi instanciado. O atributo __name__ desse objeto armazena o nome da classe.
            tipo = funcionario.__class__.__name__
            salario = funcionario.calcular_salario()

            print("-"*30)
            print(f"= Nome: {nome}")
            print(f"= Tipo: {tipo}")
            print(f"= Salário: {salario:.2f}")
            print("")

if __name__ == "__main__":

    maria = FuncionarioCLT("Maria das Dores", 2000)
    joao = FuncionarioCLT("João da Silva", 1850)
    valter = FuncionarioTerceirizado("Válter Carvalho", 55, 125)
    amanda = FuncionarioTerceirizado("Amanda Barros", 60, 85)
    daniel = FuncionarioComissionado("Daniel Torres", 145098.74, 5)
    vanessa = FuncionarioComissionado("Vanessa Bezerra", 239554.12, 5)
    romario = FuncionarioComissionado("Romário Brito", 99561.84, 7)

    lista_funcionarios = [maria, joao, valter, amanda, daniel, vanessa, romario]

    FolhaDePagamento(lista_funcionarios).gerar()

    # Diferentemente do Java e C#, no Python não conseguimos fazer sobrecarga de métodos em uma classe, ou seja, vários metódos com o mesmo nome, porém com assinaturas diferentes.
    # Porém, podemos utiliza *args e **kwargs para criar uma função/método que recebe a quantidade de argumentos que quisermos. Ou seja, estamos simulando o mesmo comportamento que temos no Java

    # Duck typing: "Se parece com um pato, nada como um pato, e faz barulho como um pato, provavelmente é um pato"