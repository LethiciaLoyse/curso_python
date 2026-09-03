# pintando uma parede 
print("Pintando uma parede")
largura = float(input("Insira a largura da parede: "))
altura = float(input("Insira a altura da parede: "))
area = largura * altura
tinta = area / 2
print(f"A área da parede é {area :.2f} e você precisará de {tinta} litros de tinta para pinta-la.")