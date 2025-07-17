import tkinter as tk

main = tk.Tk()
main.title("Smart Home Sim")
main.geometry("550x300")
main.configure(background = "white")

lightframe = tk.LabelFrame(main, text="House Controls", padx=10, pady=10)
lightframe.pack(padx=20, pady=40, fill="both", expand=True)


def togglelight():
    if lightbutton["text"] == "Turn Light On":
        lightbutton.config(text = "Turn Light Off")
        bulblabel.config(text = "💡", fg="yellow")
        lightstatus.config(text = "Light is On")
    else:
        lightbutton.config(text = "Turn Light On")
        bulblabel.config(text = "💡", fg="black")
        lightstatus.config(text = "Light is Off")

def togglelock():
    if lockbutton["text"] == "Lock Door":
        lockbutton.config(text = "Open Door")
        locklabel.config(text = "🔒")
        lockstatus.config(text = "Door is Locked")
    else:
        lockbutton.config(text = "Lock Door")
        locklabel.config(text = "🔓")
        lockstatus.config(text = "Door is Open")

def togglefan():
     global fanspeednum
     fanspeednum = ((fanspeednum + 1) % len(fanspeed))
     fanlabel.config(text = "Fan Speed: "+fanspeed[fanspeednum])

def toggletempup():
    global Temp
    Temp += 1
    templabel.config(text="Temperature: "+str(Temp)+"°F")

def toggletempdown():
    global Temp
    Temp -= 1
    templabel.config(text="Temperature: "+str(Temp)+"°F")

def toggleswitch():
    if tempswitch["text"] == "Turn Thermostat Off":
        tempswitch.config(text="Turn Thermostat On")
        tempup.config(bg="gray",state="disabled")
        tempdown.config(bg="gray",state="disabled")
    else:
        tempswitch.config(text="Turn Thermostat Off")
        tempup.config(bg="red",state="normal")
        tempdown.config(bg="royal Blue",state="normal")
    
    

lightbutton = tk.Button(lightframe, text="Turn Light On", command=togglelight, width=13)
lightbutton.grid(row=0, column=0, padx=(0,40))
bulblabel = tk.Label(lightframe, text="💡", font=("Arial", 20))
bulblabel.grid(row=3, column=0, padx=(0,40))
lightstatus = tk.Label(lightframe, text="Light is Off", font=("Arial",10, "bold"))
lightstatus.grid(row=2, column=0, padx=(0,40))


lockbutton = tk.Button(lightframe, text="Lock Door", command=togglelock, width=13)
lockbutton.grid(row=0, column=2, padx=(0,60))
locklabel = tk.Label(lightframe, text="🔓", font=("Arial", 20))
locklabel.grid(row=3, column=2, padx=(0,60))
lockstatus = tk.Label(lightframe, text="Door is Open", font=("Arial",10, "bold"))
lockstatus.grid(row=2, column=2, padx=(0,60))

fanspeed = ["Off", "Low", "Medium", "High"]
fanspeednum = 0
fanbutton = tk.Button(lightframe, text="Fan Speed", command=togglefan, width=13)
fanbutton.grid(row=0, column=3)
fanlabel = tk.Label(lightframe, text=("Fan Speed: Off"), font=("Arial",10,"bold"), width=16)
fanlabel.grid(row=2, column=3)

Temp = 72
templabel = tk.Label(lightframe, text="Temperature: 72°F", font=("Arial",10))
templabel.grid(row=4, column=0, padx=(0,20), pady=(30))
tempup=tk.Button(lightframe, text="▲", command=toggletempup, bg="red")
tempup.grid(row=4, column=1, padx=(0,20), pady=(30))
tempdown=tk.Button(lightframe, text="▼", command=toggletempdown, bg="royal Blue")
tempdown.grid(row=4, column=1, padx=(0,20), pady=(50,0))

tempswitch = tk.Button(lightframe, text="Turn Thermostat Off", command=toggleswitch)
tempswitch.grid(row=4, column=0, padx=(0,20), pady=(60,0))
main.mainloop()
    




        
        
        
        
        
    
    
    
    
    
    
