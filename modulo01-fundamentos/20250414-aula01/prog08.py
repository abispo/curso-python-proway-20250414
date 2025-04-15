# Operadores em Python

# Operadores lógicos

if __name__ == "__main__":

    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))
    n3 = float(input("Informe a terceira nota: "))

    media = (n1 + n2 + n3) / 3
    aprovado = False

    if media < 5:
        print(f"O aluno foi reprovado com a média {media:.1f}")
    
    elif media >= 5 and media < 7:
        print(f"O aluno está de recuperação com a média {media:.1f}")

    else:
        print(f"O aluno foi aprovado com a média {media:.1f}")
        aprovado = True

    print(not aprovado)
    print(True or False)
    print(False or False)


"""
AND
V   V   -> V
F   V   -> F
V   F   -> F
F   F   -> F

OR
V   V   -> V
F   V   -> V
V   F   -> V
F   F   -> F

NOT
V   -> F
F   -> v
"""