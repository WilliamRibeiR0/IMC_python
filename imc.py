# Função calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# Solicitando valor para jogar na função
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

# Adicionando calor a uma variavel
imc = calcular_imc(peso, altura)

# Mostrando em tela o imc do usuario
print(f"Seu imc é de {imc:.2f}")

# Classificar o IMC de acordo com as categorias da OMS

if imc < 18.5:
    print("voce está abaixo do peso!")
elif imc < 25:
    print("seu peso está normal!")
elif imc < 30:
    print("você está acima do peso!")
elif imc < 35:
    print("você está com obesidade grau 1")
elif imc < 41:
    print("você está com obesidade grau 2")
else:
    print("você esta com obesidade grau 3")
