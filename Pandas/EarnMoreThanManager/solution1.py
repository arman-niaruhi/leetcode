import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Self-join: employee with their manager
    employee_manager = pd.merge(employee, employee,left_on="managerId", right_on="id", suffixes=("", "_manager"))
    
    # Filter employees earning more than their managers
    result = employee_manager[employee_manager["salary"] > employee_manager["salary_manager"]][["name"]]
    
    result.rename(columns={
        "name":"Employee"
    }, inplace = True)
    
    return result