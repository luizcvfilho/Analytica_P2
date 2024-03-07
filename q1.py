import math
import re

def calcularangulo(hora, minuto):
    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
        raise ValueError("Horário inválido")
    if hora >= 12:
        hora -= 12   
    angulo = abs((11*minuto - 60*hora)/2)
    minimo = min(angulo, 360 - angulo)
    return minimo

def analisar_padrao(horario):
    padrao = re.compile(r'^\d{2}:\d{2}$')
    if(padrao.match(horario)):
        return horario
    else:
        raise ValueError("Horário fora do padrão XX:XX")
    
while True:
        horario = input("\nDigite o horário (hh:mm) ou 'f' para encerrar: ")
        if horario == 'f':
            print("Programa encerrado.")
            break
        try:
            horario = analisar_padrao(horario)
            hora, minuto = map(int, horario.split(':'))
            angulo = calcularangulo(hora, minuto)
            print(f"Menor ângulo entre os ponteiros: {angulo} graus")
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
