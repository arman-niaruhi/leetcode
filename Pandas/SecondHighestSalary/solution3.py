import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Rank salaries in descending order, method='dense' avoids gaps in ranks
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    
    # Select the salary with rank 2 (second highest)
    second_highest = employee.loc[employee['rank'] == 2, 'salary']
    
    # Return result or None if it doesn't exist
    result = second_highest.iloc[0] if not second_highest.empty else None
    return pd.DataFrame([{'SecondHighestSalary': result}])
