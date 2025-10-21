#Faça um programa que leia três números e mostre o maior e o menor deles:
#Desenvolvido por: JAQUELINE FANTON

numero1=float(input("Qual o primeiro número:"))
numero2=float(input("Qual o segundo número:"))
numero3=float(input("Qual o terceiro número:"))

#maior
maior=numero1
#se
if numero2>maior:
  maior=numero2

if numero3>maior:
  maior=numero3
print(maior,"é o maior!")

#menor
menor=numero1
#se
if numero2<menor:
  menor=numero2

if numero3<menor:
  menor=numero3
print(menor,"é o menor!")