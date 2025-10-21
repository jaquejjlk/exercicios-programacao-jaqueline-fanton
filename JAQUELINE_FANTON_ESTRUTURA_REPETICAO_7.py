#Faça um programa que leia 5 números e informe o maior número.
#Desenvolvido por: JAQUELINE FANTON

numero1=float(input("Digite primeiro número:"))
numero2=float(input("Digite o segundo número:"))
numero3=float(input("Digite o terceiro número:"))
numero4=float(input("Digite o quarto número:"))
numero5=float(input("Digite o quinto número:"))

maior=numero1
#se
if numero2>maior:
  maior=numero2

if numero3>maior:
  maior=numero3

if numero4>maior:
  maior=numero5

if numero5>maior:
  maior=numero5
print(maior,"é o maior!")