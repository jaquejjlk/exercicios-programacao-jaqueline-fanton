#Faça um programa que peça um número inteiro e determine se ele é par ou impar.
#Dica: utilize o operador módulo (resto da divisão).
#Desenvolvido por: JAQUELINE FANTON

numero=int(input("Digite um número:"))
numero%2
#se
if numero==0:
 print("Seu número é par:")
 #Par:0,2,4,6,8
#senao
else:
  print("Seu número é impar:")
  #Impar:1,3,5,7,9