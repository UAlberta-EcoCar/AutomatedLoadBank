
import tkinter as tk
from PIL import ImageTk, Image
import math
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# 
#
#
#
#
#
#
#
#
#
#
#
#


style.use('ggplot')
#from scrolledtext import scrolledtext

#variable used for example down below
#testvalueimportant = 5

# Function to draw disclaimer

def view_disclaimer():
    disclaimer_frame = tk.Frame(root, height=380, width=600)
    disclaimer_frame.pack_propagate(False)
    disclaimer_frame.place(x=80, y=50)

    disclaimer_label = tk.Label(disclaimer_frame, text='WARNING')
    disclaimer_label.config(font=("Arial", 24), bg='red')
    disclaimer_label.pack(fill="both")

    #disclaimer_scrollbar = tk.Scrollbar(disclaimer_frame)
    #disclaimer_scrollbar.pack(anchor='e', fill='y')

    disclaimer_button = tk.Button(disclaimer_frame, text="I Accept", command=vehicle_select)
    disclaimer_button.config(font=("Arial", 16), bg='black', fg='white')
    disclaimer_button.pack(side="bottom", fill="x")

    disclaimer_textbox = tk.Text(disclaimer_frame, width=50, height=20)
    disclaimer_textbox.config(font=("Arial", 12))
    disclaimer_textbox.pack(fill="both")
    disclaimer_textbox.insert(tk.END, "-Warning text 1\n\n-Warning text 2\n\n-Warning text 3\n\n")
    


    #scrollbar.config(command=disclaimer_textbox.yview)

    # create a Text widget with a Scrollbar attached
    #disclaimer_textbox = scrolledtext(disclaimer_frame, undo=True)
    #disclaimer_textbox['font'] = ('consolas', '12')
    #disclaimer_textbox.pack(expand=True, fill='both')
def vehicle_select():
    
    class selection:
        def __init__(self,master):
        
            vehicle_select_frame = tk.Frame(root, height=480, width=800,)
            vehicle_select_frame.pack_propagate(False)
            vehicle_select_frame.place(x=0, y=0)
            
            self.canvas1 = tk.Canvas(vehicle_select_frame,width=800,height=480)
            self.canvas1.config(bg=color_scheme.primary)
            self.canvas1.pack(expand='yes')
            
            self.ecocar_logo = ImageTk.PhotoImage(Image.open("ecocar_logo.png").resize((150,50),Image.ANTIALIAS))
            self.canvas1.create_image(10,425,anchor='nw',image=self.ecocar_logo)
            self.canvas1.image = self.ecocar_logo
            
            self.vehicle_select_title = tk.Label(vehicle_select_frame, text="Select a Vehicle",anchor='center')
            self.vehicle_select_title.config(font=("Helvetica", 24,'bold'),bg=color_scheme.secondary,fg='white')
            self.vehicle_select_title.place(x=3,y=0,height=75,width=794)
            
            self.canvas1.create_line(0,85,800,85,fill=color_scheme.green,width=5)
            
            self.name_box1=self.canvas1.create_rectangle(43,105,262,165,fill=color_scheme.secondary,outline=color_scheme.secondary)
            self.name_box2=self.canvas1.create_rectangle(293,105,512,165,fill=color_scheme.secondary,outline=color_scheme.secondary)
            self.name_box3=self.canvas1.create_rectangle(543,105,762,165,fill=color_scheme.secondary,outline=color_scheme.secondary)
            
            self.box1 = self.canvas1.create_rectangle(44,184,261,401,fill=color_scheme.green,outline=color_scheme.secondary)
            self.box2 = self.canvas1.create_rectangle(294,184,511,401,fill=color_scheme.green,outline=color_scheme.secondary)
            self.box3 = self.canvas1.create_rectangle(544,184,761,401,fill=color_scheme.green,outline=color_scheme.secondary)
            
            self.alice_label= self.canvas1.create_text((150,135),text='Alice',font='Helvetica 24 bold',fill=color_scheme.blue)
            self.sofie_label=self.canvas1.create_text((400,135),text='Sofie',font='Helvetica 24 bold',fill=color_scheme.blue)
            self.other_label=self.canvas1.create_text((650,135),text='Other',font='Helvetica 24 bold',fill=color_scheme.blue)
        
            self.alice_button = tk.Button(vehicle_select_frame, image = alice2img,compound='c', command=self.alice_select)
            self.alice_button.config(width=200, height=200)
            self.alice_button.place(x=50, y=190)
            
            self.sofie_button = tk.Button(vehicle_select_frame,image = sofieimg, compound='c', command=self.sofie_select)
            self.sofie_button.config(width=200, height=200)
            self.sofie_button.place(x=300, y=190)
            
            self.other_button = tk.Button(vehicle_select_frame, image = fuelcellimg, compound='c', command=self.picked_other)
            self.other_button.config(state='disabled',width=200, height=200,bg='light grey')
            self.other_button.place(x=550, y=190)
            
            self.continue_button=tk.Button(vehicle_select_frame,state='disabled',command=self.change_header)
            self.continue_button.config(font=('Helvetica',16,'bold'),bg=color_scheme.primary,relief='flat')
            self.continue_button.place(height=50,width=100,x=525,y=410) 
            
            self.back_button = tk.Button(vehicle_select_frame,state='disabled' ,command=vehicle_select)
            self.back_button.config(font=("Helvetica", 16,'bold'),bg=color_scheme.primary,relief='flat')
            self.back_button.place(width=100, height=50, x=675, y=410)
            
            self.multipurpose_label=tk.Label(vehicle_select_frame)
            
        def alice_select(self):
            global carchoice
            carchoice = 0
            
            self.canvas1.delete(self.box2,self.box3,self.alice_label,self.sofie_label,self.other_label)
            self.sofie_button.destroy()
            self.other_button.destroy()
            
            self.canvas1.delete(self.name_box2,self.name_box3)
            self.car_label = self.canvas1.create_text((150,135),text='Alice',font='Helvetica 24 bold',fill=color_scheme.blue)
            
            self.continue_button.configure(text='NEXT',state='normal',relief='raised',bg=color_scheme.blue,fg='white')
            self.back_button.configure(text='BACK',state='normal',relief='raised',bg=color_scheme.orange,fg='white')
            
            self.canvas1.create_line(300,85,300,480,fill=color_scheme.green,width=5)
            
            self.multipurpose_label.configure(text='Vehicle Specifications',font=('Helvetica',20,'bold'),bg=color_scheme.secondary,fg=color_scheme.blue)
            self.multipurpose_label.place(height=60,width=430,x=335,y=105)
            
        def sofie_select(self):
            global carchoice
            carchoice = 1
            
            self.canvas1.delete(self.box2,self.box3,self.alice_label,self.sofie_label,self.other_label)
            self.alice_button.destroy()
            self.other_button.destroy()
            self.sofie_button.place(x=50, y=190)
            
            self.canvas1.delete(self.name_box2,self.name_box3)
            self.car_label = self.canvas1.create_text((150,135),text='Sofie',font='Helvetica 24 bold',fill=color_scheme.blue)
            
            self.continue_button.configure(text='NEXT',state='normal',relief='raised',bg=color_scheme.blue,fg='white')
            self.back_button.configure(text='BACK',state='normal',relief='raised',bg=color_scheme.orange,fg='white')
            
            self.canvas1.create_line(300,85,300,480,fill=color_scheme.green,width=5)
            
            self.multipurpose_label.configure(text='Vehicle Specifications',font=('Helvetica',20,'bold'),bg=color_scheme.secondary,fg=color_scheme.blue)
            self.multipurpose_label.place(height=60,width=430,x=335,y=105)
        
        def picked_other(): # not operational
            
            pickedotherFrame = tk.Frame(root, height=480, width=800)
            pickedotherFrame.pack_propagate(False)
            pickedotherFrame.place(x=0, y=0)
        
            pickedothertitle = tk.Label(pickedotherFrame, text="What are we doing with this button")
            pickedothertitle.config(font=("Arial", 24), pady=50)
            pickedothertitle.pack()
        
            pickedother_button = tk.Button(root, text="OH NO GO BACK", command=vehicle_select)
            pickedother_button.config(font=("Arial", 16), bg='black', fg='white')
            pickedother_button.place(width=400, height=100, x=200, y=300)
            
        def change_header(self):
            self.vehicle_select_title.configure(text='Select Process to Run')
            process_select()
            
    selection(root)
      
def process_select():

    global methodchoice
    
    baseFrame = tk.Frame(root, height=392, width=497,bg=color_scheme.primary)
    baseFrame.pack_propagate(False)
    baseFrame.place(x=303, y=88)
    
    selectConditioning = tk.Radiobutton(baseFrame, text="Fuel cell conditioning", variable=methodchoice, value=0)
    selectConditioning.config(font=("Helvetica", 18,'bold'), anchor='w',fg='white',bg=color_scheme.primary,indicatoron=0,
                              activebackground=color_scheme.secondary,activeforeground='white',selectcolor=color_scheme.green)
    selectConditioning.place(x=40,y=50,width=420,height=50)

    selectPreStarvePolCurve = tk.Radiobutton(baseFrame, text="Polarization curve before air starve", variable=methodchoice, value=1)
    selectPreStarvePolCurve.config(font=("Helvetica", 18,'bold'), anchor='w',fg='white',bg=color_scheme.primary,indicatoron=0,
                                   activebackground=color_scheme.secondary,activeforeground='white',selectcolor=color_scheme.green)
    selectPreStarvePolCurve.place(x=40,y=105,width=420,height=50)

    selectAirStarve = tk.Radiobutton(baseFrame, text="Air starve", variable=methodchoice, value=2)
    selectAirStarve.config(font=("Hevetica", 18,'bold'), anchor='w',fg='white',bg=color_scheme.primary,indicatoron=0,
                           activebackground=color_scheme.secondary,activeforeground='white',selectcolor=color_scheme.green)
    selectAirStarve.place(x=40,y=160,width=420,height=50)

    selectPostStarvePolCurve = tk.Radiobutton(baseFrame, text="Polarization curve after air starve", variable=methodchoice, value=3)
    selectPostStarvePolCurve.config(font=("Helvetica", 18,'bold'), anchor='w',fg='white',bg=color_scheme.primary,indicatoron=0,
                                    activebackground=color_scheme.secondary,activeforeground='white',selectcolor=color_scheme.green)
    selectPostStarvePolCurve.place(x=40,y=215,width=420,height=50)

    menu_continue_button = tk.Button(root, text="NEXT", command=run_screen)
    menu_continue_button.config(font=("Helvetica", 16,'bold'), bg=color_scheme.blue, fg='white')
    menu_continue_button.place(width=100, height=50, x=500, y=400)
    
    menu_back_button = tk.Button(root, text="BACK", command=vehicle_select)
    menu_back_button.config(font=("Helvetica", 16,'bold'), bg=color_scheme.orange,fg='white')
    menu_back_button.place(width=100, height=50, x=650, y=400)
    
def run_screen():

    #this code is an example of how to do updating button text in tkinter
    #note for RS_stopbutton replace after text= with: "Stop %s" % (testvalueimportant), command=additem)
    #def additem():
       # global testvalueimportant
        #testvalueimportant += 1
        #RS_stop_button.config(text="Stop %s" % (testvalueimportant))
    global carchoice
    global methodchoice
         
    cars = ["Alice", "Sofie"]
    methods = ["conditioning", "polarization before air starve", "air Starve", "polarization after air starve"]
    
    RS_baseFrame = tk.Frame(root, height=360, width=600,bg=color_scheme.orange)
    RS_baseFrame.pack_propagate(False)
    RS_baseFrame.place(x=100, y=60)
    
    matting = tk.Label(RS_baseFrame,bg=color_scheme.primary)
    matting.place(x=7,y=7,width=586,height=346)
    
    conf_title = tk.Label(RS_baseFrame, text="Confirmation",anchor='center')
    conf_title.config(font=("Helvetica", 30,'bold','underline'),fg='white',bg=color_scheme.primary)
    conf_title.place(x=150,y=20,width=300,height=75)
    
    run_details = tk.Label(RS_baseFrame,text='Running %s\n on vehicle %s' %(methods[methodchoice.get()], cars[carchoice]))
    run_details.config(bg=color_scheme.primary,fg='white',font=('Helvetica',20),anchor='center')
    run_details.place(width=500,height=100,x=50,y=100)
    
    run_button = tk.Button(RS_baseFrame,text='RUN',command=recap_run,anchor='center')
    run_button.config(bg=color_scheme.blue,fg='white',font=('Helvetica',16,'bold'))
    run_button.place(height=50,width=100,y=250,x=175)
    
    quit_button = tk.Button(RS_baseFrame,text='EXIT',command=vehicle_select)
    quit_button.config(bg=color_scheme.orange,fg='white',font=('Helvetica',16,'bold'))
    quit_button.place(height=50,width=100,y=250,x=325)
    
#def recap_run():
#
#    cars = ["Alice", "Sofie"]
#    methods = ["conditioning", "polarization before air starve", "air Starve", "polarization after air starve"]
#    global carchoice
#    global methodchoice

#    recap_sentence = "Running %s on vehicle %s" % (methods[methodchoice.get()], cars[carchoice])
#    
#    recap_frame = tk.Frame(root, height=380, width=600)
#    recap_frame.pack_propagate(False)
#    recap_frame.place(x=80, y=50)
#
#    recap_label = tk.Label(recap_frame, text='Recap of what happened')
#    recap_label.config(font=("Arial", 24), bg='blue')
#    recap_label.pack(fill="both")
#
#    recap_button = tk.Button(recap_frame, text="Okee Dokey", command=run_screen)
#    recap_button.config(font=("Arial", 16), bg='black', fg='white')
#    recap_button.pack(side="bottom", fill="x")

#    recap_textbox = tk.Text(recap_frame, width=50, height=20)
#    recap_textbox.config(font=("Arial", 12))
#    recap_textbox.pack(fill="both")
#    recap_textbox.insert(tk.END, "%s\n" % (recap_sentence))
###################################################################################################
###################################################################################################

def recap_run():
    
    cars = ["Alice", "Sofie"]
    methods = ["conditioning", "polarization before air starve", "air Starve", "polarization after air starve"]

    recap_sentence = "Running %s on vehicle %s..." % (methods[methodchoice.get()], cars[carchoice])
       
    class A:
        def __init__(self, master):
            
            # create frame
            recap_frame = tk.Frame(root, height=480,width=800)
            recap_frame.pack_propagate(False)
            recap_frame.place(x=0,y=0)
            
            #create a canvas
            self.canvas = tk.Canvas(recap_frame,width=800,height=480)
            self.canvas.config(bg=color_scheme.primary)
            self.canvas.pack(expand='yes')
            
            # create ecocar logo in bottom right screen
            self.ecocar_logo = ImageTk.PhotoImage(Image.open("ecocar_logo.png").resize((150,50),Image.ANTIALIAS))
            self.canvas.create_image(10,425,anchor='nw',image=self.ecocar_logo)
            self.canvas.image = self.ecocar_logo
            
            # create lines to divide the gui screen
            self.canvas.create_line(0,160,800,160,fill=color_scheme.green,width=3)
            self.canvas.create_line(440,160,440,480,fill=color_scheme.green,width=3)
            self.canvas.create_line(440,390,800,390,fill=color_scheme.green,width=3)
            
            # create circles underlayed with changing arcs for the voltage,current, and temp. to be displayed on
            self.arc1 = self.canvas.create_arc(450,275,550,375,start=90,extent=-180,fill=color_scheme.green,outline=color_scheme.green)
            self.circle1 = self.canvas.create_oval(455,280,545,370,fill=color_scheme.secondary,outline=color_scheme.secondary)
            
            self.arc2 = self.canvas.create_arc(570,275,670,375,start=90,extent=-180,fill=color_scheme.orange,outline=color_scheme.orange)
            self.circle2 = self.canvas.create_oval(575,280,665,370,fill=color_scheme.secondary,outline=color_scheme.secondary)
            
            self.arc3 = self.canvas.create_arc(690,275,790,375,start=90,extent=-180,fill=color_scheme.blue,outline=color_scheme.blue)
            self.circle3 = self.canvas.create_oval(695,280,785,370,fill=color_scheme.secondary,outline=color_scheme.secondary)
            
            # This creates a blue outline for the progress bar
            progress_label1 = tk.Label(recap_frame,anchor='w',bg=color_scheme.blue)
            progress_label1.place(x=247,y=92,height=46,width=413)
            
            progress_outline = tk.Label(recap_frame, anchor="w",bg=color_scheme.primary)
            progress_outline.place(height=40,width=407,x=250,y=95)
            
            # initialize the color changing progress bar
            self.progress_bar = tk.Label(recap_frame, anchor="w")
            self.progress_bar.place(x=255,y=100,height=30)
            # percentage label on canvas
            self.percent_label = self.canvas.create_text((400,200),text="%3.2d%c" %(0,'%'),fill=color_scheme.blue)
            
            # displays at the top of the screen the process and vehicle
            recap_label = tk.Label(recap_frame, text = "%s" % (recap_sentence))
            recap_label.config(font=("Helvetica", 20,'bold'),bg=color_scheme.secondary,fg='white')
            recap_label.place(height=75,width=796, x=2, y=0)
            
            # header title for the current operating stats of the fuel cell
            stats_label = tk.Label(recap_frame,text='Current Operating Stats')
            stats_label.config(font=('Helvetica',17),bg=color_scheme.secondary,fg='white')
            stats_label.place(x=450,y=172,width=340,height=50)
            
            # we will now initialize the voltage, current, and temperature displays
            # voltage value, label, and units
            self.V_value = self.canvas.create_text((500,325), text='0 V')
            self.V_units = self.canvas.create_text((500,355),text='V',font='Helvetica 10',fill='white')
            self.V_label = self.canvas.create_text((500,250), text='Voltage',font='Helvetica 12 bold',fill='white')
          
            # current value, label, and units
            self.I_value = self.canvas.create_text((620,325), text='0 A')
            self.I_units = self.canvas.create_text((620,355),text='A',font='Helvetica 10',fill='white')
            self.I_label = self.canvas.create_text((620,250), text='Current',font='Helvetica 12 bold',fill='white')
            
            # temperature value, label, and units
            self.T_value = self.canvas.create_text((740,325), text='0 C')
            self.T_units = self.canvas.create_text((740,355),text='C',font='Helvetica 10',fill='white')
            self.T_label = self.canvas.create_text((740,250), text='Temperature',font='Helvetica 12 bold',fill='white')
            
            # initialize the time display
            self.Time_label=tk.Label(master)
            self.Time_label.place(x=10,y=85,width=230,height=60)
            self.Time_label.configure(font=("Helvetica",14),bg=color_scheme.secondary,fg='white')
    
            # create emergency stop button that will terminate program
            RS_emerstop_button = tk.Button(recap_frame, text="STOP", command=emergencystop_run)
            RS_emerstop_button.config(font=("Heelvetica", 16,'bold'), bg=color_scheme.orange, fg='white')
            RS_emerstop_button.place(width=100, height=50, x=675, y=410)
            
            # create continue button that will become active once the process is complete
            self.continue_button1=tk.Button(master,text='NEXT',state='disabled',command=vehicle_select)
            self.continue_button1.config(font=('Helvetica',16,'bold'),relief='sunken',fg='black',bg='grey')
            self.continue_button1.place(height=50,width=100,x=525,y=410)
            
            # we will now initialize the numerical values we will display on the running screen
            self.V = 0
            self.T = 0
            self.I = 0
            
            self.curr_time_sec = 0
            self.curr_time_min = 0
            self.total_time_sec = 0
            self.percent = 0
                    
            self.duration = 60
            self.width_multiplier = 400 / self.duration
            self.color_multiplier = 255 / self.duration
            self.increment_green = 0
            self.increment_red = 0
            self.green = 0
            self.red = 255
            
            self.v_arc = 0
            self.I_arc = 0
            self.T_arc = 0
            
            self.degree_counter=0;
            
            # create graph 
            
            self.V_list=[]
            self.I_list=[]
            canvas2 = tk.Frame(root,width=438,height=265)
            canvas2.pack_propagate(False)
            canvas2.place(x=1,y=162)
          
            fig=Figure(figsize=(5,5),dpi=70)
            x=[0,10,20,30,40,50,55]
            y=[120,80,65,55,45,42,40]
            ax = fig.add_subplot(111)
            ax.plot(x,y,color=color_scheme.orange,linewidth=4)
            ax.set_yticks([0,20,40,60,80,100,120])
            ax.set_xticks([0,10,20,30,40,50,60])
            fig.set_facecolor(color_scheme.primary)
            ax.set_facecolor(color_scheme.secondary)
            ax.tick_params(axis='both',colors='white')
            
            
            ax.set_ylabel("Voltage [V]",color='white',fontsize=16)
            ax.set_xlabel("Current [A]",color='white',fontsize=16)
            canvas = FigureCanvasTkAgg(fig,canvas2)
            #canvas.draw()
            #canvas._tkcanvas.place(height=260,width=439,x=0,y=0)
            canvas._tkcanvas.pack()
            
            canvas.get_tk_widget().place(height=265,width=439,x=1,y=0)
            
            
            #toolbar = NavigationToolbar2TkAgg(canvas,canvas2)
            #toolbar.update()
            
#            canvas2 = tk.Canvas(recap_frame,width=435,height=260)
#           
#            canvas2.place(x=0,y=162)
            
            
#            fig.patch.set_facecolor('blue')
#            plt.plot(self.I_list,self.V_list)
#            plt.savefig("Graph.jpeg",dpi=100)
            
            
           
            
#            self.graph = ImageTk.PhotoImage(Image.open("Graph.jpeg"))
           
#            self.canvas2 = tk.Frame(root,width=435,height=260)
#            self.canvas2.pack_propagate(False)
#            self.canvas2.place(x=0,y=162)
#            self.graph_live = self.canvas2.create_image(217,130,anchor='center',image=self.graph)
            
            
            
            
            
            #function call to update the data on the run screen
            self.update_labels()
           
        def update_labels(self):
            
            # get values for voltage, current, and temperature
            # this generates oscillating values ans should be replaced with the code to get the actual values
            #self.V = np.round(120*(np.sin(np.radians(self.degree_counter)))**2,decimals=0)
            self.V = np.round(40 +80*(np.exp(-0.1*self.I)),decimals=0)
            self.I = np.round(60*(np.sin(np.radians(self.degree_counter)))**2,decimals=0)
            self.T = np.round(40*(np.sin(np.radians(self.degree_counter)))**2,decimals=0)+35
            self.degree_counter = self.degree_counter + 2
            
            if self.I % 5 == 0:
                self.I_list.append(self.I)
                self.V_list.append(self.V)
                
#                # update graph
#                plt.close('all')
#                fig=plt.figure(figsize=(4.7,2.7))
#                fig.patch.set_facecolor("red")
#                
#                
#                self.canvas2.delete(self.graph_live)
#                plt.plot(self.I_list,self.V_list,'ko',markerfacecolor='k',markersize=4,linestyle='--',color='red')
#                
#                plt.axvspan(-2,60,facecolor=color_scheme.primary)
#                
#                
#                
#                plt.xticks(np.arange(0,71,10))
#                plt.yticks(np.arange(0,145,20))
#                plt.xlim([-2,60])
#                plt.ylim([0,125])
#                plt.savefig("Graph.jpeg",dpi=100)
#                self.graph = ImageTk.PhotoImage(Image.open("Graph.jpeg"))
#                self.graph_live = self.canvas2.create_image(217,130,anchor='center',image=self.graph)
#            
            
            # calculates arc length of underlayed circle. Represents the fraction of the current stat to the max
            self.v_arc=np.floor(359*(self.V/120))
            self.I_arc=np.floor(359*(self.I/60))
            self.T_arc=np.floor(359*(self.T/75))
            
            # update and display timer (this looks elaborate because placeholder zeros are inserted when needed)
            if self.curr_time_min < 10:
                if self.curr_time_sec <10:
                    self.Time_label.configure(text = "Elapsed Time:    %d%d:%d%d" %(0,self.curr_time_min,0,self.curr_time_sec))
                else:
                    self.Time_label.configure(text = "Elapsed Time:    %d%d:%d" %(0,self.curr_time_min,self.curr_time_sec))
            else: 
                if self.curr_time_sec <10:
                    self.Time_label.configure(text = "Elapsed Time:    %d:%d%d" %(self.curr_time_min,0,self.curr_time_sec))
                else:
                    self.Time_label.configure(text = "Elapsed Time:    %d:%d" %(self.curr_time_min,self.curr_time_sec))
            
            # delete previous underlayed arcs and replace with updated ones
            # because of layering, the circles and units also have to be reimplemented
            self.canvas.delete(self.arc1,self.arc2,self.arc3)
            
            self.arc1 = self.canvas.create_arc(450,275,550,375,start=90,extent=-self.v_arc,fill=color_scheme.green,outline=color_scheme.green)
            self.circle1 = self.canvas.create_oval(455,280,545,370,fill=color_scheme.secondary,outline=color_scheme.secondary)
            self.V_units = self.canvas.create_text((500,355),text='V',font='Helvetica 10',fill='white')
           
            self.arc2 = self.canvas.create_arc(570,275,670,375,start=90,extent=-self.I_arc,fill=color_scheme.orange,outline=color_scheme.orange)
            self.circle2 = self.canvas.create_oval(575,280,665,370,fill=color_scheme.secondary,outline=color_scheme.secondary)
            self.I_units = self.canvas.create_text((620,355),text='A',font='Helvetica 10',fill='white')
            
            self.arc3 = self.canvas.create_arc(690,275,790,375,start=90,extent=-self.T_arc,fill=color_scheme.blue,outline=color_scheme.blue)
            self.circle3 = self.canvas.create_oval(695,280,785,370,fill=color_scheme.secondary,outline=color_scheme.secondary)
            self.T_units = self.canvas.create_text((740,355),text='C',font='Helvetica 10',fill='white')
            
            #delete voltage, current, and temperature values and replace with updated values
            self.canvas.delete(self.V_value,self.I_value,self.T_value)
            
            self.V_value = self.canvas.create_text((500,325), text='%d' %(self.V),font='Helvetica 26',fill=color_scheme.green)
            self.I_value = self.canvas.create_text((620,325), text='%d' %(self.I),font='Helvetica 26',fill=color_scheme.green)
            self.T_value = self.canvas.create_text((740,325), text='%d' %(self.T),font='Helvetica 26', fill=color_scheme.green)
            
            # Change size and colour of progress bar
            tk_rgb = "#%02x%02x%02x" % (self.red, self.green, 0) #converts rgb color code to hexadecimal representation (needed for tkinter)
            # the rate at which the colors change... you're going to have to trust me
            
            self.increment_green = self.increment_green + self.color_multiplier
            self.green = math.floor(self.increment_green)
            
            if self.green > 170:
                self.increment_red = self.increment_red + 3*self.color_multiplier
                self.red = (255-math.floor(self.increment_red))
                
            if (self.total_time_sec)<=self.duration:
                
                self.progress_bar.place(x=255,y=100,height=30,width=self.width_multiplier*self.total_time_sec) #increases size of progress bar
                self.progress_bar.config(bg=tk_rgb)
            
            # keep track of time
            self.total_time_sec += 1
            self.curr_time_sec = self.total_time_sec % 60
            self.curr_time_min = math.floor(self.total_time_sec/60)
            
            # delete percentage label and replace with updated value
            self.canvas.delete(self.percent_label) 
            self.percent_label=self.canvas.create_text((720,115),text="%d%c" %(self.percent,'%'),fill=color_scheme.blue,font= "Helvetica 20 bold")

            self.percent = 100*(self.total_time_sec/self.duration)
            
            
            
            #repeat function every 1 second until duration is reached
            if self.total_time_sec<=self.duration:
                self.progress_bar.after(1000, self.update_labels) 
            else: # process is completed
                self.continue_button1.configure(state='normal',relief='raised',bg=color_scheme.blue,fg='white') #activate continue button
    A(root)
###############################################################################        
###############################################################################
 
def end_run(self):
    end_frame = tk.Frame(root, height=380, width=600)
    end_frame.pack_propagate(False)
    end_frame.place(x=80, y=50)
    

    end_label = tk.Label(end_frame, text='Ending Process')
    end_label.config(font=("Arial", 24), bg='blue')
    end_label.pack(fill="both")

    end_button = tk.Button(end_frame, text="Okee Dokey", command=vehicle_select)
    end_button.config(font=("Arial", 16), bg='black', fg='white')
    end_button.pack(side="bottom", fill="x")

    end_textbox = tk.Text(end_frame, width=50, height=20)
    end_textbox.config(font=("Arial", 12))
    end_textbox.pack(fill="both")
    end_textbox.insert(tk.END, "Oh man hope this works")

def emergencystop_run():
    #code to stop everything
    root.destroy()

class Colors: # create class that holds color scheme information
    def __init__(color,primary,secondary,green,blue,orange):
        
        color.primary = primary
        color.secondary = secondary
        color.green = green
        color.blue = blue
        color.orange = orange
        
color_scheme = Colors('#36454f','#20292f','#97C14B','#45b6fe','#ff781f') # set color scheme

# Create the main window
root = tk.Tk()
root.title("EcoCar GUI")

# define variables
carchoice = tk.IntVar()
methodchoice = tk.IntVar()

# import images to be used as buttons on the vehicle selection screen
alice2img = ImageTk.PhotoImage(Image.open("Alice2 (2).jpg").resize((200,200),Image.ANTIALIAS))

sofieimg = ImageTk.PhotoImage(Image.open("Sofie (2).jpg").resize((200,200),Image.ANTIALIAS))

fuelcellimg = ImageTk.PhotoImage(Image.open("FuelCell.png").resize((200,200),Image.ANTIALIAS))

# Import image for background
img = ImageTk.PhotoImage(Image.open("Alice.PNG"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

# Create Title using Ecocar logo
ecocar_logo = ImageTk.PhotoImage(Image.open("ecocar_logo.png").resize((300,100),Image.ANTIALIAS))
ecocar_title = tk.Label(root, image = ecocar_logo)
ecocar_title.place( x=10,y=5)

# create subtitles for main screen
subtitle1 = tk.Label(root, text="Resistive Load Bank")
subtitle1.config(font=("Arial", 16))
subtitle1.place(width=300, x=10, y=90)

subtitle1 = tk.Label(root, text="Version 0.1")
subtitle1.config(font=("Arial", 16))
subtitle1.place(width=300, x=10, y=115)

#create continue button
continue_button = tk.Button(root, text="Continue", command=view_disclaimer)
continue_button.config(font=("Arial", 16), bg=color_scheme.green, fg='white')
continue_button.place(width=200, x=300, y=375)

# Set window size to match 7" SparkFun LCD (800 x 480)
root.resizable(False, False)
root.geometry("800x480")

# Run forever!
root.mainloop()