# gravity-simulation

This project is a simulation of the solar system I created.

## Formulas
For a closed n-bodies system, the net gravitational force exert on object *i* is
<br/><br/>
<img src="formulas/force.gif">
<br/>
where ![](formulas/m_i.gif) and ![](formulas/m_j.gif) are the masses of object *i* and *j*, <img src="formulas/G.gif"> is the gravity constant, <img src="formulas/r.gif"> is the relative position vector between object *i* and object *j*
<br/>
And hence, object *i* accelerates at 
<br/><br/>
<img src="formulas/acc.gif"> 
<br/><br/>
Once we have the acceleration, we can approximate the velocity and hence, position of that object *i* at each time step *t* with the time duration <img src="formulas/dt.gif"> 
between every iteration
<br/><br/> 
<img src="formulas/vel.gif">
<br>
<img src="formulas/pos.gif">
<br/><br/>
## More details 

I initialize the position and velocity as follows:
<br/><br/>
<img src="formulas/x0.gif">
<br/>
<img src="formulas/v0.gif">
<br/>
where <img src="formulas/D.gif"> and <img src="formulas/vi_orb.gif"> are the distance from the Sun's center and the orbital velocity of the planets obtained from [NASA planetary fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/). I chose <img src="formulas/theta.gif"> randomly in the range <img src="formulas/02pi.gif">. The initial acceleration doesn't matter because I recompute it at every timestep in the for loop. 
<br/><br/>
The orbital velocity of the sun is 
<br/>
<img src="formulas/vorb_sun.gif"> 
<br/>so that the total momentum of the system is zero and the reference frame is the center of mass's.
<br/><br/>
Note that during visualization, I plotted the sun and planets as markers with size propotional to the log of their relative diameters (as the their relatives diameters are very disproportionate to each other):
<br/>
<img src="formulas/s.gif">
<br/>

## Installation & Run

- If you haven't already, you should install ```matplotlib``` with the command
```pip install matplotlib```
Or if you are using Anaconda, then it is 
```conda install -c conda-forge matplotlib```

- Open terminal/git bash and clone the repository:
```git clone https://github.com/pkien01/gravity-simulation```
- Finally, run the script: ```python3 solar_system_simulator.py```

## Demo
Here is the result:
<br/>
<img src="https://github.com/pkien01/gravity-simulation/blob/master/solar_system.gif">
<br/><br/><br/>
I hope you enjoy it!

