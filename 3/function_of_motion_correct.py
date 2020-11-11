from math import sin, sqrt


def motionOne(mass, force_constant, time):
    """
    You will got the position of the mass.
    """
    frequency = 20
    u = 1/sqrt(2)
    return  [u * sin(frequency*time),u* sin(frequency*time)]

def motionSecond(mass, force_constant, time):
    """
    You will got the position of the mass.
    """
    frequency = 21.9
    u = 1/sqrt(2)
    return  [u * sin(frequency*time), -u * sin(frequency*time)]

#SUGESTÃO utilizar a equação de definição do movimento
#    frequency = 21.9
#    u = 1/sqrt(2)
#    return  [u* sin(frequency*time),\
#             -u* sin(frequency*time)]
