menor = 1000000000000000000000000000

formatacao = '+---------------+---------------+\n|     Peixe     |    Preço R$   |'

k = 0
while True:
    peixe, valor = input().split()
    valor = float(valor)
    formatacao = formatacao + (f'\n+---------------+---------------+\n| {peixe:<14}|{valor:>14.2f} |')
    if peixe != 'fim':
        if float(valor) < menor:
            menor = float(valor)
            menor_valor_peixe = peixe
        k += 1
    else:
        break

if k != 0:
    print(formatacao + (f'\n+---------------+---------------+\n\n+---------------+---------------+\n|    Cambada de menor preço     |\n+---------------+---------------+\n| {menor_valor_peixe:<14}|{float(menor):>14.1f} |\n+---------------+---------------+'))
else:
    print('+---------------+---------------+\n|     Peixe     |    Preço R$   |\n+---------------+---------------+\n|      Hoje não tem peixe       |\n+---------------+---------------+')
