print("alugel de carros ")
quilometros = float(input("Digite os km`s percorridos: "))
dias = int(input("digite por quantos dias você alugou o carro: "))
quilometros_percorridos = quilometros * 0.15
dias_usados = dias * 60
preco_total = quilometros_percorridos + dias_usados
print(f"O alugel total ficou R${preco_total :.2f}")