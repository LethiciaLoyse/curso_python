# variaveis, constantes e complexidade de código

velocidade = 61
local_carro = 100

LOCAL_1 = 100
RADA_1 = 60
RADAR_RANGE = 1
velocidadeAlta = velocidade > RADA_1
carro_multado = local_carro  >= RADA_1 and local_carro <= RADA_1

if velocidadeAlta:
    print("A velocidade do carro ultrapassou o limite!")
else: 
    print(" O carro passou no limite de velocidade")

if carro_multado and velocidadeAlta:
    print("O carrou foi multado em radar 1")