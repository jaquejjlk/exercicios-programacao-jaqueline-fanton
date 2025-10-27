#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
#Desenvolvidopor: JAQUELINE FANTON

pares=0
impares=0
#for:para in range:intervalo
for i in range(10):
    numero=int(input(f"Digite o {i+1}º número inteiro: "))
    #se
    if numero % 2 == 0:
        pares += 1
    #senao
    else:
        impares += 1
print("Quantidade de números pares:",pares)
print("Quantidade de números ímpares:",impares)