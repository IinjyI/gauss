#######################################    HELPERS   #######################################

import sys
import re
import msvcrt
from time import sleep
subMatrix=[]
matrix=[]
matrixInOperation=[]
inService=True

#######################################    FUNCTION TO PRINT THE AUGMENTED MATRIX    #######################################

def printMatrix():
    print('\n Augmented matrix for the system : \n')
    for row in range(0, len(matrix)):
        print(f'\t{matrix[row]}\n')
    print('\n\n')

#######################################    BEGIN THE PROGRAM    #######################################

while inService:
    nEqns= int(input('enter number of equations\n'))
    nVars=int(input('enter number of variables\n'))

#######################################    STORE THE VALUES    #######################################

    for nEqn in range (1,nEqns+1):
        for coVar in range (1,nVars+1):
            variableCoefficient=input(f'Enter the coefficient for #{coVar} variable in equation #{nEqn}\n' )
            if not re.match('[0-9-.]', variableCoefficient):
                subMatrix.append(0)
            else:
                subMatrix.append(float(variableCoefficient))
            
       
        absoluteValue=input(f'Enter the absolute value in equation #{nEqn}\n' )
        if not re.match('[0-9-.]', absoluteValue):
            subMatrix.append(0)
        else:
            subMatrix.append(float(absoluteValue))
        matrix.append(subMatrix.copy())
        subMatrix.clear()
        matrixInOperation.append(0)
    printMatrix()

#######################################    EDIT A VALUE    #######################################

    print("press E if you want to edit a number, otherwise press enter\n")
    if msvcrt.getwche().lower()=='e':
        print('\n')
        rowEdit=int(input('number of row?\n'))
        columnEdit=int(input('number of column?\n'))
        matrix[rowEdit-1][columnEdit-1]=float(input('enter the value\n'))
        printMatrix()

#######################################    SOLVE    #######################################

    for i in range(0,nEqns):
        for j in range (i+1,nVars):
            ratio = matrix[j][i]/matrix[i][i]
            for k in range(nVars+1):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
                printMatrix()
    matrixInOperation[nVars-1]=matrix[nVars-1][nVars]/matrix[nVars-1][nVars-1]
    print(matrixInOperation)
    

    for i in range(nVars-2,-1,-1):
        matrixInOperation[i] = matrix[i][nVars]
        print(matrixInOperation)
        for j in range(i+1,nVars):
            matrixInOperation[i] = matrixInOperation[i] - matrix[i][j]*matrixInOperation[j]
            printMatrix()
        matrixInOperation[i] = matrixInOperation[i]/matrix[i][i]
        print(matrixInOperation)
        printMatrix()

#######################################    PRINT SOLUTION    #######################################

    print('\nRequired solution is: \n')
    for i in range(nVars):
        print('X%d = %0.2f' %(i+1,matrixInOperation[i]), end = '\t')
    
#######################################    END PROGRAM    #######################################
    
    print("\n\npress R if you want to solve another system, otherwise press any key\n")
    if  msvcrt.getwche().lower()=='r':
        print('\n')
    else:
        print('\nexiting...')
        matrix.clear()
        matrixInOperation.clear()
        sleep(3)
        sys.exit()