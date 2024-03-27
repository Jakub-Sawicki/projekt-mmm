class Simulation:
    def __init__(self, parameters):
        self.parameters = parameters
        self.theta = []
        self.rot_speed = []
        self.time = []

        self.theta.append(0)
        self.rot_speed.append(0)
        self.time.append(0)
        self.number_of_steps = self.parameters.simulation_duration / self.parameters.step_size
    
    def f1(self, t, x, v):
        return v
    
    def f2(self, t, x, v):
        u = self.parameters.input_function(t)
        
        a1 = u/(self.parameters.J1*self.parameters.n2/self.parameters.n1 + self.parameters.J2)
        a2 = self.parameters.k/(self.parameters.J1+self.parameters.J2*self.parameters.n1/self.parameters.n2)
        a3 = self.parameters.b/(self.parameters.J1*self.parameters.n2/self.parameters.n1 + self.parameters.J2)

        return a1 - a2*x - a3*v
