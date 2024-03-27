from gui import GUI
from rk_simulation import RKSimulation

gui = GUI()
parameters = gui.get_parameters()

rk_simulation = RKSimulation(parameters)
theta, rot_speed, time = rk_simulation.rk4()

gui.show_plots(theta, rot_speed, time)

