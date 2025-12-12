import pyautogui as p

def pular2():
    p.hotkey('Shift', 'enter')
    p.hotkey('Shift', 'enter')


def distribuicao(conta):  # geralmente são um casal
    return (conta / 14) * 2  # 14 inquilinos no total


def pec(nome, conta, distri, leitura, apto, v_mensalid):  # Todas as 'diversidades' vem para esta função
    if (False): #a condição que fazemos aqui é que caso o apto tenha mais que tres pessoas; nome == ( Beatriz): distri = conta / 14 * (quantidade de adultos)
        ...
    saudacoes(conta, distri, leitura, apto, v_mensalid)


def saudacoes(conta, distri, leitura, apto, v_mensalid):
    p.click(x=167, y=205, duration=1)
    p.write(apto + nome, interval=0.05)
    p.sleep(1)
    p.press('enter')
    p.sleep(3)

    if bom_dia:
        p.write(f"Ola, {nome}! Bom dia", interval=0.05)
        p.hotkey('shift', 'enter')
        p.write("Esperamos que voce e sua familia estejam bem!", interval=0.05)
        boleto(v_mensalid, conta, distri, leitura, apto)

    elif boa_tarde:
        p.write(f"Ola, {nome}! Boa tarde", interval=0.05)
        p.hotkey('shift', 'enter')
        p.write("Esperamos que voce e sua familia estejam bem!", interval=0.05)
        boleto(v_mensalid, conta, distri, leitura, apto)

    else:
        p.write(f"Ola, {nome}! Boa noite", interval=0.05)
        p.hotkey('shift', 'enter')
        p.write("Esperamos que voce e sua familia estejam bem!", interval=0.05)
        boleto(v_mensalid, conta, distri, leitura, apto)


def boleto(v, total, distri, leitura, apto):  # Aqui todos os detalhes do boleto sao escritos
    pular2()
    p.typewrite(f'Estes sao os detalhes da sua conta deste mes (Apto {apto})', interval=0.025)
    pular2()
    p.typewrite(f'Leitura da agua: {leitura}', interval=0.025)
    pular2()

    # Pessoas no local
    p.write("Pessoas 16+ anos no local: ")
    if apto in []:
        p.write("3")
    if apto in ['805','802','803', '804', '801', '806']:
        p.write("2")
    

    # Valores
    pular2()
    p.typewrite(f'Aluguel:  R$  {v:.2f}', interval=0.025)
    p.hotkey('Shift', 'enter')
    p.typewrite(f'Agua:  R$  {total:.2f}', interval=0.025)
    p.hotkey('Shift', 'enter')

    if apto in lista_aptos:  # Apartamentos com diversidades
        p.typewrite(f'Parcial:  R$  {distri:.2f}', interval=0.025)
        p.hotkey('Shift', 'enter')

        if apto == '804':  # Marilia paga com servicos domesticos
            v -= 1250

        elif apto == '806':  # Caso especial
            pular2()
            p.typewrite("Aluguel (807):  R$  700.00")
            p.hotkey('Shift', 'enter')
            p.write(f'Parcial (807):  R$  {conta / 14 * 2:.2f}')
            pular2()
            p.write(f'*Valor total 807:  R$  {700 + (conta / 14 * 2):.2f}*')

        pular2()

        if apto == '806':  # Parte adicional da Jeane
            p.typewrite(f'*Valor total 806:  R$  {v + distri:.2f}*', interval=0.025)
            pular2()

            p.typewrite('Nome: PEDRO HENRIQUE', interval=0.025)
            p.hotkey('Shift', 'enter')
            p.typewrite('Instituicao: PagSeguro', interval=0.025)
            pular2()
            p.typewrite('Obs: Caso identifique algum erro na distribuicao dos valores, faremos a correcao em ate 10 minutos.', interval=0.025)
            pular2()
            p.typewrite('_A distribuicao sempre sera feita de forma justa para todos os moradores. Caso tenha qualquer duvida, nos chame por gentileza._', interval=0.05)
            p.sleep(1)
            p.press('enter')
            p.hotkey('Shift', 'Home')
            p.sleep(1)
            p.press('Del')
            

        p.typewrite(f'*Valor total:  R$  {v + distri:.2f}*', interval=0.01)
        pular2()
        p.typewrite('Nome: PEDRO HENRIQUE', interval=0.025)
        p.hotkey('Shift', 'enter')
        p.typewrite('Instituicao: PagSeguro', interval=0.025)
        pular2()
        p.typewrite('Obs: Caso identifique algum erro na distribuicao dos valores, faremos a correcao em ate 10 minutos.', interval=0.025)
        pular2()
        p.typewrite('_A distribuicao sempre sera feita de forma justa para todos os moradores. Caso tenha qualquer duvida, nos chame por gentileza._', interval=0.05)
        p.sleep(1)
        p.press('enter')
        p.hotkey('Shift', 'Home')
        p.sleep(1)
        p.press('Del')
        return

    else:
        p.typewrite(f'Parcial:  R$  {distri:.2f}', interval=0.01)

    pular2()
    p.typewrite(f'*Valor total:  R$  {v + distri:.2f}*', interval=0.01)
    pular2()
    p.typewrite('O pagamento pode ser realizado via PIX:', interval=0.01)
    p.hotkey('Shift', 'Home')
    p.typewrite('Nome: PEDRO HENRIQUE', interval=0.01)
    p.hotkey('Shift', 'enter')
    p.typewrite('Instituicao: PagSeguro', interval=0.01)
    pular2()
    p.typewrite('Obs: Caso identifique algum erro na distribuicao dos valores, faremos a correcao em ate 10 minutos.', interval=0.01)
    pular2()
    p.typewrite('_A distribuicao sempre sera feita de forma justa para todos os moradores. Caso tenha qualquer duvida, nos chame por gentileza._', interval=0.05)
    p.sleep(1)
    p.press('enter')
    p.hotkey('Shift', 'Home')
    p.sleep(1)
    p.press('Del')
    return


# =====================
# CONFIGURAÇÕES GERAIS
# =====================
v_mensalid = 1250.00

horario = int(input('Horario de expedicao: '))
bom_dia = horario < 12
boa_tarde = horario <= 18

conta = float(input('Valor da conta: '))
leitura = input('Data da Leitura: ')
distri = distribuicao(conta)

dicionario = {
    
    '802': ' Savia',
    '803': ' Victor',
    '804': ' Marilia',
    '805': ' Beatriz',
    '806': ' Jeane',
}

# Setor diversidade
lista = [] #ao adicionar o nome na lista, a função pec deve ser adicionada a lógica também
lista_aptos = ['804', '806']
# =====================

p.sleep(5)

for apto, nome in dicionario.items():  # distribuicao para cada inquilino
    if nome in lista:  # Sessão diversidade
        pec(nome, conta, distri, leitura, apto, v_mensalid)
    else:
        saudacoes(conta, distri, leitura, apto, v_mensalid)  # Fluxo comum
