from math import sin, sqrt


def motionOne(mass, force_constant, time):
    """
    You will got the position of the mass.
    """
    frequency = 0.32
    u = 1/sqrt(2)
    return  [int( sin(frequency*time) * ((11*force_constant) - (pow(frequency,2)*mass))*(u) - (force_constant*u)),\
             int( sin(frequency*time) * (force_constant*u) - ((11*force_constant) - (pow(frequency,2)*mass))*(u))]


#SUGESTÃO utilizar a equação de definição do movimento
#    frequency = 21.9
#    u = 1/sqrt(2)
#    return  [u* sin(frequency*time),\
#             -u* sin(frequency*time)]


# def motionSecond(mass, force_constant, time):
#     """
#     You will got the position of the mass.
#     """
#     frequency = 0.32
#     u = 1/sqrt(2)
#     return  [int( sin(frequency*time) * ((11*force_constant) - (pow(frequency,2)*mass))*(u) - (force_constant*u)),\
#              int( sin(frequency*time) * (force_constant*u) - ((11*force_constant) - (pow(frequency,2)*mass))*(u))]
