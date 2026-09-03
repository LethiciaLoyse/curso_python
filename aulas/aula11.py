# introdução a f- strings (formatação de strings)
nome = 'Lethicia Loyse'
altura = float(1.58)
peso = float(73)
imc = peso / (altura * altura) # ou fazer a exponenciação. altura elvado a 2
print(f'{nome},tem {altura:.2f} de altura e pesa {peso} quilos! e seu imc é {imc:.2f}' )
# :.2f é a formatação da qnt de casas decamais. 
