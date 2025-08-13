# 🚗 Verificador de Idade para Veículos

Este é um programa em Python que verifica se uma pessoa tem idade suficiente para dirigir ou usar diferentes tipos de veículos.

## 📜 Como funciona
O programa:
1. Solicita ao usuário seu nome e idade.
2. Pergunta qual tipo de veículo deseja utilizar (carro, moto, bicicleta, caminhão, ônibus ou avião).
3. Verifica se o usuário tem idade mínima para o veículo escolhido.
4. Exibe uma mensagem informando se ele pode ou não usar o veículo.

### Idades mínimas definidas:
- Carro e moto: 18 anos  
- Bicicleta: 16 anos  
- Caminhão e ônibus: 21 anos  
- Avião: 18 anos  

## 📂 Código
```python
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
