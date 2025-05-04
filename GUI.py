import tkinter as tk

clicks = 0
def onButton():
    global clicks
    clicks += 1
    if clicks == 1:
        click_label.config(text=f"You have clicked me {clicks} time!")
    else:
        click_label.config(text=f"You have clicked me {clicks} times!")

gui_name = input("What would you like your GUI's name to be?\nEnter: ")
while gui_name == "":
    gui_name = input("What would you like your GUI's name to be?\nEnter: ")

gui_text = input("What would you like to display on your GUI's home page?\nEnter: ")

print("What should be the resolution of your GUI?")
gui_resX = input("Enter resolution for X (for example, 500): ")

while gui_resX == "" or gui_resX.isspace():
    gui_resX = input("Enter resolution for X (for example, 500): ")

while gui_resX.isalpha():
    gui_resX = input("Enter resolution for X (for example, 500): ")

gui_resY = input("Enter resolution for Y (for example, 500): ")

while gui_resY == "" or gui_resY.isspace():
    gui_resY = input("Enter resolution for Y (for example, 500): ")

while gui_resY.isalpha():
    gui_resY = input("Enter resolution for Y (for example, 500): ")

gui = tk.Tk()
gui.geometry(f"{gui_resX}x{gui_resY}")
gui.title(gui_name)
label = tk.Label(gui, text=(gui_text), font=('Arial', 20))
label.pack(padx=10, pady=10)
click_label = tk.Label(gui, text="You haven't clicked me yet!", font=("Arial", 15))
click_label.pack(padx = 15, pady = 15)
buttonframe = tk.Frame(gui)
button = tk.Button(gui, text="Click me!", command=onButton, font=('Arial', 15))
button.pack()
gui.mainloop()