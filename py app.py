"""
Student Result Management Terminal System (SRMTS)
Author:Adaeze
Description:
A command-line application to manage student results for School:
- Add student results with validation
- View all results in a formatted table
- Search for students by name
- Display class summary with statistics and grade distribution
This program demonstrates structured programming concepts, including:
- Use of functions for modularity
- Decision structures for grade calculation
- Loops for input validation and data processing
- In-memory data storage using lists and dictionaries
"""

# ---------------------- CONSTANTS ----------------------
PASS_MARK = 50
MAX_MARK  = 100
GRADE_A   = 70
GRADE_B   = 60
GRADE_C   = 50

# In-memory student records (list of dicts)
students = []


# ===================== FUNCTIONS =======================

def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("   STUDENT RESULT MANAGEMENT TERMINAL SYSTEM")
    print("        Limkokwing University - Sierra Leone")
    print("=" * 50)
    print("  1. Add Student Result")
    print("  2. View All Results")
    print("  3. Search Student by ID")
    print("  4. Display Class Summary")
    print("  5. Exit")
    print("=" * 50)


def calculate_grade(average):
    """
    Determine letter grade and remark based on average score.
    Uses decision structures (if/elif/else).
    """
    if average >= GRADE_A:
        grade  = "A"
        remark = "Distinction"
    elif average >= GRADE_B:
        grade  = "B"
        remark = "Merit"
    elif average >= GRADE_C:
        grade  = "C"
        remark = "Pass"
    else:
        grade  = "F"
        remark = "Fail"
    return grade, remark


def get_valid_score(subject):
    """
    Prompt user for a score and validate it is between 0 and MAX_MARK.
    Uses a loop to keep asking until valid input is entered.
    """
    while True:
        try:
            score = float(input(f"   Enter score for {subject}: "))
            if 0 <= score <= MAX_MARK:
                return score
            else:
                print(f"   [!] Score must be between 0 and {MAX_MARK}. Try again.")
        except ValueError:
            print("   [!] Invalid input. Please enter a number.")


def add_student():
    """Collect student details and scores, then store the record."""
    print("\n--- ADD STUDENT RESULT ---")
    name       = input("   Enter student name    : ").strip()
    student_id = int(input("   Enter student ID      : ").strip())

    if not name or not student_id:
        print("   [!] Name and ID cannot be empty.")
        return

    # Check for duplicate ID
    for s in students:
        if s["id"] == student_id:
            print(f"   [!] Student ID '{student_id}' already exists.")
            return

    subjects = ["Math", "English", "Science", "ICT", "Social Studies"]
    scores   = {}

    print(f"\n   Enter scores for {name} (0 - {MAX_MARK}):")
    for subject in subjects:
        scores[subject] = get_valid_score(subject)

    # Calculate average
    total   = sum(scores.values())
    average = total / len(scores)
    grade, remark = calculate_grade(average)

    # Build record
    record = {
        "name"   : name,
        "id"     : student_id,
        "scores" : scores,
        "total"  : total,
        "average": round(average, 2),
        "grade"  : grade,
        "remark" : remark
    }
    students.append(record)
    print(f"\n   [✓] Record saved! {name} scored an average of {average:.2f} — Grade {grade} ({remark}).")


def view_all_results():
    """Display a formatted table of all student results."""
    if not students:
        print("\n   [!] No student records found.")
        return

    print("\n--- ALL STUDENT RESULTS ---")
    print(f"{'No.':<4} {'Name':<20} {'ID':<12} {'Total':<8} {'Average':<10} {'Grade':<7} {'Remark'}")
    print("-" * 70)

    for i, s in enumerate(students, start=1):
        print(f"{i:<4} {s['name']:<20} {s['id']:<12} {s['total']:<8.1f} {s['average']:<10.2f} {s['grade']:<7} {s['remark']}")


def search_student():
    """Search for a student by name and display their full result."""
    if not students:
        print("\n   [!] No records to search.")
        return

    query  = int(input("\n   Enter student ID to search: "))
    found  = [s for s in students if query == s["id"]]

    if not found:
        print(f"   [!] No student found matching '{query}'.")
        return

    for s in found:
        print("\n" + "-" * 40)
        print(f"   Name    : {s['name']}")
        print(f"   ID      : {s['id']}")
        print(f"   Scores  :")
        for subject, score in s["scores"].items():
            status = "PASS" if score >= PASS_MARK else "FAIL"
            print(f"      {subject:<20}: {score:.1f}  [{status}]")
        print(f"   Total   : {s['total']:.1f}")
        print(f"   Average : {s['average']:.2f}")
        print(f"   Grade   : {s['grade']}  ({s['remark']})")
        print("-" * 40)


def class_summary():
    """Calculate and display class-wide statistics."""
    if not students:
        print("\n   [!] No records available for summary.")
        return

    total_students = len(students)
    passed  = sum(1 for s in students if s["remark"] != "Fail")
    failed  = total_students - passed
    all_avg = [s["average"] for s in students]
    highest = max(all_avg)
    lowest  = min(all_avg)
    class_avg = sum(all_avg) / total_students

    top_student = max(students, key=lambda s: s["average"])

    print("\n--- CLASS SUMMARY ---")
    print(f"   Total Students  : {total_students}")
    print(f"   Passed          : {passed}")
    print(f"   Failed          : {failed}")
    print(f"   Class Average   : {class_avg:.2f}%")
    print(f"   Highest Average : {highest:.2f}%")
    print(f"   Lowest Average  : {lowest:.2f}%")
    print(f"   Top Student     : {top_student['name']} ({top_student['average']:.2f}%)")

    # Grade distribution using a loop
    print("\n   Grade Distribution:")
    for g in ["A", "B", "C", "F"]:
        count = sum(1 for s in students if s["grade"] == g)
        bar   = "#" * count
        print(f"      Grade {g} : {bar} ({count})")


# ======================== MAIN =========================

def main():
    """Main program loop — entry point of the application."""
    print("\n   Welcome to SRMTS — Powered by Structured Python")
    print("   SDG 4: Quality Education | Limkokwing University SL")

    while True:
        display_menu()
        choice = input("   Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_results()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_summary()
        elif choice == "5":
            print("\n   Thank you for using SRMTS. Goodbye!\n")
            break
        else:
            print("   [!] Invalid choice. Please enter a number between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()
