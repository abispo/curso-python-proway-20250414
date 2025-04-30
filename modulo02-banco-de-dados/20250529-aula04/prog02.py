"""
Programação Orientada a Objetos em Python

Herança

A herança ocorre quando uma classe filha (ou subclasse) herda características (atributos e/ou métodos) de uma classe mãe (ou superclasse)
"""

from contas import ContaCorrente, ContaInvestimento, CDBItau

if __name__ == "__main__":

    conta_corrente_itau = ContaCorrente(
        "Conta Corrente Itaú", 100
    )

    saldo = conta_corrente_itau.sacar(55)
    print(f"Saquei o valor de R$ 55, meu saldo atual é de R$ {saldo:.2f}")

    saldo = conta_corrente_itau.depositar(15.80)
    print(f"Depositei o valor de 15.80, meu saldo atual é de R$ {saldo}")

    conta_poupanca_caixa = ContaInvestimento(
        "Conta Poupança Caixa", taxa=0.03
    )

    saldo = conta_poupanca_caixa.depositar(1200)
    print(f"Depositei o valor de 1200, meu saldo atual é de R$ {saldo}")

    rendimento = conta_poupanca_caixa.render()
    print(
        "A {} rendeu R$ {:.2f}. Seu saldo atual é de R$ {}".format(
            conta_poupanca_caixa.nome,
            rendimento,
            conta_poupanca_caixa.saldo
        )
    )

    rendimento = conta_poupanca_caixa.render()
    print(
        "A {} rendeu R$ {:.2f}. Seu saldo atual é de R$ {}".format(
            conta_poupanca_caixa.nome,
            rendimento,
            conta_poupanca_caixa.saldo
        )
    )

    rendimento = conta_poupanca_caixa.render()
    print(
        "A {} rendeu R$ {:.2f}. Seu saldo atual é de R$ {:.2f}".format(
            conta_poupanca_caixa.nome,
            rendimento,
            conta_poupanca_caixa.saldo
        )
    )