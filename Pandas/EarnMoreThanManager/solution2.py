import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Creates a Series where the index is employee id and the value is salary.
    salary = employee.set_index('id')['salary']
    mask = employee[employee['salary']>employee['managerId'].map(salary)]
    result = mask[['name']].rename(columns={'name':'Employee'})
    return result