# 🚦 Verificador de Idade para Veículos

Este projeto em Python é um programa simples que verifica se o usuário tem idade suficiente para dirigir ou usar diferentes tipos de veículos. Ele solicita o **nome**, a **idade** e o **tipo de veículo** e retorna uma mensagem personalizada informando se a pessoa **pode ou não** dirigir ou pilotar o veículo escolhido.

O programa considera as seguintes regras de idade mínima:  
- 🚗 Carros – 18 anos  
- 🏍️ Motos – 18 anos  
- 🚲 Bicicletas – 16 anos  
- 🚚 Caminhões – 21 anos  
- 🚌 Ônibus – 21 anos  
- ✈️ Aviões – 18 anos  

Se o usuário digitar um veículo que não esteja na lista, o programa avisa que o tipo de veículo não é reconhecido.

## 💻 Como usar
1. Clone o repositório:
```bash
git clone <URL_DO_SEU_REPOSITORIO>

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
veiculo = input("Digite o tipo de veículo (carro, moto ou etc...): ").lower()

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
