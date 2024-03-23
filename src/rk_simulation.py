class RKSimulation:
    def __init__(self, parameters):
        self.parameters = parameters
        self.theta = []
        self.rot_speed = []

    def rk4(self):
        self.theta[0] = 0
        self.rot_speed[0] = 0

        def f1(t, x, v):
            return v
        
        def f2(t, x, v):
            a1 = self.parameters.input_function(t)/(self.parameters.J1*self.parameters.n2/self.parameters.n1 + self.parameters.J2)
            a2 = self.parameters.k/(self.parameters.J1+self.parameters.J2*self.parameters.n1/self.parameters.n2)
            a3 = self.parameters.b/(self.parameters.J*self.parameters.n2/self.parameters.n1 + self.parameters.J2)

            return a1 - a2*x - a3*v



    

    
    


    

    