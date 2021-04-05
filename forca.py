import os, time

os.system('cls' if os.name == 'nt' else 'clear')

print('''\033[1;34m
	      jj  ooooooo  ggggrgg  ooooooo      dddddd   aaaaaaa
 	      jj  oo   oo  gg       oo   oo      dd   dd  aa   aa
	 jj   jj  oo   oo  gg  ggg  oo   oo      dd   dd  aaaaaaa
	 jj   jj  oo   oo  gg   gg  oo   oo      dd   dd  aa   aa
	 jjjjjjj  ooooooo  ggggggg  ooooooo      dddddd   aa   aa''')
print('''\033[1;31m
	FFFFFFFFFF  OOOOOOOOOO	RRRRRRRRRR  CCCCCCCCCC  AAAAAAAAAA
	FFFFFFFFFF  OOOOOOOOOO	RRRRRRRRRR  CCCCCCCCCC  AAAAAAAAAA
	FFF         OOO    OOO	RRR    RRR  CCC         AAA    AAA
	FFF         OOO    OOO	RRR    RRR  CCC         AAA    AAA
	FFFFFFF     OOO    OOO	RRRRRRRRRR  CCC         AAAAAAAAAA
	FFFFFFF     OOO    OOO	RRRRRRRRRR  CCC         AAAAAAAAAA
	FFF         OOO    OOO  RRRRR       CCC         AAA    AAA
	FFF         OOO    OOO  RRR RRR     CCC         AAA    AAA
	FFF         OOOOOOOOOO	RRR  RRR    CCCCCCCCCC  AAA    AAA
	FFF         OOOOOOOOOO	RRR    RRR  CCCCCCCCCC  AAA    AAA''')

time.sleep(2)
# os.system('cls' if os.name == 'nt' else 'clear')

print('\033[1;34m')
pOriginal = input('Digite a palavra: ').strip().upper()
tam = len(pOriginal)
pForca = ''
acertos = int(0)
erros = int(5)
digitadas = []

for k in range(0, tam):
    if pOriginal[k] == ' ':
        pForca = pForca + pOriginal[k]
    else:
        pForca = pForca + '_'

while pOriginal != pForca:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'\033[1;31m          ATENÇÃO VOCE TEM {erros} CHANCES PARA ACERTAR A PAVAVRA\n\n')
    print(f'\033[1;34m          Acertos: {acertos} \033[1;30m- \033[1;31mErros: {erros}\n')
    print(f'\033[1;30m          Letras já digitas({digitadas})\n\n')
    print(f'\033[1;33m          Dica: A palavra tem {len(pOriginal)} letras e {len(pOriginal.strip().split())-1} espaço[s].\n\n')
    print(f'\033[0;40m {pForca:^100}\n\n')

    lApoio = int(0)
    lAtual = ''

    while lAtual == '':
        lAtual = input('\033[1;35m          Digite uma letra: ').strip().upper()

        if len(lAtual) > 1:
            print('\033[1;31m             Deve conter uma letra apenas.')
            lAtual = ''

        if digitadas.count(lAtual) == 1:
            print('\033[1;31m             Letra já digitada anteriormente.')
            lAtual = ''

    digitadas.append(lAtual)

    qtd = pOriginal.count(lAtual)
    # os.system('cls' if os.name == 'nt' else 'clear')

    if qtd > 0:
        acertos += 1

        for i in range(0, qtd):
            lEncontrada = pOriginal.find(lAtual, lApoio, )
            lApoio = lEncontrada + 1
            pForca2 = ''

            for j in range(0, tam):
                if j == lEncontrada:
                    pForca2 = pForca2 + lAtual
                else:
                    pForca2 = pForca2 + pForca[j]

            pForca = pForca2
    else:
        erros = erros - 1

    # print(f'\033[1;34m{pForca:^40}')
    # print(f'\033[1;34mAcertos: {acertos} \033[1;30m- \033[1;31mErros: {erros}')

    if erros == 0:
        print('\033[1;31m')
        print('''
      ___         ___           ___          _____          ___           ___     
     /  /\       /  /\         /  /\        /  /::\        /  /\         /__/\    
    /  /::\     /  /:/_       /  /::\      /  /:/\:\      /  /:/_        \  \:\   
   /  /:/\:\   /  /:/ /\     /  /:/\:\    /  /:/  \:\    /  /:/ /\        \  \:\  
  /  /:/~/:/  /  /:/ /:/_   /  /:/~/:/   /__/:/ \__\:|  /  /:/ /:/_   ___  \  \:\ 
 /__/:/ /:/  /__/:/ /:/ /\ /__/:/ /:/___ \  \:\ /  /:/ /__/:/ /:/ /\ /__/\  \__\:
 \  \:\/:/   \  \:\/:/ /:/ \  \:\/:::::/  \  \:\  /:/  \  \:\/:/ /:/ \  \:\ /  /:/
  \  \::/     \  \::/ /:/   \  \::/~~~~    \  \:\/:/    \  \::/ /:/   \  \:\  /:/ 
   \  \:\      \  \:\/:/     \  \:\         \  \::/      \  \:\/:/     \  \:\/:/  
    \  \:\      \  \::/       \  \:\         \__\/        \  \::/       \  \::/   
     \__\/       \__\/         \__\/                       \__\/         \__\/    
        \n\n\n''')

    elif pOriginal == pForca:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\033[1;31m          ATENÇÃO VOCE TEM {erros} CHANCES PARA ACERTAR A PAVAVRA\n\n')
        print(f'\033[1;34mAcertos: {acertos} \033[1;30m- \033[1;31mErros: {erros}\n')
        print(f'\033[1;30m          Letras já digitas({digitadas})\n\n')

        print(f'\033[0;40m {pForca:^100}\n\n')

        print('\033[1;33m')
        print('''
      ___          /  /\         /  /\         /  /\         /  /\         /  /\    
     /  /\        /  /::\       /  /::|       /  /::\       /  /::\       /  /:/    
    /  /:/       /  /:/\:\     /  /:|:|      /  /:/\:\     /  /:/\:\     /  /:/     
   /  /:/       /  /::\ \:\   /  /:/|:|__   /  /:/  \:\   /  /::\ \:\   /  /:/      
  /__/:/  ___  /__/:/\:\ \:\ /__/:/ |:| /\ /__/:/ \  \:\ /__/:/\:\ \:\ /__/:/     /
  |  |:| /  /\ \  \:\ \:\_\/ \__\/  |:|/:/ \  \:\  \__\/ \  \:\ \:\_\/ \  \:\    /:/
  |  |:|/  /:/  \  \:\ \:\       |  |:/:/   \  \:\        \  \:\ \:\    \  \:\  /:/ 
  |__|:|__/:/    \  \:\_\/       |__|::/     \  \:\        \  \:\_\/     \  \:\/:/  
   \__\::::/      \  \:\         /__/:/       \  \:\        \  \:\        \  \::/   
       ~~~~        \__\/         \__\/         \__\/         \__\/         \__\/    
        \n\n\n''')

        erros = int(0)

    while erros == 0:
        resp = str(input('\033[1;32mDeseja jogar novamante? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print(f'resposta deve ser S ou N')
        elif resp == 'S':
            print('\033[1;34m')
            pOriginal = input('Digite a palavra: ').strip().upper()
            tam = len(pOriginal)
            pForca = ''
            acertos = int(0)
            erros = int(5)
            digitadas = []

            for k in range(0, tam):
                if pOriginal[k] == ' ':
                    pForca = pForca + pOriginal[k]
                else:
                    pForca = pForca + '_'
        elif resp == 'N':
            print('\033[0;30')
            exit()
