import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

planet_idx = {'MERCURY':0, 'VENUS':1, 'EARTH':2, 'MARS':3, 'JUPITER':4, 'SATURN':5,	'URANUS':6, 'NEPTUNE':7, 'PLUTO':8}
planet_masses_e24 = [0.330,	4.87,	5.97,	0.642,	1898,	568,	86.8,	102, 0.0146]
planet_dists_e9 = [57.9,	108.2,	149.6,	227.9,	778.6,	1433.5,	2872.5,	4495.1,	5906.4] 

planet_name = input("Enter your planet name: ").upper()
G=6.67408e-11 
M=1.98847e30 
m=planet_masses_e24[planet_idx[planet_name]]*1e24 
D=planet_dists_e9[planet_idx[planet_name]]*1e9

dt=24*3600

class CelestrialBody:
    def __init__(self, x=[0.,0.], v=[0.,0.], a=[0.,0.]):
        self.x = np.array(x, dtype=float)
        self.v = np.array(v, dtype=float)
        self.a = np.array(a, dtype=float)

planet = CelestrialBody([D,0.], [0.,math.sqrt(G*M/D)], [0.,0.])
star = CelestrialBody([0.,0.], -planet.v*m / M, [0., 0.])

fig = plt.figure()
#plt.suptitle("%d years, %d days" % (total_days//365, total_days%365))
    
ax = fig.add_subplot(1, 1, 1)

total_days = 0
def animate(frame):
    R = planet.x - star.x 

    planet.a = -G*M*R*((R[0]**2 + R[1]**2)**-1.5) 
    planet.v += planet.a * dt 
    planet.x += planet.v * dt

    star.a = G*m*R*((R[0]**2 + R[1]**2)**-1.5) 
    star.v += star.a * dt
    star.x += star.v * dt
    ax.clear()
    ax.set_xlim(-D*1.5, D*1.5)
    ax.set_ylim(-D*1.5, D*1.5)

    planet_plot, = ax.plot(*planet.x, 'b.')
    star_plot, = ax.plot(*star.x, 'r.')

    global total_days
    total_days += 1
    ax.set_title("%d years, %d days" % (total_days//365, total_days%365))
    
    ax.set_xlabel('x-coordinate (m)',fontsize=10)
    ax.set_ylabel('y-coordinate (m)',fontsize=10)


    return planet_plot, star_plot

ani = FuncAnimation(fig, animate, frames=None, interval=10)

plt.show()