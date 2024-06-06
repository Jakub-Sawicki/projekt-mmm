from simulation import Simulation

class Eu_simulation(Simulation):
    def eu(self):
        h = self.parameters.step_size
        t = 0
        x = 0

        max = 0
        for i in range(int(self.number_of_steps)):
            self.theta.append(self.theta[i] + h*self.rot_speed[i])
            self.rot_speed.append(self.rot_speed[i] + h*(self.f2(t, self.theta[i], self.rot_speed[i])))

            t = t + h
            #if self.theta[i] > max:
            #    max = self.theta[i]
            self.time.append(t)
        
        #print(max)
        return self.theta, self.rot_speed, self.time