import csv
import os
import time

def attendance_rule(attendance):
    if attendance >= 75:
        return "✅ Eligible to take exams"
    else:
        return "❌ Not eligible to take exams"

def grading_rule(grade):
    if grade >= 90:
        return "🏆 Excellent"
    elif grade >= 75:
        return "✅ Passed"
    else:
        return "❌ Failed"

def login_rule(has_account, correct_password):
    if has_account and correct_password:
        return "🔓 Login successful"
    elif has_account and not correct_password:
        return "❌ Incorrect password"
    else:
        return "⚠️ No account found"

def bonus_rule(participation, projects_submitted):
    if participation and projects_submitted >= 2:
        return "🎉 Bonus points awarded"
    elif participation:
        return "✨ Partial bonus"
    else:
        return "❌ No bonus points"

def library_rule(valid_id):
    if valid_id:
        return "📚 Allowed to borrow books"
    else:
        return "🚫 Borrowing not allowed"


def main():
    print("=" * 50)
    print("🎓 MINI EXPERT SYSTEM FOR STUDENT EVALUATION 🎓".center(50))
    print("=" * 50)
    print("\nThis system will evaluate student conditions based on rules.")
    print("Results will automatically be saved to logic_results.csv\n")
    print("-" * 50)

    students = []
    num_students = int(input("👩‍🎓 How many students do you want to test? (e.g., 3): "))

    for i in range(num_students):
        print(f"\n🧍 Student {i+1}")
        print("-" * 30)
        name = input("Enter student name: ").strip()
        attendance = int(input("Enter attendance percentage (0–100): "))
        grade = int(input("Enter grade (0–100): "))
        has_account = input("Does the student have an account? (y/n): ").lower() == 'y'
        correct_password = input("Entered correct password? (y/n): ").lower() == 'y'
        participation = input("Participated in class activities? (y/n): ").lower() == 'y'
        projects_submitted = int(input("Number of projects submitted: "))
        valid_id = input("Has a valid library ID? (y/n): ").lower() == 'y'


        result_attendance = attendance_rule(attendance)
        result_grading = grading_rule(grade)
        result_login = login_rule(has_account, correct_password)
        result_bonus = bonus_rule(participation, projects_submitted)
        result_library = library_rule(valid_id)

        print("\n📊 Evaluation Results:")
        print(f"Attendance Rule: {result_attendance}")
        print(f"Grading Rule: {result_grading}")
        print(f"Login System Rule: {result_login}")
        print(f"Bonus Points Rule: {result_bonus}")
        print(f"Library Rule: {result_library}")

        students.append({
            "Name": name,
            "Attendance Rule": result_attendance,
            "Grading Rule": result_grading,
            "Login Rule": result_login,
            "Bonus Rule": result_bonus,
            "Library Rule": result_library
        })

        print("-" * 50)
        time.sleep(1)


    file_exists = os.path.isfile("logic_results.csv")
    with open("logic_results.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=students[0].keys())
        if not file_exists:
            writer.writeheader()
        writer.writerows(students)

    print("\n✅ All results successfully saved to 'logic_results.csv'")
    print("📂 You can open this file to view all recorded evaluations.")
    print("\nThank you for using the Mini Expert System!")
    print("=" * 50)


if __name__ == "__main__":
    main()
