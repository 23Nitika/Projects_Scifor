import tkinter as tk
def submit_form():
    name = myentry_name.get()
    age = myentry_age.get()
    gender = gender_var.get()
    address = textbox_address.get("1.0", "end-1c")
    email = myentry_email.get()
    contact_no = myentry_contact.get()
    country = myentry_country.get()
    state = myentry_state.get()
    diseases = [disease.get() for disease in disease_vars]

    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Address:", address)
    print("Email:", email)
    print("Contact No:", contact_no)
    print("Country:", country)
    print("State:", state)
    print("Diseases:", diseases)

window = tk.Tk()
window.geometry("800x600")
window.title("Covid Vaccination Registration Form")

# Header
header_label = tk.Label(window, text="Covid Vaccination Registration Form", font=('Arial', 20, 'bold'), pady=10, bg='#FFB6C1', fg='white')
header_label.grid(row=0, column=0, columnspan=2, sticky="ew")

# Left Side
left_frame = tk.Frame(window, bg='#ecf0f1')
left_frame.grid(row=1, column=0, padx=20, pady=20, sticky="ne")

label_name = tk.Label(left_frame, text="Name of Visitor", font=('Arial', 14), bg='#ecf0f1', fg='#2c3e50')
label_name.grid(row=0, column=0, sticky=tk.W)

label_age = tk.Label(left_frame, text="Age of Visitor", font=('Arial', 14), bg='#ecf0f1', fg='#2c3e50')
label_age.grid(row=1, column=0, sticky=tk.W, pady=5)

label_gender = tk.Label(left_frame, text="Gender", font=('Arial', 14), bg='#ecf0f1', fg='#2c3e50')
label_gender.grid(row=3, column=0,sticky=tk.W, pady=7)

label_address = tk.Label(left_frame, text="Address", font=('Arial', 14), bg='#ecf0f1', fg='#2c3e50')
label_address.grid(row=4, column=0,sticky=tk.W, pady=(5,60))

label_email = tk.Label(left_frame, text="Email ID", font=('Arial', 14), bg='#ecf0f1', fg='#2c3e50')
label_email.grid(row=5, column=0,sticky=tk.W,pady=5)

label_contact = tk.Label(left_frame, text="Contact No.", font=('Arial', 14), bg='#ecf0f1', fg='#2c3e50')
label_contact.grid(row=6, column=0,sticky=tk.W,pady=5)

label_country = tk.Label(left_frame, text="Country", font=('Arial', 14), bg='#ecf0f1', fg='#2c3e50')
label_country.grid(row=7, column=0,sticky=tk.W,pady=3)

label_state = tk.Label(left_frame, text="State", font=('Arial', 14), bg='#ecf0f1', fg='#2c3e50')
label_state.grid(row=8, column=0,sticky=tk.W,pady=5)

label_disease = tk.Label(left_frame, text="Select Disease (if any)", font=('Arial', 14), bg='#ecf0f1', fg='#2c3e50')
label_disease.grid(row=9, column=0,sticky=tk.W,pady=5)

# Right Side
right_frame = tk.Frame(window, bg='#ecf0f1')
right_frame.grid(row=1, column=1, padx=20, pady=20, sticky="ne")

buttonframe = tk.Frame(right_frame)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=2)
buttonframe.columnconfigure(2, weight=3)

myentry_name = tk.Entry(right_frame, font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
myentry_name.grid(row=0, column=1, padx=10, pady=5, sticky="nw")

myentry_age = tk.Entry(right_frame, font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
myentry_age.grid(row=1, column=1, padx=10, pady=5, sticky="nw")

gender_var = tk.StringVar()
gender_var.set("Male")
gender_radio_male = tk.Radiobutton(right_frame, text="Male", variable=gender_var, value="Male", font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
gender_radio_female = tk.Radiobutton(right_frame, text="Female", variable=gender_var, value="Female", font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
gender_radio_male.grid(row=2, column=1, sticky="nw", padx=(5, 5), pady=5)
gender_radio_female.grid(row=2, column=1, padx=(5, 5), pady=5)

textbox_address = tk.Text(right_frame, height=3, font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
textbox_address.grid(row=4, column=1, padx=10, pady=5, sticky="nw")

myentry_email = tk.Entry(right_frame, font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
myentry_email.grid(row=5, column=1, padx=10, pady=5, sticky="nw")

myentry_contact = tk.Entry(right_frame, font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
myentry_contact.grid(row=6, column=1, padx=10, pady=5, sticky="nw")

myentry_country = tk.Entry(right_frame, font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
myentry_country.grid(row=7, column=1, padx=10, pady=5, sticky="nw")

myentry_state = tk.Entry(right_frame, font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
myentry_state.grid(row=8, column=1, padx=10, pady=5, sticky="nw")

disease_vars = [tk.IntVar() for _ in range(4)]
disease_checkboxes = [
    tk.Checkbutton(right_frame, text=disease, variable=disease_var, font=('Arial', 14), bg='#ecf0f1', fg='#34495e')
    for disease, disease_var in zip(["Cold", "Cough", "Fever", "Headache"], disease_vars)
]
for idx, checkbox in enumerate(disease_checkboxes):
    checkbox.grid(row=9 + idx, column=1, sticky="nw", padx=10, pady=5)

# Submit Button
submit_button = tk.Button(window, text="Submit", command=submit_form, font=('Arial', 16), bg='#2ecc71', fg='white', padx=10, pady=5)
submit_button.grid(row=10, column=0, columnspan=2, pady=20)

window.mainloop()