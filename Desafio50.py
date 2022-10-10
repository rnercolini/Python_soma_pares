# Retorna com a soma dos números pares digitados no laço de repetição.
soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você digitou {} números e a soma dos números pares é {}'.format(cont, soma))
