import tkinter as Tkinter


root = Tkinter.Tk()
root.title("Stopwatch")
root.iconbitmap('image/stopwatch.ico')
hh = 00  # hour
mm = 00  # min
ss = 00  # sec
stp = 0  # stop
rst = 0  # reset


# start function with all global variabel
def Start():
    global hh, mm, ss, stp, rst
    ss = ss + 1
    # condition for stop
    if(stp == 1):
        stp = 0
        return
        # condition for reset
    if(rst == 1):
        hh = 0
        mm = 0
        ss = 0
        rst = 0
        return
        # condition for second
    if(ss == 60):
        mm = mm+1
        ss = 00
        # condition for min
    if(mm == 60):
        hh = hh+1
    data = str(str(hh)+":"+str(mm)+":"+str(ss))
    # changing text
    label.config(text=data)
    start.config(state = Tkinter.DISABLED)
    stop.config(state = Tkinter.NORMAL)
    reset.config(state = Tkinter.NORMAL)
    # after function callback start in every 500 millisecond
    label.after(500, Start)

# stop function


def Stop():
    global stp
    start.config(state = Tkinter.NORMAL)
    stop.config(state = Tkinter.DISABLED)
    stp = 1

# reset function
def Reset():
    global rst
    rst = 1
    start.config(state = Tkinter.NORMAL)
    reset.config(state = Tkinter.DISABLED)
    label.config(text="Welcome!")
    lapData.delete(0,Tkinter.END)
    


# lap function
lapCount = 0
def lap():
    global hh, mm, ss,lapCount
    lapCount = lapCount + 1
    data = str(str(hh)+":"+str(mm)+":"+str(ss))
    lapData.insert(lapCount, data)


# Fixing the window size.
root.minsize(width=250, height=70)
# label
label = Tkinter.Label(root, text="Welcome!", fg="black",
                      font="Verdana 30 bold")
label.pack()
# frame
f = Tkinter.Frame(root)
# start button
start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start())
# stop button
stop = Tkinter.Button(f, text='Stop', width=6, state=Tkinter.DISABLED, command=Stop)
# reset button
reset = Tkinter.Button(f, text='Reset', width=6, state=Tkinter.DISABLED, command=lambda: Reset())
# lap button
lapsButton = Tkinter.Button(f, text='lap', width=6, command=lambda: lap())

# lap data
laps = Tkinter.Label(root, text="Laps", fg="black",
                      font="Verdana 16 bold")
lapData = Tkinter.Listbox(root,fg="black",font="Verdana 10")

f.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
lapsButton.pack(side="left")
label.pack()
lapData.pack()

root.mainloop()
