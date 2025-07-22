import csv

# Predefined dosage guidelines (mg/kg)
DRUG_GUIDELINES = {
    "amoxicillin": 20,
    "paracetamol": 15,
    "ibuprofen": 10,
    "ceftriaxone": 50
}

def calculate_dosage(weight_kg, dose_per_kg):
    return weight_kg * dose_per_kg

def convert_mg_to_ml(dose_mg, strength_mg, volume_ml):
    return (dose_mg / strength_mg) * volume_ml

def main():
    print("💊 Drug Dosage Calculator 💊\n")

    while True:
        # Drug input
        drug_name = input("Enter drug name (or type 'list' to view options): ").strip().lower()

        if drug_name == "list":
            print("Available drugs:", ", ".join(DRUG_GUIDELINES.keys()))
            continue

        if drug_name in DRUG_GUIDELINES:
            dose_per_kg = DRUG_GUIDELINES[drug_name]
            print(f"✔ Using standard dose for {drug_name}: {dose_per_kg} mg/kg")
        else:
            try:
                dose_per_kg = float(input(f"Enter dose per kg for {drug_name} (mg/kg): "))
            except ValueError:
                print("❌ Invalid input. Try again.")
                continue

        try:
            weight = float(input("Enter patient weight (kg): "))
        except ValueError:
            print("❌ Invalid weight. Try again.")
            continue

        total_dose_mg = calculate_dosage(weight, dose_per_kg)
        print(f"🧮 Total dosage of {drug_name}: {total_dose_mg:.2f} mg")

        convert = input("Convert mg to mL? (yes/no): ").strip().lower()
        if convert == "yes":
            try:
                strength_mg = float(input("Enter drug strength (mg): "))
                volume_ml = float(input("Enter volume it comes in (mL): "))
                dose_ml = convert_mg_to_ml(total_dose_mg, strength_mg, volume_ml)
                print(f"💉 Volume to administer: {dose_ml:.2f} mL")
            except ValueError:
                print("❌ Invalid conversion values. Skipping.")

        # Ask to process another patient
        again = input("\nCalculate for another patient? (yes/no): ").strip().lower()
        if again != "yes":
            print("✅ Finished. Stay safe!")
            break

if __name__ == "__main__":
    main()
