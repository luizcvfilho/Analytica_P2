def calcular_frequencia_num(numeros):
    frequencia = {}
    for numero in numeros:
        if numero in frequencia:
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1
    return frequencia


numeros = []
while True:
    try:
        entrada = input("Digite um número inteiro (ou 'f' para finalizar): ")
        if entrada == 'f':
            break
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida.")

for numero, c in calcular_frequencia_num(numeros).items():
    print(f"O número {numero} apareceu {c} vezes.")

