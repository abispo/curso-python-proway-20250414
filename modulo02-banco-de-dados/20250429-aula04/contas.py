# Módulo de contas

class ContaFinanceira:

    def __init__(self, nome: str, saldo: float = 0):
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value


    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome

    def sacar(self, valor: float) -> float:
        if valor > self._saldo:
            raise Exception("Você não possui saldo suficiente.")
        
        # self._saldo = self._saldo - valor
        self._saldo -= valor

        return self._saldo
    
    def depositar(self, valor: float) -> float:
        if valor <= 0:
            raise Exception("O valor a depositar deve ser maior que zero.")
        
        self._saldo += valor

        return self._saldo

# Abaixo, criamos a classe ContaCorrente que herda as características da classe ContaFinanceira. Como não alteramos em nada a classe filha, ela será idêntica a classe mãe.
class ContaCorrente(ContaFinanceira):
    pass


# Abaixo criamos a classe ContaInvestimento, que também herda as características da classe ContaFinanceira
class ContaInvestimento(ContaFinanceira):

    # Abaixo, estamos implementando o método __init__. Nesse caso, o método __init__ que está sendo herdado da classe ContaFinanceira está sendo substituído pelo método __init__ da classe filha.
    def __init__(self, nome, saldo = 0, taxa = 0.01):

        # Como o método está sendo substituído, podemos utilizar a função built-in super(), que irá chamar qualquer método da classe mãe. Nesse caso, estamos chamando o método __init__ para manter a criação dos atributos _nome e _saldo, e com isso evitar repetição de código
        super().__init__(nome, saldo)
        self._taxa = taxa

    # Abaixo criamos o método render, que fará parte de todas as classes que porventura herdarem de ContaInvestimento
    def render(self) -> float:
        valor_rendimento = self._saldo * self._taxa
        saldo_antigo = self._saldo

        self._saldo += valor_rendimento

        return self._saldo - saldo_antigo
    

# Criação de classes especializadas
class CDBItau(ContaInvestimento):
    def __init__(self):
        super().__init__("CDB Itau 105%", 0, 0.05)