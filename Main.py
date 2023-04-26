
resetar = 0 #função para resetar(uau)
while resetar == 0:
    try:
        print('-----CALCULADORA SIMPLES v1.0-----')
        nun1 = float(input(' digite o primeiro numero '))
        nun2 = float(input(' digite o segundo numero '))
        #funções
        print('--------------------------')
        print(' digite 1 para adição ')
        print(' digite 2 para subtração ')
        print(' digite 3 para multiplicação ')
        print(' digite 4 para divisão ')
        operacao = int(input(' qual operação deseja? '))
        if operacao in range(1,5):
            # verificar o numero digitado para continuar(vai de 1 até o 4, range para uma casa antes)
            if operacao == 1:
                resultado = nun1 + nun2
                print(f'nun1 + nun2 = {resultado}')
            elif operacao == 2:
                resultado = nun1 - nun2
                print(f'nun1 - nun2 = {resultado}')
            elif operacao == 3:
                resultado = nun1 * nun2
                print(f'nun1 * nun2 = {resultado}')
            elif operacao == 4:
                resultado = nun1 / nun2
                print(f'nun1 / nun2 = {resultado}')
            #quando finaliza a operacão pergunta se o usuario quer finalizar ou recomeçar
            sair = input(' se deseja finalizar digite S, caso contrario digite outra coisa ').lower().startswith('s')
            if sair is True:
                break
            else:
                resetar += 1
                resetar = 0
        else:
            #caso seja digitado um numero q não esteja ente 1 e 4, finaliza ou recomeça
            sair = input(' operação invalida, deseja reiniciar? [s]im ').lower().startswith('s')
            if sair is True:
                resetar += 1
                resetar = 0
            else:
                break
    except ValueError:
        #se não forem digitador numeros, reseta ou finaliza
        print(' digite apenas números! ')
        sair = input(' deseja reiniciar? [s]im ').lower().startswith('s')
        if sair is True:
            resetar += 1
            resetar = 0
        else:
            break