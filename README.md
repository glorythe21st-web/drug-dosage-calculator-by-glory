# 💊 Drug Dosage Calculator

A simple, interactive Python tool that calculates drug dosages based on patient weight and drug-specific dosage guidelines. Designed for nurses, pharmacology students, and health professionals.

# 🚀 Features

- ✅ Calculates total drug dose in mg based on patient weight (kg)
- ✅ Converts mg to mL using drug concentration (optional)
- ✅ Includes standard drug dosage references
- ✅ Supports multiple patients in one session
- ✅ Input validation and error handling

# 📦 How It Works

1. Enter the drug name
2. If listed, it uses the standard dosage (mg/kg)
3. Enter patient weight (kg)
4. Optionally, convert total mg to volume (mL)
5. Repeat or exit

---

# 🧪 Example Usage

```bash
$ python dosage_calculator.py

Enter drug name (or type 'list' to see options): paracetamol
✔ Using standard dose for paracetamol: 15 mg/kg
Enter patient weight (kg): 45
💉 Total dosage of paracetamol: 675.00 mg
Convert mg to mL? (yes/no): yes
Enter drug strength (mg): 250
Enter volume it comes in (mL): 5
💧 Volume to administer: 13.50 mL
````

---

# 🧠 Drug Reference Table

| Drug Name   | Dose (mg/kg) |
| ----------- | ------------ |
| Paracetamol | 15           |
| Ibuprofen   | 10           |
| Amoxicillin | 20           |

> You can add more drugs in the `DRUG_GUIDELINES` dictionary inside the code.

---

# 🔧 Installation

1. Clone the repo:

```bash
git clone https://github.com/glorythe21st-web/drug-dosage-calculator-by-glory.git
cd drug-dosage-calculator-by-glory
```

2. Run the calculator:

```bash
python dosage_calculator.py
```

---

# 📁 File Structure

```
drug-dosage-calculator/
├── dosage_calculator.py   # Main program logic
├── README.md              # Project documentation
└── .gitignore             # Git exclusions
```

---

# 📌 Future Enhancements

* Web-based UI (Flask or Streamlit)
* Mobile version (Kivy or React Native)
* Export dosage reports as PDF
* Add drug interaction alerts
* Unit testing support

---

# 👨‍⚕️ Author

*Glory Joseph Mamani*
Pharmacology Enthusiast | Researcher | Open Source Learner
🔗 GitHub: [@glorythe21st-web](https://github.com/glorythe21st-web)

---

# 📜 License

This project is licensed under the MIT License.

---

## 🙌 Contributions

Pull requests, issues, and ideas are welcome!
Feel free to [open an issue](https://github.com/glorythe21st-web/drug-dosage-calculator-by-glory/issues) or fork the repo to improve the project.

```

---

Would you like help turning this into a live **web app** next? Or should we add **unit tests** first?
```
