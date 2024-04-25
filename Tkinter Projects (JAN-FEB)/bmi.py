import tkinter as tk
from tkinter import ttk
from datetime import date

def update_height_label(value):
    height_label.config(text=f"Height: {float(value):.2f} {height_unit_var.get()}")

def update_weight_label(value):
    weight_label.config(text=f"Weight: {float(value):.2f} {weight_unit_var.get()}")

def update_height_scale(unit):
    if unit == "cm":
        height_scale.config(from_=100, to=250)
    elif unit == "inches":
        height_scale.config(from_=39.37, to=98.42)  # 100 cm to inches, 250 cm to inches

def calculate_bmi():
    height = height_scale.get()
    weight = weight_scale.get()
    height_unit = height_unit_var.get()
    weight_unit = weight_unit_var.get()

    print("Height:", height, height_unit)
    print("Weight:", weight, weight_unit)

    if height_unit == "inches":
        height /= 39.37
    if weight_unit == "pounds":
        weight /= 2.205

    bmi = weight / (height ** 2)
    bmi_result.set(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        result_label.config(text="Underweight", foreground="red")
    elif 18.5 <= bmi < 25:
        result_label.config(text="Normal", foreground="green")
    else:
        result_label.config(text="Overweight", foreground="red")

    with open("bmi_logs.txt", "a") as file:
        file.write(f"Date: {date.today()}, Height: {height}, Weight: {weight}, BMI: {bmi}\n")


root = tk.Tk()
root.title("BMI Calculator")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0)

height_label = ttk.Label(main_frame, text="Height: 0.00 cm")
height_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
height_scale = ttk.Scale(main_frame, from_=100, to=250, length=200, orient="horizontal", command=update_height_label)
height_scale.grid(row=0, column=1, padx=10, pady=5)
height_unit_var = tk.StringVar()
height_unit_combobox = ttk.Combobox(main_frame, values=["cm", "inches"], textvariable=height_unit_var, state="readonly", 
                                    postcommand=lambda: update_height_scale(height_unit_var.get()))
height_unit_combobox.current(0)
height_unit_combobox.grid(row=0, column=2, padx=10, pady=5)

weight_label = ttk.Label(main_frame, text="Weight: 0.00 kg")
weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
weight_scale = ttk.Scale(main_frame, from_=20, to=200, length=200, orient="horizontal", command=update_weight_label)
weight_scale.grid(row=1, column=1, padx=10, pady=5)
weight_unit_var = tk.StringVar()
weight_unit_combobox = ttk.Combobox(main_frame, values=["kg", "pounds"], textvariable=weight_unit_var, state="readonly")
weight_unit_combobox.current(0)
weight_unit_combobox.grid(row=1, column=2, padx=10, pady=5)

calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, column=1, pady=10)

bmi_result = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=bmi_result, font=("Arial", 12, "bold"))
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
