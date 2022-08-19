import os

import unidecode as unidecode

pastas = ["Conflicto israelí-palestino",
          "Enfrentamientos israelíes y palestinos",
          "Enfrentamientos árabes y judíos",
          "Jerusalém",
          "Faixa de Gaza",
          "Ramadán",
          "Palestina ataques",
          "Israel ataques",
          "Hamas"]

for termo in pastas:
    ocorrencias = 0
    #termo = 'Hamas'

    pasta = './{}'.format(termo)

    termo = unidecode.unidecode(termo)
    termo = termo.lower()
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            #print(os.path.join(diretorio, arquivo))
            arq = open(os.path.join(diretorio, arquivo))
            linhas = arq.readlines()
            for linha in linhas:
                #print(linha)
                linha = unidecode.unidecode(linha)
                linha = linha.lower()
                ocorrencias = ocorrencias + linha.count(termo)

    print(ocorrencias)
