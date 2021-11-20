import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import random

G=6.67408e-11 
class GravitySimulator:
    G=6.67408e-11 
    def __init__(num_planets, star_mass, planet_masses, planet_dists, rel_sizes, dt=24*3600, theta=None, orbital_vel=None):
        net_p = 0
        if theta is None: 
            theta = [random.uniform(0, math.pi*2) for i in range(num_planets)]
        
        # include both star and planets
        self.pos = np.zeros([num_planets + 1, 2])
        self.vel = np.zeros([num_planets + 1, 2])
        net_p = 0
        for i in range(num_planets + 1):
            if i == 0: 
                pos[i,:] = np.array([0., 0.])
            else: 
                pos[i,:] = np.array([dist[i]*math.cos(theta[i]), dist[i]*math.sin(theta[i])]) 
                v_mag = orbital_vel[i]
                theta_v = math.pi/2 + theta[i]
                vel[i,:] = np.array([v_mag*math.cos(theta_v), v_mag*math.sin(theta_v)])
                net_p += mass[i]*vel[i]
                vel[0,:] = -net_p/star_mass
                vel = np.array(vel)

            vel[i] = -net_p/star_mass
            vel = np.array(vel)
        
        self.fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1)
        lim_D = max(dist)*1.1
        self.ax.set_xlim(-lim_D, lim_D)
        self.ax.set_ylim(-lim_D, lim_D)
        self.ax.set_xlabel('x-coordinate (m)',fontsize=10)
        self.ax.set_ylabel('y-coordinate (m)',fontsize=10)

        planet_plot = ax.scatter(pos[1:,0], pos[1:, 1],  s=rel_sz[1:])
        star_plot = ax.scatter(*pos[0], s=rel_sz[0])

    def update(frame):
        for t in range(100):
            for i in range(n):
                net_acc = [0., 0.]
                for j in range(n):
                    if j != i: 
                        Rij = self.pos[i] - self.pos[j]
                        net_acc += -G*mass[j]*Rij*((Rij[0]**2 + Rij[1]**2)**-1.5)

                vel[i] += net_acc*dt 
                pos[i] += vel[i]*dt

        total_days = 100*frame
        ax.set_title("%d years, %d days" % (total_days//365, total_days%365))
    
        planet_plot.set_offsets(pos[1:])
        star_plot.set_offsets(pos[0])
        return planet_plot, star_plot