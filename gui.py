from simulation_parameters import SimulationParameters
from rk_simulation import RKSimulation
from eu_simulation import Eu_simulation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self):
        # initializing deafult parameter values
        self.step_size = 0.01
        self.simulation_duration = 200
        self.k = 1
        self.b = 10
        self.n1 = 5
        self.n2 = 15
        self.J1 = 10
        self.J2 = 15
        self.signal_type = "square"
        
        self.signal_duration = 1
        self.signal_amplitude = 1
        self.signal_period = 1
        self.signal_frequency = 1/self.signal_period

        self.error_code = -10000000

    def square_funciton(self, t):
        if (t >= 0 and t <= self.signal_duration):
            return self.signal_amplitude 
        else:
            return 0

    def triangle_function(self, t):
        # Calculate the angular frequency 
        omega = 2 * np.pi * self.signal_frequency

        # Calculate the phase shift (normalized by period)
        phase_shift = t / self.signal_period

        # Define the triangular wave function using absolute values
        y = abs(2 * self.signal_amplitude * (phase_shift % 1) - self.signal_amplitude)

        return y

    def harmonic_function(self, t):
        return self.signal_amplitude*np.sin(2*np.pi*self.signal_frequency*t)

    def get_parameters(self):
        if (self.signal_type == "square"):
            return SimulationParameters(self.step_size, self.simulation_duration, self.square_funciton, self.k, self.b, self.n1, self.n2, self.J1, self.J2)
        elif (self.signal_type == "triangle"):
            return SimulationParameters(self.step_size, self.simulation_duration, self.triangle_function, self.k, self.b, self.n1, self.n2, self.J1, self.J2)
        elif (self.signal_type == "harmonic"):
            return SimulationParameters(self.step_size, self.simulation_duration, self.harmonic_function, self.k, self.b, self.n1, self.n2, self.J1, self.J2)

    def show_plots(self, theta_rk, rot_speed_rk, theta_eu, rot_speed_eu, time):
        fig, axes = plt.subplots(1, 4, figsize=(15, 4))  # 2 row, 2 columns

        # theta plot rk
        axes[0].plot(time, theta_rk, linestyle='-')
        axes[0].set_title("Theta Plot for Runge–Kutta method")
        axes[0].set_xlabel("Time")
        axes[0].set_ylabel("Theta")

        # rotational speed plot rk
        axes[1].plot(time, rot_speed_rk, linestyle='-')
        axes[1].set_title("Rotational Speed Plot for Runge–Kutta method")
        axes[1].set_xlabel("Time")
        axes[1].set_ylabel("Rotational Speed")

         # theta plot eu
        axes[2].plot(time, theta_eu, linestyle='-')
        axes[2].set_title("Theta Plot for Euler method")
        axes[2].set_xlabel("Time")
        axes[2].set_ylabel("Theta")

        # rotational speed plot eu
        axes[3].plot(time, rot_speed_eu, linestyle='-')
        axes[3].set_title("Rotational Speed Plot for Euler method")
        axes[3].set_xlabel("Time")
        axes[3].set_ylabel("Rotational Speed")
        
        plt.tight_layout()
        #plt.show()
        
        return fig
        
    def show_gui(self):
        def plot_display():
            rk_simulation = RKSimulation(self.get_parameters())
            eu_simulation = Eu_simulation(self.get_parameters())

            theta_eu, rot_speed_eu, time = eu_simulation.eu()
            theta_rk, rot_speed_rk, time = rk_simulation.rk4()

            canvas = FigureCanvasTkAgg(self.show_plots(theta_rk, rot_speed_rk, theta_eu, rot_speed_eu, time), master=root)
            canvas.draw()
            canvas.get_tk_widget().grid(column=1, row=22, columnspan=4, sticky=SW)

        def clicked():
            for widget in root.winfo_children():
                if isinstance(widget, Label) and widget.cget("text") != "Write down parameters you want to update" and widget.cget("text") != "k: " and widget.cget("text") != "b: " and widget.cget("text") != "step size: " and widget.cget("text") != "simulation duration: " and widget.cget("text") != "n1: " and widget.cget("text") != "n2: "  and widget.cget("text") != "J1: " and widget.cget("text") != "J2: " and widget.cget("text") != "Input signal: " and widget.cget("text") != "Signal duration (square function): " and widget.cget("text") != "Signal period: " and widget.cget("text") != "Signal amplitude: ":
                    widget.destroy()
            errors = []
            if self.number(step_size_new.get()) != self.error_code:
                self.step_size = self.number(step_size_new.get())
            else:
                errors.append("step_size")

            if self.number(simulation_duration_new.get()) != self.error_code:
                self.simulation_duration = self.number(simulation_duration_new.get())
            else:
                errors.append("simulation_duration")

            if self.number(k_new.get()) != self.error_code:
                self.k = self.number(k_new.get())
            else:
                errors.append("k")

            if self.number(b_new.get()) != self.error_code:
                self.b = self.number(b_new.get())
            else:
                errors.append("b")

            if self.number(n1_new.get()) != self.error_code:
                self.n1 = self.number(n1_new.get())
            else:
                errors.append("n1")

            if self.number(n2_new.get()) != self.error_code:
                self.n2 = self.number(n2_new.get())
            else:
                errors.append("n2")

            if self.number(J1_new.get()) != self.error_code:
                self.J1 = self.number(J1_new.get())
            else:
                errors.append("J1")

            if self.number(J2_new.get()) != self.error_code:
                self.J2 = self.number(J2_new.get())
            else:
                errors.append("J2")

            if self.number(duration_new.get()) != self.error_code:
                self.signal_duration = self.number(duration_new.get())
            else:
                errors.append("signal_duration")

            if self.number(period_new.get()) != self.error_code and self.number(period_new.get()) > 0:
                self.signal_period = self.number(period_new.get())
                self.signal_frequency = 1/self.signal_period
            else:
                errors.append("signal_period")

            if self.number(amplitude_new.get()) != self.error_code:
                self.signal_amplitude = self.number(amplitude_new.get())
            else:
                errors.append("signal_amplitude")

            if(signal_new.get() == "Square function"):
                self.signal_type = "square"
            elif(signal_new.get() == "Triangle function"):
                self.signal_type = "triangle"
            elif(signal_new.get() == "Harmonic function"):
                self.signal_type = "harmonic"
            else:
                errors.append("signal_type")
                
            
            error_lbl1 = Label(root)
            error_lbl2 = Label(root)
            error_lbl1.grid(column=2, row=9, sticky=NW)
            error_lbl2.grid(column=2, row=10, sticky=NW)
            if len(errors) != 0:
                error_msg1 = errors
                error_msg2 = "have not been a number and were not updated, other parameters have been updated successfully"
                error_lbl1.configure(text = error_msg1)
                error_lbl2.configure(text = error_msg2)
            else:
                error_lbl1.configure(text = "All parameters has been updated properly")
                error_lbl2.configure(text = "")
            errors.clear()

        root = Tk()

        root.title("MMM")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (screen_width, screen_height, 0, 0))

        intro = Label(root, text = "Write down parameters you want to update")
        intro.grid(column=1, row=0, sticky=NW)

        step_size_lbl = Label(root, text = "step size: ")
        step_size_lbl.grid(column=1, row=1, sticky=NW)
        step_size_new = Entry(root, width=30)
        step_size_new.grid(column=1, row=2, sticky=NW)

        simulation_duration_lbl = Label(root, text = "simulation duration: ")
        simulation_duration_lbl.grid(column=1, row=3, sticky=NW)
        simulation_duration_new = Entry(root, width=30)
        simulation_duration_new.grid(column=1, row=4, sticky=NW)

        k_lbl = Label(root, text = "k: ")
        k_lbl.grid(column=1, row=5, sticky=NW)
        k_new = Entry(root, width=30)
        k_new.grid(column=1, row=6, sticky=NW)
        
        b_lbl = Label(root, text = "b: ")
        b_lbl.grid(column=1, row=7, sticky=NW)
        b_new = Entry(root, width=30)
        b_new.grid(column=1, row=8, sticky=NW)

        n1_lbl = Label(root, text = "n1: ")
        n1_lbl.grid(column=1, row=9, sticky=NW)
        n1_new = Entry(root, width=30)
        n1_new.grid(column=1, row=10, sticky=NW)

        n2_lbl = Label(root, text = "n2: ")
        n2_lbl.grid(column=1, row=11, sticky=NW)
        n2_new = Entry(root, width=30)
        n2_new.grid(column=1, row=12, sticky=NW)

        J1_lbl = Label(root, text = "J1: ")
        J1_lbl.grid(column=1, row=13, sticky=NW)
        J1_new = Entry(root, width=30)
        J1_new.grid(column=1, row=14, sticky=NW)

        J2_lbl = Label(root, text = "J2: ")
        J2_lbl.grid(column=1, row=15, sticky=NW)
        J2_new = Entry(root, width=30)
        J2_new.grid(column=1, row=16, sticky=NW)


        signal_lbl = Label(root, text = "Input signal: ")
        signal_lbl.grid(column=2, row=1, sticky=NW)
        signal_new = ttk.Combobox(root, values = ["Square function", "Triangle function", "Harmonic function"])
        signal_new.grid(column=2, row=2, sticky=NW)
        signal_new.set("Square function")

        duration_lbl = Label(root, text = "Signal duration (square function): ")
        duration_lbl.grid(column=2, row=3, sticky=NW)
        duration_new = Entry(root, width=30)
        duration_new.grid(column=2, row=4, sticky=NW)

        period_lbl = Label(root, text = "Signal period: ")
        period_lbl.grid(column=2, row=5, sticky=NW)
        period_new = Entry(root, width=30)
        period_new.grid(column=2, row=6, sticky=NW)

        amplitude_lbl = Label(root, text = "Signal amplitude: ")
        amplitude_lbl.grid(column=2, row=7, sticky=NW)
        amplitude_new = Entry(root, width=30)
        amplitude_new.grid(column=2, row=8, sticky=NW)
        

        btn = Button(root, text = "Update parameters", command=clicked)
        btn.grid(column=2, row=11, sticky=NW)

        btn2 = Button(root, text = "Show plots", command=plot_display)
        btn2.grid(column=2, row=12, sticky=NW)

        btn3 = Button(root, text = "Quit", command = exit)
        btn3.grid(column=2, row=13, sticky=NW)

        root.mainloop()

    def number(self, check):
        try:
            value = float(check)
            return value
        except ValueError:
            return self.error_code
        
