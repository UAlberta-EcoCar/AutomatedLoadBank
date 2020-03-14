
import tkinter as tk
import time
from random import randint



class A:
    def __init__(self, master):
        
        self.V_label=tk.Label(master)
        self.V_label.place(x=250,y=50,width=300,height=50)
        self.V_label.configure(font=("Arial",16))
        self.V_label.pack_propagate(False)
        
        self.I_label=tk.Label(master)
        self.I_label.place(x=250,y=100,width=300,height=50)
        self.I_label.configure(font=("Arial",16))
        self.V_label.pack_propagate(False)
        
        self.T_label=tk.Label(master)
        self.T_label.place(x=250,y=150,width=300,height=50)
        self.T_label.configure(font=("Arial",16))
        self.T_label.pack_propagate(False)
        
        self.Time_label=tk.Label(master)
        self.Time_label.place(x=250,y=200,width=300,height=50)
        self.Time_label.configure(font=("Arial",16))
        self.Time_label.pack_propagate(False)
        
        self.V = 0
        self.T = 0
        self.I = 0
        self.curr_time_sec = 0
        self.curr_time_min = 0
        self.start_time = time.time()
      
        self.update_labels()

    def update_labels(self):
        
        self.V = randint(0,120)
        self.I = randint(0,60)
        self.T = randint(35,75)
        self.curr_time_sec = time.time() - self.start_time
        
        if self.curr_time_sec <60 and self.curr_time_sec > 58.5:
            self.curr_time_sec = 0
            self.curr_time_min += 1
            self.start_time = time.time()
        
        if self.curr_time_min < 10:
            if self.curr_time_sec <10:
                self.Time_label.configure(text = "Elapsed Time: %d%d:%d%d" %(0,self.curr_time_min,0,self.curr_time_sec))
            else:
                self.Time_label.configure(text = "Elapsed Time: %d%d:%d" %(0,self.curr_time_min,self.curr_time_sec))
        else: 
            if self.curr_time_sec <10:
                self.Time_label.configure(text = "Elapsed Time: %d:%d%d" %(self.curr_time_min,0,self.curr_time_sec))
            else:
                self.Time_label.configure(text = "Elapsed Time: %d:%d" %(self.curr_time_min,self.curr_time_sec))
                
        
        
        self.V_label.configure(text = "Voltage: %3d V" %(self.V))
        self.I_label.configure(text = "Current: %3d A" %(self.I))
        self.T_label.configure(text = "Temperature: %3d C" %(self.T))
        #self.Time_label.configure(text = "Elapsed Time: %d:%d" %(self.curr_time_min,self.curr_time_sec))
        self.V_label.after(1000, self.update_labels) 
        
root = tk.Tk()
A(root)
root.resizable(False, False)
root.geometry("800x480")
root.mainloop()
