"""
Impressão de ponto flutuante. 

Em python, algumas vezes pode acontecer de um resultado com ponto flutuante, não sair certo. 
por isso, há jeitos de formatar esses resultados.
O 1° é usar f-strings (:.2f), o 2° é o round(numero3, 2) e o 3° seria usar um 
import decimal (modulo) mas são usados em números flutuantes muito especificos!
"""
import decimal

# Format
numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2
print(f'{numero3:.2f}')

#Round
numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2
print(round(numero3, 2))

#Import decimal
numero1 = decimal.Decimal(0.1) #Aqui se vc colocar uma string no lugar dos número, o resultado é arredondado
numero2 = decimal.Decimal(0.7)
numero3 = numero1 + numero2
print(numero3)