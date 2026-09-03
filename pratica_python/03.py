# calculo imc 
p = float(input('Por favor, informe seu peso corporal: '))
a = float(input('Por favor, informe sua altura: '))
imc = p/(a**2)

if p == 18.5:
    print(f'Você está com o peso normal. Seu imc é {imc:.2f}')
elif p == 24.9:
    print(f'Você está acima do peso. Seu imc é {imc:.2f}!')
else:
    print(f'Seu peso está muito elevado! seu imc é {imc:.2f}. Procure um médico!')
