from simulation import Simulation

class RKSimulation(Simulation):
    def rk4(self):
        h = self.parameters.step_size
        x = 0
        v = 0
        t = 0
        max = 0
        for i in range(int(self.number_of_steps)):
            K1x = self.f1(t, x, v)
            K1v = self.f2(t, x, v)
            K2x = self.f1(t + h/2, x + h*K1x/2, v + h*K1v/2)
            K2v = self.f2(t + h/2, x + h*K1x/2, v + h*K1v/2)
            K3x = self.f1(t + h/2, x + h*K2x/2, v + h*K2v/2)
            K3v = self.f2(t + h/2, x + h*K2x/2, v + h*K2v/2)
            K4x = self.f1(t + h, x + h*K3x, v + h*K3v) 
            K4v = self.f2(t + h, x + h*K3x, v + h*K3v)
            x = x + h/6*(K1x + 2*K2x + 2*K3x + K4x)
            v = v + h/6*(K1v + 2*K2v + 2*K3v + K4v)
            t = t + h
            #if x > max:
            #    max = x
            self.theta.append(x)
            self.rot_speed.append(v)
            self.time.append(t)
        #print(max)
        return self.theta, self.rot_speed, self.time
    