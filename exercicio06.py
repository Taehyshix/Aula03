time1 = input("Nome do primeiro time: ")
goltime1 = int(input(f"Quantidade de gols do {time1} fez:"))
time2 = input("Nome do segundo time: ")
goltime2 = int(input(f"Quantidade de gols do {time2} fez:"))

if goltime1 == goltime2:
    print("Empate")
else:
    if goltime1>goltime2:
        print(f"O {time1} ganhou!!")
    else:
        print(f"O {time2} ganhou!!")
