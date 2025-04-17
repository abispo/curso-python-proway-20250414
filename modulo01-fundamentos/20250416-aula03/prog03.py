"""
Funções (ou Procedures)

Com relação aos parâmetros de uma função, também podemos criar parâmetros opcionais, ou seja, parâmetros que já possuem um valor definido.
"""

def calculo_hora_extra(valor_hora_extra: float, quantidade_horas_extras: int = 0) -> float:
    return valor_hora_extra * quantidade_horas_extras

if __name__ == "__main__":

    # Passando todos os valores:
    print(f"{calculo_hora_extra(45, 10)}.")

    # Passando apenas o valor da hora extra
    print(f"{calculo_hora_extra(20)}.")

    # Não há problemas em mesclar a maneira que passamos os valores para a função. Abaixo o primeiro valor está sendo passado via posição, e o segundo valor está sendo passado pelo nome do parâmetro
    print(f"{calculo_hora_extra(40, quantidade_horas_extras=20)}")

    # Porém, a linha abaixo irá causar um erro, pois o Python proíbe que um valor via posição seja passado depois de um valor via nome de parâmetro
    # print(f"{calculo_hora_extra(quantidade_horas_extras=10, 50)}")