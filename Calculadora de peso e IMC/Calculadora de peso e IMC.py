import sys
print('Calculadora de peso ideal e IMC')
print('Aqui vamos calcular o seu peso ideal e o índice do seu imc.')
print('Vamos calcular primeiro seu IMC!')
peso = input('Qual é o seu peso? (KG): ')
altura = input('Qual é a sua altura?(M): ')
if peso.isalpha() or altura.isalpha():
    print('Você precisa digitar apenas números!')
    sys.exit()
try:
    peso = float(peso)
    altura = float(altura)
except:
    print('Verifique se você digitou os valores corretamente!')
    sys.exit()
imc = peso / (altura*altura)
print(f'Acabei de ver que seu índice de massa corporal é de {imc:.1f}')
if imc <= 18.5:
    print('Seu IMC é abaixo do peso!')
elif imc <= 24.9:
    print('Seu IMC está no peso normal!')
elif imc <= 29.9:
    print('Seu IMC está no sobrepeso!')
elif imc <= 34.9:
    print('Seu IMC está em obesidade de grau 1!')
elif imc <= 39.9:
    print('Seu IMC está em obesidade de grau 2!')
else:
    print('Seu IMC está em obesidade mórbida!')
print('Agora vamos calcular seu peso ideal:')
altura = input('Qual a sua altura?(M): ')
try:
    altura = float(altura)
except:
    print('Erro, verifique se os valores estão digitados corretamente!')
PI = (altura*altura) * 23
print(f'O seu peso ideal seria de {PI:.1f} kg!')