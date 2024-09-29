#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
#em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
area = float(input("Me diga qual o tamanho da área da parede? "))
litros = area/6
#Desconbrindo a quantidade de litros necessários
latas = int(litros/18) + 1
latas_comp = latas*80
#Parte das latas
galao = int(litros/3.6) + 1
galao_comp = galao*25
#Parte dos galao
print("Caso você queira em latas teremos "+ str(latas) + " latas, o que dará: "+ str(latas_comp)+ " reais")
print("Caso você queira em galões teremos "+ str(galao) + " galões, o que dará: "+ str(galao_comp)+ " reais")
