'''
Bem vindo! Este é meu programa para distribuição de valores, este programa foi criado com um simples intúito: distribuir valores para inquilinos.

#MOTIVO
Gerencio apartamentos, tomo conta de valores a receber, dados pessoas, contratos, etc. Daí então criei esta aplicação que
faz calculos e fornece valores para cada pessoa automaticamente; usei RPA para isso (pyautogui) como podem ver.

#FUNCIONAMENTO
O programa pede 2 entradas: Data de expedição da conta de água e o valor, com esses dados o programa começa a passar nas informações de cada inquilino
e realiza o calculo baseando-se na quantidade de pessoas que moram no apartamento.

Por exemplo: se tiver 1 adulto morando no apartamento e a conta de água no mês for 700:
** 700.00 / total de inquilinos que moram no mesmo predio * a quantidade de inquilinos que moram neste apartamento específico (neste caso é 1) **
A distribuição é feita através do Watssapp.

#OBSERVAÇÕES IMPORTANTES:
Este programa foi pensado e desenvolvido no meu 3° semestre (2023), assim quando tinha passado pela linguagem C, atualmente estou na linguagem JAVA e em breve irei criar
outro projeto para com este mesmo intúito. Muito Obrigado pela visualização, abraços!

pedro_henrique
'''

import pyautogui as p

def pular2():
    p.hotkey('Shift', 'enter')
    p.hotkey('Shift', 'enter')

def distribuicao(conta):    #geralmente são um casal
    return (conta / 14) * 2 #14 inquilinos no total

def pec(nome,conta,distri,leitura,apto,v_mensalid): #Todas as 'diversidades' vem para esta função

    if (nome == ' Samira'): #Samira mora sozinha e em um apartamento menor:
        v_mensalid = 650
        distri = conta / 14 * 1

    elif (nome == ' Marilia'):
        distri = conta / 14 * 1

    elif (nome == ' Lidamara'):
        v_mensalid = 800
        distri = conta / 14 * 1

    saudacoes(conta,distri,leitura,apto,v_mensalid)

def saudacoes(conta,distri,leitura,apto,v_mensalid): #Aqui uma mensagem educada é escrita para o user
    p.click(18, 233, duration=1)
    p.click(265, 115, duration=1)
    p.typewrite(apto + nome, interval=0.05)
    p.sleep(4)
    p.press('enter')
    p.sleep(2)

    if (bom_dia):
        p.typewrite(f'Ola! Bom dia,{nome}.', interval=0.05);
        p.hotkey('Shift', 'enter');
        p.typewrite('esperamos que esteja bem!', interval=0.05)
        boleto(v_mensalid, conta, distri, leitura, apto)

    elif (boa_tarde):
        p.typewrite(f'Ola! Boa tarde,{nome}.', interval=0.05);
        p.hotkey('Shift', 'enter');
        p.typewrite('esperamos que esteja bem!', interval=0.05)
        boleto(v_mensalid, conta, distri, leitura, apto)

    else:
        p.typewrite(f'Ola! Boa noite,{nome}.', interval=0.05);
        p.hotkey('Shift', 'enter');
        p.typewrite('esperamos que esteja bem!', interval=0.05)
        boleto(v_mensalid, conta, distri, leitura, apto)


def boleto(v,total,distri,leitura,apto):  #Aqui todos o detalhes do boleto é escrito para o user
    pular2()
    p.typewrite(f'Estes sao os detalhes de sua conta no mes; (APTO {apto})', interval=0.05)
    p.hotkey('Shift', 'enter');
    p.typewrite(f'_Segue em anexo os valores:', interval=0.05)
    pular2()
    p.typewrite(f'*LEITURA DA AGUA* - {leitura}',interval=0.05)
    pular2()
    p.typewrite(f'Alugel do imovel = {v:.2f}R$',interval=0.05)
    pular2()
    p.typewrite(f'Agua = {total:.2f}R$')
    p.hotkey('Shift', 'enter')
    if (apto in lista_aptos):#Os aptos com diversidades são listados aqui.
        p.typewrite(f'Parcial = {distri:.2f}R$', interval=0.05)
        p.hotkey('Shift', 'enter')
        if apto == '804':
            p.typewrite('Valor pago externamente: 1200.00R$') #Marilia é um parente, ela paga com servicos domésticos (organização, limpeza, etc.).
            v -= 1200
        elif apto == '807':
            distri = 0
        elif(False):
            p.typewrite() #Aqui é caso tenha qualquer outra diversidade
        pular2()
        p.typewrite(f'*Valor Total: {v + distri:.2f} R$*', interval=0.05)
        pular2()
        p.typewrite('Caso consiga, a melhor forma de recebimento no momento seria em especie; senao, pix tambem sera viavel! ', interval=0.05) #O pagamento pode ser realizado via PIX; caso nao tenha a chave, podemos enviar.
        pular2()
        p.typewrite('Nome: PEDRO HENRIQUE', interval=0.05)
        p.hotkey('Shift', 'enter')
        p.typewrite('Instituicao: PagSeguro', interval=0.05)
        pular2()
        p.typewrite(
            'OBS: Erros podem ocorrer na distribuicao dos valores, caso aconteca, sera corrigido em ate 3min!',
            interval=0.05)
        pular2()
        pular2()
        p.typewrite('_A distribuicao sempre sera feita de forma justa para todos os moradores. Caso tenha qualquer duvida, nos chame por gentileza._',interval=0.05)
        p.sleep(1)
        p.press('enter')

        p.click(220, 109, duration=0.8)
        p.hotkey('Shift', 'Home')
        p.sleep(1)
        p.press('Del')
        p.click(18, 233, duration=0.8)
        return
    else:
        p.typewrite(f'Parcial = {distri:.2f}R$',interval=0.05)
    pular2()
    p.typewrite(f'*Valor Total: {v + distri:.2f} R$*',interval=0.05)
    pular2()
    p.typewrite('Caso consiga, a melhor forma de recebimento no momento seria em especie; senao, pix tambem sera viavel! ', interval=0.05)
    pular2()
    p.typewrite('Nome: PEDRO HENRIQUE', interval=0.05)
    p.hotkey('Shift', 'enter')
    p.typewrite('Instituicao: PagSeguro', interval=0.05)
    pular2()
    p.typewrite(
        'OBS: Erros podem ocorrer na distribuicao dos valores, caso aconteca, sera corrigido em ate 3min!',
        interval=0.05)
    pular2()
    pular2()
    p.typewrite('_A distribuicao sempre sera feita de forma justa para todos os moradores. Caso tenha qualquer duvida, nos chame por gentileza._', interval=0.05)
    p.sleep(1)
    p.press('enter')

    p.click(776, 1408,duration=0.8)
    p.hotkey('Shift','Home')
    p.sleep(1)
    p.press('Del')
    p.click(18, 233, duration=0.8)
    return

v_mensalid = 1200.00

horario = int(input('Horario de expedição: '))
bom_dia = horario < 12
boa_tarde = horario <= 18

conta = float(input('Valor da conta: '))
leitura = input('Data da Leitura: ')
distri = distribuicao(conta)

dicionario = {'801':' Vivian','802':' Flavia','803':' Savia','804':' Marilia','805': ' Nayara','806':' Jeane','807':' Samira','808':' Lidamara'}

#Setor diversidade
lista=[' Marilia',' Samira',' Lidamara'] #As pessoas que estiverem nesta lista estarão fora do "fluxo comum" do programa, por exemplo: mora sozinho, então o calculo será diferente.

lista_aptos=['804']#A mesma lógica, porém, contendo mensagens personalizadas para o apartamento que estiver referido.
#Setor diversidade

p.sleep(5)

for apto,nome in dicionario.items(): #distribuição para cada inquilino

    if(nome in lista): #Tudo que entra aqui vai para a sessão de diversidade.
        pec(nome,conta,distri,leitura,apto,v_mensalid)
    elif False:
        ...
    else:
        saudacoes(conta,distri,leitura,apto,v_mensalid)#Fluxo comum do programa.

