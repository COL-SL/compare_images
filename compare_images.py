# ! /usr/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt
import pylab
np.set_printoptions(threshold=np.nan)


def load_compare_images():
    COMPARE_PATH_ONE = sys.argv[1]
    COMPARE_PATH_TWO = sys.argv[2]
    NUMBER_ROWS = int(sys.argv[3])
    NUMBER_COLUMNS = int(sys.argv[4])
    count_numbers_rows = 0
    count_numbers_columns = 0
    Matrix_initial = np.empty((NUMBER_ROWS, NUMBER_COLUMNS,))
    Matrix_recognition = np.empty((NUMBER_ROWS, NUMBER_COLUMNS,))
    Matrix_final = np.empty((NUMBER_ROWS, NUMBER_COLUMNS,))
    list_initial = []
    list_initial_recognition = []
    norm_l1 = 0
    np.set_printoptions(suppress=True)
    #FILE PROBANDO

    file_initial = open(COMPARE_PATH_ONE, 'r')
    for linea in file_initial:
        list_initial.append(linea)
    file_initial.close()

    list_initial = str(list_initial)
    list_initial = list_initial.replace('[', '')
    list_initial = list_initial.replace(']', '')
    list_initial = list_initial.replace(',', '')
    list_initial = list_initial.replace('\\n','')
    list_initial = list_initial.replace('\'', '')
    list_initial = str(list_initial).split(" ")

    for i in range(0,len(list_initial)):
        if list_initial[i] != '':
            #print "fila: ", count_numbers_rows
            #print "columna: ", count_numbers_columns
            #print list_initial[i]
            Matrix_initial[int(count_numbers_rows)][int(count_numbers_columns)] = float(list_initial[i])
            count_numbers_columns = count_numbers_columns + 1
            if count_numbers_columns == NUMBER_COLUMNS:
                #print "\n"
                count_numbers_rows = count_numbers_rows + 1
                count_numbers_columns = 0

    #print count_numbers
    #print count_numbers_rows
    '''
    for i in range (0,NUMBER_ROWS):
        for j in range (0,NUMBER_COLUMNS):
            print "fila: ", i
            print "columna: ", j
            print Matrix_initial[int(i)][int(j)]
        print "\n"
    '''
    file_initial_recognition = open(COMPARE_PATH_TWO, 'r')
    for linea in file_initial_recognition:
        list_initial_recognition.append(linea)
    file_initial_recognition.close()

    list_initial_recognition = str(list_initial_recognition)
    list_initial_recognition = list_initial_recognition.replace('[', '')
    list_initial_recognition = list_initial_recognition.replace(']', '')
    list_initial_recognition = list_initial_recognition.replace(',', '')
    list_initial_recognition = list_initial_recognition.replace('\\n', '')
    list_initial_recognition = list_initial_recognition.replace('\'', '')
    list_initial_recognition = str(list_initial_recognition).split(" ")

    count_numbers_rows = 0
    count_numbers_columns = 0

    for i in range(0,len(list_initial_recognition)):
        if list_initial_recognition[i] != '':
            #print "fila: ", count_numbers_rows
            #print "columna: ", count_numbers_columns
            #print list_initial[i]
            Matrix_recognition[int(count_numbers_rows)][int(count_numbers_columns)] = float(list_initial_recognition[i])
            count_numbers_columns = count_numbers_columns + 1
            if count_numbers_columns == NUMBER_COLUMNS:
                #print "\n"
                count_numbers_rows = count_numbers_rows + 1
                count_numbers_columns = 0
    '''
    for i in range (0,NUMBER_ROWS):
        for j in range (0,NUMBER_COLUMNS):
            print "fila: ", i
            print "columna: ", j
            print Matrix_recognition[int(i)][int(j)]
        print "\n"
    '''
    for i in range(0, NUMBER_ROWS):
        for j in range(0, NUMBER_COLUMNS):
            norm_l1 = norm_l1 + abs(Matrix_initial[int(i)][int(j)] - Matrix_recognition[int(i)][int(j)])

    print norm_l1

    #print abs(Matrix_initial[int(0)][int(0)] - Matrix_recognition[int(0)][int(0)])

    for i in range(0, NUMBER_ROWS):
        for j in range(0, NUMBER_COLUMNS):
            Matrix_final[int(i)][int(j)] = (float(Matrix_initial[int(i)][int(j)]) - float(Matrix_recognition[int(i)][int(j)]))/float(norm_l1)

    for i in range(0, NUMBER_ROWS):
        for j in range(0, NUMBER_COLUMNS):
            print "fila: ", i
            print "columna: ", j
            print Matrix_final[int(i)][int(j)]
        print "\n"

    plt.plot(Matrix_final, marker='+', linestyle=' ')
    plt.title('Compare Images')
    plt.legend()
    plt.show()


load_compare_images()
