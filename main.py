#Faça um programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

parede = float(input("Bom dia cliente me diga qual o tamanho da parede, em metros, que você gostaria de pintar? "))
conver = parede/3
#Aqui é para saber a quantidade de litros necessários para cobrir a parede 
latas = int(conver/18)
#Aqui é para saber quantas latas seram necessárias para cobrir a parede
conver2 = latas*80
#Aqui é para saber o valor
print("Olha você vai precisar de: "+ str(latas) + " latas, o que vai dar: "+  str(conver2)+ " reais.")
