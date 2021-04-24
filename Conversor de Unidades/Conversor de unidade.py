import sys
print('Aqui você vai poder converter as unidades de medidas mais comuns!(KM) (M) (CM)')
print('')
print('Conversão de Kilomêtros: KM para M digite (1); KM para CM digite (2)')
print('Conversão de Metros: M para KM digite (3); M para CM digite (4)')
print('Conversão de Centímetros: CM para KM digite (5); CM para M digite (6)')
print('')
opção = input('Sua escolha: ')
if len(opção) > 1 or len(opção) < 1:
    print('ERRO, Verifique se você digitou corretamente')
    sys.exit()   
elif not opção.isnumeric():
    print('ERRO, Verifique se você digitou corretamente')
    sys.exit()
if opção == '1':
    print('Você escolheu converter Kilomêtros para Metros!')
    km = input('Sua medida em KM: ')
    try:
        km = float(km)
    except:
        print('ERRO, Verifique se você digitou corretamente')
        sys.exit()
    km_em_metros = km * 10 * 10 * 10
    print(f'{km} KM são {km_em_metros} Metros.')
if opção == '2':
    print('Você escolheu converter Kilomêtros para Centímetros!')
    km = input('Sua medida em KM: ')
    try:
        km = float(km)
    except:
        print('ERRO, Verifique se você digitou corretamente')
        sys.exit()
    km_em_cm = km * 10 * 10 * 10 * 10 * 10
    print(f'{km} KM são {km_em_cm} centímetros.')
if opção == '3':
    print('Você escolheu converter Metros para Kilomêtros!')
    metros = input('Sua medida em metros: ')
    try:
        metros = float(metros)
    except:
        print('ERRO, Verifique se você digitou corretamente')
        sys.exit()
    metros_em_km = metros / 10 / 10 / 10
    print(f'{metros} M são {metros_em_km} KM.')
if opção == '4':
    print('Você escolheu converter Metros para Centímetros!')
    metros = input('Sua medida em metros:')
    try:
        metros = float(metros)
    except:
        print('ERRO, Verifique se você digitou corretamente')
        sys.exit()
    metros_em_cm = metros * 10 * 10
    print(f'{metros} M são {metros_em_cm} CM')
if opção == '5':
    print('Você escolheu converter Centímetros para Kilomêtros!')
    cm = input('Sua medida em CM: ')
    try:
        cm = float(cm)
    except:
        print('ERRO, Verifique se você digitou corretamente')
        sys.exit()
    cm_em_km = cm / 10 / 10 / 10 / 10 / 10
    print(f'{cm} CM são {cm_em_km} KM')
if opção == '6':
    print('Você escolheu converter Centímetros para Metros!')
    cm = input('Sua medida em Cm: ')
    try:
        cm = float(cm)
    except:
        print('ERRO, Verifique se você digitou corretamente')
        sys.exit()
    cm_em_m = cm / 10 / 10
    print(f'{cm} CM são {cm_em_m} M')