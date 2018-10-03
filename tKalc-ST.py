#Tkinter calculator (Scientific), by Benedict RM, 2016-07-04
#CC-BY-NC

import tkinter as tk

#creating the main window
window=tk.Tk()
window.title("tKalc-ST")
window.resizable(width=False, height=False)


#object in position x,y - Name: [FIXME]4
#oxy=tk.Button(text = "^")
#oxy.grid(column=0,row=1)

#Row 0

#Input in position 0,0 - Name: Display
i00=tk.Entry(text = "")
i00.grid(column=0,row=0,columnspan=4,)

#Row 1

#Input in position 1,0 - Name: Display
i01=tk.Entry(text = "")
i01.grid(column=0,row=1,columnspan=4,)

#Row 2

#button in position 0,2 - Name: Exponent
b02=tk.Button(text = "^",padx = 10)
b02.grid(column=0,row=2)
#button in position 1,2 - Name: Square Root
b12=tk.Button(text = "√",padx = 11)
b12.grid(column=1,row=2)
#button in position 2,2 - Name: Clear
b22=tk.Button(text = "C",padx = 11)
b22.grid(column=2,row=2)
#button in position 3,2 - Name: Backspace
b32=tk.Button(text = "←",padx = 11)
b32.grid(column=3,row=2)

#Row 3

#button in position 0,3 - Name: One
b03=tk.Button(text = "1",padx = 11)
b03.grid(column=0,row=3)
#button in position 1,3 - Name: Two
b13=tk.Button(text = "2",padx = 11)
b13.grid(column=1,row=3)
#button in position 2,3 - Name: Three
b23=tk.Button(text = "3",padx = 11)
b23.grid(column=2,row=3)
#button in position 3,3 - Name: Plus
b33=tk.Button(text = "+",padx = 11)
b33.grid(column=3,row=3)

#Row 4

#button in position 0,4 - Name: Four
b04=tk.Button(text = "4",padx = 11)
b04.grid(column=0,row=4)
#button in position 1,4 - Name: Five
b14=tk.Button(text = "5",padx = 11)
b14.grid(column=1,row=4)
#button in position 2,4 - Name: Six
b24=tk.Button(text = "6",padx = 11)
b24.grid(column=2,row=4)
#button in position 3,3 - Name: Minus
b34=tk.Button(text = "-",padx = 14)
b34.grid(column=3,row=4,)

#Row 5

#button in position 0,5 - Name: Seven
b05=tk.Button(text = "7",padx = 11)
b05.grid(column=0,row=5)
#button in position 1,5 - Name: Eight
b15=tk.Button(text = "8",padx = 11)
b15.grid(column=1,row=5)
#button in position 2,5 - Name: Nine
b25=tk.Button(text = "9",padx = 11)
b25.grid(column=2,row=5)
#button in position 3,5 - Name: Multiply
b35=tk.Button(text = "×",padx = 11)
b35.grid(column=3,row=5)

#Row 6

#button in position 0,6 - Name: Nought
b06=tk.Button(text = "0",padx = 11)
b06.grid(column=0,row=6)
#button in position 1,6 - Name: Point
b16=tk.Button(text = ".",padx = 13)
b16.grid(column=1,row=6)
#button in position 2,6 - Name: Equals
b26=tk.Button(text = "=", padx = 10)
b26.grid(column=2,row=6)
#button in position 3,6 - Name: Divide
b36=tk.Button(text = "÷",padx = 11)
b36.grid(column=3,row=6)

#Row 7

#button in position 0,7 - Name: Functions
b07=tk.Button(text = "FN",padx = 7)
b07.grid(column=0,row=7)
#button in position 1,7 - Name: Memory
b17=tk.Button(text = "MEM",padx = 1)
b17.grid(column=1,row=7)
#button in position 2,7 - Name: AC
b27=tk.Button(text = "AC", padx = 7)
b27.grid(column=2,row=7)
#button in position 3,7 - Name: Pi
b37=tk.Button(text = "π",padx = 12)
b37.grid(column=3,row=7)

window.mainloop()
print ("Program ending...")
