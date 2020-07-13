import Tkinter
m = 0.001
k = 1000
M = 1000000
main_window = Tkinter.Tk()
main_window.title("Simple Wheatstone Bridge Calculator")

###### Theory button

def button():


    class SeaofBTCapp(Tkinter.Tk):

        def __init__(self, *args, **kwargs):
        
            Tkinter.Tk.__init__(self, *args, **kwargs)
            container = Tkinter.Frame(self)

            container.pack(side="top", fill="both", expand = True)

            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            for F in (StartPage, PageOne, PageTwo):
    
                frame = F(container, self)

                self.frames[F] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(StartPage)

        def show_frame(self, cont):

            frame = self.frames[cont]
            frame.tkraise()

        
    class StartPage(Tkinter.Frame):

        def __init__(self, parent, controller):
            Tkinter.Frame.__init__(self, parent)
            label = Tkinter.Label(self, text="Please select a following topic you wish to learn about", font = "Arial")
            label.pack(pady=10,padx=10)

            button = Tkinter.Button(self, text="Theory of the Wheatstone Bridge",
                                command=lambda: controller.show_frame(PageOne))
            button.pack()

            button2 = Tkinter.Button(self, text="Programme function",
                                command=lambda: controller.show_frame(PageTwo))
            button2.pack()


    class PageOne(Tkinter.Frame):

        def __init__(self, parent, controller):
            Tkinter.Frame.__init__(self, parent)
            label = Tkinter.Label(self, text="Theory", font= "Arial")
            label.pack(pady=10,padx=10)

            label2 = Tkinter.Label(self, text = "The theory of the Wheatstone bridge is based around what is known as the 'Balance equation'; \n \n R1 * Rv = R2 * Rx \n \n Where two opposite resistors multiplied together equal the two remaining resistors multiplied together \n \n In order for this equation to be true the P.D. between the two potential dividers must equal '0' as shown on the diagram in the programme itself \n \n If values for three of the resistor are already known then using the 'Balance equation' we can figure out the last resistor value by rearranging the formula", font = "Arial")
            label2.pack()
            
            button1 = Tkinter.Button(self, text="Back to topics",
                                command=lambda: controller.show_frame(StartPage))
            button1.pack()


    class PageTwo(Tkinter.Frame):

        def __init__(self, parent, controller):
            Tkinter.Frame.__init__(self, parent)
            label = Tkinter.Label(self, text="Programme function", font= "Arial")
            label.pack(pady=10,padx=10)

            label2 = Tkinter.Label(self, text = "The programme is allowing the user to input three values for resistance 'R1, R2, Rv' to solve for the unknown value 'Rx' \n \n Rx = (R1 * Rv) / R2 \n \n The programme is rearranging the 'Balance equation' into the form above \n \n This is the function that is happening when you are finding the missing resistor value", font = "Arial")
            label2.pack()
            
            button1 = Tkinter.Button(self, text="Back to topics",
                                command=lambda: controller.show_frame(StartPage))
            button1.pack()
        

    app = SeaofBTCapp()
    app.mainloop()




###### function x

def x():
    while True:
         try:
             if float(r1_entry.get())<=1000 and float(r1_entry.get())>=0:
                 if r1_drop_value.get() == "m":
                     New_r1_m = float(r1_entry.get()) * m
                     return New_r1_m
                     break
                 elif r1_drop_value.get() == "None":
                     New_r1_none = float(r1_entry.get())
                     return New_r1_none
                     break
                 elif r1_drop_value.get() == "k":
                     New_r1_k = float(r1_entry.get()) * k
                     return New_r1_k
                     break
                 elif r1_drop_value.get() == "M":
                     New_r1_M = float(r1_entry.get()) * M
                     return New_r1_M
                     break
                 else:
                     return "Error read instructions"
                     break
             else:
                 return -1
                 break
         except ValueError:
             return -1

######## function y

def y():
    while True:
         try:
             if float(r2_entry.get())<=1000 and float(r2_entry.get())>=0:
                 if r2_drop_value.get() == "m":
                     New_r2_m = float(r2_entry.get()) * m
                     return New_r2_m
                     break
                 elif r2_drop_value.get() == "None":
                     New_r2_none = float(r2_entry.get())
                     return New_r2_none
                     break
                 elif r2_drop_value.get() == "k":
                     New_r2_k = float(r2_entry.get()) * k
                     return New_r2_k
                     break
                 elif r2_drop_value.get() == "M":
                     New_r2_M = float(r2_entry.get()) * M
                     return New_r2_M
                     break
                 else:
                     return "Error read instructions"
                     break
             else:
                 return -1
                 break
         except ValueError:
             return -1

############ function z

def z():
     while True:
         try:
             if float(rv_entry.get())<=1000 and float(rv_entry.get())>=0:
                 if rv_drop_value.get() == "m":
                     New_rv_m = float(rv_entry.get()) * m
                     return New_rv_m
                     break
                 elif rv_drop_value.get() == "None":
                     New_rv_none = float(rv_entry.get())
                     return New_rv_none
                     break
                 elif rv_drop_value.get() == "k":
                     New_rv_k = float(rv_entry.get()) * k
                     return New_rv_k
                     break
                 elif rv_drop_value.get() == "M":
                     New_rv_M = float(rv_entry.get()) * M
                     return New_rv_M
                     break
                 else:
                     return "Error read instructions"
                     break
             else:
                 return -1
                 break
         except ValueError:
             return -1

########## Calculation function    

def rx():
    r1_x = x()
    r2_y = y()
    rv_z = z()
    while True:
        try:
            if  r1_x<0 or  r2_y<0 or  rv_z <0:
                answer = "try again"
                final = "try again"
                break
            else:
                answer = r1_x *  rv_z /  r2_y
                if answer >= 0 and answer <= 0.999:
                    final_millie = answer * 1000
                    final2_millie = round(final_millie, 2)
                    final = str(final2_millie) + "m ohms"
                    break
                elif answer > 0 and answer < 1000:
                    final_none = round(answer, 2) 
                    final = str(final_none) + " ohms"
                    break
                elif answer >= 1000 and answer < 1000000:
                    final_killer = answer / 1000
                    final2_killer = round(final_killer, 2)
                    final = str(final2_killer) + "k ohms"
                    break
                elif answer >= 1000000 and answer < 1000000000:
                    final_mega = answer / 1000000
                    final2_mega = round(final_mega, 2)
                    final = str(final2_mega) + "M ohms"
                    break
                elif answer >= 1000000000 and answer < 1000000000000:
                    final_giga = answer / 1000000000
                    final2_giga = round(final_giga, 2)
                    final = str(final2_giga) + "G ohms"
                    break
                elif answer >= 1000000000000 and answer < 1000000000000000:
                    final_tera = answer / 1000000000000
                    final2_tera = round(final_tera, 2)
                    final = str(final2_tera) + "T ohms"
                    break
                elif answer >= 1000000000000000 and answer < 1000000000000000000:
                    final_peta = answer / 1000000000000000
                    final2_peta = round(final_peta, 2)
                    final = str(final2_peta) + "P ohms"
                    break
                elif answer >= 1000000000000000000 and answer < 1000000000000000000000:
                    final_exa = answer / 1000000000000000000
                    final2_exa = round(final_exa, 2)
                    final = str(final2_exa) + "E ohms"
                    break
                else:
                    return "try again"
                    break
                break
        except ValueError:
            answer = "try again"
            final = answer
            break
        
    rx_result.config(text = answer)    
    Final_result.config(text = final)
    return answer

####### Geometry Size

main_window.geometry("%dx%d+%d+%d" % (820, 560, 500, 500))
box = Tkinter.Canvas(main_window, width= 820,height = 560)
box.place(x=0,y = 0)

####### Photo
box.create_rectangle(9,9,432,312,outline = "black")
photo = Tkinter.PhotoImage(file="Wheatstone.gif")
Image = Tkinter.Label(main_window,image=photo,bd=1)
Image.place( x=10, y=10)

####### operating box

box.create_rectangle(810,310,440,10,outline = "black")

######Label

r1_label = Tkinter.Label(main_window, text = "R1 Input",font = "Arial")
r1_label.place(x=450,y=20)

r2_label = Tkinter.Label(main_window, text = "R2 Input",font = "Arial")
r2_label.place(x=450,y=60)

rv_label = Tkinter.Label(main_window, text = "Rv Input",font = "Arial")
rv_label.place(x=450,y=100)

######Entry

r1_entry = Tkinter.Entry(main_window,bd = 3,font = "Arial")
r1_entry.place(x=525,y=20)

r2_entry = Tkinter.Entry(main_window,bd = 3,font = "Arial")
r2_entry.place(x=525,y=60)

rv_entry = Tkinter.Entry(main_window,bd = 3,font = "Arial")
rv_entry.place(x=525,y=100)

###### Option Menu

r1_drop_value = Tkinter.StringVar(main_window)
r1_drop_value.set("None")

r1_drop = Tkinter.OptionMenu(main_window, r1_drop_value, "m", "None", "k", "M")
r1_drop.place(x=725,y=16)

r2_drop_value = Tkinter.StringVar(main_window)
r2_drop_value.set("None")

r2_drop = Tkinter.OptionMenu(main_window, r2_drop_value, "m", "None", "k", "M")
r2_drop.place(x=725,y=56)

rv_drop_value = Tkinter.StringVar(main_window)
rv_drop_value.set("None")

rv_drop = Tkinter.OptionMenu(main_window, rv_drop_value, "m", "None", "k", "M")
rv_drop.place(x=725,y=96)

######### Button

calc_button = Tkinter.Button(main_window, text = "CALCULATE!",bd=3,font = "Arial", width = 30,command = rx)
calc_button.place(x=490,y=140)

######### Theory button

theory_button = Tkinter.Button(main_window, text = "Theory", bd=3, font = "Arial", width = 30, command = button)
theory_button.place(x = 490, y = 270)

######### result label

rx_label = Tkinter.Label(main_window, text = "Rx = ",font = "Arial")
rx_label.place(x=450,y=200)

######## result display

rx_result = Tkinter.Label(main_window, text = "",font = "Arial")
rx_result.place(x=525,y=200)

######## Final Label

Final_label = Tkinter.Label (main_window, text ="Final = ",font = "Arial" )
Final_label.place(x=450,y=240)

######## Final diaplay

Final_result = Tkinter.Label(main_window, text ="",font = "Arial")
Final_result.place(x=525,y=240)

######## Instruction box

box.create_rectangle(810,320,10,550,outline = "black")

######## Instruction

Instruction = Tkinter.Label(main_window, text = "Instruction : ", font = "Arial")
Instruction.place(x = 20, y = 330)
one = Tkinter.Label(main_window, text = " 1. Enter numerical values from 0 to 1000 in all resistors Entries.", font = "Arial")
one.place(x = 20, y = 370)
two = Tkinter.Label(main_window, text = " 2. Select the unit in all resistors from the selection.", font = "Arial")
two.place(x = 20, y = 410)
three = Tkinter.Label(main_window, text = " 3. Push the calculate button to find the answer for the unknown resistor 'Rx'.", font = "Arial")
three.place(x = 20, y = 450)
four = Tkinter.Label(main_window, text = " 4. Rx is the raw value and the 'Final' value is rounded with an appropriate unit assigned.", font = "Arial")
four.place(x = 20, y = 490)

main_window.mainloop()



