# Crie um módulo chamado "conversor"
# que contenha duas funções: uma para
# converter graus Celsius para Fahrenheit e
# outra para converter graus Fahrenheit para Celsius.
#  Em seguida, crie um programa principal que importe
#  esse módulo e peça ao usuário para digitar uma temperatura
#  e a unidade de medida (C ou F). O programa deve imprimir a
#  temperatura convertida para a outra unidade.


def celsius(c):
    return (c * 9 / 5) + 32


def fahrenheit(f):
    return (f - 32) * 5 / 9
