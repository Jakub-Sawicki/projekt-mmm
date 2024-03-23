from simulation_parameters import SimulationParameters

class GUI:
    def __init__(self):
        pass

    def input_function(self, t):
        unit_step = lambda t: 1 if t >= 0 else 0

    def get_parameters(self):
        return SimulationParameters(step_size, simulation_duration, input_function, k, b, n1, n2, J1, J2)
