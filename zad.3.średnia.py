# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def srednia(a,b):
    if a>0 and b>a:
        suma=0;
        suma_niepodzielnych=0
        for i in range(a,b+1):
            if i/2:
                suma_niepodzielnych=1
                suma=suma+i
        print("Średnia arytmetyczna liczb nieparzystych należących do przedziału:",a,b,"wynosi:",suma/suma_niepodzielnych)
    else:
        print("niepoprawny przedział")
            
a=input("Proszę podać początek przedziału:")
b=input("Proszę podać koniec przedziału:")

srednia(int(a),int(b))
