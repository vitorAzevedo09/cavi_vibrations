from math import pi
from math import sin
from math import cos
from math import acos   # arccos()


def motion(mass, force_constant, position, velocity,t):
    """
    You will got the position of the mass.
    """
    amplitude = None
    phase_angle = None
    natural_frequency = (force_constant/mass)**0.5

    if position != 0 and velocity == 0:     # x(0) = X, ẋ(0) = 0.
        amplitude = position
        phase_angle = 0.5*pi
        return amplitude*sin(t*natural_frequency + phase_angle)

    elif position == 0 and velocity != 0:   # x(0) = 0, ẋ(0) = V.
        amplitude = velocity / natural_frequency
        phase_angle = 0
        return amplitude*sin(t*natural_frequency + phase_angle)

    else:                                   # x(0) = X, ẋ(0) = V.
        amp1 = position
        amp2 = velocity / natural_frequency
        return amp1*cos(natural_frequency*t) + amp2*sin(natural_frequency*t)
        #phase_angle = acos(velocity/(amplitude*natural_frequency))
        #amplitude = position / sin(phase_angle)
