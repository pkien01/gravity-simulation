import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import random

n = 10
name_id = {'SUN': 0, 'MERCURY':1, 'VENUS': 2, 'EARTH': 3, 'MARS': 4, 'JUPITER': 5, 'SATURN': 6,	'URANUS': 7, 'NEPTUNE': 8, 'PLUTO': 9}
mass = [m*1e24 for m in [1.98847e6, 0.330, 4.87, 5.97, 0.642,	1898, 568, 86.8, 102, 0.0146]]
dist = [d*1e9 for d in [0., 57.9, 108.2, 149.6, 227.9,	778.6,	1433.5,	2872.5,	4495.1,	5906.4]]
orbital_vel = [v*1e3 for v in [0., 47.4, 35.0, 29.8, 24.1, 13.1, 9.7, 6.8, 5.4, 4.7]]
diam = [1.3927e6, 4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]
min_diam = min(diam)
rel_sz = [math.floor(math.log(sz / min_diam))*3 + 1 for sz in diam]
#print(rel_sz)
G=6.67408e-11 
dt = 24*3600

pos = np.zeros([n, 2])
vel = np.zeros([n, 2])
net_p = 0
for i in range(n):
    theta_r = random.uniform(0, math.pi*2)
    pos[i,:] = np.array([dist[i]*math.cos(theta_r), dist[i]*math.sin(theta_r)])
    if i > 1:
        v_mag = orbital_vel[i]
        theta_v = math.pi/2 + theta_r
        vel[i,:] = np.array([v_mag*math.cos(theta_v), v_mag*math.sin(theta_v)])
        net_p += mass[i]*vel[i]
vel[0,:] = -net_p/mass[0]
vel = np.array(vel)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
lim_D = max(dist)*1.1
ax.set_xlim(-lim_D, lim_D)
ax.set_ylim(-lim_D, lim_D)
ax.set_xlabel('x-coordinate (m)',fontsize=10)
ax.set_ylabel('y-coordinate (m)',fontsize=10)

planet_plot = ax.scatter(pos[1:,0], pos[1:, 1],  s=rel_sz[1:])
star_plot = ax.scatter(*pos[0], s=rel_sz[0])

def animate(frame):
    for t in range(100):
        for i in range(n):
            net_acc = [0., 0.]
            for j in range(n):
                if j != i: 
                    Rij = pos[i] - pos[j]
                    net_acc += -G*mass[j]*Rij*((Rij[0]**2 + Rij[1]**2)**-1.5)

            vel[i] += net_acc*dt 
            pos[i] += vel[i]*dt

    total_days = 100*frame
    ax.set_title("%d years, %d days" % (total_days//365, total_days%365))
    
    planet_plot.set_offsets(pos[1:])
    star_plot.set_offsets(pos[0])
    return planet_plot, star_plot

anim = FuncAnimation(fig, animate, frames=None, interval=30, repeat=False)
plt.show()
#anim.save('solar_system.gif', fps=30)