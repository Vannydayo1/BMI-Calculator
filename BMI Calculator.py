import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Please enter valid positive values for weight and height.")
            return

        bmi = weight / (height / 100) ** 2
        result_label.config(text=f"Your BMI: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

# Create the main window
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("1280x720")  # Set window size
app.configure(bg="#ffe3ff")  # Set background color

# Define a custom font
custom_font = ("Arial", 20, "bold")

# Create and place widgets
label_weight = tk.Label(app, text="Enter weight (kg):", font=custom_font, bg="#ffe3ff")
label_weight.pack(pady=5)

entry_weight = tk.Entry(app, font=custom_font)
entry_weight.pack(pady=5)

label_height = tk.Label(app, text="Enter height (cm):", font=custom_font, bg="#ffe3ff")
label_height.pack(pady=5)

entry_height = tk.Entry(app, font=custom_font)
entry_height.pack(pady=5)

calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi, font=custom_font, bg="#ffe3ff")
calculate_button.pack(pady=10)

result_label = tk.Label(app, text="Your BMI: ", font=custom_font, bg="#ffe3ff")
result_label.pack(pady=5)

# Start the GUI application
app.mainloop()
