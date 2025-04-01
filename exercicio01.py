nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario atual: "))
aumento = float(input("Digite a porcentagem de aumento do salário: "))
valor_real = salario*aumento/100
novo_salario = salario+valor_real

print(f"Olá {nome}, voce tem {idade} anos e seu salario é R${salario:.2f} e voce recebeu R${novo_salario:.2f} de aumento.")
