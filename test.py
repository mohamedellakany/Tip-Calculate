import tkinter as tk

window = tk.Tk()
window.geometry("350x350")
tk.Button(window,text="row 0 column 0").grid(row=0, column=0)
tk.Button(window,text="row 0 column 1").grid(row=0, column=1)

# #Here the column is set to 5, but it will still be placed in column=2. place

tk.Button(window,text="row 0 column 2").grid(row=0, column=5) 
tk.Button(window,text="Row 1 Column 0").grid(row=1, column=0)
tk.Button(window,text="row 1 column 1").grid(row=1, column=1)

#Place two different containers in the same location on top of each other.

# tk.Button(window,text="overlay").grid(row=1, column=1) 

window.mainloop()