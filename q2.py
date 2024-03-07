def verificarmovimento(posicao_inicial, posicao_final):
    movimentos_possiveis = [ (2,1), (1,2) ]
    if not (len(posicao_inicial) == len(posicao_final) == 2):
        raise Exception("Posição inválida.")
    
    cinicial = ord(posicao_inicial[0]) - ord('a') + 1
    linicial = int(posicao_inicial[1])
    cfinal  = ord(posicao_final[0]) - ord('a') + 1
    lfinal = int(posicao_final[1])
    difc = abs(cfinal - cinicial)
    difl = abs(lfinal - linicial)
    
    if(difc, difl) in movimentos_possiveis:
        return True
    else:
        raise Exception("Movimento inválido.")

while True:
    try:
        posicao_inicial = input("Digite a posição inicial ['f' para encerrar o programa]: ")
        if posicao_inicial == 'f':
            break
        posicao_final = input("Digite a posição final:")
        if verificarmovimento(posicao_inicial, posicao_final):
            print("Movimento válido!")
    except Exception as e:
        print(f"Erro: {e}")
