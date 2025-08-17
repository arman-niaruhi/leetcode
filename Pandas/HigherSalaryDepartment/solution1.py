import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Rename columns
    department = department.rename(columns={"id": "departmentId", "name": "Department"})
    employee = employee.rename(columns={"salary": "Salary", "name": "Employee"})
    
    # Merge tables
    merged = pd.merge(employee, department, how="inner", on="departmentId")
    
    # Find max salary per department
    merged['max_salary'] = merged.groupby('Department')['Salary'].transform('max')
    
    # Keep only employees with max salary
    result = merged[merged['Salary'] == merged['max_salary']]
    
    return result[['Department', 'Employee', 'Salary']].reset_index(drop=True)
