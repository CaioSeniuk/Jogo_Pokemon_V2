def introducao():
    import biblioteca_texto,os,time,biblioteca_cores
    from biblioteca_texto import texto
    from biblioteca_cores import cor
    time.sleep(0.0001)
    os.system("cls")
    texto(f"\n{cor.FAIL}Bem-vindo ao mundo de Pokémon!{cor.ENDC}\n")
    texto(f"\nEste é um lugar especial, onde pessoas como você treinam para se tornar o Mestre Pokémon número 1 do mundo!\n")
    texto(f"\nMas, o que é um Pokémon?\nOs Pokémons são criaturas incríveis que compartilham o mundo com os seres humanos!\n")
    texto(f"Atualmente, existem centenas de espécies de Pokémon documentadas.\n\nA sua incrível tarefa é capturar, treinar e lutar com todos eles.\nIsto não é fácil, mas uma vez que você aprenda, saberá exatamente qual Pokémon escolher em uma luta.\n")



#Função para decidir qual pokemon vai encontrar, pókemon comum = 60% de chance, pókemon épico = 30% de chance e pókemon lendário = 10% de chance
def pokemon_porcentagem():
    import random, biblioteca_texto, biblioteca_cores
    from biblioteca_texto import texto
    from biblioteca_cores import cor    
    pokemons_caverna = ["Pikachu", "Golem", "Blastoide"]
    pokemon_caverna = random.randint(0,10)
    if 0 <= pokemon_caverna <= 6: #60% de chance de capturar o Pikachu
        texto(f"- Você encontrou o Pókemon {cor.WARNING}Pikachu{cor.ENDC} -")
        return pokemons_caverna[0]
    elif 7<=pokemon_caverna<=9: #30% de chance de capturar o Golem
        texto(f"- Você encontrou o Pókemon {cor.BOLD}Golem{cor.ENDC} -") 
        return pokemons_caverna[1]        
    elif pokemon_caverna == 10: #10% de chance de capturar o Blastoide
        texto(f"- Você encontrou o Pókemon {cor.OKBLUE}Blastoide{cor.ENDC} -")
        return pokemons_caverna[2]

#Função para decidir qual pokemon vai encontrar, pókemon comum = 60% de chance, pókemon épico = 30% de chance e pókemon lendário = 10% de chance
def pokemon_porcentagem2():
    import random, biblioteca_texto, biblioteca_cores
    from biblioteca_texto import texto
    from biblioteca_cores import cor 
    pokemons_caverna = ["Bulbasaur", "Golduck", "Charizard"]
    pokemon_caverna = random.randint(0,10)
    if 0 <= pokemon_caverna <= 6: #60% de chance de capturar o Bulbasaur
        texto(f"- Você encontrou o Pókemon {cor.OKGREEN}Bulbasaur{cor.ENDC} -")
        return pokemons_caverna[0]
    elif 7<=pokemon_caverna<=9: #30% de chance de capturar o Golduck
        texto(f"- Você encontrou o Pókemon {cor.OKCYAN}Golduck{cor.ENDC} -") 
        return pokemons_caverna[1]        
    elif pokemon_caverna == 10: #10% de chance de capturar o Charizard
        texto(f"- Você encontrou o Pókemon {cor.FAIL}Charizard{cor.ENDC} -")
        return pokemons_caverna[2]
    

#Função para escolher capturar ou não o pókemon
def deseja_capturar():
    import biblioteca_texto, os, time
    from biblioteca_texto import texto
    while True:
        texto("\nDeseja capturá-lo?")
        opcao_capturar = int(input("\n1- Sim\n2- Não\n"))
        if 1>opcao_capturar<2:
            os.system("cls")
            texto("\nErro ! Insira uma opção válida...")
            time.sleep(1)
            continue


 #Função para perguntar onde devemos ir
def pergunta_fazer():
    import biblioteca_texto, time, biblioteca_cores
    from biblioteca_texto import texto
    from biblioteca_cores import cor    
    texto("\nO que devemos fazer?\n")
    texto(f"{cor.OKGREEN}1- Entrar na floresta{cor.ENDC}{cor.BOLD}\n2- Entrar na caverna{cor.ENDC}{cor.HEADER}\n3- Ver Pokédex{cor.ENDC}\n4- Sair\n")
    time.sleep(0.1)
    return (float(input("\n-> ")))


                    

        