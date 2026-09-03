'''
Operação ternária (Condição de uma linha)
Basicamente, um if/else em uma linha
'''
condicao = 10 == 11
variavel = 'valor' if condicao else 'Outro valor'
print(variavel)
# Segundo o professor, isso pode ser usado em testes rápidos de if/else

idade = 12
status = "maior de idade" if idade >= 18 else "menor de idade"
print(status)  # maior de idade