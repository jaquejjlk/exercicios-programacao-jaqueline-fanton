#Faça um programa que pergunte em que turno você estuda. Peça para digitar:
#M - Matutino
#V - Vespertino
#N - Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
#desenvolvido por: JAQUELINE FANTON

turno=input("Qual seu turno?")
#se
if turno=="Matutino":
  print("Bom Dia!")
#senao se
elif turno=="Vespertino":
  print("Boa Tarde!")
#senao se
elif turno=="Noturno":
  print("Boa noite!")
#senao
else:
  print("Valor Inválido!")