# Veda Technology - CSV Data Processor

## Python Programming Internship Task

### Project Title

**Build a CSV Data Processor**

---

## 1. Project Description

The program reads employee information from a CSV file and calculates useful statistics such as:

- Total number of employees
- Total salary
- Average salary
- Highest salary
- Lowest salary
- Number of employees in each department
- Number of valid and invalid salary records

The program also handles missing and invalid salary values without crashing.

---

## 2. Objective

The main objective of this task is to learn practical CSV processing using Python.

The project demonstrates:

- Reading CSV files
- Processing CSV data
- Performing calculations
- Handling missing data
- Handling invalid data
- Writing a summary report

---

## 3. Technologies Used

- Python 3
- CSV module
- File Handling
- Exception Handling

---

## 4. Project Files

The project contains the following files:

 text
pyyy/
│
├── csv_processor.py
├── employees.csv
├── summary_report.txt
└── README.md

5. Input CSV Dataset

The input file is employees.csv.
It contains the following columns:

Employee_ID
Name
Department
Salary

Example:
Employee_ID,Name,Department,Salary
101,Ankita,IT,45000
102,Rahul,HR,38000
103,Neha,IT,52000
104,Amit,Sales,41000
105,Priya,Sales,47000
106,Rohan,HR,
107,Sneha,IT,invalid
108,Kiran,Finance,60000

The dataset contains:
One missing salary value
One invalid salary value
These are included to demonstrate error handling.

6. How to Run the Program

Step 1: Install Python
Make sure Python 3 is installed.
Check the Python version:
python --version

Step 2: Open the Project Folder
The project folder should contain:
csv_processor.py
employees.csv
README.md

Step 3: Open Terminal
Open the terminal in the project folder.
For example:
cd "C:\Users\Admin\Desktop\pyyy"

Step 4: Run the Program
Execute:
python csv_processor.py
If Python is configured differently, you can also run:
py csv_processor.py

Step 5: Check the Output
After successful execution, the program creates:
summary_report.txt
The terminal will display:
CSV processing completed successfully.
Summary report saved to: summary_report.txt

7. Output
The program generates the following summary:
CSV DATA PROCESSING SUMMARY
========================================
Total employees: 8
Valid salary records: 6
Invalid/missing salary records: 2
Total salary: Rs. 283,000.00
Average salary: Rs. 47,166.67
Highest salary: Rs. 60,000.00
Lowest salary: Rs. 38,000.00

EMPLOYEE COUNT BY DEPARTMENT
----------------------------------------
Finance: 1
HR: 2
IT: 3
Sales: 2
8. Calculations Performed

The program performs the following calculations:

Total Employees
Counts the total number of employee records in the CSV file.
Total Salary
Adds all valid salary values.
Average Salary

Calculates:
Average Salary = Total Salary / Number of Valid Salaries
Highest Salary
Finds the maximum valid salary.
Lowest Salary
Finds the minimum valid salary.
Department Count
Counts how many employees belong to each department.

9. Handling Missing and Invalid Values

The program handles missing and invalid salary values using exception handling.
For example:
Rohan → Salary is missing
Sneha → Salary is invalid

These values are not included in the salary calculations.
Instead, they are counted as invalid/missing salary records.
The program does not crash when it encounters these values.