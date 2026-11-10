# MedCase
MedCase is a python-based case learning simulator designed for medical students.
The application allows students to explore fictional clinical cases across five medical specialties, answer multiple-choice questions, receive immediate feedback, and track their scores.
MedCase includes cardiovascular, neurological, respiratory, gastrointestinal, and endocrinological cases. Students can select a specialty or a random case.
The project was developed as a final project for Harvard's CS50 introduction to Programming with Python(CS50P).

## Features
- Five clinical cases across different medical specialties.
- Interactive multiple-choice questions with immediate feedback.
- Automatic score calculation for each completed case.
- Random case selection for varied learning experiences.
- Student ID validation using regular expressions.
- Patient information management using JSON files.
- Object-oriented patient representation using a python class.
- Student performance tracking using CSV files.
- Input validation and error  handling for invalid answers.
- Automated unit testing using pytest.

## How to Run

### Requirements

- Python 3
- pytest (for running the automated tests)

### Running the Application

1. Download or clone the repository.
2. Open a terminal in the 'medcase' directory.
3. Run the following command:

    python project.py

4. Enter a student ID, such as 'MED123'.
5. Select a medical specialty (1-5) or chose option 6 for a random case.
6. Read the patient's information and answer the two clinical questions.
7. View your score. The result will be saved automatically in 'results.csv'.

### Running the Tests

To run the automated tests, use:

    pytest test_project.py
## Project Structure

MedCase consists of the following files.

- 'project.py': The main Python application. It handles the user interface, specialty selection, clinical questions, answer validation, scoring, and saving results.It also contains the patient class.
- 'cases.json': Stores clinical case information, including patient age, sex, chief complaint, symptom duration, and associated symptoms .
- 'test_project.py': contains automated unit tests for the project's functions and Patient class.
- 'results.csv': Stores completed case results, including student IDs, selected specialties, and scores.
- 'README.md': Provides documentation, installation instructions, project features, and design explanations

## Design Choices

Medcase was designed as a terminal-based application to keep the user interface simple and focus on clinical reasoning and python programming concepts.

### JSON for Clinical Cases

I choose JSON to store patient information separately from the python code.This makes it easier to organize and update clinical cases without modifying the main application.

### Object-Oriented Programming

I created a Patient class to represent each patient as an object with attributes such as age, sex, chief complaint, duration, and symptoms.

### CSV for score Tracking

I used CSV files to store student IDs, selected specialties, and scores. This allows results to remain available after the application is closed.

### Regular Expressions

I used regular expressions to validate student IDs. Each ID must follow the format MED followed by three digits.

### Random Case Selection

I added a random case selection option to allow students to practice different clinical scenarios without selecting a specialty manually.

### Unit Testing

I used pytest to test important functions and the patient class. Automated testing helps verify that different parts of the application behave as expected.

