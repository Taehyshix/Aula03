tipo = input("Digite o tipo abastecido\n"
             "G para Gasolina\n"
             "E para Etanol\n")

qtdlitro = float(input("Quantos litros: "))

vGas = 5.80
vEta = 4.90

if tipo == "G" or tipo == "g":
    valor = qtdlitro * vGas
elif tipo == "E" or tipo  == "e":
      valor = qtdlitro * vEta
else:
    print("Tipo de combustivel inválido!")
print(f"Valor a pagar: R${valor:.2f}")
