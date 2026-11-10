import json
import csv
import random
import re
class Patient:
    def __init__(self, age, sex, case, duration, symptoms):
        self.age = age
        self.sex = sex
        self.case = case
        self.duration = duration
        self.symptoms = symptoms
def main():
    cases_data = load_cases()
    student_id = get_student_id()
    print(f"Welcome, {student_id}!")
    print("Welcome to MedCase!")
    print("Clinical Case Learning Simulator")
    print()

    print("Choose a medical specialty:")
    print("1. Cardiovascular")
    print("2. Neurology")
    print("3. Respiratory")
    print("4. Gastrointestinal")
    print("5. Endocrinology")
    print("6. Random Case")

    choice = input("Enter specialty number: ")
    specialty = choose_specialty(choice)
    if choice == "6":
        specialty = random_case()
        print("A random specialty has been selected!")
    if specialty is not None:
        print(f"You selected {specialty}")
        case = get_case(specialty)
        print(f"Clinical Case: {case}")

        patient_data = cases_data[specialty]
        patient = Patient(
            patient_data["age"],
            patient_data["sex"],
            patient_data["case"],
            patient_data["duration"],
            patient_data["symptoms"],
        )
        show_patient(patient)
        if case == "Chest Pain":
            answer = ask_question()
            result = check_answer(answer, "1")
            show_feedback(result)

            diagnosis = ask_diagnosis()
            diagnosis_result = check_answer(diagnosis, "1")

            if diagnosis_result:
                print("Correct! Acute Coronary Syndrome must be considered urgently.")
            else:
                print("Incorrect! Acute Coronary Syndrome is most likely to be the answer.")
            score = calculate_score(result, diagnosis_result)
            print(f"Your score: {score}/2")
            save_result(student_id, specialty, score)
        if case == "Headache":
            answer = ask_headache_question()
            result = check_answer(answer, "1")
            headache_feedback(result)

            diagnosis = ask_headache_diagnosis()
            diagnosis_result = check_answer(diagnosis, "1")

            if diagnosis_result:
                print("Correct! Migraine is consistent with the symptoms.")
            else:
                print("Incorrect! Migraine is one possible diagnosis to consider.")

            score = calculate_score(result, diagnosis_result)
            print(f"Your score: {score}/2")
            save_result(student_id, specialty, score)
        if case == "Shortness of Breath":
            answer = ask_respiratory_question()
            result = check_answer(answer, "1")
            respiratory_feedback(result)
            diagnosis = ask_respiratory_diagnosis()
            diagnosis_result = check_answer(diagnosis, "2")

            if diagnosis_result:
                print("Correct! Pneumonia is a possible diagnosis.")
            else:
                print("Incorrect! Pneumonia should be considered.")

            score = calculate_score(result, diagnosis_result)
            print(f"Your score: {score}/2")
            save_result(student_id, specialty, score)
        if case == "Abdominal Pain":
            answer = ask_abdominal_question()
            result = check_answer(answer, "2")
            abdominal_feedback(result)

            diagnosis = ask_abdominal_diagnosis()
            diagnosis_result = check_answer(diagnosis, "2")

            if diagnosis_result:
                print("Correct! Acute appendicitis is a possib
                le diagnosis.")
            else:
                print("Incorrect! Acute appendicitis should be considered.")

            score = calculate_score(result, diagnosis_result)
            print(f"Your score: {score}/2")
            save_result(student_id, specialty, score)
        if case == "Hypoglycemia":
            answer = ask_endocrine_question()
            result = check_answer(answer, "2")
            endocrine_feedback(result)

            diagnosis = ask_endocrine_diagnosis()
            diagnosis_result = check_answer(diagnosis, "3")

            if diagnosis_result:
                print("Correct! Too much insulin can cause hypoglycemia.")
            else:
                print("Incorrect! Excess insulin is a possible cause of hypoglycemia.")

            score = calculate_score(result, diagnosis_result)
            print(f"Your score: {score}/2")
            save_result(student_id, specialty, score)
    else:
        print("Invalid specialty number")

def choose_specialty(choice):
    if choice == "1":
        return "Cardiovascular"
    elif choice == "2":
        return "Neurology"
    elif choice == "3":
        return "Respiratory"
    elif choice == "4":
        return "Gastrointestinal"
    elif choice == "5":
        return "Endocrinology"
    else:
        return None
def random_case():
    specialties = [
        "Cardiovascular",
        "Neurology",
        "Respiratory",
        "Gastrointestinal",
        "Endocrinology"
    ]

    return random.choice(specialties)
def get_case(specialty):
    cases = {
        "Cardiovascular": "Chest Pain",
        "Neurology": "Headache",
        "Respiratory": "Shortness of Breath",
        "Gastrointestinal": "Abdominal Pain",
        "Endocrinology": "Hypoglycemia",
    }

    return cases[specialty]
def show_patient(patient):
        print()
        print("Patient Information")
        print("-------------------")
        print(f"Age: {patient.age}")
        print(f"Sex: {patient.sex}")
        print(f"Chief Complaint: {patient.case}")
        print(f"Duration: {patient.duration}")
        print("Associated Symptoms:")

        for number, symptom in enumerate(patient.symptoms, start=1):
            print(f"{number}.{symptom}")

def ask_question():
    print()
    print("Question 1:")
    print("Which investigation should be performed immediately?")
    print("1. ECG")
    print("2. Urinanalysis(U/A) ")
    print("3. Blood tests")

    return get_valid_answer()
def ask_diagnosis():
    print()
    print("Question 2:")
    print("Which one is the most likely diagnosis?")
    print("1. Acute Coronary Syndrome(ACS)")
    print("2. Migraine ")
    print("3. Gastroenteritis")

    return get_valid_answer()
def ask_headache_question():
    print()
    print("Neurology - Question 1:")
    print("Which finding is a red flag in a patient with headache?")
    print("1. Sudden onset of the worst headache of their life")
    print("2. Mild headache after studying ")
    print("3. Headache relieved by rest")

    return get_valid_answer()
def ask_headache_diagnosis():
    print()
    print("Neurology - Question 2:")
    print("Which diagnosis is most consistent with these symptoms?")
    print("1. Migraine")
    print("2. Appendicitis")
    print("3. Pneumonia")

    return get_valid_answer()
def ask_respiratory_question():
    print()
    print("Respiratory - Question 1:")
    print("Which measurement is important in the initial assessment?")
    print("1. Oxygen saturation")
    print("2. Blood cholesterol")
    print("3. Visual acuity")

    return get_valid_answer()
def respiratory_feedback(result):
    if result:
        print("Correct!")
        print("Oxygen saturation is important in the initial assessment of a patient with shortness of breath.")
    else:
        print("Incorrect!")
        print("Oxygen saturation should be checked during the initial assessment of shortness of breath.")
def ask_respiratory_diagnosis():
    print()
    print("Respiratory - Question 2:")
    print("Which diagnosis should be considered?")
    print("1. Migraine")
    print("2. Pneumonia")
    print("3. Appendicitis")

    return get_valid_answer()
def ask_abdominal_question():
    print()
    print("Gastrointestinal - Question 1:")
    print("Which question is  more important in the initial history?")
    print("1. What caused the pain?")
    print("2. Where is the abdominal pain located?")
    print("3. When did the pain start?")

    return get_valid_answer()
def ask_abdominal_diagnosis():
    print()
    print("Gastrointestinal - Question 2:")
    print("Which diagnosis is most likely to be considered in this patient?")
    print("1. Heart Attack")
    print("2. Acute Appendicitis")
    print("3. Asthma Attack")

    return get_valid_answer()
def abdominal_feedback(result):
    if result:
        print("Correct!")
        print("The location of abdominal pain is important in identifying possible causes.")
    else:
        print("Incorrect!")
        print("Asking about the location of abdominal pain is an important part of taking a medical history.")


def headache_feedback(result):
    if result:
        print("Correct!")
        print("A sudden, severe headache is an important red flag.")
    else:
        print("Incorrect!")
        print("A sudden, severe headache may indicate a serious condition and requires urgent evaluation.")

def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return True
    else:
        return False
def calculate_score(result1, result2):
    score = int(result1) + int(result2)
    return score
def show_feedback(result):
    if result:
        print("Correct!")
        print("An ECG shold be done ASAP to detect alternations(especially ST elevations) in a patient with suspected acute coronary syndrome.")
    else:
        print("Incorrect!")
        print("An ECG is an important initial investigation for suspected acute coronary syndrome.")
def get_valid_answer():
    while True:
        try:
            answer = int(input("What is your answer? "))

            if answer in [1, 2, 3]:
                return str(answer)
            else:
                print("Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")
def ask_endocrine_question():
    print()
    print("Endocrinology - Question 1:")
    print("Which test should be performed immediately?")
    print("1. Thyroid test")
    print("2. Blood glucose")
    print("3. Liver function test")

    return get_valid_answer()
def ask_endocrine_diagnosis():
    print()
    print("Endocrinology - Question 2:")
    print("Which factor can cause hypoglycemia in a patient with diabetes?")
    print("1. Drinking water")
    print("2. Taking a short walk")
    print("3. Taking too much insulin")

    return get_valid_answer()

def endocrine_feedback(result):
    if result:
        print("Correct!")
        print("Checking blood glucose is important when hypoglycemia is suspected.")
    else:
        print("Incorrect!")
        print("Blood glucose should be checked promptly in a patient with suspected hypoglycemia.")
def load_cases():
    with open("cases.json", "r") as file:
        cases = json.load(file)

        return cases
def save_result(student_id, specialty, score):
        with open("results.csv", "a+", newline="") as file:
            writer = csv.writer(file)

            file.seek(0, 2)

            if file.tell() == 0:
                writer.writerow(["student_id", "specialty", "score"])

            writer.writerow([student_id, specialty, score])

def validate_student_id(student_id):
    if re.fullmatch(r"MED[0-9]{3}", student_id):
        return True
    else:
        return False
def get_student_id():
    while True:
        student_id = input("Enter your student ID (e.g. MED123): ").strip().upper()

        if validate_student_id(student_id):
            return student_id
        print("Invalid ID! Please use MED followed by 3 digits.")
if __name__ == "__main__":
    main()
