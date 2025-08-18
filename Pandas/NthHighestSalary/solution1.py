import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Rank the salaries
    salary_rank_set = sorted(set(employee['salary']), reverse = True)
    return pd.DataFrame([
        {
            f'getNthHighestSalary({N})': salary_rank_set[N-1] if len(salary_rank_set) >= N  else None
        }
    ])