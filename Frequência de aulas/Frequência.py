import sys
import datetime
while True:
    print('Calculadora de frequência')
    print('')

    tempo = input('O seu curso tem carga horária definida? [S] ou [N]: ')
    if len(tempo) > 1 or len(tempo) < 1:
        print('ERRO! Verifique se você digitou corretamente!')
    elif tempo.isnumeric():
        print('ERRO! Verifique se você digitou corretamente!')
    elif not 's' in tempo.lower() and not 'n' in tempo.lower():
            print('ERRO, você precisa digitar S ou N')
    else:
        pass
    if tempo.lower() == 's':
        d_h = input('O seu curso tem carga horária em horas? [S] ou [N]: ')
        if d_h.lower() == 's':
            print('')
            print('Vamos converter essas horas para dias!')
            horas = input('Quantas horas tem o seu curso?: ')
            try:
                horas = float(horas)
            except:
                print('ERRO, Verifique se você digitou corretamente!')
                continue
            horas_paradias = horas / 24
            print(f'A sua carga horária total em dias é de {horas_paradias:.0f} dias!')
            frequentou = input('Para calcular a sua frequência, preciso saber quantos dias você frequentou: ')
            try:
                frequentou = float(frequentou)
            except:
                print('ERRO, Verifique se você digitou corretamente!')
            frequência = (frequentou * 100) / horas_paradias
            print(f'Até o momento, a sua frequência é de {frequência:.1f}%')
        elif not 's' in d_h.lower() and not 'n' in d_h.lower():
            print('ERRO, você precisa digitar S ou N')
        if d_h.lower() == 'n':
            print('')
            dias = input('A sua carga horária é em dias, quantos dias você precisa cumprir?: ')
            try:
                dias = float(dias)
            except:
                print('Erro, verifique se você digitou corretamente!')
            print(f'Então a sua carga horária é de {dias:.0f} dias')
            diasateagr = input('Quantos dias você frequentou?: ')
            try:
                diasateagr = float(diasateagr)
            except:
                print('ERRO, verifique se você digitou corretamente!')
            frequênciad = (diasateagr * 100) / dias
            print(f'A sua frequência até agora é de {frequênciad:.1f}% ')
    elif tempo.lower() == 'n':
        print('')
        sabeqntsdias = input('Você sabe há quantos dias começou o curso?[S] [N]:  ')
        if not 's' in sabeqntsdias.lower() and not 'n' in sabeqntsdias.lower():
            print('Você precisigar digitar S ou N')
        elif sabeqntsdias.lower() == 's':
            qtsdias = input('Há quantos dias você começou?: ')
            try:
                qtsdias = float(qtsdias)
            except:
                print('ERRO, Verifique se você digitou os valores corretamente!')
            qtdaulas = input('Quantas aulas você viu até agora?: ')
            try:
                qtdaulas = float(qtdaulas)
            except:
                print('ERRO, Verifique se você digitou os valores corretamente!')
            aproveitamento = qtdaulas / qtsdias
            print(f'O seu aproveitamento médio até agora é de {aproveitamento:.1f} aulas por dia!')
        elif sabeqntsdias.lower() == 'n':
            print('Então vamos precisar calcular!')
            dia = input('Me diga o dia que você começou!: ')
            mês = input('Me diga o mês que você começou![1,2,3,4. ETC]: ')
            ano = input('Me diga o ano que você começou!: ')
            try:
                dia = int(dia)
                mês = int(mês)
                ano = int(ano)
            except:
                print('ERRO, Verifique se você digitou os valores corretamente!')
                continue
            if dia > 31 or dia < 0:
                print('ERRO, Verifique se você digitou os valores corretamente!')
                continue
            elif mês < 0 or mês > 12:
                print('ERRO, Verifique se você digitou os valores corretamente!')
                continue
            começo = datetime.datetime(ano,mês,dia)
            começo2 = começo.date()
            print(f'Você começou na data {começo2}')            
            print('')
            print('Agora vamos descobrir...')
            hj = input('Qual o dia de hoje?[1,2,3,4.ETC]: ')
            hjmês = input('Qual o mês atual?[1,2,3,4 ETC]:')
            hjano = input('Em que ano estamos?: ')
            try:
                hj = int(hj)
                hjmês = int(hjmês)
                hjano = int(hjano)
            except:
                print('ERRO, Verifique se você digitou os valores corretamente!')
                continue
            if hj > 31 or hj < 0:
                print('ERRO, Verifique se você digitou os valores corretamente!')
                continue
            elif hjmês < 0 or hjmês > 12:
                print('ERRO, Verifique se você digitou os valores corretamente!')
                continue
            hoje = datetime.datetime(hjano,hjmês,hj)
            hoje2 = hoje.date()
            print(hoje2)
            percorreu = hoje2 - começo2
            from datetime import datetime
            diferença = (percorreu.days * 24 * 60 * 60) + percorreu.seconds
            diferença2 = diferença/24/60/60
            print('Você começou o curso há', diferença2, 'dias')
            print('')
            print('Para poder calcular sua frequência, preciso saber quantas aulas você viu até agora nesses 52 dias')
            aulas = input('Quantas aulas você viu até agora?: ')   
            try:
                aulas = int(aulas)              
            except:
                print('ERRO, Verifique se você digitou os valores corretamente!')
                continue
            frequências = aulas / diferença2
            print(f'Você em {diferença2} dias acompanhou {aulas} aulas')
            print(f'Isso te da uma média de {frequências:.1f} aulas por dia')
            porcentagemdeaula = (aulas * 100) / diferença2
            print(f'E uma média de comparecimento de {porcentagemdeaula:.1f}% ')
    dnv = input('Você deseja calcular novamente?[S] ou [N]: ')
    if len(dnv) > 1 or len(dnv) < 1:
        print('ERRO, Verifique se você digitou corretamente!')
    elif dnv.isnumeric():
        print('ERRO, Verifique se você digitou corretamente!')
    if dnv.lower() == 'n':
        print('Bons estudos!')
        break
    else:
        continue