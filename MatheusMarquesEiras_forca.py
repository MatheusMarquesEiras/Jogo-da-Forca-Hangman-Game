from tkinter import *
from random import *
import unicodedata

# Desenha as partes do layout
# Desenha a linha de cima
def linha_cima():
    # Variaveis que fazem os quadrados se moverem da esquerda para direita
    primeiroX = 0
    segundoX = 25

    # Lopp que move os quadrados
    for quadrado in range(1,33):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgTela.create_rectangle(primeiroX, 0, segundoX, 25, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgTela.create_rectangle(primeiroX, 0, segundoX, 25, fill='white', outline='white')

        # Move os quadrados 25 pixels
        primeiroX += 25
        segundoX += 25

# Desenha a linha da direita
def linha_direita():
    # Variaveis que movem os quadrados de cima para baixo
    primeiroY = 25
    segundoY = 50

    # Loop que movem os quadrados
    for quadrado in range(1,23):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgTela.create_rectangle(775, primeiroY, 800, segundoY, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgTela.create_rectangle(775, primeiroY, 800, segundoY, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroY += 25
        segundoY += 25

# Desenha a linha de baixo
def linha_baixo():
    # Variaveis que movem os quadrados da direita para esquerda
    primeiroX = 800
    segundoX = 775

    # Loop que movem os quadrados
    for quadrado in range(1,33):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgTela.create_rectangle(primeiroX, 575, segundoX, 600, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgTela.create_rectangle(primeiroX, 575, segundoX, 600, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroX -= 25
        segundoX -= 25

# Desenha a linha da esquerda
def linha_esquerda():
    # Variaveis que movem os quadrados de baixo pra cima
    primeiroY = 550
    segundoY = 575

    # Loop que movem os quadrados
    for quadrado in range(1,23):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgTela.create_rectangle(0, primeiroY, 25, segundoY, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgTela.create_rectangle(0, primeiroY, 25, segundoY, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroY -= 25
        segundoY -= 25

# Desenha a linha central
def linha_centro():
    # Variaveis que movem os quadrdos de cima para baixo
    primeiroY = 25
    segundoY = 50

    # Loop que movem os quadrados
    for quadrado in range(1,23):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgTela.create_rectangle(475, primeiroY, 500, segundoY, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgTela.create_rectangle(475, primeiroY, 500, segundoY, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroY += 25
        segundoY += 25

# Desenha o layout
def desenha_layout():
    linha_cima()
    linha_direita()
    linha_baixo()
    linha_esquerda()
    linha_centro()

# Desenha a forca
def desenha_forca():
    confgTela.create_line(575,350,700,350, fill="#6E3000", width=7)
    confgTela.create_line(600,350,600,150, fill="#6E3000", width=7)
    confgTela.create_line(600,150,665,150, fill="#6E3000", width=7)
    confgTela.create_line(665,150,665,180, fill="#6E3000", width=7)

# Desenha partes da pessoa
# Desenha a cabeça do boneco
def desenha_cabeca():
    # Variavel usada
    global cabeca

    cabeca = confgTela.create_oval(655,180,675,200, fill="white", width=3)

# Desenha o tronco do boneco
def desenha_tronco():
    # Variavel global usada
    global tronco

    tronco = confgTela.create_line(665,200,665,240, fill="black", width=3)

# Desenha o braço esquerdo do boneco
def desenha_braco_esquerdo():
    # Variavel global usada
    global bracoEsquerdo

    bracoEsquerdo = confgTela.create_line(665,200,690,220, fill="black", width=3)

# Desenha o braço direito do boneco
def desenha_braco_direito():
    # Variavel global usada
    global bracoDireito

    bracoDireito = confgTela.create_line(665,200,640,220, fill="black", width=3)

# Desenha a perna esquerda do boneco
def desenha_perna_esquerda():
    # Variavel global usada
    global pernaEsquerda

    pernaEsquerda = confgTela.create_line(665,240,690,260, fill="black", width=3)

# Desenha a perna direita do boneco
def desenha_perna_direita():
    # Variavel global usada
    global pernaDireita

    pernaDireita = confgTela.create_line(665,240,640,260, fill="black", width=3)

# Desenha a pessoa inteira
def desenha_pessoa():
    desenha_cabeca()
    desenha_tronco()
    desenha_braco_esquerdo()
    desenha_braco_direito()
    desenha_perna_esquerda()
    desenha_perna_direita()

# Deleta toda a pessoa
def deleta_pessoa():
    # Variaveis globais usadas
    global cabeca
    global tronco
    global bracoEsquerdo
    global bracoDireito
    global pernaEsquerda
    global pernaDireita

    confgTela.delete(cabeca)
    confgTela.delete(tronco)
    confgTela.delete(bracoEsquerdo)
    confgTela.delete(bracoDireito)
    confgTela.delete(pernaEsquerda)    
    confgTela.delete(pernaDireita)

# Sai do jogo
def sair_jogo():
    tela.quit()

# Mostra mais informações ao usuario
def informacao():
    deleta_menu()
    desenha_informacao()

# Deleta o menu principal
def deleta_menu():
    labelMenu.destroy()
    botaoNovoJogo.destroy()
    botaoInformacao.destroy()
    botaoSair.destroy()

# Faz o menu do jogo
def menu_inicial():
    # Variaveis globais usadas
    global labelMenu
    global botaoNovoJogo
    global botaoInformacao
    global botaoSair

    # Desenha o label escrito "Menu inicial" e o posiciona na tela e o posiciona
    labelMenu = Label(confgTela, text="Menu Principal")
    labelMenu.place(x=100,y=75,width=300,height=50)

    # Desenha o botão "novo jogo" que chama a função para desenhar os botões de dificuldade e o posiciona
    botaoNovoJogo = Button(confgTela, text="Novo Jogo", width= 20, height=2, command=desenha_layout_dificuldade)
    botaoNovoJogo.place(x=175, y=200)

    # Desenha o botão "informação" que chama a função que desenha a informação do jogo e quem o fez e o posiciona
    botaoInformacao = Button(confgTela, text="Informação", width= 20, height=2, command=informacao)
    botaoInformacao.place(x=175, y=250)

    # Desenha o botão "sair" que chama a função para sair do jogo e o posiciona
    botaoSair = Button(confgTela, text="Sair", width= 20, height=2, command=sair_jogo)
    botaoSair.place(x=175, y=300)

# sorteia a palavra que será usada
def sorteia_palavra():
    # Variaveil global usada
    global palavraSorteada

    with open("forca.txt", encoding="utf-8 ") as arquivo: # Lê o arquivo na forma de "utf-8"
        palavras = arquivo.readlines() # Lê cada linha do arquivo e guarda elas em uma lista
    palavras = list(map(str.strip, palavras)) # Remove possiveis espaços em brancono inicio e no final da lista
    palavraSorteada = choice(palavras).lower() # padroniza a palavra sorteada para que todas as letras sejam minusculas

# Gera os botões de dificuldade
def desenha_menu_dificuldade():
    # Variaveis globais usadas
    global labelDificuldade
    global botaoNormal
    global botaoTormento
    global botaoInferno
    global botaoNightmare
    global botaoVolta

    # desenha o label escrito "escolha a dificuldade" e o posiciona
    labelDificuldade = Label(confgTela, text="Escolha a dificuldade")
    labelDificuldade.place(x=100,y=75,width=300,height=50)
    
    # Desenha o botão difilculdade normal que gere com o respectivo numero de tentativas e o posiciona
    botaoNormal = Button(confgTela, text="Normal (6 tentativas)", width= 20, height=2, command=dificuldade_normal)
    botaoNormal.place(x=175, y=200)

    # desenha o botão dificuldade tromento que gere com o respectivo numero de tentativas e o posiciona
    botaoTormento = Button(confgTela, text="Tormento (4 tentativas)", width= 20, height=2, command=dificuldade_tormento)
    botaoTormento.place(x=175, y=250)

    # desenha o botão dificuldade inferno que gere com o respectivo numero de tentativas e o posiciona
    botaoInferno = Button(confgTela, text="Inferno (2 tentativas)", width= 20, height=2, command=dificuldade_inferno)
    botaoInferno.place(x=175, y=300)

    # desenha o botão dificuldade nightmare que gere com o respectivo numero de tentativas 
    botaoNightmare = Button(confgTela, text="Nightmare (1 tentativas)", width= 20, height=2, command=dificuldade_nightmare)
    botaoNightmare.place(x=175, y=350)

    # desenha o botão para voltar para o menu incial e o posiciona
    botaoVolta = Button(confgTela, text="Voltar", width= 20, height=2, command=volta_dificuldade_menu_inicial)
    botaoVolta.place(x=175, y=400)

# Desenha o label da informação
def desenha_informacao():
    # Variaveis globais usadas
    global labelMenuInformacao
    global labelInformacao
    global botalInformacaoVolta

    # Desenha o label "informaçoes sobre o jogo" e o posiciona
    labelMenuInformacao = Label(confgTela, text="Informaçoes sobre o jogo")
    labelMenuInformacao.place(x=100,y=75,width=300,height=50)

    # Informaçoes sobre o jogo e que o fez o seguinte programa e o posiciona
    labelInformacao = Label(confgTela, text="\tO jogo da forca é um jogo em que o jogador deve adivinhar uma palavra oculta, tendo como dica o número de letras e as letras já utilizadas. A cada letra errada, é desenhado uma parte do corpo do personagem enforcado. O objetivo é descobrir a palavra antes de completar o desenho.\n\n\tEste programa foi feito por Matheus Marques Eiras no ano de 2023. Cursando em Bacharelado Ciência da Computação - IFPR campus Pinhais.", wraplength=300)
    labelInformacao.place(x=100,y=150,width=300,height=250)

    # Desenha botão "volta" e chama a função para voltar ao menu incial e o posiciona
    botalInformacaoVolta = Button(confgTela, text="Volta", command=deleta_informacao)
    botalInformacaoVolta.place(x=150,y=450,width=200,height=50)

# Deleta todo o menu da informação
def deleta_informacao():
    labelMenuInformacao.destroy()
    labelInformacao.destroy()
    botalInformacaoVolta.destroy()
    menu_inicial()

# Faz os botões de dificuldade do menu dificuldade
def desenha_layout_dificuldade():
    deleta_menu()
    desenha_menu_dificuldade()

# Retorna ao menu inicial
def volta_dificuldade_menu_inicial():
    deleta_menu_dificuldade()
    menu_inicial()

# Deleta os botões das dificuldades
def deleta_menu_dificuldade():
    labelDificuldade.destroy()
    botaoNormal.destroy()
    botaoTormento.destroy()
    botaoInferno.destroy()
    botaoNightmare.destroy()
    botaoVolta.destroy()

# Configura a dificulade normal
def dificuldade_normal():
    # Variavel global usada
    global tentativas

    tentativas = 6 # define o numero de tentativas
    sorteia_palavra() # Sorteia a palavra
    elabora_jogo() # Desenha o jogo

# Configura a dificulade tromento
def dificuldade_tormento():
    # Variavel global usada
    global tentativas

    tentativas = 4 # define o numero de tentativas
    sorteia_palavra() # Sorteia a palavra
    elabora_jogo() # Desenha o jogo

# Configura a dificulade inferno
def dificuldade_inferno():
    # Variavel global usada
    global tentativas

    tentativas = 2 # define o numero de tentativas
    sorteia_palavra() # Sorteia a palavra
    elabora_jogo() # Desenha o jogo

# Configura a dificulade nightmare
def dificuldade_nightmare():
    # Variavel global usada
    global tentativas

    tentativas = 1 # define o numero de tentativas
    sorteia_palavra() # Sorteia a palavra
    elabora_jogo() # Desenha o jogo

# Elabora o jogo em si
def elabora_jogo():
    deleta_menu_dificuldade()
    deleta_pessoa()
    verifica_tentativas()
    texto_misterioso()
    palavras_usadas()
    gera_caixa_texto()
    botao_verificar()
    verificacao()
    botao_volta_jogo_menu()

# Desenha o label que ira conter as letras que o usuario ja usou
def palavras_usadas():
    # Variavel global usada
    global letrasUsadas

    # Desenha o label letras usadas e o posiciona
    letrasUsadas = Label(confgTela, text="Letras usadas:", font=("arial", 10), wraplength=200)
    letrasUsadas.place(x=150, y=250, width=200, height=50)

# Desenha a caixa de texto que será usada pelo usuario
def gera_caixa_texto():
    # Variavel global usada
    global botaoResposta

    # Desenha a caixa de texto e a posiciona
    botaoResposta = Entry(confgTela, width=20)
    botaoResposta.place(x=185,y=450)

# Desenha o botão verificar que chama a função verificacao que verifica a resposta do usuario
def botao_verificar():
    # Variavel global usada
    global botaoVerificaResposta

    # Desenh o botão verificar e o posiciona
    botaoVerificaResposta = Button(confgTela, text="Verificar",command=verificacao)
    botaoVerificaResposta.place(x=225,y=500)
    
# Verifica a tentativa do usuário e desenha o boneco de acordo com as tentativas que o usuario possui 
def verifica_tentativas():
    # Variaveis globais usadas
    global tentativas
    global cabeca
    global tronco
    global bracoEsquerdo
    global bracoDireito
    global pernaEsquerda
    global pernaDireita

    if tentativas == 5:
        confgTela.delete(cabeca) # Limpa memória da parte do boneco
        desenha_cabeca()  # Desenha parte do boneco

    if tentativas == 4:
        confgTela.delete(cabeca) # Limpa memória da parte do boneco   
        confgTela.delete(tronco) # Limpa memória da parte do boneco   
        desenha_cabeca() # Desenha parte do boneco
        desenha_tronco() # Desenha parte do boneco

    if tentativas == 3:
        confgTela.delete(cabeca) # Limpa memória da parte do boneco   
        confgTela.delete(tronco) # Limpa memória da parte do boneco   
        confgTela.delete(bracoEsquerdo) # Limpa memória da parte do boneco
        desenha_cabeca() # Desenha parte do boneco
        desenha_tronco() # Desenha parte do boneco
        desenha_braco_esquerdo() # Desenha parte do boneco

    if tentativas == 2:
        confgTela.delete(cabeca) # Limpa memória da parte do boneco   
        confgTela.delete(tronco) # Limpa memória da parte do boneco   
        confgTela.delete(bracoEsquerdo) # Limpa memória da parte do boneco
        confgTela.delete(bracoDireito) # Limpa memória da parte do boneco 
        desenha_cabeca() # Desenha parte do boneco
        desenha_tronco() # Desenha parte do boneco
        desenha_braco_esquerdo() # Desenha parte do boneco
        desenha_braco_direito() # Desenha parte do boneco

    if tentativas == 1:
        confgTela.delete(cabeca) # Limpa memória da parte do boneco   
        confgTela.delete(tronco) # Limpa memória da parte do boneco   
        confgTela.delete(bracoEsquerdo) # Limpa memória da parte do boneco
        confgTela.delete(bracoDireito) # Limpa memória da parte do boneco 
        confgTela.delete(pernaEsquerda) # Limpa memória da parte do boneco
        desenha_cabeca() # Desenha parte do boneco
        desenha_tronco() # Desenha parte do boneco
        desenha_braco_esquerdo() # Desenha parte do boneco
        desenha_braco_direito() # Desenha parte do boneco
        desenha_perna_esquerda() # Desenha parte do boneco

    if tentativas == 0:
        deleta_pessoa() # Limpa memória de todo o boneco
        desenha_pessoa() # desenha boneco inteiro

# Botoes volatar ao menu inicial ou sair do jogo se o usuário perdeu
def botoes_volta_sai_perdeu():
    # Variaveis globais usadas
    global botaoSairJogoFinal
    global botaoVoltaMenuPerdeu

    # Desenha o botão voltar que chma a função perdeu_retorna_comeco para voltar ao menu incial e reiniciar o jogo e o posiciona
    botaoVoltaMenuPerdeu = Button(confgTela, text="Jogar novamente", width=13, height=2, command=perdeu_retorna_comeco)
    botaoVoltaMenuPerdeu.place(x=275, y=225)

    # Desenha o botão sair do jogo que chama a função sair_jogo para sair do jogo e o posiciona
    botaoSairJogoFinal = Button(confgTela, text="Sair do jogo", width=13, height=2, command=sair_jogo)
    botaoSairJogoFinal.place(x=125, y=225)

# Botoes volatar ao menu inicial ou sair do jogo se o usuario ganhou
def botoes_volta_sai_ganhou():
    # Variaveis globais usadas
    global botaoSairJogoFinal
    global botaoVoltaMenuGanhou

    # Desenha o botão para jogar novamente que chama a função ganhou_retorna_comeco para voltar para o menu inicial o posiciona
    botaoVoltaMenuGanhou = Button(confgTela, text="Jogar novamente", width=13, height=2, command=ganhou_retorna_comeco)
    botaoVoltaMenuGanhou.place(x=275, y=225)

    # Desenha o botão para sair do jogo que chama a função sair_jogo que sai do jogo o posiciona
    botaoSairJogoFinal = Button(confgTela, text="Sair do jogo", width=13, height=2, command=sair_jogo)
    botaoSairJogoFinal.place(x=125, y=225)

# Retorna ao começo se perdeu destruindo o label e refazendo o menu incial
def perdeu_retorna_comeco():
    # Variaveis globais usadas
    global textoPerdeu
    global botaoSairJogoFinal
    global botaoVoltaMenuPerdeu

    textoPerdeu.destroy()
    botaoSairJogoFinal.destroy()
    botaoVoltaMenuPerdeu.destroy()
    menu_inicial()

# Retorna ao começo se ganhou destruindo o label e refazendo o menu incial
def ganhou_retorna_comeco():
    # Variaveis globais usadas
    global textoGanhou
    global botaoSairJogoFinal
    global botaoVoltaMenuGanhou

    textoGanhou.destroy()
    botaoSairJogoFinal.destroy()
    botaoVoltaMenuGanhou.destroy()
    menu_inicial()

# Desenha o texto perdeu
def texto_perdeu():
    # Variavel global usada
    global textoPerdeu

    # Desenha o label de quando o usuario perde e junto a ele a palavra sorteada e o posiciona
    textoPerdeu = Label(confgTela, text="Você perdeu  a palavra era: " + str(palavraSorteada))
    textoPerdeu.place(x=100, y=125, width=300, height=50)

# Desenha o menu de quando o suario perde
def perdeu():
    texto_perdeu()
    botoes_volta_sai_perdeu()

# Desenha o texto ganhou
def texto_ganhou():
    # Variavel global usada
    global textoGanhou

    # desenha o label de quando o usuario ganha e junto a ele a palavra sorteada e o posiciona
    textoGanhou = Label(confgTela, text="Você ganhou a palavra era: " + str(palavraSorteada))
    textoGanhou.place(x=100, y=125, width=300, height=50)

# Desenha o menu de quando o usuario ganha
def ganhou():
    texto_ganhou()
    botoes_volta_sai_ganhou()

# Gera o texto misterioso que irá orientar o usuario
def texto_misterioso():
    # Variaveis globais usadas
    global palavraSorteada
    global labelMisterioso
    global palavraMistJunta
    global palavraMistConvertida
    global palavraMisteriosaLista

    # converte a palavra sorteada em uma lista de caracteres
    palavraMisteriosaLista = list(palavraSorteada)

    # converte cada caractere da lista em "_"
    for letra in range(len(palavraSorteada)):
        palavraMisteriosaLista[letra] = "_"

    # converte a lista em string e separa cada "_" por um espaço em branco
    palavraMistConvertida = " ".join(palavraMisteriosaLista)

    # fas o label misterioso na tela
    labelMisterioso = Label(confgTela, text=palavraMistConvertida, font=("arial", 10))
    labelMisterioso.place(x=100, y=150, width=300, height=50)

    # retira da string os espaços em branco
    palavraMistJunta = palavraMistConvertida.replace(" ","")

# Função responsavel por normalizar tanto palavras inteiras quanto letras para retirar caracteres especiais como "ç" e letras com acento
def normaliza(texto):
    normalizada = unicodedata.normalize('NFD', texto) # Usa a função unicodedata com a opção de normalização "Normalização Canônica Decomposta" para tirar o cedilha e oas acento das letras
    return normalizada.encode('ascii', 'ignore').decode('utf-8').casefold() # Converte a string para uma string composta somente de caracteres ascii e ignora os que não podem ser decodificados para tabela ascii são ignorados e em seguida os caracteres ascii são convertidos para utf-8 novamente mas sem os caracteres especiais (ç e acentos)

# Verifica o input da caixa de texto que o usuario forneceu
def verificacao():
    # Variaveis globais usadas
    global tentativas
    global palavraSorteada
    global botaoResposta
    global palavraMisteriosa
    global labelMisterioso
    global palavraMistJunta
    global palavraMisteriosaLista
    global palavraMistConvertida
    global listaPalavrasUsadas
    global letrasUsadas

    resposta = botaoResposta.get().lower() # Obtem a resposta da caixa de texto do usuario

    # Verifica se a caixa de texto não esta vazia
    if resposta:
        # Verifica se o usuario digitou uma letra
        if len(resposta) == 1 and resposta.isalpha():

            # Normaliza a palvra sorteada e a resposta do usuario
            palavraNormalizada = normaliza(palavraSorteada)
            respostaNormalizada = normaliza(resposta)

            # Converte a palavra sorteada junta e a palavra sorteada padronizada em uma lista cada uma
            atualizaPalavraLista = list (palavraMistJunta)
            listaPalavraNormalizada = list (palavraNormalizada)

            # Verifica letra a letra da palavra sorteada
            for letra in range(len(listaPalavraNormalizada)):
                # Se a letra normalizada estiver na lista de caracteres da palavra sorteada ela é substituida no lugar do "_"
                if listaPalavraNormalizada[letra] == respostaNormalizada:
                    atualizaPalavraLista[letra] = palavraSorteada[letra]

                # Se a resposta não esta na lista de palavras usadas e a resposta normalizada não esta na lista de palavras usadas e a resposta normalizada não esta na palavra normalizada e a resposta nao esta na palavra sorteada ela é adicionada na lista de palavras usadas e se diminue as tentativas
                elif resposta not in listaPalavrasUsadas and respostaNormalizada not in listaPalavrasUsadas and respostaNormalizada not in palavraNormalizada and resposta not in palavraSorteada:
                    listaPalavrasUsadas += resposta
                    tentativas -= 1

            # Faz a lista atualiza palavra lista para separar cada carctere com um espaço em branco
            palavraMistJunta = " ".join(atualizaPalavraLista)
            listaPalavrasUsadas = ",".join(listaPalavrasUsadas)

            # Atualiza cada um dos labels
            letrasUsadas.config(text="Letras usadas: " + str(listaPalavrasUsadas))
            labelMisterioso.config(text=palavraMistJunta)

            # Retira da lista de palavras usadas as virgulas e converte a lista palavras usadas para uma lista
            listaPalavrasUsadas = listaPalavrasUsadas.replace(",","")
            listaPalavrasUsadas = list(listaPalavrasUsadas)

            # Retira os espaçõs em branco na palavra mist junta
            palavraMistJunta = palavraMistJunta.replace(" ", "")

            # Verifica as tentativas e atualiza o boneco
            verifica_tentativas()

            # Se todas as letras forem liberadas o usuario ganha
            if palavraMistJunta == palavraSorteada:
                deleta_jogo()
                ganhou()

            # Se as tentativas chegarem a zero o usuario perde
            if tentativas == 0:
                deleta_jogo()
                perdeu()

        # Se a resposta for uma palavra composta somente de caracteres alfabeticos
        elif len(resposta) > 1 and resposta.isalpha:
            # Se for diferente da palavra sorteada se diminui as tentativas e atualiza o boneco
            if palavraSorteada != resposta:
                tentativas -= 1
                verifica_tentativas()

                # Se as tentativas chegarem a zero o usuario perde
                if tentativas == 0:
                    deleta_jogo()
                    perdeu()
            
            # Se o usuario acertar a palavra o usuario ganha
            elif palavraSorteada == resposta:
                deleta_jogo()
                ganhou()

                # Se as tentativas chegarem a zero o usuario perde
                if tentativas == 0:
                    deleta_jogo()
                    perdeu()

        # Limpa a caixa de texto
        botaoResposta.delete(0,END)

# Faz um botão para voltar ao menu
def botao_volta_jogo_menu():
    # Variavel global usada
    global botaoJogoMenu

    # Desenha o botao voltar que chama a função volta_jogo_menu_inicial e o posiciona
    botaoJogoMenu = Button(confgTela, text="voltar", command=volta_jogo_menu_inicial)
    botaoJogoMenu.place(x=232,y=530)

# Deleta todo o jogo e limpa a lista lista palavras usadas
def deleta_jogo():
    # Variavel global usada
    global listaPalavrasUsadas

    listaPalavrasUsadas = []
    deleta_pessoa()
    desenha_pessoa()
    labelMisterioso.destroy()
    letrasUsadas.destroy()
    botaoResposta.destroy()
    botaoVerificaResposta.destroy()
    botaoJogoMenu.destroy()

# Função que volta para o menu principal
def volta_jogo_menu_inicial():
    deleta_jogo()
    menu_inicial()

# Função principal
if __name__ == "__main__":

    # Variaveis que serão usadas para acessar partes individuais da pessoa
    cabeca = None
    tronco = None
    bracoEsquerdo = None
    bracoDireito = None
    pernaEsquerda = None
    pernaDireita = None

    # Variaveis que serão usadas para acessar os botoes do jogo
    # Botoes menu
    botaoNovoJogo = None
    botaoSair = None
    botaoInformacao = None

    # Seção da informação
    labelMenuInformacao = None
    labelInformacao = None
    botalInformacaoVolta = None

    # Botoes dificuldade
    botaoNormal = None
    botaoTormento = None
    botaoInferno = None
    botaoNightmare = None
    botaoVolta = None

    # Variavel para guardar a palavra sorteada
    palavraSorteada = ""

    # Variavel que guarda quantas tentativas o usuario irá ter de acordo com a difiiculdade escolhida
    tentativas = 0

    # Variavel que guarda o texto misterioso (a palavra sorteada porrem cada letra substituida por "_ ")
    palavraMisteriosa = None
    palavraMistJunta = None
    palavraMistConvertida = None
    palavraMisteriosaLista = None

    # Labels usadas
    labelMisterioso = None
    labelMenu = ""
    labelDificuldade = ""

    # Guarda a resposta do usuario
    botaoResposta = None
    verifica = ""
    listaPalavrasUsadas = []
    letrasUsadas = None

    # Botão que executa a verificação
    botaoVerificaResposta = None

    # textos que aparecem quando se vence ou perde
    textoPerdeu = None
    textoGanhou = None

    # Botoes de quando perde ou ganha
    botaoSairJogoFinal = None
    botaoVoltaMenuGanhou = None
    botaoVoltaMenuPerdeu = None

    # Define a tela em que o jogo sera feito
    tela = Tk()

    # Configurações da tela do jogo
    tela.title("jogo da forca")
    tela.geometry("800x600")
    confgTela = Canvas(tela, width=800, height=600, bg="blue")

    # Faz o layout
    desenha_layout()

    # Desenha a forca
    desenha_forca()

    #desenha boneco e menu
    desenha_pessoa()
    menu_inicial()
    
    # Junta todos os botõe elementos na tela
    confgTela.pack()
    tela.mainloop()