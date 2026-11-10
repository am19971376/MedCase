from project import calculate_score, choose_specialty, get_case
from project import validate_student_id
from project import Patient
def test_calculate_score():
    assert calculate_score(True, True) == 2
    assert calculate_score(True, False) == 1
    assert calculate_score(False, False) == 0
def test_choose_specialty():
    assert choose_specialty("1") == "Cardiovascular"
    assert choose_specialty("2") == "Neurology"
    assert choose_specialty("5") == "Endocrinology"
    assert choose_specialty("9") is None
def test_get_case():
    assert get_case("Cardiovascular") == "Chest Pain"
    assert get_case("Neurology") == "Headache"
    assert get_case("Respiratory") == "Shortness of Breath"
    assert get_case("Gastrointestinal") == "Abdominal Pain"
    assert get_case("Endocrinology") == "Hypoglycemia"
def test_validate_student_id():
    assert validate_student_id("MED123") == True
    assert validate_student_id("MED007") == True
    assert validate_student_id("MED12") == False
    assert validate_student_id("123MED") == False
def test_patient():
    patient = Patient(
        28,
        "Female",
        "Headache",
        "6 hours",
        ["Nausea", "Sensitivity to light"]
    )

    assert patient.age == 28
    assert patient.sex == "Female"
    assert patient.case == "Headache"
    assert patient.duration == "6 hours"
    assert patient.symptoms == ["Nausea", "Sensitivity to light"]
