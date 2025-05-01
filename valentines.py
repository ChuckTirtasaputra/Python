import tkinter as tk
from tkinter import messagebox
'''
this code "hacks" into your partners computer and asks them to be your valentines
'''

'''
THE CODE BELOW IS A DIFFERENT VERSION OF THE FINAL CODE

def show_alert():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    heart=u"\u2665"
    skull=chr(9760)

    messagebox.showwarning("Form", (skull +" YOU GOT HACKED! "+ skull), icon ='warning')
    count = 1    
    result = messagebox.askquestion("Form", ("Will you be my Valentines, Pookie Bear? " + heart))

    while result == 'no' and (count < 3):   
        result = messagebox.askquestion("Form", ("Please? " + heart*count))
        count = count+1
    while result == 'no' and (count >= 3):
        result = messagebox.askquestion("Form", ("Pretty Please? " + heart*count))
        count = count+1
        
    if result == "yes":
        messagebox.showinfo("Form", ("YAY!! "+heart*10))
        messagebox.showinfo("Form", ("I love you the most by the way!! "+heart*100 +"\nI win!!"))

    root.destroy()

show_alert()

'''

heart=u"\u2665"
skull=chr(9760)
count = 1   
    
def hacked():
    # Create main window
    global window
    window = tk.Tk()
    window.title("yoU gOt HaCkEd!!")
    window.geometry("750x150")

    # Create a label with text
    message = str(skull +" YOU GOT HACKED! "+ skull)
    label = tk.Label(window, text=message, font=("Arial", 48), fg="red")
    label.pack()

    
    next_button = tk.Button(window, text="OK", command=ask, width=20, height=2, font=("Arial", 16))
    next_button.pack(pady=20)


def ask():
    window.destroy()
    # Create main window
    global question
    question = tk.Tk()
    question.title("")
    question.geometry("750x150")

    # Create a label with text
    label = tk.Label(question, text="However, I just have one question...", font=("Arial", 30), fg="pink")
    label.pack()

    next_button = tk.Button(question, text="Okay...", command=val, width=20, height=2, font=("Arial", 16))
    next_button.pack(pady=20)


def val():
    question.destroy()
    # Create main window
    global valen
    valen = tk.Tk()
    valen.title("")
    valen.geometry("750x150")

    # Create a label with text
    label = tk.Label(valen, text=("Will you be my Valentines, Pookie Bear? " + heart), font=("Arial", 30), fg="pink")
    label.pack()

    # Create a frame to center the buttons
    button_frame = tk.Frame(valen)
    button_frame.pack(pady=10)  # Add padding for spacing

    # Center the buttons inside the frame
    yes = tk.Button(button_frame, text=(heart + " YES " + heart), command=yuh, width=20, height=2, font=("Arial", 16), fg="#e75480")
    yes.pack(side="left", padx=10)  # Add horizontal padding

    no = tk.Button(button_frame, text="NO", command=nah, width=20, height=2, font=("Arial", 16), fg="red")
    no.pack(side="left", padx=10)


def nah():
    global nahh
    global count
    try:
        if valen.winfo_exists():
            valen.destroy()
    except NameError:
        pass  # If valen is not defined, just continue
    except tk.TclError:
        pass  # If valen is already destroyed, just continue
    
    try:
        if nahh.winfo_exists() and count>1:
            nahh.destroy()
    except NameError:
        pass  # If nahh is not defined, just continue
    except tk.TclError:
        pass  # If nahh is already destroyed, just continue

    # Create main window
    nahh = tk.Tk()
    nahh.title("")
    nahh.geometry("750x150")

    count = count+1

    # Create a label with text
    label = tk.Label(nahh, text=("Pleasee? " + heart*count), font=("Arial", 30), fg="#e75480")
    label.pack()

    # Create a frame to center the buttons
    button_frame = tk.Frame(nahh)
    button_frame.pack(pady=10)  # Add padding for spacing

    # Center the buttons inside the frame
    yes = tk.Button(button_frame, text="fine", command=yuh, width=20, height=2, font=("Arial", 16), fg="#e75480")
    yes.pack(side="left", padx=10)  # Add horizontal padding

    no = tk.Button(button_frame, text="NO", command=nah, width=20, height=2, font=("Arial", 16), fg="red")
    no.pack(side="left", padx=10)

def yuh():
    # Check if valen exists before calling winfo_exists()
    try:
        if valen.winfo_exists():
            valen.destroy()
    except NameError:
        pass  # If valen is not defined, just continue
    except tk.TclError:
        pass  # If valen is already destroyed, just continue
        # Create main window
    
    try:
        if nahh.winfo_exists() and count>1:
            nahh.destroy()
    except NameError:
        pass  # If nahh is not defined, just continue
    except tk.TclError:
        pass  # If nahh is already destroyed, just continue

    global yuhh
    yuhh = tk.Tk()
    yuhh.title("")
    yuhh.geometry("750x150")

    # Create a label with text
    label = tk.Label(yuhh, text=("YAY!! "+heart*10), font=("Arial", 30), fg="#e75480")
    label.pack()

    next_button = tk.Button(yuhh, text="Continue", command=yay, width=20, height=2, font=("Arial", 16))
    next_button.pack(pady=20)

def yay():
    yuhh.destroy()
    # Create main window
    yayy = tk.Tk()
    yayy.title("")
    yayy.geometry("1000x250")

    # Create a label with text
    label = tk.Label(yayy, text=("I love you the most by the way!! \n"+ heart*50 + "\n"+heart*50+ "\nI win!!"), font=("Arial", 30), fg="#e75480")
    label.pack()

    next_button = tk.Button(yayy, text="Goodbye", command=yayy.destroy, width=20, height=2, font=("Arial", 16))
    next_button.pack(pady=20)

hacked()







