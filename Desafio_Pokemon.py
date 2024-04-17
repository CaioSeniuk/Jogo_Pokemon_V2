#Bibliotecas
import biblioteca_funcoes, biblioteca_texto,os,time, random
from biblioteca_texto import texto
from biblioteca_cores import cor
from biblioteca_funcoes import pokemon_porcentagem, pokemon_porcentagem2, introducao, pergunta_fazer

pokedex = []
#Função chamada para a aparecer no console a introdução animada
introducao()

#Variável fora do looping para poder sair do jogo quando quiser
sair = 0

#Número de tentativas totais de captura aos Pókemons no jogo
tentativa_captura = 3

#O jogo se baseia em um Looping infinito até que o usuário decida sair ou acabem as tentativas de captura aos Pókemons
while True:

    #Se o usuário optar por sair do jogo, sairá do looping, encerrando o jogo
    if sair == 1:
            for i in range(0,2):
                os.system("cls")
                texto("\nSaindo do jogo...")
                time.sleep(1)
                os.system("cls")
            break
    
    #Se as tentativas de captura chegarem a 0, irá encerrar o jogo
    if tentativa_captura == 0:
        texto("\nAcabaram as tentativas... Reinicie o Jogo\n\n")
        time.sleep(1)
        break

    texto(f"\nVamos começar?\n\n{cor.OKGREEN}1- Sim{cor.ENDC}{cor.FAIL}\n2- Não{cor.ENDC}\n")
    opcao_introducao = float(input("\n-> "))

    #COMEÇA O JOGO se o usuário decidir começar o jogo
    if opcao_introducao == 1:
        
        #Nova tela para inserir o nome
        os.system("cls")
        texto(f"\n\nQual o seu nome?\n")
        nome = input("-> ")

        #Limpar o console
        os.system("cls")

        #Professor Carvalho se apresentando 
        texto(f"\nOlá, {nome}.\n\nEu sou o Professor Carvalho e eu vou te ajudar nesta jornada.\nPara começarmos às capturas dos pokémons devemos escolher um lugar para irmos.")
        
        #JOGO COMEÇA AQUI
        while True:

            #Se as tentativas de captura esgotarem, sairá do looping do jogo
            if tentativa_captura == 0:
                break

            #Variável para printar o texto da função e receber o valor inserido do usuário, com seus respectivos caminhos
            escolha = pergunta_fazer()

            #Se 1, entrar na floresta
            if escolha == 1:
                
                #Nova tela para o ambiente da floresta
                os.system("cls")
                print("\n'Escolheu entrar na floresta'\n")

                #Variável para armazenar o valor retornado pela função na qual calcula o Pókemon encontrado com base nas probabilidades de encontro de cada um
                pokemon_encontrado = pokemon_porcentagem()
                if pokemon_encontrado in pokedex: #se o pokemon não estiver na pokedex, adicionar, se não, não adicionar
                    texto(f"\nPókedex: {pokedex}\nVocê já tem este pókemon!\n")
                    continue
                texto(f"\nDeseja tentar capturar {pokemon_encontrado}?\n1- Sim\n2- Não\n")
                escolha_capturar = int(input("\n-> "))
                
                #Se desejar capturar o pókemon, irá acontecer a tentativa
                if escolha_capturar == 1:
                    chance_captura = random.randint(1,100)
                    if 1<=chance_captura<= 50:
                        pokedex.append(pokemon_encontrado)
                        texto(f"\nPókemon {pokemon_encontrado} capturado com {cor.UNDERLINE}{cor.OKGREEN}sucesso!{cor.ENDC}\n")
                    elif 51<=chance_captura<=100:
                        tentativa_captura -= 1
                        texto(f"\nPókemon {pokemon_encontrado} {cor.UNDERLINE}{cor.FAIL}não capturado{cor.ENDC}, tente novamente!\nTentativas restantes: {tentativa_captura}") 
                    continue
                    
                #Se não desejar capturar o pókemon, irá sair da floresta
                elif escolha_capturar == 2:
                    #Animação do texto
                    for i in range(0,2):
                        os.system("cls")
                        texto("\nSaindo da floresta...")
                        time.sleep(1)
                        os.system("cls")
                    continue                  

                #Se o usuário inserir um valor fora do intervalo [1,2], irá retornar à pergunta
                elif 1>escolha_capturar>2:
                    os.system("cls")
                    texto("\nErro ! Insira uma opção válida...")
                    time.sleep(1)
                    break                     
                
            #Se 2, entrar na caverna
            elif escolha == 2:
                #Nova tela para o ambiente da caverna
                os.system("cls")
                print("\n'Escolheu entrar na caverna'\n")

                #Variável para armazenar o valor retornado pela função na qual calcula o Pókemon encontrado com base nas probabilidades de encontro de cada um
                pokemon_encontrado2 = pokemon_porcentagem2()
                #Se o pokemon estiver na pókedex, não prosseguir
                if pokemon_encontrado2 in pokedex:
                    texto(f"\nPókedex: {pokedex}\nVocê já tem este pókemon!\n")
                    continue
                texto(f"\nDeseja tentar capturar {pokemon_encontrado2}?\n1- Sim\n2- Não\n")
                escolha_capturar = int(input("\n-> "))

                #Se desejar capturar o pókemon, irá acontecer a tentativa
                if escolha_capturar == 1:
                    chance_captura = random.randint(1,100)
                    if 1<=chance_captura<= 50:
                        pokedex.append(pokemon_encontrado2)
                        texto(f"\nPókemon {pokemon_encontrado2} capturado com {cor.UNDERLINE}{cor.OKGREEN}sucesso!{cor.ENDC}\n")
                    elif 51<=chance_captura<=100:
                        tentativa_captura -= 1
                        texto(f"\nPókemon {pokemon_encontrado2} {cor.UNDERLINE}{cor.FAIL}não capturado{cor.ENDC}, tente novamente!\nTentativas restantes: {tentativa_captura}") 
                    continue
                    
                #Se não desejar capturar o pókemon, irá sair da floresta
                elif escolha_capturar == 2:
                    #Animação do texto
                    for i in range(0,2):
                        os.system("cls")
                        texto("\nSaindo da caverna...")
                        time.sleep(1)
                        os.system("cls")
                    continue                  
            
            #Se 3, mostrar Pókedex
            elif escolha == 3:
                os.system("cls")
                print(f"\nPókedex: {pokedex}")
                time.sleep(1)
                continue
            
            #Se 4, sair do jogo
            elif escolha == 4:
                sair += 1
                break
            
            #Se o usuário inserir qualquer valor fora do intervalo [1,4] irá retornar o loop com a pergunta e nada será feito
            else:
                os.system("cls")
                texto("\nErro ! Insira uma opção válida...")
                time.sleep(1)
                continue      
    
    #DESPEDIDA se o usuário decidir não começar o jogo
    elif opcao_introducao == 2: 
        texto("\nQue pena! Até Logo...\n")
        break
    
    #ERRO, caso o usuário insira um valor fora do intervalo [1,2] para decidir se começa ou não o jogo
    else:
        os.system("cls")
        texto("\nErro ! Insira uma opção válida...")
        time.sleep(1)
        continue