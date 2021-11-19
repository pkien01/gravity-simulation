# gravity-simulation

This project is a simulation of the solar system I created.

## Formulas
For a closed n-body system, the net force exert on object *i* is
<br/><br/>
<img src="https://github.com/pkien01/gravity-simulation/blob/master/formulas/force.gif">
<br/><br/>
And hence, object *i* accelerates at 
<br/><br/>
<img src="https://github.com/pkien01/gravity-simulation/blob/master/formulas/acc.gif">
<br/><br/>
Once we have the acceleration, we can approximate the velocity and hence, position of that object *i* at each time step *t*
<br/><br/>
<img src="https://github.com/pkien01/gravity-simulation/blob/master/formulas/vel.gif">
<br>
<img src="https://github.com/pkien01/gravity-simulation/blob/master/formulas/pos.gif">
<br/><br/>

## Installation & Run

- If you haven't already, you should install ```matplotlib``` with the command
```pip install matplotlib```
Or if you are using Anaconda, then it is 
```conda install -c conda-forge matplotlib```

- Open terminal/git bash and clone the repository:
```git clone https://github.com/pkien01/gravity-simulation```
- Finally, run the script: ```python3 solar_system_simulator.py```

# Demo
Here is the result:
<br/>
<img src="https://github.com/pkien01/gravity-simulation/blob/master/solar_system.gif">
<br/><br/>

I hope you enjoy it!

