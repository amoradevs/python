print('Calcular área e quantidade de tinta.')
l = float(input('Digite a largura da área (m):'))
a = float(input('Digite a altura da área (m):'))
ar = l * a
t = ar /2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}'.format(l, a, ar))
print('A quantidade de tinta necessária para pintar sua área é: {:.1f} litros.'.format(t))
