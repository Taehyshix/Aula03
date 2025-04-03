tipo = input("Digite o tipo abastecido\n"
             "G para Gasolina\n"
             "E para Etanol\n")

qtdlitro = float(input("Quantos litros: "))

vGas = 5.80
vEta = 4.90

if tipo == "G" or "g":
    valor = qtdlitro * vGas
else:
   if tipo == "E" or "e":
      valor = qtdlitro * vEta
print(f"Valor a pagar: R${valor:.2f}")
