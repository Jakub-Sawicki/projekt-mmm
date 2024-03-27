class SimulationParameters:
    def __init__(self, step_size, simulation_duration, input_function, k, b, n1, n2, J1, J2):
        self.step_size = step_size
        self.simulation_duration = simulation_duration

        self.input_function = input_function

        self.k = k
        self.b = b
        self.n1 = n1
        self.n2 = n2
        self.J1 = J1
        self.J2 = J2
