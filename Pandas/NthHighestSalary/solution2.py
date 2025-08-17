import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_distinct_salaries = employee['salary'].dropna().drop_duplicates().sort_values(ascending=False)

    if len(sorted_distinct_salaries) < N or N <= 0:
        return pd.DataFrame(
            {f"getNthHighestSalary({N})": [None]}
        )
    
    result = sorted_distinct_salaries.iloc[N - 1]
    return pd.DataFrame(
        {f"getNthHighestSalary({N})": [result]}
    )