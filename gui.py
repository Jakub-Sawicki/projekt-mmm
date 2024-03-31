from simulation_parameters import SimulationParameters

import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
from rk_simulation import RKSimulation
from eu_simulation import Eu_simulation
#import PySimpleGUI as sg
#import numpy as np

class GUI:
    def __init__(self):
        self.step_size = 0.01
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

    def show_plots(self, theta_rk, rot_speed_rk, theta_eu, rot_speed_eu, time):
        fig, axes = plt.subplots(1, 4, figsize=(24, 6))  # 2 row, 2 columns

        # theta plot
        axes[0].plot(time, theta_rk, linestyle='-')
        axes[0].set_title("Theta Plot for RK method")
        axes[0].set_xlabel("Time")
        axes[0].set_ylabel("Theta")

        # rotational speed plot
        axes[1].plot(time, rot_speed_rk, linestyle='-')
        axes[1].set_title("Rotational Speed Plot for RK method")
        axes[1].set_xlabel("Time")
        axes[1].set_ylabel("Rotational Speed")

         # theta plot
        axes[2].plot(time, theta_eu, linestyle='-')
        axes[2].set_title("Theta Plot for Eu method")
        axes[2].set_xlabel("Time")
        axes[2].set_ylabel("Theta")

        # rotational speed plot
        axes[3].plot(time, rot_speed_eu, linestyle='-')
        axes[3].set_title("Rotational Speed Plot for Eu method")
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
                canvas.get_tk_widget().pack()
            
            def clicked():
                for widget in root.winfo_children():
                    if isinstance(widget, Label) and widget.cget("text") != "Write down parameters you want to update" and widget.cget("text") != "k: " and widget.cget("text") != "b: " and widget.cget("text") != "step size: " and widget.cget("text") != "simulation duration: " and widget.cget("text") != "n1: " and widget.cget("text") != "n2: "  and widget.cget("text") != "J1: " and widget.cget("text") != "J2: ":
                        widget.destroy()
                errors = []
                if self.number(step_size_new.get()) != -10000000:
                    self.step_size = self.number(step_size_new.get())
                else:
                    errors.append("step size")

                if self.number(simulation_duration_new.get()) != -10000000:
                    self.simulation_duration = self.number(simulation_duration_new.get())
                else:
                    errors.append("simulation_duration")

                if self.number(k_new.get()) != -10000000:
                    self.k = self.number(k_new.get())
                else:
                    errors.append("k")

                if self.number(b_new.get()) != -10000000:
                    self.b = self.number(b_new.get())
                else:
                    errors.append("b")

                if self.number(n1_new.get()) != -10000000:
                    self.n1 = self.number(n1_new.get())
                else:
                    errors.append("n1")

                if self.number(n2_new.get()) != -10000000:
                    self.n2 = self.number(n2_new.get())
                else:
                    errors.append("n2")

                if self.number(J1_new.get()) != -10000000:
                    self.J1 = self.number(J1_new.get())
                else:
                    errors.append("J1")

                if self.number(J2_new.get()) != -10000000:
                    self.J2 = self.number(J2_new.get())
                else:
                    errors.append("J2")
                error_lbl1 = Label(root)
                error_lbl2 = Label(root)

                error_lbl1.pack()
                error_lbl2.pack()
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
            intro.pack()

            step_size_lbl = Label(root, text = "step size: ")
            step_size_lbl.pack()
            step_size_new = Entry(root, width=30)
            step_size_new.pack()

            simulation_duration_lbl = Label(root, text = "simulation duration: ")
            simulation_duration_lbl.pack()
            simulation_duration_new = Entry(root, width=30)
            simulation_duration_new.pack()

            k_lbl = Label(root, text = "k: ")
            k_lbl.pack()
            k_new = Entry(root, width=30)
            k_new.pack()
            
            b_lbl = Label(root, text = "b: ")
            b_lbl.pack()
            b_new = Entry(root, width=30)
            b_new.pack()

            n1_lbl = Label(root, text = "n1: ")
            n1_lbl.pack()
            n1_new = Entry(root, width=30)
            n1_new.pack()

            n2_lbl = Label(root, text = "n2: ")
            n2_lbl.pack()
            n2_new = Entry(root, width=30)
            n2_new.pack()

            J1_lbl = Label(root, text = "J1: ")
            J1_lbl.pack()
            J1_new = Entry(root, width=30)
            J1_new.pack()

            J2_lbl = Label(root, text = "J2: ")
            J2_lbl.pack()
            J2_new = Entry(root, width=30)
            J2_new.pack()

            

            btn = Button(root, text = "Update parameters", command=clicked)
            btn.pack()

            btn2 = Button(root, text = "Show plots", command=plot_display)
            btn2.pack()

            root.mainloop()

    def number(self, check):
        try:
            value = float(check)
            return value
        except ValueError:
            return -10000000
        
