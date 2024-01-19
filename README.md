# Employee Data Analysis

This project involves analyzing employee data from an Excel file and identifying specific patterns related to working hours. The analysis includes finding employees who:

- Have worked for 7 consecutive days.
- Have less than 10 hours between shifts but greater than 1 hour.
- Have worked for more than 14 hours in a single shift.

## Instructions

1. **Input File:** Provide the Excel file containing employee data as the input.

2. **Run the Program:**
   - Execute the `process_employee_data` function in the provided Python script (`employee_data_analysis.py`).
   - Ensure that the necessary Python libraries (`pandas` and `datetime`) are installed.

3. **Output:**
   - The program will print the details of employees meeting the specified criteria to the console.

## Code Overview

### Functions

1. **`process_employee_data(file_path)`**
   - Main function to read and process employee data.
   - Loads the Excel file, renames columns, and performs necessary data conversions.
   - Groups data based on different criteria (e.g., consecutive days, hours between shifts).
   - Calls specific functions to analyze and print employee details based on the specified criteria.

### Helper Functions

1. **`seven_consecutive_days(grouped_data)`**
   - Identifies employees who have worked for 7 consecutive days.

2. **`between_ten_and_one(grouped_data)`**
   - Identifies employees with less than 10 hours between shifts but greater than 1 hour.

3. **`fourteen_hours(grouped_data)`**
   - Identifies employees who have worked for more than 14 hours in a single shift.

### Assumptions

- The input Excel file follows the expected format with relevant columns (e.g., 'Position ID', 'Time In', 'Time Out').
- The 'Timecard Hours' column is in the format '%H:%M'.
- The script assumes the presence of the required Python libraries (`pandas`, `datetime`).

## Error Handling

- The script includes basic error handling to catch and display any exceptions that may occur during execution.

## Notes

- The project assumes that the input data is consistent and follows the expected structure.
- Ensure the required Python libraries are installed before running the script.
