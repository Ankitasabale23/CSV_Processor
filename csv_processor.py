import csv

INPUT_FILE = "employees.csv"
OUTPUT_FILE = "summary_report.txt"


def process_csv(filename):
    """Read CSV data and calculate useful statistics."""

    salaries = []
    departments = {}

    total_employees = 0
    valid_salary_count = 0
    invalid_salary_count = 0

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                total_employees += 1

                # Get department
                department = (row.get("Department") or "Unknown").strip()

                if department:
                    departments[department] = (
                        departments.get(department, 0) + 1
                    )

                # Get and validate salary
                salary_text = (row.get("Salary") or "").strip()

                try:
                    salary = float(salary_text)
                    salaries.append(salary)
                    valid_salary_count += 1

                except (ValueError, TypeError):
                    invalid_salary_count += 1

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    # Calculate salary statistics
    if salaries:
        total_salary = sum(salaries)
        average_salary = total_salary / len(salaries)
        highest_salary = max(salaries)
        lowest_salary = min(salaries)
    else:
        total_salary = 0
        average_salary = 0
        highest_salary = 0
        lowest_salary = 0

    return {
        "total_employees": total_employees,
        "valid_salary_count": valid_salary_count,
        "invalid_salary_count": invalid_salary_count,
        "total_salary": total_salary,
        "average_salary": average_salary,
        "highest_salary": highest_salary,
        "lowest_salary": lowest_salary,
        "department_counts": departments
    }


def create_report(summary, filename):
    """Create a text summary report."""

    with open(filename, mode="w", encoding="utf-8") as file:

        file.write("CSV DATA PROCESSING SUMMARY\n")
        file.write("=" * 40 + "\n")

        file.write(
            f"Total employees: "
            f"{summary['total_employees']}\n"
        )

        file.write(
            f"Valid salary records: "
            f"{summary['valid_salary_count']}\n"
        )

        file.write(
            f"Invalid/missing salary records: "
            f"{summary['invalid_salary_count']}\n"
        )

        file.write(
            f"Total salary: "
            f"Rs. {summary['total_salary']:,.2f}\n"
        )

        file.write(
            f"Average salary: "
            f"Rs. {summary['average_salary']:,.2f}\n"
        )

        file.write(
            f"Highest salary: "
            f"Rs. {summary['highest_salary']:,.2f}\n"
        )

        file.write(
            f"Lowest salary: "
            f"Rs. {summary['lowest_salary']:,.2f}\n"
        )

        file.write("\nEMPLOYEE COUNT BY DEPARTMENT\n")
        file.write("-" * 40 + "\n")

        for department, count in sorted(
            summary["department_counts"].items()
        ):
            file.write(f"{department}: {count}\n")


# Main program
if __name__ == "__main__":

    summary = process_csv(INPUT_FILE)

    if summary:
        create_report(summary, OUTPUT_FILE)

        print("CSV processing completed successfully.")
        print(f"Summary report saved to: {OUTPUT_FILE}")