def funcao_imprime_numeros(n):
    for i in range(n):
        i += 1
        print(str(i) * i)

n = int(input('Digite um número: '))
funcao_imprime_numeros(n)