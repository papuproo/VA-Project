# and, or, not

from numpy import true_divide


gas = True
encendido = True
edad = 18

if gas and (encendido or edad > 17):
    print("Puedes avanzar")
