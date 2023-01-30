#Escreva um programa que converta uma temperatura digitada em graus Celsius e Fahrenheit
#Resolvi melhorar esse desafio!
temp = str(input('Qual a escala termométrica? ')).upper()
if temp == '°C' or 'CELSIUS' or 'C':
    graus1 = float(input('Quantos graus estão fazendo? '))
    print('Na escala Fahrenheit estão fazendo {} graus.\nNa escala Kelvin estão fazendo {} graus.'.format(graus1 * 1.8 + 32, graus1 + 273))
elif temp == '°F' or 'FAHRENHEIT' or 'F':
    graus2 = float(input('Quantos graus estão fazendo? '))
    print("Na escala Celsius estão fazendo {} graus.\nNa escala Kelvin estão fazendo {} graus.".format(graus2 / 1.8 - 32, (graus2-32)*5/9 + 273 ))
elif temp == '°K' or 'KELVIN' or 'K':
    graus3 = float(input('Quantos graus estão fazendo? '))
    print("Na escala Celsius estão fazendo {} graus.\nNa escala Fahrenheit estão fazendo {} graus.".format(graus3-273, (graus3-273)*1.8 + 32))
print('O clima está bem bom né!')