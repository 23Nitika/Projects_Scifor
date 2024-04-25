class Patient:
    def __init__(self, id, name, disease, doctor):
        self.id = id
        self.name = name
        self.disease = disease
        self.doctor = doctor

class Hospital:
    def __init__(self):
        self.patients = []
    
    def admit_patients(self, id, name, disease, doctor):
        self.patients.append(Patient(id, name, disease, doctor))
        print("Patient admitted successfully.")
    
    def get_patient(self, key, value):
        found_patients = []
        for patient in self.patients:
            if getattr(patient, key) == value:
                found_patients.append(patient)
        return found_patients
    
    def show_all_patients(self):
        print("All Patients: ")
        for patient in self.patients:
            print("ID: ", patient.id)
            print("Name:", patient.name)
            print("Disease:", patient.disease)
            print("Doctor Incharge:",patient.doctor)
    
    def discharge_patient(self, key, value):
        found_patients = self.get_patient(key, value)
        if not found_patients:
            print("Patient not found")
            return
        for patient in found_patients:
            self.patients.remove(patient)
            print("Patient discharged successfully.")

def main():
    hospital = Hospital()
    while True:
        print("\nOptions:")
        print("1. Admit a new patient")
        print("2. Get a patient")
        print("3. Show all patient")
        print("4. Discharge a patient")
        print("5. Exit")
        choice = input("Enter yur choice: ")

        if choice == '1':
            id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            disease = input("Enter patient disease: ")
            doctor = input("Enter doctor incharge: ")
            hospital.admit_patients(id, name, disease, doctor)
        
        elif choice == '2':
            search_key = input("Enter search key(id/name/disease/doctor): ").lower()
            search_value = input("Enter search value: ")
            patients = hospital.get_patient(search_key, search_value)
            if patients:
                print("Found patient(s):")
                for patient in patients:
                    print("ID:",patient.id)
                    print("Name:",patient.name)
                    print("Disease:",patient.disease)
                    print("Doctor Incharge:",patient.doctor)
            else:
                print("Patient not found.")

        elif choice == '3':
            hospital.show_all_patients()

        elif choice == '4':
            search_key = input("Enter search key (id/name/disease/doctor): ").lower()
            search_value = input("Enter search value: ")
            hospital.discharge_patient(search_key, search_value)

        elif choice == '5':
            print("Exited program")
            break
        else:
            print("Invalid choice. Please choose again. ")

if __name__ == "__main__":
    main()
