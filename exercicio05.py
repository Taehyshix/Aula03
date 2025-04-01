nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
medianota = (nota1 + nota2 + nota3) /3

if medianota >=7:
    print(f"Média: {medianota:.2f}, você foi Aprovado!")
else:
    print(f"Média: {medianota:.2f}, você foi Reprovado.")