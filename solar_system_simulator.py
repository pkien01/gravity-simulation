import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import random

n = 10
name_id = {'Sun': 0, 'Mercury':1, 'Venus': 2, 'Earth': 3, 'Mars': 4, 'Jupiter': 5, 'Saturn': 6,	'Uranus': 7, 'Neptune': 8, 'Pluto': 9}
mass = [m*1e24 for m in [1.98847e6, 0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102, 0.0146]]
aphelion = [d*1e9 for d in [0., 69.8, 108.9, 152.1, 249.2, 816.6, 1514.5, 3003.6, 4545.7, 7375.9]]
diam = [1.3927e6, 4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]
orbit_vel = [v0*1000. for v0 in [0., 38.86, 34.79, 29.29, 21.97, 12.44, 9.09, 6.49, 5.37, 3.71]]
eccentricity = [0., 0.205, 0.007, 0.017, 0.094, 0.049, 0.057, 0.046, 0.011, 0.244]
min_diam = min(diam)
rel_sz = [math.floor(math.log(sz / min_diam))*3 + 1 for sz in diam]
#print(rel_sz)
G=6.67408e-11 
dt = 24*3600

pos = np.zeros([n, 2])
vel = np.zeros([n, 2])
net_p = 0
net_cm = 0
for i in range(1, n):
    theta_r = random.uniform(0, math.pi*2)
    dist = aphelion[i]
    pos[i,:] = np.array([dist*math.cos(theta_r), dist*math.sin(theta_r)])
    net_cm += mass[i]*pos[i]

    v_mag = orbit_vel[i]
    #v_mag = math.sqrt(G*mass[0]/dist[i])
    theta_v = math.pi/2 + theta_r
    vel[i,:] = np.array([v_mag*math.cos(theta_v), v_mag*math.sin(theta_v)])
    net_p += mass[i]*vel[i]

pos[0,:] = -net_cm/mass[0]
vel[0,:] = -net_p/mass[0]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
lim_D = max(aphelion)*1.1
ax.set_xlim(-lim_D, lim_D)
ax.set_ylim(-lim_D, lim_D)
ax.set_aspect('equal', 'box')
ax.set_xlabel('x (m)',fontsize=10)
ax.set_ylabel('y (m)',fontsize=10)

obj_plot = ax.scatter(pos[:,0], pos[:, 1],  s=rel_sz)

sweep_angle = np.zeros([n,])
orbit = [[pos[i].copy(),] for i in range(n)]
orbit_plot = [None]*n
for i in range(n): 
    cur_orbit = np.array(orbit[i])
    orbit_plot[i], = ax.plot(cur_orbit[:,0], cur_orbit[:,1], linewidth=1.)


ax.legend(orbit_plot, name_id.keys())
def animate(frame, display_freq=80):
    orbit_displayed = False
    for t in range(display_freq):
        for i in range(n):
            net_acc = [0., 0.]
            for j in range(n):
                if j != i: 
                    r_vec = pos[i] - pos[j]
                    net_acc += -G*mass[j]*r_vec*((r_vec[0]**2 + r_vec[1]**2)**-1.5)

            vel[i] += net_acc*dt 
            pos[i] += vel[i]*dt
	
            omega = math.hypot(*vel[i])/math.hypot(*pos[i])
            sweep_angle[i] += omega*dt
            orbit[i].append(pos[i].copy())
            if sweep_angle[i] > 2.*math.pi*3:
                orbit[i].pop(0)
         
           
    for i in range(n): 
        #orbit[i].append(pos[i].copy())
        #if sweep_angle[i] > 2.*math.pi:
        #    orbit[i].pop(0)
        cur_orbit = np.array(orbit[i])
        orbit_plot[i].set_data(cur_orbit[:, 0], cur_orbit[:, 1])
    

    total_days = display_freq*frame
    ax.set_title("%d years, %d days" % (total_days//365, total_days%365))
    
    obj_plot.set_offsets(pos)
    return obj_plot

if __name__ == "__main__":
    anim = FuncAnimation(fig, animate, frames=None, interval=30, repeat=False)
    plt.show()
    anim.save('solar_system.gif', fps=30)
