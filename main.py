import numpy as np

def print_map(matrix):
    for i in range(0, 5):
        print("\n")
        for j in range(0, 5):
            print(matrix[i][j], " ", end=' ')
    return 0

def fill_matrix2(matrix2, list_char):
    for i in range(0, 5):
        for j in range(0, 5):
            matrix2[i][j] = list_char[i][j]
    return matrix2

def change_map(line, column, matrix1, matrix2):
    char = str
    char = matrix2[line][column]
    return char

archive = open("C:/Users/eduar/Downloads/atividade1.txt", "r")  # onde esta o arquivo
txt = archive.readlines()
matrix1 = np.empty([5, 5], str)
matrix2 = np.empty([5, 5], str)
list_char = []
lost = False


for i in range(0, 5):
    for j in range(0, 5):
        matrix1[i][j] = '-'

#print(txt, '\n')

for j in txt:
    here_auxiliar = j.split(" ")
    list_char.append(here_auxiliar)
print(list_char, '\n')


fill_matrix2(matrix2, list_char)
print_map(matrix1)

while lost == False:
    line = int(input(f"Digite a LINHA desejada: "))
    column = int(input(f"Digite a COLUNA desejada: "))
    verif = change_map(line, column, matrix1, matrix2)
    matrix1[line][column] = verif
    print(matrix1, '/n')
    if verif == '#':
        lost =True
        print("Você perdeu ")