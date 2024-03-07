def decomporvalor(valor):
    notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
    moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    for nota in notas:
        quantidade = int(valor // nota)
        valor -= quantidade * nota
        print(f"{quantidade} nota(s) de R${nota:.2f}")
    print("\n")
    for moeda in moedas:
        quantidade = int(valor // moeda)
        valor -= quantidade * moeda
        print(f"{quantidade} moeda(s) de R${moeda:.2f}")
    return

def verificar_decimais(valor):
    if '{:.2f}'.format(valor) == str(valor):
        return valor
    else:
        raise ValueError("Número inválido de casas decimais")

try:
    valor = float(input("Digite um valor monetário (com duas casas decimais): "))
    valor = verificar_decimais(valor)
    decomporvalor(valor)
except ValueError as e:
    print(f"Erro: {e}. Digite um número válido.")

