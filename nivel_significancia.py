import numpy as np
import sys
import math as mt


def covarianza():
    paro = [13.9, 10.63, 11.61, 11.37, 10.53, 8.71, 8.26, 8.57, 13.79, 18.66, 20.11, 22.56, 25.77, 25.73, 23.70, 20.90]
    pres = [45.10, 47.57, 51.88, 56.09, 59.37, 61.05, 64.02, 67.1, 73.55, 76.07, 73.92, 70.47, 68.59, 66.76, 65.01, 61.61]

    #paro = [6, 4, 8, 9, 4, 8, 10, 9, 5, 6]
    #pres = [5, 5, 7, 5, 3, 8, 10, 8, 7, 6]
    total_data = 16

    media_paro = np.average(paro)
    print '\n',"media_paro: ", media_paro
    desviacion_tipica_paro = np.std(paro)
    print "desviacion_tipica_paro: ", desviacion_tipica_paro

    media_pres =  np.average(pres)
    print '\n',"media_pres: ", media_pres
    desviacion_tipica_pres =  np.std(pres)
    print "desviacion_tipica_pres: ", desviacion_tipica_pres,'\n'

    mul_paro_pres = np.dot(np.array(paro), np.array(pres))

    covarianza_paro_pres = ((mul_paro_pres/total_data) - (media_paro * media_pres))

    resul_final = covarianza_paro_pres / (desviacion_tipica_paro * desviacion_tipica_pres)

    print resul_final

    value_resta_promedio_paro = paro - media_paro
    value_resta_promedio_pres = pres - media_pres

    print "muestra promedio paro:", value_resta_promedio_paro
    print "muestra promedio pres", value_resta_promedio_pres

    '''
    value = value * value

    print value
    sum = 0

    for i in range (0,total_data):
        sum = sum + value[i]

    print mt.sqrt(sum / total_data - 1)


    #for i in range(0, int(total_data)):
    #    corrected = [value - media_pres  for value in (pres[int(i)])]






    for i in range(0, 15):
        mean = np.average(Matrix[:, i])
        corrected = [value - mean for value in (Matrix[:, i])]
        Matrix[:, i] =  np.array(corrected)
    '''



covarianza()