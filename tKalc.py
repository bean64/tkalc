#!/usr/bin/python3
#Tkinter calculator, by Benedict RM, 2016-06-29, updated 2016-06-30 and again 2017-03-17 to add rounding and thus avert 0.1+0.2=0.30000000004
#CC-BY-NC
#global mop
#global strd

#E1:Empty Var
#E2:Sqrt Err
#E3:Maths Err
print ("importing Tkinter")
import tkinter as tk

#defining the functions

#determining OS
import platform
import sys
wince = False
global wince
try:
    print ("OS:",(platform.system()))
    if (platform.system()) == ("Windows"):
        wince = True #Linux master race
except:
    print ("OS get failed")

#appends to the value onscreen, makes sure operation is possible and if error displayed, clears screen
def app(x):
    print ("Disp:Adding",x)
    txt = i00.get()
    if "E" in txt:
        print ("Disp:Clearing error")
        clear()
    if "." in txt and x == ".":
        print ("Disp:Can't have >1 dots")
    else:
        leng = len(txt)
        i00.insert(leng, x)

#backspace button, should also be optimised
def bksp():
    txt = i00.get()
    leng = len(txt)
    print ("Disp:Backspace")
    i00.delete(leng-1, leng+1)
    
#mathematical operator variable:
#1 is +, 2 is -, 3 is ×, 4 is ÷, 5 is ^, 6 is √ (special as has no second arg), 0 is unset

# takes current number into memory, sets mathematical operator. If special case square root it outputs the answer straight away
def setmop(x):
    print ("Set Opcode:",x,"old was",mop)
    if mop != 0:
        print ("Opcode was not reset, multiple operators detected!")
        finish()
    mop = x
    global mop
    strd = i00.get()
    try:
        strd = float(strd)
    except:
        print ("EMPTY VARIABLE")
        clear()
        app("E1")
        return True #this does nothing except end the subroutine
    global strd
    if mop == 6:
        try:
            print ("Special case: Opcode 6")
            print ("Calculating Root...")
            ans = float(strd)**0.5
            clear()
            app(ans)
            mop = 0
            global mop
        except Exception as e:
            print ("MATHEMATICAL ERROR: %s"%str(e))
            clear()
            app("E2")
        return True #this does nothing except end the subroutine
    clear()


#takes the numbers and operator provided, calculates and displays result

def finish():
    try:
        print ("Running calculation.")
        disp = i00.get()
        print ("Operation Code=",mop)
        print ("Variable 1=",strd)
        disp = float(disp)
        print ("Variable 2=",disp)
        if mop == 1:
            print ("Adding...")
            ans = strd+disp
        if mop == 2:
            print ("Subtracting...")
            ans = strd-disp
        if mop == 3:
            print ("Multiplying...")
            ans = strd*disp
        if mop == 4:
            print ("Dividing...")
            ans = strd/disp
        if mop == 5:
            print ("Raising to power...")
            ans = strd**disp
        print ("Result:",ans)
        clear()
        if int(ans) == ans:
            print ("Integer mode")
            ans = int(ans)
        print ("Rounding")
        app(round(ans,15))
        mop = 0
        global mop
        
    except Exception as e:
        print(type(e))
        print ("MATHEMATICAL ERROR: %s"%str(e))
        clear()
        app("E3")
      
    
mop = 0

#Clears the screen, wipes all the working variables and resets the calculator.
def clear():
    print ("Disp:Cleared,formerly",i00.get())
    i00.delete(0, 300) 

def ac():
    clear()
    mop = 0
    global mop

    

#creating the window
window=tk.Tk()
window.title("tKalc")
window.resizable(width=False, height=False)


#object in position x,y - Name: [FIXME]4
#oxy=tk.Button(text = "^")
#oxy.grid(column=0,row=1)

#Row 0

#Input in position 0,0 - Name: Display
i00=tk.Entry(text = "")
i00.grid(column=0,row=0,columnspan=4,)

#Row 1

#button in position 0,1 - Name: Exponent
if wince == True:
    b01=tk.Button(text = "^", command=lambda: setmop(5),padx = 10)
else:
    b01=tk.Button(text = "^", command=lambda: setmop(5),padx = 10)
b01.grid(column=0,row=1)

#button in position 1,1 - Name: Square Root
if wince == True:
    b11=tk.Button(text = "√",command=lambda: setmop(6),padx = 10)
else:
    b11=tk.Button(text = "√",command=lambda: setmop(6),padx = 11)
b11.grid(column=1,row=1)
#button in position 2,1 - Name: Clear
if wince == True:
    b21=tk.Button(text = "C",command=ac,padx = 10)
else:
    b21=tk.Button(text = "C",command=ac,padx = 11)
b21.grid(column=2,row=1)
#button in position 3,1 - Name: Backspace
if wince == True:
    b31=tk.Button(text = "←",command=bksp,padx = 10)
else:
    b31=tk.Button(text = "←",command=bksp,padx = 11)
b31.grid(column=3,row=1)

#Row 2

#button in position 0,2 - Name: One
b02=tk.Button(text = "1", command=lambda: app(1),padx = 11)
b02.grid(column=0,row=2)
#button in position 1,2 - Name: Two
b12=tk.Button(text = "2", command=lambda: app(2),padx = 11)
b12.grid(column=1,row=2)
#button in position 2,2 - Name: Three
b22=tk.Button(text = "3", command=lambda: app(3),padx = 11)
b22.grid(column=2,row=2)
#button in position 3,2 - Name: Plus
b32=tk.Button(text = "+", command=lambda: setmop(1),padx = 11)
b32.grid(column=3,row=2)

#Row 3

#button in position 0,3 - Name: Four
b03=tk.Button(text = "4", command=lambda: app(4),padx = 11)
b03.grid(column=0,row=3)
#button in position 1,3 - Name: Five
b13=tk.Button(text = "5", command=lambda: app(5),padx = 11)
b13.grid(column=1,row=3)
#button in position 2,3 - Name: Six
b23=tk.Button(text = "6", command=lambda: app(6),padx = 11)
b23.grid(column=2,row=3)
#button in position 3,3 - Name: Minus
if wince == True:
    b33=tk.Button(text = "- ", command=lambda: setmop(2),padx = 11)
else:
    b33=tk.Button(text = "-", command=lambda: setmop(2),padx = 14)
b33.grid(column=3,row=3,)

#Row 4

#button in position 0,4 - Name: Seven
b04=tk.Button(text = "7", command=lambda: app(7),padx = 11)
b04.grid(column=0,row=4)
#button in position 1,4 - Name: Eight
b14=tk.Button(text = "8", command=lambda: app(8),padx = 11)
b14.grid(column=1,row=4)
#button in position 2,4 - Name: Nine
b24=tk.Button(text = "9", command=lambda: app(9),padx = 11)
b24.grid(column=2,row=4)
#button in position 3,4 - Name: Multiply
b34=tk.Button(text = "×", command=lambda: setmop(3),padx = 11)
b34.grid(column=3,row=4)

#Row 5

#button in position 0,5 - Name: Nought
b05=tk.Button(text = "0", command=lambda: app(0),padx = 11)
b05.grid(column=0,row=5)
#button in position 1,5 - Name: Point
if wince == True:
    b15=tk.Button(text = ".", command=lambda: app("."),padx = 12)
else:
    b15=tk.Button(text = ".", command=lambda: app("."),padx = 13)
b15.grid(column=1,row=5)
#button in position 2,5 - Name: Equals
b25=tk.Button(text = "=", command=finish, padx = 10)
b25.grid(column=2,row=5)
#button in position 3,5 - Name: Divide
b35=tk.Button(text = "÷", command=lambda: setmop(4),padx = 11)
b35.grid(column=3,row=5)

window.mainloop()
print ("Program ending...")
