import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Sort the salary column desc
    employee_sorted = employee.sort_values('salary', ascending= False)
    # Drop dublicated and reset index
    highest_salary = employee_sorted['salary'].drop_duplicates().reset_index(drop = True)

    # Check the lenght and create the new df to put the second highest salary
    if len(highest_salary) > 1:
        second_highest_salary_value = highest_salary.iloc[1]
        result_df = pd.DataFrame({"SecondHighestSalary": [second_highest_salary_value]})
    else:
        result_df = pd.DataFrame({"SecondHighestSalary": [None]})

    return result_df




    