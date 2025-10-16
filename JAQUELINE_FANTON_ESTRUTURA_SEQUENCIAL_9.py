#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#Formula
#C = 5 * ((F-32) / 9).
#Desenvolvido por: JAQUELINE FANTON

fahrenheit=float(input("Qual a temperatura em graus Fahrenheit:"))
celsius = 5 * ((fahrenheit-32) / 9)
print(fahrenheit,"em graus Celsius é:",celsius)