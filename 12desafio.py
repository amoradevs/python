print('Preço do produto com desconto.')
p = float(input('Digite o preço real do produto: R$'))
pd = p - p * (5 / 100)
print('O valor do produto com 5% de desconto é: R$ {:.2f}.'.format(pd))
