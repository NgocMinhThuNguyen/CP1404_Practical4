"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Get the data and display the subject details"""
    subjects = get_subjects()
    print(subjects)
    print_subjects(subjects)


def get_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()
    return subjects


def print_subjects(subjects):
    """Print subject details"""
    for subject in subjects:
        subject_code = subject[0]
        lecturer = subject[1]
        number_of_students = str(subject[2])
        print(f"{subject_code} is taught by {lecturer:.10} and has {number_of_students:>3} students")


main()
