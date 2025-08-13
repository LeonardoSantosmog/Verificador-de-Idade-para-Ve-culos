nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

veiculo = input("Digite o tipo de veículo (carro, moto ou etc...): ").lower()  # transforma em minúscula

if veiculo == "carro":
    if idade < 18:
        print(f"Com {idade} anos, você não pode dirigir carros")
    else:
        print(f"Com {idade} anos, você pode dirigir carros")

elif veiculo == "moto":
    if idade < 18:
        print(f"Com {idade} anos, você não pode dirigir motos")
    else:
        print(f"Com {idade} anos, você pode dirigir motos")

elif veiculo == "bicicleta":
    if idade < 16:
        print(f"Com {idade} anos, você não pode andar de bicicleta")
    else:
        print(f"Com {idade} anos, você pode andar de bicicleta")
elif veiculo == "caminhão": 
    if idade < 21:
        print(f"Com {idade} anos, você não pode dirigir caminhões")
    else:
        print(f"Com {idade} anos, você pode dirigir caminhões")
elif veiculo == "ônibus":
    if idade < 21:
        print(f"Com {idade} anos, você não pode dirigir ônibus")
    else:
        print(f"Com {idade} anos, você pode dirigir ônibus")
elif veiculo == "aviao":
    if idade < 18:
        print(f"Com {idade} anos, você não pode pilotar aviões")
    else:
        print(f"Com {idade} anos, você pode pilotar aviões")
else:
    print(f"Tipo de veículo '{veiculo}' não reconhecido")