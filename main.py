from gui import GUI
from rk_simulation import RKSimulation
from eu_simulation import Eu_simulation

gui = GUI()
parameters = gui.get_parameters()

rk_simulation = RKSimulation(parameters)
eu_simulation = Eu_simulation(parameters)
theta_eu, rot_speed_eu, time = eu_simulation.eu()
theta_rk, rot_speed_rk, time = rk_simulation.rk4()

gui.show_plots(theta_rk, rot_speed_rk, theta_eu, rot_speed_eu, time)

