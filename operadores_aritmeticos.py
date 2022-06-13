# Ordem de precedência: 1º (), 2º **, 3º */ // %, 4º + -
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# para reduzir casas decimais, editar chave com {:.número de casas e f de float}.
print('A soma é {}, o produto é {} e a divisão é {:.2f}.'.format(s, m, d), end=' ')
# para não quebrar a linha, digitar: , end=' qualquer coisa dentro') aparecerá tudo na mesma linha.
# para quebrar linha, basta digitar: \n após a informação desejada.
print('Divisão inteira {} e potência {:.1f}.'.format(di, e))

