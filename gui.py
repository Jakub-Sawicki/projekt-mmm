from simulation_parameters import SimulationParameters

import math
import matplotlib.pyplot as plt
import numpy as np

class GUI:
    def __init__(self):
        self.step_size = 0.1
        self.simulation_duration = 200
        self.k = 1
        self.b = 10
        self.n1 = 5
        self.n2 = 15
        self.J1 = 10
        self.J2 = 15

    def input_function(self, t):
        #return 1 if t >= 0 else 0
        #return 100000 if t == 0 else 0
        #return math.sin(2*3.14*t)
        #return 0
        return 1 if t >= 0 and t <= 10 else 0

    def get_parameters(self):
        return SimulationParameters(self.step_size, self.simulation_duration, self.input_function, self.k, self.b, self.n1, self.n2, self.J1, self.J2)

    def show_plots(self, theta, rot_speed, time):
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns

        # theta plot
        axes[0].plot(time, theta, linestyle='-')
        axes[0].set_title("Theta Plot")
        axes[0].set_xlabel("Time")
        axes[0].set_ylabel("Theta")

        # rotational speed plot
        axes[1].plot(time, rot_speed, linestyle='-')
        axes[1].set_title("Rotational Speed Plot")
        axes[1].set_xlabel("Time")
        axes[1].set_ylabel("Rotational Speed")

        plt.tight_layout()
        plt.show()
