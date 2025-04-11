import pyautogui as p

def pular2():
    p.hotkey('Shift', 'enter')
    p.hotkey('Shift', 'enter')

def distribuicao(conta):    #geralmente são um casal
    return (conta / 16) * 2 #16 inquilinos no total

def pec(nome,conta,distri,leitura,apto,v_mensalid): #Todas as 'diversidades' vem para esta função

    if(nome == ' Flavia' or nome == ' Geane' or nome == ' Beatriz'):
        distri = conta / 16 * 3

    elif (nome == ' Samira'): #Samira mora sozinha e em um apartamento menor:
        v_mensalid = 650
        distri = 0
        
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
    p.typewrite(f'Aluguel do imovel = {v:.2f}R$',interval=0.05)
    pular2()
    p.typewrite(f'Agua = {total:.2f}R$')
    p.hotkey('Shift', 'enter')
    if (apto in lista_aptos):#Os aptos com diversidades são listados aqui.
        p.typewrite(f'Parcial = {distri:.2f}R$', interval=0.05)
        p.hotkey('Shift', 'enter')
        if apto == '804' or apto == '802':
            p.typewrite('Valor pago externamente: 1350.00R$') #Marilia é um parente, ela paga com servicos domésticos (organização, limpeza, etc.).
            v -= 1350
        elif(False):
            p.typewrite() #Aqui é caso tenha qualquer outra diversidade
        pular2()
        p.typewrite(f'*Valor Total: {v + distri:.2f} R$*', interval=0.05)
        pular2()                         #Caso consiga, a melhor forma de recebimento no momento seria em especie; senao, pix tambem sera viavel!
        p.typewrite('O pagamento pode ser realizado via PIX; caso nao tenha a chave, podemos enviar.', interval=0.05)
        pular2()
        p.typewrite('Nome: PEDRO HENRIQUE', interval=0.05)
        p.hotkey('Shift', 'enter')
        p.typewrite('Instituicao: PagSeguro', interval=0.05)
        pular2()
        p.typewrite(
            'OBS: Erros podem ocorrer na distribuicao dos valores, caso aconteca, sera corrigido em ate 10min.',
            interval=0.05)
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
    p.typewrite('O pagamento pode ser realizado via PIX; caso nao tenha a chave, podemos enviar.', interval=0.05)
    pular2()
    p.typewrite('Nome: PEDRO HENRIQUE', interval=0.05)
    p.hotkey('Shift', 'enter')
    p.typewrite('Instituicao: PagSeguro', interval=0.05)
    pular2()
    p.typewrite(
        'OBS: Erros podem ocorrer na distribuicao dos valores, caso aconteca, sera corrigido em ate 3min!',
        interval=0.05)
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

v_mensalid = 1350.00

horario = int(input('Horario de expedição: '))
bom_dia = horario < 12
boa_tarde = horario <= 18

conta = float(input('Valor da conta: '))
leitura = input('Data da Leitura: ')
distri = distribuicao(conta)

dicionario = {'801':' Vivian','802':' Flavia','803':' Savia','804':' Marilia','805': ' Beatriz','806':' Jeane','807':' Samira'}

#Setor diversidade
lista=[' Samira',' Vivian', ' Geane', ' Beatriz', ' Flavia'] #As pessoas que estiverem nesta lista estarão fora do fluxo comum do programa, por exemplo: mora sozinho, então o calculo será diferente.

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