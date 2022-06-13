print('Aluguel de Carros')
d = int(input('Quantos dias alugados?'))
k = float(input('Quantos Km foram rodados?'))
c = d * 60
kr = k * 0.15
print('O valor total a pagar é de R$ {:.2f}'.format((c+kr)))
# podia ser: pago = d * 60) + (k * 0.15)
