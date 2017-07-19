import numpy as np
import sys
import math as mt


def covarianza():
    # datos desde 1996 hasta 2017. un total de 22 anios
    paro = [22.1, 20.6, 18.6, 15.6, 13.9, 10.63, 11.61, 11.37, 10.53, 8.71, 8.26, 8.57, 13.79, 18.66, 20.11, 22.56, 25.77, 25.73, 23.70, 20.90, 18.91, 17.7]
    pres = [41.90,42.75, 44.370, 44.197, 45.10, 47.57, 51.88, 56.09, 59.37, 61.05, 64.02, 67.1, 73.55, 76.07, 73.92, 70.47, 68.59, 66.76, 65.01, 61.61, 59.58, 60.49]

    #paro = [6, 4, 8, 9, 4, 8, 10, 9, 5, 6]
    #pres = [5, 5, 7, 5, 3, 8, 10, 8, 7, 6]
    total_data = 22

    media_paro = np.average(paro)
    desviacion_tipica_paro = np.std(paro)

    media_pres =  np.average(pres)
    desviacion_tipica_pres =  np.std(pres)

    mul_paro_pres = np.dot(np.array(paro), np.array(pres))

    covarianza_paro_pres = ((mul_paro_pres/total_data) - (media_paro * media_pres))

    resul_final = covarianza_paro_pres / (desviacion_tipica_paro * desviacion_tipica_pres)

    print resul_final


    #for i in range(0, int(total_data)):
    #   corrected = [value - media_pres  for value in (pres[int(i)])]





    '''
    for i in range(0, 15):
        mean = np.average(Matrix[:, i])
        corrected = [value - mean for value in (Matrix[:, i])]
        Matrix[:, i] =  np.array(corrected)
    '''



covarianza()