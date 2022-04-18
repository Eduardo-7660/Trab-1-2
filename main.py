import numpy as np
# Ideia do código, fazer com que uma matriz se espelhe na outra, uma servindo como front outra como back, conforme vai solicitando
# as colunas ela vai se abrindo na matriz de frente, se o valor for um '#' ele ira acabar o jogo pos é uma bomba.
from pathlib import Path
import os

def print_map(matrix,len_line,len_column):
    for i in range(0, len_line):
        print("\n")
        for j in range(0, len_column):
            print(matrix[i][j], " ", end=' ')
    return 0

def fill_matrix3(matrix1, matrix2, matrix3,len_line,len_column): #só serve pra fazer a verificação do win do game
    for a in range (0,len_line):
        for b in range (0,len_column):
            if matrix2[a][b] == "#":
                matrix3[a][b] = "-"
            else:
                matrix3[a][b] = matrix2[a][b]
    return 0

def fill_matrix2(matrix2, list_char,len_line,len_column): #preenche a matrix2
    for i in range(0, len_line):
        for j in range(0, len_column):
            matrix2[i][j] = list_char[i][j]
    return matrix2

def change_map(line, column, matrix1, matrix2):
    char = str
    char = matrix2[line][column]
    return char





list_maps = []
path = Path().absolute()
for _, _, arquivo in os.walk(path / 'mapas'):
    for i in range(len(arquivo)):
        list_maps.append(arquivo[i])



for i in range(len(list_maps)):
    print("[" + str(i+1) + "]" + " para  " + list_maps[i])

map_option = int(input(f"Selecione o mapa acima:"))

archive = open(path / "mapas" / list_maps[map_option-1], "r")  # onde esta o arquivo
txt = archive.readlines()

list_char = []
first = True
len_line = 0
len_column = 0
score_max = 0

for j in txt:
    if first:
        here_auxiliar = j.split(";")
        score_max = int(here_auxiliar[0])
        len_line = int(here_auxiliar[1])
        len_column = int(here_auxiliar[2])
        first = False
    else:
        here_auxiliar = j.split(" ")
        list_char.append(here_auxiliar)

matrix1 = np.empty([len_line, len_column], str)
matrix2 = np.empty([len_line, len_column], str)
matrix3 = np.empty([len_line, len_column], str)
lost = False


for i in range(0, len_line):
    for j in range(0, len_column):
        matrix1[i][j] = '-'

fill_matrix2(matrix2, list_char,len_line,len_column)
fill_matrix3(matrix1, matrix2, matrix3,len_line,len_column)
print_map(matrix1,len_line,len_column)
score = 0


while lost == False:
    print('\n')
    line = int(input(f"Digite a LINHA desejada: "))
    column = int(input(f"Digite a COLUNA desejada: "))


    verif = change_map(line-1, column-1, matrix1, matrix2)
    matrix1[line-1][column-1] = verif
    print_map(matrix1,len_line,len_column)
    if verif == '#':
        lost = True
        print(f"Você perdeu ")
    elif score < score_max:
        score += 1
    elif score == score_max:
        print(f"Você ganhou!")



archive.close