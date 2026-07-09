# STUDENT MANAGEMENT SYSTEM

students = []

# function to add a student
def add_student(roll_no, name, marks1, marks2, marks3):
    new_student = {
        "roll_no": roll_no,
        "name": name,
        "marks": [marks1, marks2, marks3]
    }
    students.append(new_student)
    print(f"Added student: {name} (Roll No: {roll_no})")


# function to show all students
def show_students():
    print("\n----- ALL STUDENTS -----")
    if len(students) == 0:
        print("No students yet.")
        return

    for student in students:
        print(f"Roll No {student['roll_no']}: {student['name']} -> Marks: {student['marks']}")


# function to find student by roll number
def find_student_by_roll(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


# function to calculate total and average marks
def student_result(roll_no):
    student = find_student_by_roll(roll_no)

    if student is None:
        print("Student not found.")
        return

    total = sum(student["marks"])
    average = total / len(student["marks"])

    print(f"\n{student['name']}'s Result:")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")


# function to find the topper (highest average marks)
def find_topper():
    if len(students) == 0:
        print("No students yet.")
        return

    topper = students[0]
    highest_total = sum(topper["marks"])

    for student in students:
        total = sum(student["marks"])
        if total > highest_total:
            highest_total = total
            topper = student

    print(f"\nTopper: {topper['name']} (Roll No: {topper['roll_no']}) with total {highest_total} marks")


# function to delete a student
def delete_student(roll_no):
    student = find_student_by_roll(roll_no)

    if student is None:
        print("Student not found.")
        return

    students.remove(student)
    print(f"Deleted student with Roll No {roll_no}")


if __name__ == "__main__":
    add_student(1, "Aditya", 85, 90, 88)
    add_student(2, "Palak", 78, 82, 91)
    add_student(3, "Adi", 95, 89, 93)

    show_students()

    student_result(1)
    student_result(2)

    find_topper()

    delete_student(2)

    show_students()