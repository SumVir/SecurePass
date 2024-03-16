# Import the modules
import tkinter as tk
from tkinter import Tk, Canvas
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage, NW, messagebox
import zxcvbn
import webbrowser
from pygame import mixer
# Image handling && Image resizing 
class AutoResizingImage:
    def __init__(self, master, path):
        self.master = master
        self.path = path
        self.img = None
        self.tk_img = None
        self.image_id = None
        self.update_image()

    def update_image(self):
        width, height = self.master.winfo_width(), self.master.winfo_height()
        self.img = Image.open(self.path)
        self.img = self.img.resize((width, height), Image.LANCZOS)
        if self.tk_img is not None:
            # Delete the previous image from the canvas
            self.master.delete(self.image_id)
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.image_id = self.master.create_image(0, 0, image=self.tk_img, anchor=NW)

window = Tk()
window.geometry('1200x600')  # Set the window size to 1200x600
window.title("Password Strength Checker")

canv = Canvas(window, width=1200, height=600, bg='white')
canv.pack(fill='both', expand=True)

img = AutoResizingImage(canv, r"C:\Users\PC\OneDrive\.vscode\Tests.tool\appbg.png")

def resize(event):
    img.update_image()

window.bind('<Configure>', resize)



# Create the widgets
label1 = tk.Label(window, text="Enter a password to check:" , fg="black", bg=None)
entry1 = tk.Entry(window, show="*")
label2 = tk.Label(window, text="Strength Information: ", fg="black", bg= None)
label3 = tk.Label(window, text=None, bg=None  )
button1 = tk.Button(window, text="Check", fg="white", bg="blue", cursor="hand2")
button2_clear = tk.Button(window, text="Clear", fg="white", bg="red", cursor="hand2", command=lambda: clearEntry())
button3_pwned = tk.Button(window, text="Have I been pwned? Check your password", fg="white", bg="black", cursor="hand2")


# Define qualitative terms for password strength
def evaluateStrength(score):
    if score == 0:
        return "Very weak. Please change it to a stronger password."
    elif score == 1:
        return "Weak. It's very vulnerable to password attacks. Change it !"
    elif score == 2:
        return "Moderate. Consider adding more characters and complexity."
    elif score == 3:
        return "Strong. Your password is reasonably secure, but there's room for improvement."
    elif score == 4:
        return "Very strong. Excellent job! Your password is highly secure."
    
# Define the function to check the password strength
def checkPassword(event=None):
    # Get the password from the entry widget
    password = entry1.get()
    # Check the password strength with zxcvbn
    result = zxcvbn.zxcvbn(password)
    # Get the score and feedback from the result
    score = result["score"]
    strength = evaluateStrength(score)
    feedback = result["feedback"]
    # Update the label widget with the score and feedback
    label3.config(text=f"Your password is {strength}.\nHere is some feedback on how to improve your password:\n{feedback}", wraplength=900)

# Define the function to clear the entry field
def clearEntry():
    entry1.delete(0, tk.END)
    label3.config(text="")
# Links
def open_link(event):
    webbrowser.open("https://saidsecurity.com")

def open_link2(event):
    webbrowser.open("https://haveibeenpwned.com/Passwords")



def show_usage_info():
    messagebox.showinfo("Usage info", "This app helps you create strong passwords and avoid common pitfalls.\n\nHere's how to use it:\n\n Enter your password: Type your password into the designated input bar.\n\nClick 'Check': Press the 'Check' button to analyze your password's strength.\n\nView Strength Information: The application will display the strength of your password under the 'Strength Information:' label.\n\nClear Password: To start fresh or check another password, simply click the 'Clear' button. This will erase both the displayed information and your entered password from the input bar, saving you time compared to manually deleting a long password.")

Info_button = tk.Button(window, text="About", fg="black", bg="white", cursor="hand2", command=show_usage_info)
Info_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
Info_button.configure(font=("Times",9))
Info_button.bind(show_usage_info)

# List of TOP 20 passwords
def show():
    dropMenu.tk_popup(*dropMenu.winfo_pointerxy())

options = [
    "12345", "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "1234567",
    "1234567890",
    "qwerty",
    "password1",
    "123123",
    "111111",
    "123456a",
    "admin",
    "1234",
    "123456aA",
    "abc123",
    "password123",
    "password1234",
    "qwerty123",
    "root"
]



# Create the drop-down menu
dropMenu = tk.Menu(window, tearoff=0)
for option in options:
    dropMenu.add_command(label=option, command=lambda option=option:"")

# Create the button
list_button = tk.Button(window, text="Display Top 20+ Most Commonly Used Passwords to Avoid ! ☰ ", cursor="hand2", command=show)
list_button.place()

# Create a Label widget with a clickable link
link_label = tk.Label(window, text="Learn more 👉 www.saidsecurity.com", fg="Blue",cursor="hand2")
#About_me = tk.Button(window, text="About" ,fg="Blue", bg=None)
link_label.bind("<Button-1>", open_link)
link_label.configure(font=("Times", 14))
button3_pwned.bind("<Button-1>", open_link2)


# Bind the function to the button widget
button1.config(command=checkPassword)

# Arrange the widgets with the grid geometry manager
# Place the widgets in the center of the window
label1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
label1.configure(bg=None,  font=("Times", 20))
entry1.place(relx=0.5, rely=0.37, anchor=tk.CENTER)
entry1.configure(font=("New Times Roman", 19))
label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
label2.configure(font=("Times", 17))
label3.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
label3.configure(fg="black", font=("Verdana", 15))
button1.place(relx=0.7, rely=0.37, anchor=tk.CENTER)
button1.configure(font=("New Times Roman", 13))
button2_clear.place(relx=0.5, rely=0.80, anchor=tk.CENTER)
button2_clear.configure(font=("New Times Roman", 13))
button3_pwned.place(relx=0.5, rely=0.87, anchor=tk.CENTER)
button3_pwned.configure(font=("Times New Roman",11))
#About_me.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
link_label.place(x=7, y=7)
list_button.place(x=5, y=45)
list_button.configure(font=("New Times Roman",10))
# Main
window.mainloop()


