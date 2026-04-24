# Smart Calculator

import tkinter as tk
from PIL import Image, ImageTk

# Function to calculate
def calculate():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = x + y
        elif op == "-":
            result = x - y
        elif op == "*":
            result = x * y
        elif op == "/":
            if y == 0:
                result_label.config(text="Error: Cannot divide by zero")
                return
            result = x / y
        elif op == "**":
            result = x ** y
        elif op == "%":
            if y == 0:
                result_label.config(text="Error: Cannot modulo by zero")
                return
            result = x % y
        else:
            result_label.config(text="Invalid operation")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Error: Enter valid numbers")

# GUI Setup
root = tk.Tk()
root.title("Smart Calculator")
root.geometry("1920x1080")
Font= ("Lucida Handwriting",40, "bold") 

bg_image = Image.open(r"C:\Users\welcome\Downloads\download (1).jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Keep a reference to the image so it doesn't disappear
bg_label.image = bg_photo 

# 2. Place it at the top
title_label = tk.Label(root, text="Smart Calculator", font=Font, fg="black")
title_label.pack(pady=20)

# Input fields
tk.Label(root, text="Enter the First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter the Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()
# Operation selection
tk.Label(root, text="Operation (+, -, *, /, **, %)").pack()
operation = tk.StringVar()
op_entry = tk.Entry(root, textvariable=operation)
op_entry.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result will appear here")
result_label.pack()

root.mainloop()
