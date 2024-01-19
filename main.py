import pandas as pd
from datetime import timedelta


processed_employees14 = set()
processed_employees10 = set()

def fourteen_hours(grouped_data):
    for (fileno, day), group in grouped_data:
            total_hours = group['TimeHours'].sum()

            # b) Employees who has worked for more than 14 hours in a single shift
            if total_hours >= timedelta(hours=14):
                employee_key = (fileno, group['Name'].iloc[0], group['PositionStatus'].iloc[0])

                # Check if the employee has already been processed for this shift
                if employee_key not in processed_employees14:
                    processed_employees14.add(employee_key)
                    print(f"FileNumber: {fileno} Name: {group['Name'].iloc[0]} Position: {group['PositionStatus'].iloc[0]}")

def between_ten_and_one(grouped_data):
     for (fileno, day), group in grouped_data:
            total_hours = group['TimeHours'].sum()

            # b) Employees with less than 10 hours between shifts but greater than 1 hour
            if total_hours > timedelta(hours=1) and total_hours < timedelta(hours=10):
                employee_key = (fileno, group['Name'].iloc[0], group['PositionStatus'].iloc[0])

                # Check if the employee has already been processed for this shift
                if employee_key not in processed_employees10:
                    processed_employees10.add(employee_key)
                    print(f"FileNumber: {fileno} Name: {group['Name'].iloc[0]} Position: {group['PositionStatus'].iloc[0]}")
           
def seven_consecutive_days(grouped_data):
        lastFileNo = None
        lastDay = None
        consecutiveCount = 0
        employees = set()
        for (fileno, day), group in grouped_data:
            day = pd.to_datetime(day, unit='D')
            if lastFileNo is None or lastFileNo != fileno:
                lastFileNo = fileno
                lastDay = day
                consecutiveCount = 1
            elif (day - lastDay).days == 1 and lastFileNo == fileno:
                consecutiveCount += 1
                lastDay = day
                lastFileNo = fileno
            else:
                consecutiveCount = 1
                lastDay = day
                lastFileNo = fileno
            if consecutiveCount == 7:
                employees.add(fileno)
                employee_key = (fileno, group['Name'].iloc[0], group['PositionStatus'].iloc[0])
                # Check if the employee has already been processed for this shift
                if employee_key not in employees:
                    employees.add(employee_key)
                    print(f"FileNumber: {fileno} Name: {group['Name'].iloc[0]} Position: {group['PositionStatus'].iloc[0]}")

def process_employee_data(file_path):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)

        # Adjust these column names according to your actual data
        df = df.rename(columns={
            'Position ID': 'PositionID',
            'Position Status': 'PositionStatus',
            'Time': 'TimeIn',
            'Time Out': 'TimeOut',
            'Timecard Hours (as Time)': 'TimeHours',
            'Pay Cycle Start Date': 'StartDate',
            'Pay Cycle End Date': 'CycleEnd',
            'Employee Name': 'Name',
            'File Number': 'FileNumber'
        })

        # Convert 'StartDate' and 'CycleEnd' and 'TimeHours' columns to datetime format
        df['StartDate'] = pd.to_datetime(df['StartDate'])
        df['CycleEnd'] = pd.to_datetime(df['CycleEnd'])
        df['TimeHours'] = pd.to_datetime(df['TimeHours'], format='%H:%M').dt.time

        # Additional processing for 'Timecard Hours' containing empty values
        df['TimeHours'] = df['TimeHours'].apply(lambda x: timedelta(hours=x.hour, minutes=x.minute) if pd.notnull(x) else pd.NaT)

        # Group data by 'FileNumber' and 'Time'
        grouped_data = df.groupby(['FileNumber', df['TimeIn'].dt.day])

        print("\nEmployees who has worked for 7 consecutive days\n")
        seven_consecutive_days(grouped_data)

        # Group data by 'FileNumber' and 'StartDate'
        grouped_data = df.groupby(['FileNumber', df['TimeIn'].dt.date])
        print('\n\nEmployees with less than 10 hours between shifts but greater than 1 hour\n')
        between_ten_and_one(grouped_data)

        print('\n\nEmployees who has worked for more than 14 hours in a single shift\n')
        fourteen_hours(grouped_data)

        
    except Exception as e:
        print(f"Error: {e}")

# Call the function with your Excel file path
process_employee_data("./data.xlsx")

