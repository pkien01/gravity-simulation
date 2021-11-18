import numpy as np
import matplotlib.pyplot as plt
import math
import random

years = 1.
tdur = years*365.*24*3600. # duration of the motion, in seconds
nstep = int(1000*years) # number of steps to calculate

dt = tdur/nstep # duration of a single step.
print(dt)

#Some constants
G = 6.67408e-11
au = 1.496e11 #dist of 1AU in m
M = 1.98847e30 #mass of sun
m = 5.97219e24 #mass of earth
d0 = au #dist from Earth to Sun

theta_r = random.uniform(0, math.pi*2)


# initialize the planet initial position, velocity, and acceleration
planet_aa = np.array([0.,0.]) 
planet_x0 = np.array([d0*math.cos(theta_r),d0*math.sin(theta_r)])
theta_v = math.pi/2 + theta_r 
#theta_v = random.uniform(0, math.pi*2)
planet_v0_mag = math.sqrt(G*M/d0)
planet_v0 = np.array([planet_v0_mag*math.cos(theta_v),planet_v0_mag*math.sin(theta_v)])
#save the position in an array so we can plot it later
planet_pos = np.zeros([nstep+1, 2]) 
planet_pos[0,:] = planet_x0

# initialize the star initial position, velocity, and acceleration
star_x0 = np.array([0.,0.])
star_v0 = -planet_v0*m/M 
star_aa =  np.array([0.,0.])
# save the position in an array so we can plot it later
star_pos = np.zeros([nstep+1, 2])
star_pos[0,:] = star_x0

# the current planet velocity and position
planet_vv = planet_v0 
planet_xx = planet_x0

star_vv = star_v0
star_xx = star_x0


for kk in range(1,nstep+1):
    diff = planet_xx - star_xx
    dist = math.hypot(diff[0], diff[1])

    planet_aa = -G*M*diff/(dist**3)
    star_aa = G*m*diff/(dist**3)

    planet_vv += planet_aa*dt
    star_vv += star_aa*dt
    
    planet_xx += planet_vv*dt
    star_xx += star_vv*dt

    planet_pos[kk,:] = planet_xx
    star_pos[kk,:] = star_xx

    #print(planet_vv, star_vv)
    
#print(pos)
#plot the trajectory in x-y plane
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
#ax.axis('scaled')
ax.plot(planet_pos[:,0],planet_pos[:,1],'b.')
ax.plot(star_pos[:,0],star_pos[:,1],'r.')


plt.xlabel('x-coordinate (m)',fontsize=15)
plt.ylabel('y-coordinate (m)',fontsize=15)

plt.grid()
plt.savefig('Ph1401_example_python.png')
plt.savefig('Ph1401_example_python.pdf')

plt.show()
