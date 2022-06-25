from random import choice
secreto = ['marmore', 'artes', 'paralelepipedo', 'mistura', 'apostar']
while True:
    n = int(
        input('Digite 1 se quiser editar as palavras,  2 para jogar ou 3 para sair: '))
    confirmacao = 'n'
    if n == 1:
        while confirmacao == 's' or n == 1:
            n = 0
            adicionar = str(input(
                'Informe a palavra secreta que deseja adicionar: ')).lower()
            secreto.append(adicionar)
            confirmacao = input(
                'Deseja continuar adicionando palavras? S/N: ').lower()
    elif n == 3:
        print('você fechou o jogo')
        break

    aleatorio = choice(secreto)
    digitadas = []
    chances = 6
    print('-=' * 20)
    print('             JOGO DA FORCA')
    print('-=' * 20)
    secreto_temporario = ''
    for palavra_Secreta in aleatorio:
        if palavra_Secreta in digitadas:
            secreto_temporario += palavra_Secreta
        else:
            secreto_temporario += '_'
    print(f'A palavra secreta está assim: {secreto_temporario}')
    while True:
        letra = str(input('Digite uma letra: ')).lower()
        if len(letra) > int(1):
            print('ERRO, não pode digitar mais que uma letra: ')
            continue

        if letra in digitadas:
            print('Você já informou essa letra')
            continue

        digitadas.append(letra)
        secreto_temporario = ''
        for palavra_Secreta in aleatorio:
            if palavra_Secreta in digitadas:
                secreto_temporario += palavra_Secreta
            else:
                secreto_temporario += '_'
        if secreto_temporario == aleatorio:
            print(f'Voce venceu a forca! a palavra é {secreto_temporario}')
            break
        else:
            print(f'A palavra secreta está assim: {secreto_temporario}')
        if letra not in aleatorio:
            chances -= 1
        if chances == 5:
            print('____')
            print('|  |')
            print('| '' o')
            print('|')
            print('|')
        if chances == 4:
            print('____')
            print('|  |')
            print('|  o')
            print('|  |')
            print('|')
        if chances == 3:
            print('____')
            print('|  |')
            print('| \o')
            print('|  |')
            print('|')
        if chances == 2:
            print('____')
            print('|  |')
            print('| \o/')
            print('|  |')
            print('|')
        if chances == 1:
            print('____')
            print('|  |')
            print('| \o/')
            print('|  |')
            print('| / ')
        if chances <= 0:
            print('____')
            print('|  |')
            print('| \o/')
            print('|  |')
            print('| / \ ')
            print('Você perdeu!')
            break
        print(f'As letras já informadas foram:', end=' ')
        print('(', end='')
        for let in digitadas:
            print(f'{let}', end=', ')
        print(')')
        if chances > 1:
            print(f'Você tem {chances} chances. ')
        else:
            print(f'Você tem {chances} chance. ')
        print()
