#Faça um programa que leia 5 números e informe o maior número.
#Desenvolvido por: JAQUELINE FANTON

numero1=float(input("Qual o primeiro número:"))
numero2=float(input("Qual o segundo número:"))
numero3=float(input("Qual o terceiro número:"))
numero4=float(input("Qual o quarto número:"))
numero5=float(input("Qual o quinto número:"))

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