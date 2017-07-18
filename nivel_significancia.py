import numpy as np
import sys
import math as mt


def covarianza():
    #paro = [22.1, 20.6, 18.6, 15.6, 13.9, 10.63, 11.61, 11.37, 10.53, 8.71, 8.26, 8.57, 13.79, 18.66, 20.11, 22.56, 25.77, 25.73, 23.70, 20.90]
    #pres = [41.90, 42.75, 44.37, 44.19, 45.10, 47.57, 51.88, 56.09, 59.37, 61.05, 64.02, 67.1, 73.55, 76.07, 73.92, 70.47, 68.59, 66.76, 65.01, 61.61]
    paro = [13.9, 10.63, 11.61, 11.37, 10.53, 8.71, 8.26, 8.57, 13.79, 18.66, 20.11, 22.56, 25.77, 25.73, 23.70, 20.90]
    pres = [45.10, 47.57, 51.88, 56.09, 59.37, 61.05, 64.02, 67.1, 73.55, 76.07, 73.92, 70.47, 68.59, 66.76, 65.01, 61.61]
    #paro = [10.63, 11.61, 11.37, 10.53, 8.71, 8.26, 8.57, 13.79, 18.66, 20.11, 22.56, 25.77, 25.73, 23.70, 20.90]
    #pres = [47.57, 51.88, 56.09, 59.37, 61.05, 64.02, 67.1, 73.55, 76.07, 73.92, 70.47, 68.59, 66.76, 65.01, 61.61]

    #anio = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
    #paro = [20.6, 18.6, 15.6, 13.9, 10.63, 11.61, 11.37, 10.53, 8.71, 8.26, 8.57, 13.79, 18.66, 20.11, 22.56,25.77, 25.73, 23.70, 20.90]
    #pres = [0.85, 1.62, -0.18,  0.91, 2.47, 4.31, 4.21, 3.28, 1.68, 2.97, 3.08, 6.45, 2.52, -2.15, -3.45, -1.88, -1.83, -1.75, -3.4]
    #pres = [0.85, 1.62, -0.18, 0.91, 2.47, 4.31, 4.21, 3.28, 1.68, 2.97, 3.08, 6.45, 2.52, -2.15, -3.45, -1.88, -1.83, -1.75]

    #paro = [105, 116, 103, 124, 137, 126, 112, 129, 118, 105]
    #pres = [4,8,2,7,9,9,3,10,7,6]

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

    print "correlacion: ", resul_final

    t = resul_final / mt.sqrt((1-resul_final * resul_final)/(total_data - 2))

    print "t de student:", t

    '''
    value_resta_promedio_paro = paro - media_paro
    value_resta_promedio_pres = pres - media_pres

    print "muestra promedio paro:", value_resta_promedio_paro
    print "muestra promedio pres", value_resta_promedio_pres

    cuadrado_value_resta_promedio_paro = value_resta_promedio_paro * value_resta_promedio_paro
    cuadrado_value_resta_promedio_preso = value_resta_promedio_pres * value_resta_promedio_pres

    print "cuadrado muestra promedio paro: ", cuadrado_value_resta_promedio_paro
    print "cuadrado muestra promedio preso ", cuadrado_value_resta_promedio_preso

    sum_paro = 0
    for i in range(0, total_data):
        sum_paro = sum_paro + cuadrado_value_resta_promedio_paro[i]

    sum_preso = 0
    for i in range(0, total_data):
        sum_preso = sum_preso + cuadrado_value_resta_promedio_preso[i]

    sum_sqrt_paro = mt.sqrt(sum_paro / (total_data - 1))
    sum_sqrt_preso = mt.sqrt(sum_preso / (total_data - 1))

    print "sum_sqrt_paro: ", sum_sqrt_paro
    print "sum_sqrt_preso: ", sum_sqrt_preso


    sd = mt.sqrt((desviacion_tipica_paro*desviacion_tipica_paro)/total_data + (desviacion_tipica_pres*desviacion_tipica_pres)/total_data)
    print sd

    t = (media_pres - media_paro) / sd

    print "t: ", t

    gl = (total_data + total_data) - 2
    print "gl: ", gl

    value = value * value

    print value
    sum = 0

    for i in range (0,total_data):
        sum = sum + value[i]

    print mt.sqrt(sum / total_data - 1)

    
    for i in range(0, int(total_data)):
       corrected_promedio_paro = [value - media_pres  for value in (pres[int(i)])]




    
    for i in range(0, 15):
        mean = np.average(Matrix[:, i])
        corrected = [value - mean for value in (Matrix[:, i])]
        Matrix[:, i] =  np.array(corrected)
    '''



covarianza()